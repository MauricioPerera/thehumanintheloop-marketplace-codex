"""Ensure configuration reports do not contain obvious secret values."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
SECRET = re.compile(r"(?i)(password|secret|token|jwt|private[_-]?key|access[_-]?key)\s*[:=]\s*[^\s,;]+")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--report", required=True); args = parser.parse_args()
    text = Path(args.report).read_text(encoding="utf-8")
    matches = SECRET.findall(text)
    print({"status": "FAILED" if matches else "PASSED", "secret_like_fields": sorted(set(matches))})
    return 1 if matches else 0
if __name__ == "__main__": raise SystemExit(main())
