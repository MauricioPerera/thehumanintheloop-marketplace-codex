#!/usr/bin/env python3
"""Validate the hard contract of a DESIGN.md analysis."""
import argparse, json, re, sys
from pathlib import Path

REQUIRED = ("Contrato duro", "Components", "Validation Contract")

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("design_md"); parser.add_argument("--json", dest="contract")
    args = parser.parse_args(); path = Path(args.design_md); errors=[]; text=path.read_text(encoding="utf-8") if path.exists() else ""
    if not path.exists(): errors.append(f"Missing {path}")
    for heading in REQUIRED:
        if heading not in text and heading.lower() not in text.lower(): errors.append(f"Missing required section or marker: {heading}")
    if len(re.findall(r"^# ", text, re.MULTILINE)) != 1: errors.append("DESIGN.md must contain exactly one H1")
    if args.contract:
        try:
            contract=json.loads(Path(args.contract).read_text(encoding="utf-8"))
            if not isinstance(contract, dict): errors.append("design-system.json must be an object")
            if isinstance(contract, dict) and not any(key in contract for key in ("tokens", "designTokens", "colors", "typography", "components")): errors.append("design-system.json needs tokens, colors, typography or components")
        except Exception as exc: errors.append(f"Invalid design-system.json: {exc}")
    result={"status":"FAILED" if errors else "PASSED", "errors":errors, "wordCount":len(re.findall(r"\b\w+\b", text))}
    print(json.dumps(result, indent=2, ensure_ascii=False)); return 1 if errors else 0
if __name__ == "__main__": sys.exit(main())
