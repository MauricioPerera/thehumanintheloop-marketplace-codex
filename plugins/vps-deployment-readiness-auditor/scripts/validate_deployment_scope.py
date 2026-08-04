"""Reject deployment-readiness plans that mutate services or expose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker pull", "docker compose pull", "docker compose up", "docker compose down",
    "docker compose restart", "docker restart", "docker stop", "docker rm", "docker prune",
    "docker exec", "docker run", "docker system prune", "migrate", "migration run",
    "systemctl restart", "systemctl stop", "systemctl start", "nginx -s reload",
    "ufw allow", "iptables -a", "nft add", "password=", "token=", "api_key=", "secret=",
    "authorization:", "bearer ", ".env",
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
