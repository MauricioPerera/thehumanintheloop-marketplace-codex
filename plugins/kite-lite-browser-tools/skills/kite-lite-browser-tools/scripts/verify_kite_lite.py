#!/usr/bin/env python3
"""Smoke-test kite-lite's MCP server before relying on it: launches `kite-lite mcp`
(stdio transport), does the initialize + tools/list handshake, and confirms the 9
expected tools are present.

Read-only, single short-lived process, no page fetches -- safe to run any time to
confirm the binary is installed and its MCP mode responds correctly, before assuming
the bundled MCP server (see .mcp.json in this plugin) will work.

No external dependencies.
"""
import json
import shutil
import subprocess
import sys

EXPECTED_TOOLS = {
    "fetch_page", "render_screenshot", "eval_js", "browser_navigate", "browser_click",
    "browser_type", "browser_get_dom", "browser_screenshot", "browser_call_tool",
}


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    binary = sys.argv[1] if len(sys.argv) > 1 else shutil.which("kite-lite")
    if not binary:
        raise SystemExit("[FAILED] No se encontro el binario 'kite-lite' en PATH. "
                          "Instalalo con 'cargo install kite-lite', o pasa su ruta como argumento.")

    try:
        proc = subprocess.Popen([binary, "mcp"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True, bufsize=1)
    except OSError as exc:
        raise SystemExit(f"[FAILED] No se pudo ejecutar {binary!r}: {exc}")

    def send(msg):
        proc.stdin.write(json.dumps(msg) + "\n")
        proc.stdin.flush()

    def recv():
        line = proc.stdout.readline()
        if not line:
            err = proc.stderr.read()
            raise SystemExit(f"[FAILED] kite-lite mcp no respondio. stderr: {err.strip()}")
        return json.loads(line)

    try:
        send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
              "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                         "clientInfo": {"name": "verify-kite-lite", "version": "0.1.0"}}})
        init_result = recv()
        if "error" in init_result:
            raise SystemExit(f"[FAILED] initialize devolvio error: {init_result['error']}")

        send({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        list_result = recv()
        if "error" in list_result:
            raise SystemExit(f"[FAILED] tools/list devolvio error: {list_result['error']}")

        tools = {t["name"] for t in list_result["result"]["tools"]}
        missing = EXPECTED_TOOLS - tools
        extra = tools - EXPECTED_TOOLS
        print(f"[OK] kite-lite mcp responde. {len(tools)} tools: {sorted(tools)}")
        if missing:
            print(f"[WARN] Faltan tools esperadas (¿version distinta?): {sorted(missing)}")
        if extra:
            print(f"[INFO] Tools nuevas no documentadas aca: {sorted(extra)}")
    finally:
        proc.stdin.close()
        proc.terminate()

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
