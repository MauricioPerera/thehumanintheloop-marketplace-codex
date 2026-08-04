"""Reject mutating statements, secret values and resource-creating CLI in a policy-security plan."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

FORBIDDEN_TOKENS = (
    "insert ", "update ", "delete ", "truncate ", "alter ", "drop ", "grant ", "revoke ",
    "create policy", "drop policy", "create table", "create role", "alter policy",
    "supabase functions deploy", "supabase functions serve", "supabase functions delete",
    "supabase db push", "supabase migration new", "supabase migration up",
    "supabase secrets set", "supabase secrets unset", "supabase db reset",
    "docker exec", "docker restart", "docker compose up", "docker compose down",
    "docker compose restart", "psql -c ", "pg_dump", "set role", "set jwt",
)

FORBIDDEN_SECRETS = (
    "password=", "passwd=", "token=", "api_key=", "apikey=", "secret=", "jwt_secret=",
    "anon_key=", "service_role_key=", "authorization: bearer", "authorization: bearer ",
    "private_key=", "private_key file", "-----begin", "x-api-key:",
)

SECRET_VALUE = re.compile(
    r"(?i)(password|secret|token|jwt[_-]?secret|anon[_-]?key|service[_-]?role[_-]?key|api[_-]?key|private[_-]?key)\s*[:=]\s*\S+"
)

ALLOWED_PREFIXES = (
    "select ", "with ", "--", "#", "explain ", "psql -c \"select", "psql -c 'select",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command-file", required=True)
    args = parser.parse_args()
    lines = Path(args.command_file).read_text(encoding="utf-8").splitlines()
    blocked: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        lowered = line.lower()
        for token in FORBIDDEN_TOKENS:
            if token in lowered:
                blocked.append(f"[mutation/cli] {line}")
                break
        else:
            for secret in FORBIDDEN_SECRETS:
                if secret in lowered:
                    blocked.append(f"[secret-token] {line}")
                    break
            else:
                if SECRET_VALUE.search(line):
                    blocked.append(f"[secret-value] {line}")
                elif not any(lowered.startswith(prefix) for prefix in ALLOWED_PREFIXES):
                    blocked.append(f"[out-of-scope] {line}")
    print({"status": "FAILED" if blocked else "PASSED", "lines": len(lines), "blocked": blocked})
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())