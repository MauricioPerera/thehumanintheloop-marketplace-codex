#!/usr/bin/env python3
"""Instrumentos del Google TypeScript Style Guide: 17 reglas duras y mecanicamente
verificables sobre un archivo .ts puntual.

Extraidas con el metodo Knowledge-Driven Development (kdd-book) de la fuente
https://google.github.io/styleguide/tsguide.html. De las reglas normativas de
la guia, estas 17 son las que se expresan como prohibicion dura ("must not",
"never", "do not", "always") Y son detectables sin ambiguedad sobre texto: no
dependen de saber si un `any` puntual estaba justificado, ni de juzgar si una
funcion deberia haber sido arrow o declarada, ni de flujo de datos. Esas quedan
en `scripts/knowledge.json` como pila B, con su motivo.

Sin dependencias externas: son heuristicas de texto (regex y conteo de llaves),
no un parser real de TypeScript. Un `#` dentro de un string, o un `var` dentro
de un comentario de bloque, pueden producir un falso positivo puntual; por eso
cada corrida imprime la linea exacta para que la revises antes de actuar.

Exit codes (convencion KDD):
  0  la propiedad se cumple
  1  no se cumple
  2  no se pudo verificar

Uso:
    python typescript_checks.py --rule sinvar <archivo.ts> [...]
    python typescript_checks.py --list
"""
import argparse
import json
import re
import sys
from pathlib import Path

__all__ = [
    "check_sinvar", "check_exportdefault", "check_exportmutable", "check_require",
    "check_namespace", "check_arrayctor", "check_objectctor", "check_clasepuntocoma",
    "check_campoprivado", "check_constenum", "check_wrapper", "check_debugger",
    "check_with", "check_tsignore", "check_tripleigual", "check_comillas",
    "check_guionbajo",
]


def _hit(path, lineno, line, detail):
    return {"file": str(path), "line": lineno, "text": line.strip(), "detail": detail}


def _scan(path, pattern, detail, flags=0):
    """Escanea el archivo linea por linea con una regex y devuelve los hits."""
    text = Path(path).read_text(encoding="utf-8")
    hits = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if re.search(pattern, line, flags):
            hits.append(_hit(path, lineno, line, detail))
    return hits


def check_sinvar(path):
    """Never use var. https://google.github.io/styleguide/tsguide.html#local-variable-declarations"""
    return _scan(path, r"(?<![.\w$])var\s+[A-Za-z_$]", "declaracion con 'var' en vez de const/let")


def check_exportdefault(path):
    """Do not use default exports."""
    return _scan(path, r"(?<![.\w$])export\s+default\b", "export default no permitido")


def check_exportmutable(path):
    """export let is not allowed (mutable exports)."""
    return _scan(path, r"(?<![.\w$])export\s+(let|var)\s", "export mutable (export let/var)")


def check_require(path):
    """Code must use ES module imports, not require()."""
    return _scan(path, r"(?<![.\w$])require\s*\(", "import via require() en vez de import/export")


def check_namespace(path):
    """Code must not use namespace/module to declare namespaces."""
    return _scan(path, r"(?<![.\w$])(namespace|module)\s+[A-Za-z_$][\w$.]*\s*\{", "declaracion namespace/module (usa modulos ES + imports)")


def check_arrayctor(path):
    """Do not use the Array() constructor."""
    return _scan(path, r"(?<![.\w$])(new\s+)?Array\s*\(", "constructor Array() en vez de literal []")


def check_objectctor(path):
    """The Object constructor is banned; use the object literal ({}) instead."""
    return _scan(path, r"(?<![.\w$])new\s+Object\s*\(", "constructor new Object() en vez de literal {}")


def check_campoprivado(path):
    """Do not use private fields (private identifiers, #foo)."""
    return _scan(path, r"(?<![.\w$])#[A-Za-z_]\w*", "campo privado nativo (#foo); usa 'private' de TypeScript")


def check_constenum(path):
    """Code must not use const enum."""
    return _scan(path, r"(?<![.\w$])const\s+enum\b", "const enum no permitido, usa enum")


def check_wrapper(path):
    """Never invoke the wrapper types (String, Boolean, Number) as constructors."""
    return _scan(path, r"(?<![.\w$])new\s+(String|Number|Boolean)\s*\(", "wrapper type invocado como constructor")


def check_debugger(path):
    """Debugger statements must not be included in production code."""
    return _scan(path, r"(?<![.\w$])debugger\s*;", "sentencia debugger presente")


def check_with(path):
    """Do not use the with keyword."""
    return _scan(path, r"(?<![.\w$])with\s*\(", "uso del keyword with")


def check_tsignore(path):
    """Do not use @ts-ignore."""
    return _scan(path, r"@ts-ignore\b", "@ts-ignore suprime errores de tipos sin justificacion")


def check_tripleigual(path):
    """Always use === and !==, not == and !=, except for comparisons to null/undefined."""
    text = Path(path).read_text(encoding="utf-8")
    hits = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in re.finditer(r"(?<![=!<>])(==|!=)(?!=)", line):
            window = line[max(0, m.start() - 12):m.end() + 12]
            if re.search(r"(?:==|!=)\s*(null|undefined)\b", window):
                continue
            hits.append(_hit(path, lineno, line, f"'{m.group(1)}' en vez de '{m.group(1)}='"))
    return hits


def check_clasepuntocoma(path):
    """Class declarations must not be terminated with semicolons."""
    text = Path(path).read_text(encoding="utf-8")
    hits = []
    depth = 0
    in_class = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if re.search(r"(?<![.\w$])class\s+[A-Za-z_$]", line) and depth == 0:
            in_class = True
        if in_class:
            depth += line.count("{") - line.count("}")
            if depth <= 0 and "}" in line:
                if re.search(r"\}\s*;", line):
                    hits.append(_hit(path, lineno, line, "llave de cierre de clase seguida de ';'"))
                in_class = False
                depth = 0
    return hits


def check_comillas(path):
    """Ordinary string literals use single quotes; double quotes only to avoid escaping a single quote."""
    text = Path(path).read_text(encoding="utf-8")
    hits = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in re.finditer(r'"([^"\\]|\\.)*"', line):
            content = m.group(0)[1:-1]
            if "'" in content.replace("\\'", ""):
                continue
            hits.append(_hit(path, lineno, line, "string literal con comillas dobles sin necesidad de escapar una simple"))
    return hits


def check_guionbajo(path):
    """Identifiers must not use _ as a prefix or suffix."""
    text = Path(path).read_text(encoding="utf-8")
    hits = []
    decl_re = re.compile(r"(?:const|let|var|function\*?|class|interface|type)\s+(_[A-Za-z_$][\w$]*|[A-Za-z$][\w$]*_)\b")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in decl_re.finditer(line):
            hits.append(_hit(path, lineno, line, f"identificador '{m.group(1)}' con guion bajo de prefijo/sufijo"))
    return hits


RULES = {
    "sinvar": check_sinvar,
    "exportdefault": check_exportdefault,
    "exportmutable": check_exportmutable,
    "require": check_require,
    "namespace": check_namespace,
    "arrayctor": check_arrayctor,
    "objectctor": check_objectctor,
    "clasepuntocoma": check_clasepuntocoma,
    "campoprivado": check_campoprivado,
    "constenum": check_constenum,
    "wrapper": check_wrapper,
    "debugger": check_debugger,
    "with": check_with,
    "tsignore": check_tsignore,
    "tripleigual": check_tripleigual,
    "comillas": check_comillas,
    "guionbajo": check_guionbajo,
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
        if not p.exists() or p.suffix not in (".ts",):
            unverifiable.append(str(p))
            continue
        all_hits.extend(check(p))

    result = {
        "rule": args.rule,
        "status": "NO VERIFICABLE" if (unverifiable and not all_hits and len(unverifiable) == len(args.files)) else ("FAILED" if all_hits else "PASSED"),
        "hits": all_hits,
        "unverifiable_files": unverifiable,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["status"] == "NO VERIFICABLE":
        return 2
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main())
