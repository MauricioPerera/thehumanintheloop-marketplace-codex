"""Reject image-provenance plans that mutate Docker or disclose registry secrets."""
from pathlib import Path
import argparse

FORBIDDEN = (
    "docker pull", "docker push", "docker tag", "docker rmi", "docker image prune",
    "docker build", "docker compose pull", "docker compose up", "docker compose down",
    "docker restart", "docker rm", "cosign sign", "cosign verify-attestation",
    "skopeo copy", "crane auth", "password=", "token=", "api_key=", "secret=",
    "authorization:", "bearer ", "docker login", "cat .docker/config.json",
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
