#!/usr/bin/env python3
"""Instrumentos de Dockerfile best practices: 11 reglas duras y mecanicamente
verificables sobre un Dockerfile puntual.

Extraidas con el metodo Knowledge-Driven Development (kdd-book) de
https://docs.docker.com/build/building/best-practices/. La guia tiene muchas
mas recomendaciones ("should", "consider") que exigen juzgar el diseno del
servicio (una imagen por concern, base image confiable, USER solo "si el
servicio puede correr sin privilegios"); esas quedan en
scripts/knowledge.json como pila B, con su motivo. Estas 11 son las que la
guia expresa como instruccion dura ("always", "must") o cuya violacion es
un patron de texto sin ambiguedad (FROM sin tag, CMD en shell form, sudo
instalado, ADD en vez de COPY para un archivo local).

Sin dependencias externas: heuristicas de texto sobre el Dockerfile, no un
parser real del formato (que tampoco existe en la libreria estandar de
Python). Las continuaciones de linea con `\\` se unen antes de analizar,
igual que hace el propio parser de Docker.

Exit codes (convencion KDD):
  0  la propiedad se cumple
  1  no se cumple
  2  no se pudo verificar

Uso:
    python dockerfile_checks.py --rule fromlatest <Dockerfile> [...]
    python dockerfile_checks.py --list
"""
import argparse
import json
import re
import sys
from pathlib import Path

__all__ = [
    "check_fromlatest", "check_aptcombine", "check_aptcleanup", "check_execform",
    "check_userroot", "check_sudoinstall", "check_workdirabs", "check_cdinstead",
    "check_addvscopy", "check_pipefail", "check_dockerignore",
]

ARCHIVE_EXT = (".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", ".zip")


def _hit(path, lineno, line, detail):
    return {"file": str(path), "line": lineno, "text": line.strip(), "detail": detail}


def _logical_lines(path):
    """Une continuaciones de linea con `\\` en 'lineas logicas', preservando
    el numero de la primera linea fisica de cada una."""
    raw = Path(path).read_text(encoding="utf-8").splitlines()
    logical = []
    buf, start = "", None
    for i, line in enumerate(raw, start=1):
        stripped = line.rstrip()
        if start is None:
            start = i
        if stripped.endswith("\\"):
            buf += stripped[:-1] + " "
            continue
        buf += stripped
        logical.append((start, buf))
        buf, start = "", None
    if buf:
        logical.append((start, buf))
    return logical


def check_fromlatest(path):
    hits = []
    for lineno, line in _logical_lines(path):
        m = re.match(r"^\s*FROM\s+(?:--platform=\S+\s+)?(\S+)", line, re.IGNORECASE)
        if not m:
            continue
        ref = m.group(1)
        if "@sha256:" in ref:
            continue
        if ":" not in ref.split("/")[-1]:
            hits.append(_hit(path, lineno, line, "FROM sin tag (equivale a :latest, no reproducible)"))
        elif ref.endswith(":latest"):
            hits.append(_hit(path, lineno, line, "FROM con tag :latest explicito, no reproducible"))
    return hits


def check_aptcombine(path):
    hits = []
    for lineno, line in _logical_lines(path):
        if not re.match(r"^\s*RUN\b", line, re.IGNORECASE):
            continue
        if re.search(r"apt-get\s+update", line) and not re.search(r"apt-get\s+install", line):
            hits.append(_hit(path, lineno, line, "apt-get update sin apt-get install en el mismo RUN (rompe cache busting)"))
    return hits


def check_aptcleanup(path):
    hits = []
    for lineno, line in _logical_lines(path):
        if not re.match(r"^\s*RUN\b", line, re.IGNORECASE):
            continue
        if re.search(r"apt-get\s+install", line) and "/var/lib/apt/lists" not in line:
            hits.append(_hit(path, lineno, line, "apt-get install sin limpiar /var/lib/apt/lists/* en el mismo RUN"))
    return hits


def check_execform(path):
    hits = []
    for lineno, line in _logical_lines(path):
        m = re.match(r"^\s*(CMD|ENTRYPOINT)\s+(.*)$", line, re.IGNORECASE)
        if not m:
            continue
        arg = m.group(2).strip()
        if not arg.startswith("["):
            hits.append(_hit(path, lineno, line, f"{m.group(1).upper()} en shell form; usa exec form [\"executable\", \"param\"]"))
    return hits


def check_userroot(path):
    hits = []
    for lineno, line in _logical_lines(path):
        m = re.match(r"^\s*USER\s+(\S+)", line, re.IGNORECASE)
        if m and m.group(1).strip('"\'').lower() in ("root", "0"):
            hits.append(_hit(path, lineno, line, "USER root explicito"))
    return hits


def check_sudoinstall(path):
    hits = []
    for lineno, line in _logical_lines(path):
        if re.search(r"(?<![.\w-])sudo\b", line, re.IGNORECASE):
            hits.append(_hit(path, lineno, line, "instala o invoca sudo; evitalo (problemas de TTY y de capas)"))
    return hits


def check_workdirabs(path):
    hits = []
    for lineno, line in _logical_lines(path):
        m = re.match(r"^\s*WORKDIR\s+(\S+)", line, re.IGNORECASE)
        if m:
            wd = m.group(1).strip('"\'')
            if not (wd.startswith("/") or wd.startswith("$")):
                hits.append(_hit(path, lineno, line, "WORKDIR con ruta relativa; usa siempre una ruta absoluta"))
    return hits


def check_cdinstead(path):
    hits = []
    for lineno, line in _logical_lines(path):
        if re.match(r"^\s*RUN\b", line, re.IGNORECASE) and re.search(r"(?<![.\w-])cd\s+\S+\s*&&", line):
            hits.append(_hit(path, lineno, line, "RUN cd ... &&; usa WORKDIR en vez de cambiar de directorio en RUN"))
    return hits


def check_addvscopy(path):
    hits = []
    for lineno, line in _logical_lines(path):
        m = re.match(r"^\s*ADD\s+(?:--\S+\s+)*(\S+)", line, re.IGNORECASE)
        if not m:
            continue
        src = m.group(1).strip('"\'')
        if re.match(r"^https?://", src, re.IGNORECASE):
            continue
        if src.lower().endswith(ARCHIVE_EXT):
            continue
        hits.append(_hit(path, lineno, line, "ADD para un archivo/directorio local que no es URL ni archivo comprimido; usa COPY"))
    return hits


def check_pipefail(path):
    hits = []
    for lineno, line in _logical_lines(path):
        if not re.match(r"^\s*RUN\b", line, re.IGNORECASE):
            continue
        body = line
        has_pipe = bool(re.search(r"[^|]\|(?!\|)", body))
        if has_pipe and "set -o pipefail" not in body and "SHELL" not in body:
            hits.append(_hit(path, lineno, line, "RUN con pipe '|' sin 'set -o pipefail'; un fallo intermedio no rompe el build"))
    return hits


def check_dockerignore(path):
    p = Path(path)
    ignore = p.parent / ".dockerignore"
    if ignore.exists():
        return []
    return [{"file": str(p.parent / ".dockerignore"), "line": None, "text": None,
              "detail": "no existe .dockerignore junto al Dockerfile"}]


RULES = {
    "fromlatest": check_fromlatest,
    "aptcombine": check_aptcombine,
    "aptcleanup": check_aptcleanup,
    "execform": check_execform,
    "userroot": check_userroot,
    "sudoinstall": check_sudoinstall,
    "workdirabs": check_workdirabs,
    "cdinstead": check_cdinstead,
    "addvscopy": check_addvscopy,
    "pipefail": check_pipefail,
    "dockerignore": check_dockerignore,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule", choices=sorted(RULES))
    parser.add_argument("--list", action="store_true")
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    if args.list:
        print("\n".join(sorted(RULES)))
        return 0

    if not args.rule or not args.files:
        parser.error("--rule y al menos un archivo son requeridos (o usa --list)")

    check = RULES[args.rule]
    all_hits = []
    unverifiable = []
    for f in args.files:
        p = Path(f)
        if not p.exists():
            unverifiable.append(str(p))
            continue
        all_hits.extend(check(p))

    result = {
        "rule": args.rule,
        "status": "NO VERIFICABLE" if (unverifiable and len(unverifiable) == len(args.files)) else ("FAILED" if all_hits else "PASSED"),
        "hits": all_hits,
        "unverifiable_files": unverifiable,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["status"] == "NO VERIFICABLE":
        return 2
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main())
