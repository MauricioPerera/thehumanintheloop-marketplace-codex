"""Require compatibility, backup and rollback evidence for upgrade plans."""
from __future__ import annotations
import argparse
from pathlib import Path

REQUIRED = ("current:", "target:", "compatibility:", "backup:", "rollback:", "verification:")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    args = parser.parse_args()
    text = Path(args.plan).read_text(encoding="utf-8").lower()
    missing = [field for field in REQUIRED if field not in text]
    print({"status": "FAILED" if missing else "PASSED", "missing": missing})
    return 1 if missing else 0

if __name__ == "__main__":
    raise SystemExit(main())
