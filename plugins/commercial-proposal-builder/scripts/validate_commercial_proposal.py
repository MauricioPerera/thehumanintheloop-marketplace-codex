#!/usr/bin/env python3
"""Deterministic checks for a requirements-based commercial proposal."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STOPWORDS = {"about", "after", "being", "from", "have", "into", "that", "their", "this", "with", "your", "para", "como", "desde", "esta", "este", "sobre", "entre", "tiene", "debe", "una", "los", "las", "del", "que", "por"}
NUMBER = re.compile(r"\b\d{2,}(?:[.,]\d+)?%?\b|(?:USD|EUR|MXN|€|\$)\s?\d+(?:[.,]\d+)?", re.I)
FORBIDDEN = re.compile(r"\b(guaranteed|risk[- ]free|100% assured|garantizado|sin riesgo|100% asegurado)\b", re.I)
SECRET = re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA|OPENSSH|PRIVATE) KEY-----)")


def words(text: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ][A-Za-zÁÉÍÓÚáéíóúÑñ+#.-]{4,}", text) if word.lower() not in STOPWORDS}


def validate(requirements: str, source: str, output: str) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    source_material = f"{requirements}\n{source}"
    unsupported_numbers = sorted(set(NUMBER.findall(output)) - set(NUMBER.findall(source_material)))
    if unsupported_numbers:
        errors.append(f"Commercial numbers not evidenced by inputs: {', '.join(unsupported_numbers)}")
    if FORBIDDEN.search(output):
        errors.append("Proposal contains an absolute guarantee or prohibited promise")
    if SECRET.search(output):
        errors.append("Proposal contains a possible secret or private key")
    required_sections = {
        "executive summary": ("executive summary", "resumen ejecutivo"),
        "scope": ("scope", "alcance"),
        "deliverables": ("deliverables", "entregables"),
        "timeline": ("timeline", "cronograma", "plazo"),
        "investment": ("investment", "inversión", "inversion", "pricing"),
        "assumptions": ("assumptions", "supuestos", "riesgos"),
        "next steps": ("next steps", "próximos pasos", "proximos pasos"),
    }
    lowered = output.lower()
    missing_sections = [name for name, variants in required_sections.items() if not any(variant in lowered for variant in variants)]
    if missing_sections:
        errors.append(f"Missing proposal sections: {', '.join(missing_sections)}")
    requirement_words = words(requirements)
    output_words = words(output)
    covered = sorted(requirement_words & output_words)
    missing = sorted(requirement_words - output_words)
    coverage = len(covered) / len(requirement_words) if requirement_words else 0.0
    if coverage < 0.35:
        warnings.append(f"Low requirement vocabulary coverage: {coverage:.0%}")
    if "open item" not in lowered and "pendiente" not in lowered and missing:
        warnings.append("Uncovered requirement vocabulary is not explicitly marked as pending")
    word_count = len(output.split())
    if word_count < 200:
        errors.append("Proposal is too short: fewer than 200 words")
    return {"status": "FAILED" if errors else "PASSED", "word_count": word_count, "requirement_coverage": round(coverage, 3), "requirements_covered": covered, "requirements_missing": missing[:50], "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--requirements", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = validate(args.requirements.read_text(encoding="utf-8"), args.source.read_text(encoding="utf-8"), args.output.read_text(encoding="utf-8"))
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")
    return 1 if report["status"] == "FAILED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
