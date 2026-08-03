#!/usr/bin/env python3
"""Deterministic checks for a CV tailored to a specific job offer."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STOPWORDS = {"about", "after", "being", "from", "have", "into", "that", "their", "this", "with", "your", "para", "como", "desde", "esta", "este", "sobre", "entre", "tiene", "debe", "una", "los", "las", "del", "que"}
FORBIDDEN = re.compile(r"\b(invented|fabricated|made[- ]up|inventado|fabricado|ficticio|sin evidencia)\b", re.I)
SECRET = re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA|OPENSSH|PRIVATE) KEY-----)")
NUMBER = re.compile(r"\b\d{2,}(?:[.,]\d+)?%?\b")
YEAR = re.compile(r"\b(?:19|20)\d{2}\b")


def words(text: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ][A-Za-zÁÉÍÓÚáéíóúÑñ+#.-]{4,}", text) if word.lower() not in STOPWORDS}


def validate(cv: str, job: str, output: str) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    cv_years = set(YEAR.findall(cv))
    unsupported_years = sorted(set(YEAR.findall(output)) - cv_years)
    if unsupported_years:
        errors.append(f"Years not evidenced in CV: {', '.join(unsupported_years)}")
    unsupported_numbers = sorted(set(NUMBER.findall(output)) - set(NUMBER.findall(cv)) - set(NUMBER.findall(job)))
    if unsupported_numbers:
        errors.append(f"Numeric claims not evidenced by CV or offer: {', '.join(unsupported_numbers)}")
    if FORBIDDEN.search(output):
        errors.append("Output contains fabrication-related language")
    if SECRET.search(output):
        errors.append("Output contains a possible secret or private key")
    headings = {line.lstrip("#").strip().lower().rstrip(":") for line in output.splitlines() if line.startswith("#")}
    if not any("experience" in heading or "experiencia" in heading for heading in headings):
        warnings.append("Missing Experience/Experiencia heading")
    if not any("skill" in heading or "habilidad" in heading or "competencia" in heading for heading in headings):
        warnings.append("Missing Skills/Habilidades heading")
    job_words = words(job)
    output_words = words(output)
    keywords = sorted(job_words & output_words)
    missing = sorted(job_words - output_words)
    coverage = len(keywords) / len(job_words) if job_words else 0.0
    if coverage < 0.25:
        warnings.append(f"Low vocabulary overlap with offer: {coverage:.0%}")
    word_count = len(output.split())
    if word_count < 150:
        errors.append("Tailored CV is too short: fewer than 150 words")
    if word_count > 1500:
        warnings.append("Tailored CV exceeds 1500 words; review ATS readability")
    return {"status": "FAILED" if errors else "PASSED", "word_count": word_count, "keyword_coverage": round(coverage, 3), "keywords_found": keywords, "keywords_missing": missing[:50], "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cv", type=Path, required=True)
    parser.add_argument("--job", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = validate(args.cv.read_text(encoding="utf-8"), args.job.read_text(encoding="utf-8"), args.output.read_text(encoding="utf-8"))
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")
    return 1 if report["status"] == "FAILED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
