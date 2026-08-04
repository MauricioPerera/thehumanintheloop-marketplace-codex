"""Reject restore-verification plans that mutate data or disclose backup contents."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker volume rm", "docker system prune", "docker compose down", "docker compose up",
    "pg_restore", "mysql <", "mongorestore", "drop database", "dropdb", "rm -rf",
    "shred", "truncate", "delete snapshot", "restore --force", "kubectl apply",
    "curl -u", "authorization:", "bearer ", "password=", "token=", "api_key=",
    "secret=", "cat backup", "tar -x", "unzip -o",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command-file", required=True)
    args = parser.parse_args()
    lines = Path(args.command_file).read_text(encoding="utf-8").splitlines()
    blocked = [line for line in lines if any(term in line.lower() for term in FORBIDDEN)]
    print({"status": "FAILED" if blocked else "PASSED", "blocked": blocked})
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
