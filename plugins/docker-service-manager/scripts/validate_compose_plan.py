"""Require evidence, confirmation and rollback for Compose mutations."""
from __future__ import annotations
import argparse
from pathlib import Path
MUTATIONS = (" compose up", " compose down", " restart", " stop", " pull", " rm")
REQUIRED = ("target:", "preflight:", "impact:", "rollback:", "confirmation:")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--plan", required=True); args = parser.parse_args()
    text = Path(args.plan).read_text(encoding="utf-8"); lower = text.lower(); mutation = any(x in lower for x in MUTATIONS)
    missing = [x for x in REQUIRED if x not in lower] if mutation else []
    print({"status": "FAILED" if missing else "PASSED", "mutation": mutation, "missing": missing})
    return 1 if missing else 0
if __name__ == "__main__": raise SystemExit(main())
