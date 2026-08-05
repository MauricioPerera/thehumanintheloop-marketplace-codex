"""Reject mutating pg_cron operations, secret exposure and resource-creating CLI in a pg_cron audit plan.

Strictly read-only validator for the Supabase pg_cron Auditor skill. Accepts only:
  - `command -v <bin>`
  - `docker ps ...` and `docker inspect ...`
  - `docker exec ... psql ... -c "<SELECT ...>"` against cron.job / cron.job_run_details /
    pg_settings / pg_catalog / information_schema / pg_extension
  - `grep` / `awk` / `sed` / `find` over configuration files (no `.env`, no secrets)

Blocks cron.schedule / cron.unschedule / cron.alter_job, any DML/DDL
(INSERT/UPDATE/DELETE/ALTER/DROP/CREATE/TRUNCATE/GRANT/REVOKE), supabase functions deploy,
docker restart / compose up / compose down, pg_dump / pg_restore / COPY, `cat .env` and
credential patterns. Returns PASSED only when every non-comment line is allowed and clean.
"""
from __future__ import annotations
import argparse
import re
import shlex
from pathlib import Path

# Forbidden substrings (lowercase). Order-independent: presence blocks the line.
FORBIDDEN_TOKENS = (
    "cron.schedule", "cron.unschedule", "cron.alter_job", "cron.alterjob",
    "insert ", "update ", "delete ", "truncate ", "alter ", "drop ", "create ",
    "grant ", "revoke ",
    "supabase functions deploy", "supabase functions serve", "supabase functions delete",
    "supabase db push", "supabase db reset", "supabase migration",
    "supabase secrets set", "supabase secrets unset",
    "docker restart", "docker compose up", "docker compose down", "docker compose restart",
    "docker stop", "docker kill", "docker rm", "docker rmi",
    "pg_dump", "pg_restore", " copy ", "\\copy",
    "set role", "set search_path",
    ".env", "id_rsa", "id_ed25519", ".pgpass", "credentials.json", "serviceaccount",
)

FORBIDDEN_SECRETS = (
    "password=", "passwd=", "token=", "api_key=", "apikey=", "secret=",
    "jwt_secret=", "anon_key=", "service_role_key=", "service_role=",
    "authorization: bearer", "authorization: bearer ",
    "private_key=", "private_key file", "-----begin",
    "x-api-key:", "postgres://", "postgresql://",
)

SECRET_VALUE = re.compile(
    r"(?i)(password|secret|token|jwt[_-]?secret|anon[_-]?key|service[_-]?role[_-]?key|"
    r"api[_-]?key|private[_-]?key)\s*[:=]\s*\S+"
)

# Relations the psql SELECT is allowed to reference. A psql line must target at least one.
ALLOWED_PSQL_RELATIONS = (
    "cron.job", "cron.job_run_details", "pg_settings", "pg_catalog",
    "information_schema", "pg_extension", "pg_proc", "pg_namespace", "pg_class",
)

# DML/DDL keywords that must never appear inside a psql SQL payload.
SQL_FORBIDDEN_KEYWORDS = (
    "insert", "update", "delete", "truncate", "alter", "drop", "create",
    "grant", "revoke", "vacuum", "reindex", "cluster",
)

CONFIG_TOOLS = ("grep", "awk", "sed", "find")


def _extract_psql_sql(line: str) -> str | None:
    """Return the SQL payload of a `... psql ... -c "<sql>"` (or -c '<sql>') line, else None."""
    try:
        tokens = shlex.split(line, posix=True)
    except ValueError:
        tokens = line.split()
    for i, tok in enumerate(tokens):
        if tok == "-c" and i + 1 < len(tokens):
            return tokens[i + 1]
    # fall back: first quoted string after `-c`
    m = re.search(r'-c\s+(?:"([^"]*)"|\'([^\']*)\')', line)
    if m:
        return m.group(1) or m.group(2)
    return None


def _is_allowed_psql(line: str, lowered: str) -> tuple[bool, str]:
    """Validate a `docker exec ... psql ... -c "<SELECT>"` line is read-only and in scope."""
    if "psql" not in lowered:
        return False, "psql-missing"
    if "select" not in lowered:
        return False, "not-select"
    sql = _extract_psql_sql(line)
    if sql is None:
        return False, "no-sql-payload"
    sql_lower = sql.lower()
    for kw in SQL_FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{kw}\b", sql_lower):
            return False, f"sql-keyword:{kw}"
    if not any(rel in sql_lower for rel in ALLOWED_PSQL_RELATIONS):
        return False, "out-of-scope-relation"
    return True, ""


def _is_allowed(line: str, lowered: str) -> tuple[bool, str]:
    if lowered.startswith("command -v "):
        return True, ""
    if lowered.startswith("docker ps"):
        return True, ""
    if lowered.startswith("docker inspect "):
        return True, ""
    if "docker exec" in lowered:
        return _is_allowed_psql(line, lowered)
    if any(lowered.startswith(t) for t in CONFIG_TOOLS):
        return True, ""
    return False, "out-of-scope"


def classify(line: str) -> str | None:
    """Return a blocked-reason string if the line is rejected, else None."""
    stripped = line.strip()
    if not stripped:
        return None
    if stripped.startswith("#") or stripped.startswith("--"):
        return None
    lowered = stripped.lower()

    for token in FORBIDDEN_TOKENS:
        if token in lowered:
            return f"[forbidden-token:{token.strip()}] {stripped}"
    for secret in FORBIDDEN_SECRETS:
        if secret in lowered:
            return f"[secret-token] {stripped}"
    if SECRET_VALUE.search(stripped):
        return f"[secret-value] {stripped}"

    ok, reason = _is_allowed(stripped, lowered)
    if not ok:
        return f"[{reason}] {stripped}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command-file", required=True)
    args = parser.parse_args()
    lines = Path(args.command_file).read_text(encoding="utf-8").splitlines()
    blocked: list[str] = []
    for raw in lines:
        reason = classify(raw)
        if reason:
            blocked.append(reason)
    status = "FAILED" if blocked else "PASSED"
    print(f'{{"status": "{status}", "lines": {len(lines)}, "blocked": {blocked}}}')
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())