#!/usr/bin/env python3
"""Manage n8n credential lifecycle via REST API: create, rename, rotate, delete, test, transfer.

Dry-run by default: every mutating subcommand prints the exact plan and does NOT
call the API unless --apply is passed. `delete` additionally requires
--confirm-name matching the credential's real name exactly.

The secret value (`data`) is read only from a local JSON file (--data-file),
never from a CLI argument or stdin literal, and its VALUES are never printed —
only the field names, so you can confirm which fields are being sent without
ever seeing the secret itself. n8n's API never returns credential data on GET,
so this script cannot leak an existing secret even if it tried.

No external dependencies. Never prints the API key. Prefer the N8N_API_KEY
environment variable over --api-key to keep it out of shell history.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

USER_AGENT = "n8n-credential-manager/0.1.0 (+https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex)"


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


def get_credential(base_url, api_key, credential_id):
    return _request(base_url, f"/api/v1/credentials/{credential_id}", api_key)


def load_data_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or not data:
        raise SystemExit(f"[FAILED] {path} debe ser un objeto JSON no vacio con los campos del secreto.")
    return data


def describe_data_fields(data):
    return ", ".join(f"{k} (valor oculto)" for k in sorted(data.keys()))


def cmd_schema(args, api_key):
    schema = _request(args.url, f"/api/v1/credentials/schema/{args.type}", api_key)
    print(json.dumps(schema, indent=2, ensure_ascii=False))


def cmd_create(args, api_key):
    data = load_data_file(args.data_file)
    payload = {"name": args.name, "type": args.type, "data": data}
    if args.project_id:
        payload["projectId"] = args.project_id
    print(f"PLAN: crear credencial '{args.name}' de tipo '{args.type}'.")
    print(f"Campos del secreto a enviar: {describe_data_fields(data)}")
    if args.project_id:
        print(f"Proyecto destino: {args.project_id}")
    if not args.apply:
        print("\nDry-run: no se creo nada. Pasa --apply para ejecutar.")
        return
    created = _request(args.url, "/api/v1/credentials", api_key, method="POST", body=payload)
    print(f"\n[OK] Credencial creada: '{created.get('name')}' (id: {created.get('id')}).")


def cmd_rename(args, api_key):
    current = get_credential(args.url, api_key, args.credential_id)
    if current.get("name") == args.name:
        print(f"Sin cambios: la credencial ya se llama '{args.name}'.")
        return
    print(f"PLAN: renombrar '{current.get('name')}' -> '{args.name}' (id: {args.credential_id}). No se toca el secreto.")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    updated = _request(args.url, f"/api/v1/credentials/{args.credential_id}", api_key,
                        method="PATCH", body={"name": args.name})
    print(f"[OK] Credencial renombrada a '{updated.get('name')}'.")


def cmd_rotate(args, api_key):
    current = get_credential(args.url, api_key, args.credential_id)
    data = load_data_file(args.data_file)
    payload = {"data": data, "isPartialData": args.partial}
    if args.type:
        payload["type"] = args.type
    print(f"PLAN: rotar el secreto de '{current.get('name')}' (id: {args.credential_id}, tipo actual: {current.get('type')}).")
    print(f"Campos del secreto a enviar: {describe_data_fields(data)}")
    print(f"Modo: {'merge parcial con el secreto existente' if args.partial else 'reemplazo completo del secreto'}")
    if args.type:
        print(f"Tipo nuevo: {args.type}")
    if not args.apply:
        print("\nDry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    updated = _request(args.url, f"/api/v1/credentials/{args.credential_id}", api_key, method="PATCH", body=payload)
    print(f"\n[OK] Secreto rotado para '{updated.get('name')}'.")


def cmd_delete(args, api_key):
    current = get_credential(args.url, api_key, args.credential_id)
    real_name = current.get("name")
    if args.confirm_name != real_name:
        raise SystemExit(
            f"[FAILED] --confirm-name no coincide con el nombre real de la credencial ('{real_name}'). "
            "No se borro nada. Copia el nombre exacto para confirmar."
        )
    print(f"PLAN: BORRAR la credencial '{real_name}' (id: {args.credential_id}). Esto es IRREVERSIBLE.")
    if not args.apply:
        print("Dry-run: no se borro nada. Pasa --apply para ejecutar.")
        return
    _request(args.url, f"/api/v1/credentials/{args.credential_id}", api_key, method="DELETE")
    print(f"[OK] '{real_name}' fue borrada.")


def cmd_test(args, api_key):
    # No muta nada: n8n prueba la credencial ya almacenada contra su servicio.
    result = _request(args.url, f"/api/v1/credentials/{args.credential_id}/test", api_key, method="POST")
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_transfer(args, api_key):
    current = get_credential(args.url, api_key, args.credential_id)
    print(f"PLAN: transferir la credencial '{current.get('name')}' (id: {args.credential_id}) "
          f"al proyecto {args.destination_project_id}.")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    _request(args.url, f"/api/v1/credentials/{args.credential_id}/transfer", api_key,
              method="PUT", body={"destinationProjectId": args.destination_project_id})
    print(f"[OK] '{current.get('name')}' transferida a {args.destination_project_id}.")


def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--url", required=True, help="URL base de n8n, ej: https://n8n.midominio.com")
    common.add_argument("--api-key", help="API key de n8n. Preferi la variable de entorno N8N_API_KEY.")

    mutating = argparse.ArgumentParser(add_help=False, parents=[common])
    mutating.add_argument("--apply", action="store_true", help="Ejecuta la mutacion. Sin esto, dry-run.")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_schema = sub.add_parser("schema", parents=[common], help="Ver que campos necesita un tipo de credencial (solo lectura)")
    p_schema.add_argument("--type", required=True, help="Tipo de credencial, ej: githubApi")

    p_create = sub.add_parser("create", parents=[mutating], help="Crear una credencial nueva")
    p_create.add_argument("--name", required=True)
    p_create.add_argument("--type", required=True, help="Tipo de credencial, ej: githubApi. Usa 'schema' para ver los campos.")
    p_create.add_argument("--data-file", required=True, help="Archivo JSON local con los campos del secreto")
    p_create.add_argument("--project-id", help="Proyecto destino. Por defecto el proyecto personal del usuario.")

    p_rename = sub.add_parser("rename", parents=[mutating], help="Renombrar una credencial (no toca el secreto)")
    p_rename.add_argument("--credential-id", required=True)
    p_rename.add_argument("--name", required=True)

    p_rotate = sub.add_parser("rotate", parents=[mutating], help="Cambiar el valor del secreto de una credencial")
    p_rotate.add_argument("--credential-id", required=True)
    p_rotate.add_argument("--data-file", required=True, help="Archivo JSON local con los campos nuevos del secreto")
    p_rotate.add_argument("--type", help="Solo si tambien cambia el tipo de credencial")
    p_rotate.add_argument("--partial", action="store_true",
                           help="Mergea con el secreto existente en vez de reemplazarlo completo")

    p_delete = sub.add_parser("delete", parents=[mutating], help="Borrar una credencial (irreversible)")
    p_delete.add_argument("--credential-id", required=True)
    p_delete.add_argument("--confirm-name", required=True,
                           help="Nombre exacto de la credencial, para confirmar que es la correcta")

    p_test = sub.add_parser("test", parents=[common], help="Probar una credencial ya guardada (no muta nada)")
    p_test.add_argument("--credential-id", required=True)

    p_transfer = sub.add_parser("transfer", parents=[mutating], help="Transferir una credencial a otro proyecto")
    p_transfer.add_argument("--credential-id", required=True)
    p_transfer.add_argument("--destination-project-id", required=True)

    return parser


def main():
    args = build_parser().parse_args()
    api_key = args.api_key or os.environ.get("N8N_API_KEY")
    if not api_key:
        raise SystemExit("[FAILED] Falta API key: pasa --api-key o define N8N_API_KEY")

    handlers = {
        "schema": lambda: cmd_schema(args, api_key),
        "create": lambda: cmd_create(args, api_key),
        "rename": lambda: cmd_rename(args, api_key),
        "rotate": lambda: cmd_rotate(args, api_key),
        "delete": lambda: cmd_delete(args, api_key),
        "test": lambda: cmd_test(args, api_key),
        "transfer": lambda: cmd_transfer(args, api_key),
    }
    handlers[args.command]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
