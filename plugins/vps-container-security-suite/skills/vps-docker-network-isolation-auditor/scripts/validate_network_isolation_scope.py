"""Reject Docker network-audit plans that mutate networking or disclose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker network create", "docker network rm", "docker network connect", "docker network disconnect",
    "docker network prune", "docker exec", "docker run", "docker restart", "docker stop",
    "docker compose up", "docker compose down", "iptables -a", "nft add", "ufw allow",
    "curl -u", "authorization:", "bearer ", "password=", "token=", "api_key=", "secret=",
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
