#!/usr/bin/env python3
"""Validate release notes and semantic version tag."""
import argparse, json, re, sys
from pathlib import Path

def validate(text, tag):
    errors = []
    if not re.fullmatch(r"v?\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", tag): errors.append("Tag is not a semantic version.")
    if len(text.split()) < 50: errors.append("Release notes must contain at least 50 words.")
    if not re.search(r"(?im)^##?\s*(features?|funcionalidades|changes|cambios)", text): errors.append("Missing changes/features section.")
    if not re.search(r"(?im)^##?\s*(fixes?|correcciones|bugs?)", text): errors.append("Missing fixes section, or explicitly document none.")
    if not re.search(r"(?i)(#\d+|https?://github\.com/[^\s/]+/[^\s/]+/(?:pull|issues)/\d+)", text): errors.append("Release notes need at least one linked PR or Issue.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]", text): errors.append("Possible credential in release notes.")
    return {"status": "PASSED" if not errors else "FAILED", "tag": tag, "word_count": len(text.split()), "errors": errors}

def main():
    args = argparse.ArgumentParser(); args.add_argument("--input", required=True, type=Path); args.add_argument("--tag", required=True); args.add_argument("--json", dest="json_path", type=Path); parsed = args.parse_args()
    result = validate(parsed.input.read_text(encoding="utf-8"), parsed.tag)
    if parsed.json_path: parsed.json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2)); return 0 if result["status"] == "PASSED" else 1
if __name__ == "__main__": sys.exit(main())
