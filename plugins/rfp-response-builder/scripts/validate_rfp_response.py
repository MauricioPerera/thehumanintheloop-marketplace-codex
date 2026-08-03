#!/usr/bin/env python3
"""Deterministic structural linter for RFP responses."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQ_RE = re.compile(r"(?im)^\s*(?:REQ|RFP)[-_ ]?\d+\b|^\s*[A-Z]{1,4}\d{1,3}\b")
ID_RE = re.compile(r"(?i)\b(?:REQ|RFP)[-_ ]?\d+\b|\b[A-Z]{1,4}\d{1,3}\b")
NUMBER_RE = re.compile(r"(?<![A-Za-z])(?:\$|€|USD\s*)?\d{1,3}(?:[,.]\d{3})*(?:[,.]\d+)?\s*%?(?![A-Za-z])")
SECRET_RE = re.compile(r"(?i)(?:api[_ -]?key|secret|password|token)\s*[:=]\s*[^\s,;]+")
FORBIDDEN_RE = re.compile(r"(?i)\b(?:garantiz(?:ado|amos|ar)|guarantee(?:d)?|100\s*%|sin\s+riesgo|no\s+risk)\b")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_number(value: str) -> str:
    return re.sub(r"\s+", "", value).replace(".", "").replace(",", ".").lower()


def numbers(text: str) -> set[str]:
    return {normalize_number(match.group(0)) for match in NUMBER_RE.finditer(text)}


def requirement_ids(text: str) -> list[str]:
    found: list[str] = []
    for line in text.splitlines():
        if REQ_RE.search(line):
            match = ID_RE.search(line)
            if match:
                identifier = re.sub(r"[-_ ]", "-", match.group(0).upper())
                if identifier not in found:
                    found.append(identifier)
    return found


def report(rfp: str, source: str, output: str) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    ids = requirement_ids(rfp)
    output_upper = output.upper()
    covered = [identifier for identifier in ids if identifier in output_upper]

    missing = [identifier for identifier in ids if identifier not in output_upper]
    if missing:
        errors.append("Requisitos sin cobertura explícita: " + ", ".join(missing))
    if not ids:
        warnings.append("No se detectaron identificadores de requisito; revisa manualmente la trazabilidad.")

    unsupported = sorted(numbers(output) - numbers(rfp + "\n" + source))
    if unsupported:
        errors.append("Cifras o porcentajes no presentes en las fuentes: " + ", ".join(unsupported))
    if FORBIDDEN_RE.search(output):
        errors.append("La respuesta contiene promesas absolutas o garantías no autorizadas.")
    if SECRET_RE.search(output):
        errors.append("La respuesta parece contener secretos o credenciales.")

    required_sections = {
        "matriz de cumplimiento": r"(?i)matriz de cumplimiento|compliance matrix",
        "alcance": r"(?i)\b(?:alcance|scope)\b",
        "evidencia": r"(?i)\b(?:evidencia|evidence)\b",
        "pendientes": r"(?i)pendientes|preguntas abiertas|open items|excepciones|exceptions",
        "entrega": r"(?i)implementaci[oó]n|delivery|entrega|deliverables",
    }
    for label, pattern in required_sections.items():
        if not re.search(pattern, output):
            errors.append(f"Falta la sección requerida: {label}.")

    statuses = r"(?i)\b(?:compliant|partial|non-compliant|open item|cumple|parcial|no cumple|pendiente)\b"
    if not re.search(statuses, output):
        errors.append("La matriz no declara estados de cumplimiento reconocibles.")
    word_count = len(re.findall(r"\S+", output))
    if word_count < 200:
        errors.append(f"La respuesta es demasiado corta: {word_count} palabras; mínimo 200.")

    return {
        "status": "PASSED" if not errors else "FAILED",
        "word_count": word_count,
        "requirements_total": len(ids),
        "requirements_covered": len(covered),
        "coverage": round(len(covered) / len(ids), 3) if ids else None,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rfp", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args()
    result = report(read(args.rfp), read(args.source), read(args.output))
    if args.json_path:
        args.json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASSED" else 1


if __name__ == "__main__":
    sys.exit(main())
