#!/usr/bin/env python3
"""Validate a GitHub Pull Request body before creation or update."""
import argparse, json, re, sys
from pathlib import Path

def validate(text):
    errors = []
    required = [("summary", r"(?im)^##?\s*(summary|resumen)"), ("scope", r"(?im)^##?\s*(scope|alcance|changes|cambios)"), ("validation", r"(?im)^##?\s*(validation|validaci[oó]n|tests?)"), ("risks", r"(?im)^##?\s*(risks?|riesgos)")]
    for label, pattern in required:
        if not re.search(pattern, text): errors.append(f"Missing {label} section.")
    if len(text.split()) < 80: errors.append("PR body must contain at least 80 words.")
    if not re.search(r"(?i)(passed|pass|successful|green|pasa|exitos|n/a|not run|no ejecutad)", text): errors.append("Missing explicit validation result.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]", text): errors.append("Possible credential in PR body.")
    return {"status": "PASSED" if not errors else "FAILED", "word_count": len(text.split()), "errors": errors}

def main():
    args = argparse.ArgumentParser(); args.add_argument("--input", required=True, type=Path); args.add_argument("--json", dest="json_path", type=Path); parsed = args.parse_args()
    result = validate(parsed.input.read_text(encoding="utf-8"))
    if parsed.json_path: parsed.json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2)); return 0 if result["status"] == "PASSED" else 1
if __name__ == "__main__": sys.exit(main())
