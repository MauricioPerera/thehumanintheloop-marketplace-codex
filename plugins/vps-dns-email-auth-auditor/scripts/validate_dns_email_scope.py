"""Reject DNS/email-audit plans that mutate zones or expose credentials."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "nsupdate", "rndc addzone", "rndc reload", "cloudflare dns", "aws route53 change",
    "gcloud dns record-sets update", "az network dns record-set", "sendmail", "swaks",
    "curl -u", "authorization:", "bearer ",
    "password=", "token=", "api_key=", "secret=", "private_key", "nameserver add",
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
