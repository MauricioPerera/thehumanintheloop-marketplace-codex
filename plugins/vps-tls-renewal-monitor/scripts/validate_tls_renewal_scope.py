"""Reject TLS-renewal monitoring plans that issue certificates or mutate proxies."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "certbot renew", "certbot certonly", "certbot run", "acme.sh --issue", "acme.sh --renew",
    "systemctl reload", "systemctl restart", "nginx -s reload", "service nginx reload",
    "nginx -t &&", "tee /etc/nginx", "cp *.key", "rm -f", "ufw allow", "iptables -a",
    "password=", "token=", "api_key=", "secret=", "authorization:", "bearer ",
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
