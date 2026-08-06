"""Reject observability-audit plans that install, mutate, or disclose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "apt install", "apt-get install", "yum install", "dnf install", "docker pull",
    "docker run", "docker compose up", "docker compose down", "systemctl enable",
    "systemctl disable", "systemctl restart", "systemctl stop", "systemctl start",
    "kubectl apply", "helm install", "curl -u", "authorization:", "bearer ",
    "password=", "token=", "api_key=", "secret=", "webhook",
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
