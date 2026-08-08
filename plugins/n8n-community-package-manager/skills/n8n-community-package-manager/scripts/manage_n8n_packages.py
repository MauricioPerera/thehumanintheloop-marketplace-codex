#!/usr/bin/env python3
"""Manage n8n community node packages via REST API: list, install, update, uninstall.

Dry-run by default: install/update/uninstall print the exact plan and do NOT
call the API unless --apply is passed. `uninstall` additionally requires
--confirm-name matching the installed package name exactly.

Installing a community package runs third-party code inside the n8n instance
and affects every workflow that instance runs, not just one isolated object.
By default packages must be n8n-vetted (`verify`); pass --allow-unverified to
install/update an unverified version explicitly.

No external dependencies. Never prints the API key. Prefer the N8N_API_KEY
environment variable over --api-key to keep it out of shell history.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

USER_AGENT = "n8n-community-package-manager/0.1.0 (+https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex)"


def _request(base_url, path, api_key, method="GET", body=None, timeout=60):
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


def validate_package_name(name):
    # Paquetes con scope (ej. "@mercadopago/n8n-nodes-mercadopago") son
    # validos: el prefijo n8n-nodes- va despues del scope, no al principio
    # del string completo.
    unscoped = name.split("/", 1)[1] if name.startswith("@") and "/" in name else name
    if not unscoped.startswith("n8n-nodes-"):
        raise SystemExit(f"[FAILED] '{name}' no parece un paquete de nodos de n8n valido "
                          "(el nombre, sin el scope, debe empezar con 'n8n-nodes-').")


def list_packages(base_url, api_key):
    return _request(base_url, "/api/v1/community-packages", api_key)


def cmd_list(args, api_key):
    packages = list_packages(args.url, api_key)
    print(json.dumps(packages, indent=2, ensure_ascii=False))


def cmd_install(args, api_key):
    validate_package_name(args.name)
    payload = {"name": args.name}
    if args.version:
        payload["version"] = args.version
    if args.allow_unverified:
        payload["verify"] = False
    print(f"PLAN: instalar '{args.name}'" + (f" version {args.version}" if args.version else " (ultima version)") + ".")
    print("Verificacion contra la lista vetada de n8n: "
          + ("DESACTIVADA (--allow-unverified)" if args.allow_unverified else "activa (default)"))
    print("Esto corre codigo de terceros dentro de la instancia y afecta a todos los workflows, no solo a uno.")
    if not args.apply:
        print("\nDry-run: no se instalo nada. Pasa --apply para ejecutar.")
        return
    installed = _request(args.url, "/api/v1/community-packages", api_key, method="POST", body=payload)
    print(f"\n[OK] Instalado: '{installed.get('packageName')}' version {installed.get('installedVersion')}.")


def cmd_update(args, api_key):
    validate_package_name(args.name)
    payload = {}
    if args.version:
        payload["version"] = args.version
    if args.allow_unverified:
        payload["verify"] = False
    print(f"PLAN: actualizar '{args.name}'" + (f" a la version {args.version}" if args.version else " a la ultima version") + ".")
    if not args.apply:
        print("Dry-run: no se aplico nada. Pasa --apply para ejecutar.")
        return
    updated = _request(args.url, f"/api/v1/community-packages/{args.name}", api_key, method="PATCH", body=payload)
    print(f"[OK] '{updated.get('packageName')}' ahora en version {updated.get('installedVersion')}.")


def cmd_uninstall(args, api_key):
    validate_package_name(args.name)
    if args.confirm_name != args.name:
        raise SystemExit(
            f"[FAILED] --confirm-name ('{args.confirm_name}') no coincide con --name ('{args.name}'). "
            "No se desinstalo nada."
        )
    print(f"PLAN: DESINSTALAR '{args.name}'. Los workflows que usen sus nodos dejaran de poder ejecutarlos.")
    if not args.apply:
        print("Dry-run: no se desinstalo nada. Pasa --apply para ejecutar.")
        return
    _request(args.url, f"/api/v1/community-packages/{args.name}", api_key, method="DELETE")
    print(f"[OK] '{args.name}' fue desinstalado.")


def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--url", required=True, help="URL base de n8n, ej: https://n8n.midominio.com")
    common.add_argument("--api-key", help="API key de n8n. Preferi la variable de entorno N8N_API_KEY.")

    mutating = argparse.ArgumentParser(add_help=False, parents=[common])
    mutating.add_argument("--apply", action="store_true", help="Ejecuta la mutacion. Sin esto, dry-run.")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", parents=[common], help="Listar paquetes de comunidad instalados (solo lectura)")

    p_install = sub.add_parser("install", parents=[mutating], help="Instalar un paquete de comunidad")
    p_install.add_argument("--name", required=True, help="Nombre npm del paquete, ej: n8n-nodes-ejemplo")
    p_install.add_argument("--version", help="Version especifica. Por defecto, la ultima.")
    p_install.add_argument("--allow-unverified", action="store_true",
                            help="Permite instalar una version no vetada por n8n. Usar solo si el usuario lo pide explicitamente.")

    p_update = sub.add_parser("update", parents=[mutating], help="Actualizar un paquete ya instalado")
    p_update.add_argument("--name", required=True)
    p_update.add_argument("--version", help="Version especifica. Por defecto, la ultima.")
    p_update.add_argument("--allow-unverified", action="store_true")

    p_uninstall = sub.add_parser("uninstall", parents=[mutating], help="Desinstalar un paquete (afecta a los workflows que lo usen)")
    p_uninstall.add_argument("--name", required=True)
    p_uninstall.add_argument("--confirm-name", required=True,
                              help="Repite --name exacto, para confirmar que es el paquete correcto")

    return parser


def main():
    args = build_parser().parse_args()
    api_key = args.api_key or os.environ.get("N8N_API_KEY")
    if not api_key:
        raise SystemExit("[FAILED] Falta API key: pasa --api-key o define N8N_API_KEY")

    handlers = {
        "list": lambda: cmd_list(args, api_key),
        "install": lambda: cmd_install(args, api_key),
        "update": lambda: cmd_update(args, api_key),
        "uninstall": lambda: cmd_uninstall(args, api_key),
    }
    handlers[args.command]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
