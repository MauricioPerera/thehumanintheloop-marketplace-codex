"""Require evidence and rollback fields for service mutations."""
from __future__ import annotations
import argparse
from pathlib import Path
MUTATING = ("restart", "up", "pull", "stop", "down", "prune", "rm", "volume")
REQUIRED = ("target:", "command:", "impact:", "rollback:", "confirmation:")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--plan", required=True); args = parser.parse_args()
    text = Path(args.plan).read_text(encoding="utf-8"); lower = text.lower()
    mutation = any(item in lower for item in MUTATING)
    missing = [field for field in REQUIRED if field not in lower] if mutation else []
    print({"status": "FAILED" if missing else "PASSED", "mutation": mutation, "missing": missing})
    return 1 if missing else 0
if __name__ == "__main__": raise SystemExit(main())
