"""Require exact targets and confirmation for image changes or cleanup."""
from __future__ import annotations
import argparse
from pathlib import Path
MUTATIONS = ("docker pull", "docker rmi", "docker image prune", "docker system prune", "docker tag")
REQUIRED = ("images:", "space:", "impact:", "rollback:", "confirmation:")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--plan", required=True); args = parser.parse_args()
    lower = Path(args.plan).read_text(encoding="utf-8").lower(); mutation = any(x in lower for x in MUTATIONS)
    missing = [x for x in REQUIRED if x not in lower] if mutation else []
    print({"status": "FAILED" if missing else "PASSED", "mutation": mutation, "missing": missing})
    return 1 if missing else 0
if __name__ == "__main__": raise SystemExit(main())
