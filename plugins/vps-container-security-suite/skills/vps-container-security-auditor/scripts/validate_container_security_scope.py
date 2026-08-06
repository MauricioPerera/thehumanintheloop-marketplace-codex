"""Reject container-security plans that mutate Docker or disclose secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker restart", "docker stop", "docker kill", "docker rm", "docker run",
    "docker compose up", "docker compose down", "docker compose restart", "docker update",
    "docker exec", "docker commit", "docker push", "docker pull", "aa-enforce",
    "apparmor_parser", "setcap", "iptables -a", "nft add", "ufw allow",
    "password=", "token=", "api_key=", "secret=", "authorization:", "bearer ",
    "cat .env", "docker inspect --format '{{range .Config.Env",
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
