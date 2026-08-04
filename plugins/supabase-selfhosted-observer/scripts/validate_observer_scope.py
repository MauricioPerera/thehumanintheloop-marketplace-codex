"""Reject mutating or secret-reading commands in an observer plan."""
from __future__ import annotations
import argparse
from pathlib import Path

FORBIDDEN = ("docker exec", "docker restart", "docker rm", "docker compose up", "docker compose down", ".env", "docker inspect")
ALLOWED = ("docker ps", "docker compose ps", "docker stats", "df -h", "free -h", "uptime")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command-file", required=True)
    args = parser.parse_args()
    commands = [line.strip() for line in Path(args.command_file).read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
    failures = []
    for command in commands:
        lowered = command.lower()
        if any(token in lowered for token in FORBIDDEN) or not any(lowered.startswith(prefix) for prefix in ALLOWED):
            failures.append(command)
    print({"status": "FAILED" if failures else "PASSED", "commands": len(commands), "blocked": failures})
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
