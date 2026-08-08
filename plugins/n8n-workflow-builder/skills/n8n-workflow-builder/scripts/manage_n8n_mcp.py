#!/usr/bin/env python3
"""Generic client for n8n's official MCP server (JSON-RPC over HTTP).

Wraps its 33 workflow-authoring tools: SDK reference, node search/type lookup,
per-node and full-workflow validation, atomic create/update, safe(ish) test
execution with pin data, version history/restore, publish/archive, data tables.

The protocol is stateless: each request is an independent JSON-RPC POST, no
`initialize` handshake needed first.

Mutating tools are dry-run by default: the script prints the exact tool call
it would make and requires --apply to actually send it. Unknown tool names
(not in this script's classification) default to mutating -- the safer
assumption when a future n8n version adds a tool this script doesn't know
about yet.

`test_workflow` is classified as MUTATING even though its name suggests
otherwise: per n8n's own tool description, nodes with credentials/HTTP/
triggers are pinned (simulated), but nodes like Execute Command or file
read/write run for real. It is not a side-effect-free dry run.

No external dependencies. Never prints the Bearer token. Prefer the
N8N_MCP_TOKEN environment variable over --token to keep it out of shell
history. This token is DIFFERENT from N8N_API_KEY (REST API) -- the MCP
server uses its own Bearer token (JWT audience "mcp-server-api").
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

USER_AGENT = "n8n-workflow-builder/0.1.0 (+https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex)"

READ_ONLY_TOOLS = {
    "search_workflows", "get_execution", "search_executions", "get_workflow_details",
    "get_workflow_history", "get_workflow_version", "list_credentials", "list_tags",
    "search_data_tables", "search_nodes", "get_node_types", "get_workflow_best_practices",
    "explore_node_resources", "validate_workflow", "validate_node_config", "search_projects",
    "search_folders", "get_sdk_reference", "prepare_test_pin_data",
}
MUTATING_TOOLS = {
    "execute_workflow", "publish_workflow", "unpublish_workflow", "archive_workflow",
    "restore_workflow_version", "create_workflow_from_code", "update_workflow",
    "create_data_table", "rename_data_table", "add_data_table_column",
    "delete_data_table_column", "rename_data_table_column", "add_data_table_rows",
    "test_workflow",
}


def parse_sse_json(text):
    for line in text.splitlines():
        if line.startswith("data: "):
            return json.loads(line[len("data: "):])
    raise SystemExit("[FAILED] Respuesta inesperada del servidor MCP (sin linea 'data:').")


def mcp_call(base_url, token, method, params=None, timeout=90):
    body = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(
        base_url.rstrip("/"),
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            text = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:300]
        raise SystemExit(f"[FAILED] HTTP {exc.code}: {exc.reason} — {detail}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"[FAILED] No se pudo conectar a {base_url}: {exc.reason}")
    payload = parse_sse_json(text)
    if "error" in payload:
        raise SystemExit(f"[FAILED] Error MCP: {json.dumps(payload['error'], ensure_ascii=False)}")
    return payload["result"]


def cmd_list_tools(args, token):
    result = mcp_call(args.url, token, "tools/list")
    tools = result.get("tools", [])
    if args.full:
        print(json.dumps(tools, indent=2, ensure_ascii=False))
        return
    for t in sorted(tools, key=lambda t: t["name"]):
        kind = "solo lectura" if t["name"] in READ_ONLY_TOOLS else "MUTA" if t["name"] in MUTATING_TOOLS else "sin clasificar (tratado como MUTA)"
        print(f"- {t['name']} [{kind}]: {t.get('description', '')[:100]}")


def cmd_call(args, token):
    tool_args = {}
    if args.args_file:
        with open(args.args_file, "r", encoding="utf-8") as fh:
            tool_args = json.load(fh)
    is_read_only = args.tool in READ_ONLY_TOOLS
    print(f"PLAN: llamar '{args.tool}' con estos argumentos:")
    print(json.dumps(tool_args, indent=2, ensure_ascii=False))
    if not is_read_only:
        print(f"\nEsta tool esta clasificada como MUTANTE{' (sin clasificar, se asume lo peor)' if args.tool not in MUTATING_TOOLS else ''}.")
        if not args.apply:
            print("Dry-run: no se llamo a la API. Pasa --apply para ejecutar.")
            return
    result = mcp_call(args.url, token, "tools/call", {"name": args.tool, "arguments": tool_args})
    print()
    for block in result.get("content", []):
        if block.get("type") == "text":
            print(block["text"])
        else:
            print(json.dumps(block, indent=2, ensure_ascii=False))
    if result.get("isError"):
        raise SystemExit("[FAILED] La tool devolvio isError=true (ver salida arriba).")


def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--url", required=True, help="URL del endpoint MCP, ej: https://n8n.midominio.com/mcp-server/http")
    common.add_argument("--token", help="Bearer token del MCP server de n8n. Preferi N8N_MCP_TOKEN. Distinto de N8N_API_KEY.")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list-tools", parents=[common], help="Listar las tools disponibles (solo lectura)")
    p_list.add_argument("--full", action="store_true", help="Imprime el JSON completo (inputSchema incluido) en vez del resumen")

    p_call = sub.add_parser("call", parents=[common], help="Llamar una tool por nombre")
    p_call.add_argument("--tool", required=True, help="Nombre exacto de la tool, ej: search_nodes")
    p_call.add_argument("--args-file", help="Archivo JSON con los argumentos de la tool (objeto). Sin esto, argumentos vacios.")
    p_call.add_argument("--apply", action="store_true", help="Ejecuta tools clasificadas como mutantes. Sin esto, dry-run para esas.")

    return parser


def main():
    # La referencia del SDK y otros textos de n8n traen caracteres Unicode
    # (flechas, etc.); en Windows stdout es cp1252 por defecto y revienta al
    # imprimirlos. Forzar UTF-8 evita el crash sin depender de la consola.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    token = args.token or os.environ.get("N8N_MCP_TOKEN")
    if not token:
        raise SystemExit("[FAILED] Falta el Bearer token del MCP: pasa --token o define N8N_MCP_TOKEN")

    if args.command == "list-tools":
        cmd_list_tools(args, token)
    elif args.command == "call":
        cmd_call(args, token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
