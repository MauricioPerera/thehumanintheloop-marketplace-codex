"""Reject topology-audit plans that mutate services or disclose credentials."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker exec", "docker restart", "docker stop", "docker rm", "docker compose up",
    "docker compose down", "systemctl restart", "systemctl stop", "systemctl start",
    "nginx -s reload", "ufw allow", "iptables -a", "nft add", "curl -u",
    "authorization:", "bearer ", "password=", "token=", "api_key=", "secret=",
    "psql ", "mysql ", "redis-cli",
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
