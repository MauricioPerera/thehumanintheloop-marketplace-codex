"""Require bounded, redacted log diagnostics."""
from __future__ import annotations
import argparse
from pathlib import Path
FORBIDDEN = ("--env", "docker exec", "docker restart", "docker rm", ".env", "password=", "token=", "api_key=", "secret=")
REQUIRED = ("since", "limit", "redact")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--plan", required=True); args = parser.parse_args()
    lower = Path(args.plan).read_text(encoding="utf-8").lower(); blocked = [x for x in FORBIDDEN if x in lower]
    missing = [x for x in REQUIRED if x not in lower]
    print({"status": "FAILED" if blocked or missing else "PASSED", "blocked": blocked, "missing": missing})
    return 1 if blocked or missing else 0
if __name__ == "__main__": raise SystemExit(main())
