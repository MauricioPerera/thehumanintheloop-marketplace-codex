#!/usr/bin/env python3
"""Build (never run) the exact shell command to launch an ephemeral terminal
agent, for one of two backends: Ollama (`ollama launch claude`) or pool
(`pool exec`, poolside.ai).

This script does NOT execute anything and does NOT background any process.
It only writes the prompt file (if given as literal text) and prints the
command line you must then run yourself, as your own Bash tool call with
run_in_background: true. That distinction matters: a launch backgrounded by
a wrapper script becomes an orphaned subprocess your agent harness never
gets a completion notification for. One launch = one of your own background
Bash calls, never `&` chained after something else.

No external dependencies.
"""
import argparse
import json
import os
import sys


def write_prompt_file(text, path):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def cmd_probe(args):
    if args.backend == "ollama":
        model = args.model or "<MODEL>"
        print(f"ollama launch claude --model {model} -- -p \"Responde: VIVO\" --permission-mode plan < /dev/null")
        print("\nDebe imprimir VIVO. Si no responde: no sigas a ciegas, decilo al usuario.")
        print("Si sospechas degradacion por cuota, usa una sonda de TOOLS en vez de texto: pedile que cree un")
        print("archivo real dentro del cwd y respondio LISTO, y verifica que el archivo EXISTE en disco.")
    else:
        print("pool no tiene una sonda de vida barata: su propio riesgo no es colgarse esperando aprobacion")
        print("(el rechazo es casi instantaneo), es el TIEMPO DE RAZONAMIENTO antes de llegar a esa accion,")
        print("que se paga igual con o sin --unsafe-auto-allow. No hay forma barata de 'probar primero'.")
        print("Lanza directamente en un directorio descartable con --unsafe-auto-allow (ver 'build').")


def cmd_build(args):
    goal_mode = args.backend == "ollama" and args.goal
    if goal_mode:
        pass  # el prompt va inline en la condicion del /goal, no por archivo
    elif args.prompt_text is not None:
        if not args.prompt_file:
            raise SystemExit("[FAILED] --prompt-text requiere --prompt-file (donde escribirlo).")
        write_prompt_file(args.prompt_text, args.prompt_file)
        print(f"# Prompt escrito en: {args.prompt_file}\n")
    elif not args.prompt_file:
        raise SystemExit("[FAILED] Falta --prompt-file (o --prompt-text para crearlo).")
    elif not os.path.exists(args.prompt_file):
        raise SystemExit(f"[FAILED] {args.prompt_file} no existe y no se paso --prompt-text para crearlo.")

    if args.backend == "ollama":
        _build_ollama(args)
    else:
        _build_pool(args)

    print("\n# Vos (el agente orquestador) tenes que ejecutar el comando de arriba con TU PROPIA tool de Bash,")
    print("# run_in_background: true, como su propio task -- nunca encadenado con '&' detras de otro comando,")
    print("# y nunca invocado por este script. Un lanzamiento = un background task tuyo, con su propia")
    print("# notificacion de fin.")


def _build_ollama(args):
    model = args.model or "<MODEL>"
    mcp_config = args.mcp_config_file
    if mcp_config:
        if not os.path.exists(mcp_config):
            raise SystemExit(f"[FAILED] --mcp-config-file {mcp_config} no existe.")
        with open(mcp_config, "r", encoding="utf-8") as fh:
            raw = fh.read()
        try:
            mcp_json = json.loads(raw)  # valida que sea JSON antes de imprimir el comando
        except json.JSONDecodeError as exc:
            raise SystemExit(f"[FAILED] --mcp-config-file {mcp_config} no es JSON valido: {exc}")
        mcp_arg = json.dumps(mcp_json)
    else:
        mcp_json = {"mcpServers": {}}
        mcp_arg = json.dumps(mcp_json)
        print("# Sin --mcp-config-file: usando '{\"mcpServers\": {}}' (correcto si la tarea NO usa el gate CCDD).")
        print("# Si la tarea SI usa CCDD, pasa --mcp-config-file con SOLO la entrada ccdd-complexity copiada")
        print("# de la config MCP del usuario -- este script no la inventa ni la asume.\n")

    log_path = args.log or "delegation.log"
    permissions = "--dangerously-skip-permissions" if not args.allowed_tools else f'--permission-mode acceptEdits --allowedTools "{args.allowed_tools}"'

    if args.goal:
        print(f"cd {args.dir} && ollama launch claude --model {model} -y -- -p \"/goal {args.goal}\" "
              f"{permissions} < /dev/null > {log_path} 2>&1")
        print("\n# Modo /goal: un evaluador independiente juzga al final de CADA turno y reintenta con feedback")
        print("# hasta cumplir la condicion o agotar el tope de turnos que vos pusiste en la condicion misma")
        print("# (obligatorio, sin eso no hay limite de gasto). El tope de turnos NO protege un loop DENTRO de")
        print("# un turno: si el log/transcript deja de crecer por varios minutos, tratalo como colgado y matalo.")
    else:
        print(f"cd {args.dir} && ollama launch claude --model {model} -y -- --strict-mcp-config "
              f"--mcp-config '{mcp_arg}' -p \"$(cat {args.prompt_file})\" {permissions} "
              f"< /dev/null > {log_path} 2>&1")
        print("\n# < /dev/null es OBLIGATORIO: sin el, 'claude' espera stdin y el lanzamiento sale vacio (exit 0,")
        print("# cero trabajo). --strict-mcp-config es OBLIGATORIO tambien: sin el, hereda toda la flota MCP")
        print("# global del usuario -- decenas de procesos, puede colgar la app anfitriona.")
    print(f"\n# Log en: {log_path} -- se escribe AL FINAL en modo -p headless. Log vacio no es igual a colgado;")
    print("# para saber si sigue vivo mira mtime de los entregables esperados en disco, no el log.")


def _build_pool(args):
    log_path = args.log or "delegation.log"
    print(f"pool exec --unsafe-auto-allow -d {args.dir} -f {args.prompt_file} -o json > {log_path} 2>&1")
    print("\n# --unsafe-auto-allow es OBLIGATORIO en no-interactivo: sin el, la primera accion que necesite")
    print("# aprobacion falla al toque (segundos, no colgado) con exit 1. No hay modo headless sin este flag.")
    print("# Exit codes: 0 = tarea completa, 4 = fallo explicito reportado por pool, otro = error inesperado.")
    print("# Si dos delegaciones en paralelo tocan el MISMO archivo target, lanzalas en SECUENCIA, no en")
    print("# paralelo -- pool no tiene locking propio entre invocaciones.")
    print("# No le des al implementador las tools de ningun gate de verificacion (ej. CCDD): el veredicto lo")
    print("# corres vos, de forma independiente, no el autoevaluador del implementador.")


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_probe = sub.add_parser("probe", help="Comando de sonda de vida antes de delegar en serio (solo lectura, imprime el comando)")
    p_probe.add_argument("--backend", required=True, choices=["ollama", "pool"])
    p_probe.add_argument("--model", help="Solo ollama, ej: glm-5.2:cloud")

    p_build = sub.add_parser("build", help="Arma el comando de lanzamiento real (imprime, no ejecuta)")
    p_build.add_argument("--backend", required=True, choices=["ollama", "pool"])
    p_build.add_argument("--dir", required=True, help="Directorio de trabajo del agente efimero")
    p_build.add_argument("--prompt-file", help="Ruta del archivo de prompt (se crea si pasas --prompt-text). No hace falta con --goal.")
    p_build.add_argument("--prompt-text", help="Texto del prompt a escribir en --prompt-file. Sin esto, se asume que el archivo ya existe.")
    p_build.add_argument("--log", help="Ruta del log de salida. Default: delegation.log")
    p_build.add_argument("--model", help="Solo ollama, ej: glm-5.2:cloud")
    p_build.add_argument("--mcp-config-file", help="Solo ollama: archivo JSON con la config MCP minima a heredar. Sin esto, mcpServers vacio.")
    p_build.add_argument("--allowed-tools", help="Solo ollama: lista para --allowedTools con --permission-mode acceptEdits, en vez de --dangerously-skip-permissions")
    p_build.add_argument("--goal", help="Solo ollama: condicion para modo /goal en vez de -p con prompt de archivo")

    return parser


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    if args.command == "probe":
        cmd_probe(args)
    elif args.command == "build":
        cmd_build(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
