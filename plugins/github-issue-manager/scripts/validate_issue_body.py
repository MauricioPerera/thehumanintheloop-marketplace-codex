#!/usr/bin/env python3
"""Validate a GitHub Issue body before submission."""
import argparse, json, re, sys
from pathlib import Path

def validate(text):
    errors = []
    if len(text.split()) < 30: errors.append("Issue body must contain at least 30 words.")
    if not re.search(r"(?im)^##?\s*(context|contexto|problem|problema)", text): errors.append("Missing context/problem section.")
    if not re.search(r"(?im)^##?\s*(expected|esperado|acceptance|aceptaci[oó]n)", text): errors.append("Missing expected behavior or acceptance criteria.")
    if not re.search(r"(?im)^##?\s*(steps|pasos|reproduction|reproducci[oó]n)", text): errors.append("Missing reproduction steps or requested steps.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]", text): errors.append("Possible credential in issue body.")
    return {"status": "PASSED" if not errors else "FAILED", "word_count": len(text.split()), "errors": errors}

def main():
    p = argparse.ArgumentParser(); p.add_argument("--input", required=True, type=Path); p.add_argument("--json", dest="json_path", type=Path)
    result = validate(p.parse_args().input.read_text(encoding="utf-8"))
    if p.parse_args().json_path: p.parse_args().json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2)); return 0 if result["status"] == "PASSED" else 1
if __name__ == "__main__": sys.exit(main())
