#!/usr/bin/env python3
"""Run kite-lite's 4 on-page linters (seo-lint, a11y-lint, social-lint, webmcp-lint) against
a URL or local file (HTML or a kite-lite page.json snapshot) and consolidate the results into
one report.

Requires the `kite-lite` binary on PATH (install with `cargo install kite-lite`), or pass its
path with --kite-lite-bin. This script only shells out to those 4 CLI subcommands and parses
their --json output -- it does not talk to kite-lite over MCP or fetch anything itself.

No external dependencies.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

LINTERS = ["seo-lint", "a11y-lint", "social-lint", "webmcp-lint"]


def run_linter(binary, linter, target, timeout):
    try:
        proc = subprocess.run([binary, linter, target, "--json"], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"exit_code": None, "data": None, "stderr": f"timeout tras {timeout}s", "raw_stdout": None}
    try:
        data = json.loads(proc.stdout) if proc.stdout.strip() else None
    except json.JSONDecodeError:
        data = None
    return {
        "exit_code": proc.returncode,
        "data": data,
        "stderr": proc.stderr.strip(),
        "raw_stdout": proc.stdout if data is None else None,
    }


def extract_findings(linter, data):
    if data is None:
        return []
    if linter == "social-lint":
        return data.get("findings", [])
    return data  # seo-lint/a11y-lint/webmcp-lint devuelven un array plano


def build_report(binary, target, timeout):
    report = {"target": target, "linters": {}, "summary": {"error": 0, "warning": 0, "info": 0}}
    for linter in LINTERS:
        result = run_linter(binary, linter, target, timeout)
        findings = extract_findings(linter, result["data"])
        entry = {"findings": findings, "exit_code": result["exit_code"]}
        if result["data"] is None and result["stderr"]:
            entry["error"] = result["stderr"]
        if linter == "social-lint" and result["data"]:
            entry["preview"] = result["data"].get("preview")
        report["linters"][linter] = entry
        for f in findings:
            sev = f.get("severity", "info")
            report["summary"][sev] = report["summary"].get(sev, 0) + 1
    return report


def render_markdown(report):
    lines = [f"# Auditoria de pagina (kite-lite) — {report['target']}", ""]
    s = report["summary"]
    lines.append(f"Errores: {s.get('error', 0)} | Warnings: {s.get('warning', 0)} | Info: {s.get('info', 0)}")
    lines.append("")
    for linter, info in report["linters"].items():
        lines.append(f"## {linter}")
        if info.get("error"):
            lines.append(f"No se pudo correr: {info['error']}")
        elif not info["findings"]:
            lines.append("Sin hallazgos.")
        else:
            lines.append("| Severidad | Mensaje |")
            lines.append("|---|---|")
            for f in info["findings"]:
                lines.append(f"| {f.get('severity', '?')} | {f.get('message', '')} |")
        if info.get("preview"):
            p = info["preview"]
            title = p.get("title") or "(sin titulo)"
            desc = (p.get("description") or "(sin descripcion)")[:80]
            image = p.get("image") or "(sin imagen)"
            lines.append("")
            lines.append(f"Preview social: titulo=\"{title}\", descripcion=\"{desc}\", imagen={image}")
        lines.append("")
    return "\n".join(lines)


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="URL, archivo .html, o page.json de kite-lite a auditar")
    parser.add_argument("--kite-lite-bin", help="Ruta al binario kite-lite. Por defecto, busca 'kite-lite' en PATH.")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout por linter en segundos (default 60)")
    parser.add_argument("--json", dest="json_out", help="Ruta de salida JSON")
    parser.add_argument("--markdown", dest="md_out", help="Ruta de salida Markdown")
    args = parser.parse_args()

    if args.kite_lite_bin:
        if not os.path.isfile(args.kite_lite_bin):
            raise SystemExit(f"[FAILED] --kite-lite-bin {args.kite_lite_bin} no existe.")
        binary = args.kite_lite_bin
    else:
        binary = shutil.which("kite-lite")
        if not binary:
            raise SystemExit("[FAILED] No se encontro el binario 'kite-lite' en PATH. Instalalo con "
                              "'cargo install kite-lite' o pasa --kite-lite-bin con la ruta.")

    report = build_report(binary, args.target, args.timeout)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
    if args.md_out:
        with open(args.md_out, "w", encoding="utf-8") as fh:
            fh.write(render_markdown(report))

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if report["summary"].get("error", 0) > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
