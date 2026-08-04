"""Reject backup-job monitoring plans that execute jobs or disclose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "systemctl start", "systemctl restart", "systemctl stop", "service ", "cron ",
    "run-parts", "docker exec", "docker compose up", "pg_dump", "mysqldump",
    "tar -c", "rsync ", "rclone copy", "aws s3 cp", "gcloud storage cp",
    "restore", "prune", "rm -f", "rm -rf", "password=", "token=", "api_key=",
    "secret=", "authorization:", "bearer ", "cat .env",
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
