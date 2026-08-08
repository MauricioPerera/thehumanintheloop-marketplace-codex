#!/usr/bin/env python3
"""Manage n8n workflow lifecycle via REST API: create, activate, deactivate, update, delete.

Dry-run by default: every subcommand prints the exact plan (and diff for `update`)
and does NOT call the API unless --apply is passed. `delete` additionally requires
--confirm-name matching the workflow's real name exactly, verified server-side data,
not just the caller's claim.

No external dependencies. Never prints the API key. Prefer the N8N_API_KEY
environment variable over --api-key to keep it out of shell history.
"""
import argparse
import difflib
import json
import os
import sys
import urllib.error
import urllib.request

USER_AGENT = "n8n-workflow-manager/0.1.0 (+https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex)"
WORKFLOW_REQUIRED_FIELDS = {"name", "nodes", "connections", "settings"}
# Allowlist, no denylist: la API rechaza el PUT si el body trae CUALQUIER campo
# fuera de este set ("request/body must NOT have additional properties"), y la
# respuesta real de GET trae mas campos internos (sourceWorkflowId,
# activeVersionId, versionCounter, ...) que los documentados en el OpenAPI de
# n8n. Mantener una lista de exclusion se desactualiza cada vez que n8n agrega
# un campo interno nuevo; una lista de inclusion no.
WRITABLE_WORKFLOW_FIELDS = {"name", "description", "nodes", "connections", "nodeGroups", "settings", "staticData", "pinData"}
CREATE_ALLOWED_FIELDS = WRITABLE_WORKFLOW_FIELDS | {"projectId"}


def _request(base_url, path, api_key, method="GET", body=None, timeout=30):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {
        "X-N8N-API-KEY": api_key,
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(base_url.rstrip("/") + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:300]
        raise SystemExit(f"[FAILED] HTTP {exc.code} en {method} {path}: {exc.reason} — {detail}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"[FAILED] No se pudo conectar a {base_url}: {exc.reason}")


def get_workflow(base_url, api_key, workflow_id):
    return _request(base_url, f"/api/v1/workflows/{workflow_id}", api_key)


def clean_payload(payload):
    # Campos opcionales en null (ej. "description") rompen el PUT: la API
    # exige el tipo declarado (string), no acepta null aunque el propio GET
    # los devuelva asi. Los campos requeridos se dejan tal cual: si vienen
    # None ahi es un error real que debe fallar, no ocultarse.
    return {k: v for k, v in payload.items() if k in WORKFLOW_REQUIRED_FIELDS or v is not None}


def pretty(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True)


def show_diff(before, after, label):
    before_lines = pretty(before).splitlines(keepends=True)
    after_lines = pretty(after).splitlines(keepends=True)
    diff = list(difflib.unified_diff(before_lines, after_lines, fromfile=f"{label} (antes)", tofile=f"{label} (despues)"))
    if not diff:
        print("Sin cambios: el patch no modifica nada respecto al estado actual.")
        return False
    print("".join(diff))
    return True


def cmd_create(args, api_key):
    with open(args.file, "r", encoding="utf-8") as fh:
        workflow = json.load(fh)
    missing = WORKFLOW_REQUIRED_FIELDS - set(workflow.keys())
    if missing:
        raise SystemExit(f"[FAILED] Falta(n) campo(s) requerido(s) en {args.file}: {sorted(missing)}")
    payload = clean_payload({k: v for k, v in workflow.items() if k in CREATE_ALLOWED_FIELDS})
    print(f"PLAN: crear workflow '{payload.get('name')}' con {len(payload.get('nodes', []))} nodos.")
    print(pretty(payload))
    if not args.apply:
        print("\nDry-run: no se creo nada. Pasa --apply para ejecutar.")
        return
    created = _request(args.url, "/api/v1/workflows", api_key, method="POST", body=payload)
    print(f"\n[OK] Workflow creado: '{created.get('name')}' (id: {created.get('id')}).")


def cmd_set_active(args, api_key, target_active):
    action = "activar" if target_active else "desactivar"
    current = get_workflow(args.url, api_key, args.workflow_id)
    if current.get("active") == target_active:
        print(f"Sin cambios: '{current.get('name')}' ya esta {'activo' if target_active else 'inactivo'}.")
        return
    print(f"PLAN: {action} '{current.get('name')}' (id: {args.workflow_id}). "
          f"Estado actual: {'activo' if current.get('active') else 'inactivo'}.")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    path = f"/api/v1/workflows/{args.workflow_id}/{'activate' if target_active else 'deactivate'}"
    updated = _request(args.url, path, api_key, method="POST")
    print(f"[OK] '{updated.get('name')}' ahora esta {'activo' if updated.get('active') else 'inactivo'}.")


def cmd_update(args, api_key):
    with open(args.patch, "r", encoding="utf-8") as fh:
        patch = json.load(fh)
    current = get_workflow(args.url, api_key, args.workflow_id)
    unknown_patch_fields = set(patch.keys()) - WRITABLE_WORKFLOW_FIELDS
    if unknown_patch_fields:
        raise SystemExit(f"[FAILED] El patch tiene campos no editables o desconocidos: {sorted(unknown_patch_fields)}. "
                          f"Editables: {sorted(WRITABLE_WORKFLOW_FIELDS)}")
    merged = dict(current)
    merged.update(patch)
    payload = clean_payload({k: v for k, v in merged.items() if k in WRITABLE_WORKFLOW_FIELDS})
    comparable_before = clean_payload({k: v for k, v in current.items() if k in WRITABLE_WORKFLOW_FIELDS})
    changed = show_diff(comparable_before, payload, f"workflow {args.workflow_id}")
    if not changed:
        return
    if not args.apply:
        print("\nDry-run: no se aplico nada. Revisa el diff y pasa --apply para ejecutar.")
        return
    updated = _request(args.url, f"/api/v1/workflows/{args.workflow_id}", api_key, method="PUT", body=payload)
    print(f"\n[OK] Workflow actualizado: '{updated.get('name')}' (id: {updated.get('id')}).")


def cmd_set_archived(args, api_key, target_archived):
    action = "archivar" if target_archived else "desarchivar"
    current = get_workflow(args.url, api_key, args.workflow_id)
    if current.get("isArchived") == target_archived:
        print(f"Sin cambios: '{current.get('name')}' ya esta {'archivado' if target_archived else 'sin archivar'}.")
        return
    print(f"PLAN: {action} '{current.get('name')}' (id: {args.workflow_id}). "
          f"Estado actual: {'archivado' if current.get('isArchived') else 'sin archivar'}.")
    if target_archived:
        print("Nota: archivar es un soft-delete. El workflow deja de listarse activo pero se puede restaurar con 'unarchive'.")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    path = f"/api/v1/workflows/{args.workflow_id}/{'archive' if target_archived else 'unarchive'}"
    updated = _request(args.url, path, api_key, method="POST")
    print(f"[OK] '{updated.get('name')}' ahora esta {'archivado' if updated.get('isArchived') else 'sin archivar'}.")


def cmd_transfer(args, api_key):
    current = get_workflow(args.url, api_key, args.workflow_id)
    owner_entry = next((s for s in (current.get("shared") or []) if s.get("role") == "workflow:owner"), None)
    current_project = owner_entry.get("projectId") if owner_entry else None
    if current_project == args.destination_project_id:
        print(f"Sin cambios: '{current.get('name')}' ya pertenece al proyecto {args.destination_project_id}.")
        return
    print(f"PLAN: transferir '{current.get('name')}' (id: {args.workflow_id}) "
          f"del proyecto {current_project or '(desconocido)'} al proyecto {args.destination_project_id}.")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    _request(args.url, f"/api/v1/workflows/{args.workflow_id}/transfer", api_key,
              method="PUT", body={"destinationProjectId": args.destination_project_id})
    print(f"[OK] '{current.get('name')}' transferido a {args.destination_project_id}.")


def cmd_delete(args, api_key):
    current = get_workflow(args.url, api_key, args.workflow_id)
    real_name = current.get("name")
    if args.confirm_name != real_name:
        raise SystemExit(
            f"[FAILED] --confirm-name no coincide con el nombre real del workflow ('{real_name}'). "
            "No se borro nada. Copia el nombre exacto para confirmar."
        )
    print(f"PLAN: BORRAR '{real_name}' (id: {args.workflow_id}). Esto es IRREVERSIBLE.")
    if not args.apply:
        print("Dry-run: no se borro nada. Pasa --apply para ejecutar.")
        return
    _request(args.url, f"/api/v1/workflows/{args.workflow_id}", api_key, method="DELETE")
    print(f"[OK] '{real_name}' fue borrado.")


def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--url", required=True, help="URL base de n8n, ej: https://n8n.midominio.com")
    common.add_argument("--api-key", help="API key de n8n. Preferi la variable de entorno N8N_API_KEY.")
    common.add_argument("--apply", action="store_true", help="Ejecuta la mutacion. Sin esto, dry-run.")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", parents=[common], help="Crear un workflow nuevo desde un archivo JSON")
    p_create.add_argument("--file", required=True, help="Archivo JSON con name/nodes/connections/settings")

    p_activate = sub.add_parser("activate", parents=[common], help="Activar un workflow")
    p_activate.add_argument("--workflow-id", required=True)

    p_deactivate = sub.add_parser("deactivate", parents=[common], help="Desactivar un workflow")
    p_deactivate.add_argument("--workflow-id", required=True)

    p_update = sub.add_parser("update", parents=[common], help="Actualizar un workflow existente con un patch parcial")
    p_update.add_argument("--workflow-id", required=True)
    p_update.add_argument("--patch", required=True,
                           help="Archivo JSON con los campos a cambiar (reemplaza esos campos completos, sin merge profundo)")

    p_archive = sub.add_parser("archive", parents=[common], help="Archivar un workflow (soft-delete, reversible con unarchive)")
    p_archive.add_argument("--workflow-id", required=True)

    p_unarchive = sub.add_parser("unarchive", parents=[common], help="Restaurar un workflow archivado")
    p_unarchive.add_argument("--workflow-id", required=True)

    p_transfer = sub.add_parser("transfer", parents=[common], help="Transferir un workflow a otro proyecto")
    p_transfer.add_argument("--workflow-id", required=True)
    p_transfer.add_argument("--destination-project-id", required=True)

    p_delete = sub.add_parser("delete", parents=[common], help="Borrar un workflow (irreversible)")
    p_delete.add_argument("--workflow-id", required=True)
    p_delete.add_argument("--confirm-name", required=True,
                           help="Nombre exacto del workflow, para confirmar que es el correcto")

    return parser


def main():
    args = build_parser().parse_args()
    api_key = args.api_key or os.environ.get("N8N_API_KEY")
    if not api_key:
        raise SystemExit("[FAILED] Falta API key: pasa --api-key o define N8N_API_KEY")

    handlers = {
        "create": lambda: cmd_create(args, api_key),
        "activate": lambda: cmd_set_active(args, api_key, True),
        "deactivate": lambda: cmd_set_active(args, api_key, False),
        "update": lambda: cmd_update(args, api_key),
        "archive": lambda: cmd_set_archived(args, api_key, True),
        "unarchive": lambda: cmd_set_archived(args, api_key, False),
        "transfer": lambda: cmd_transfer(args, api_key),
        "delete": lambda: cmd_delete(args, api_key),
    }
    handlers[args.command]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
