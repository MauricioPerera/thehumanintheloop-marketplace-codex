"""Allow only bounded read-only Docker observer commands."""
from __future__ import annotations
import argparse
from pathlib import Path

ALLOWED = ("docker version", "docker info", "docker ps", "docker stats", "docker system df", "docker inspect --format", "df -h", "free -h", "uptime")
FORBIDDEN = ("docker exec", "docker restart", "docker rm", "docker compose up", "docker compose down", "prune", ".env")

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--command-file", required=True); args = parser.parse_args()
    commands = [line.strip() for line in Path(args.command_file).read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
    blocked = [cmd for cmd in commands if any(x in cmd.lower() for x in FORBIDDEN) or not any(cmd.lower().startswith(x) for x in ALLOWED)]
    print({"status": "FAILED" if blocked else "PASSED", "commands": len(commands), "blocked": blocked})
    return 1 if blocked else 0
if __name__ == "__main__": raise SystemExit(main())
