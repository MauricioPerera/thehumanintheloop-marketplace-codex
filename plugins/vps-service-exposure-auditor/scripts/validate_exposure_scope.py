"""Reject exposure-audit command plans that mutate the host or reveal secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "ufw allow", "ufw delete", "iptables -a", "iptables -d", "nft add", "nft delete",
    "docker publish", "docker run", "docker compose up", "docker compose down",
    "systemctl restart", "systemctl stop", "systemctl disable", "nginx -s reload",
    "curl -u", "authorization:", "bearer ", "password=", "token=", "api_key=",
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
