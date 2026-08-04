"""Reject resource-limit plans that mutate Docker or disclose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker update", "docker restart", "docker stop", "docker kill", "docker pause",
    "docker rm", "docker run", "docker compose up", "docker compose down",
    "docker compose restart", "systemctl restart", "systemctl stop", "systemctl start",
    "cgcreate", "cgset", "iptables -a", "nft add", "ufw allow", "password=", "token=",
    "api_key=", "secret=", "authorization:", "bearer ", "cat .env",
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
