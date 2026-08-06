"""Reject configuration-drift plans that mutate the host or expose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker compose up", "docker compose down", "docker restart", "docker rm", "docker run",
    "systemctl restart", "systemctl stop", "systemctl start", "systemctl daemon-reload",
    "nginx -s reload", "service nginx reload", "ufw allow", "iptables -a", "nft add",
    "sed -i", "tee /etc", "cp .env", "password=", "token=", "api_key=", "secret=",
    "authorization:", "bearer ", "cat .env", "cat id_rsa",
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
