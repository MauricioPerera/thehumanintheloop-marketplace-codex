"""Reject storage plans that read data or remove resources."""
from __future__ import annotations
import argparse
from pathlib import Path
FORBIDDEN = ("docker volume rm", "docker network rm", "cat /", ".env", "secret", "password", "token")
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--command-file", required=True); args = parser.parse_args()
    commands = [x.strip() for x in Path(args.command_file).read_text(encoding="utf-8").splitlines() if x.strip()]
    blocked = [x for x in commands if any(y in x.lower() for y in FORBIDDEN)]
    print({"status": "FAILED" if blocked else "PASSED", "commands": len(commands), "blocked": blocked})
    return 1 if blocked else 0
if __name__ == "__main__": raise SystemExit(main())
