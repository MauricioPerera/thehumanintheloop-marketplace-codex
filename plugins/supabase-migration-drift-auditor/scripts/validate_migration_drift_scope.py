"""Reject mutating statements, secret values and resource-creating CLI in a migration-drift audit plan.

Determinista, sin LLM. Análogo a validate_policy_security_scope.py. Recibe --command-file
(una lista de comandos/SQL, uno por línea) y retorna PASSED/FAILED, etiquetando cada línea
bloqueada por categoría: [mutation/cli], [secret-token], [secret-value], [out-of-scope].
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ALLOWED_PREFIXES = (
    "command -v", "which ", "find ", "sha256sum ", "awk ", "sed ", "grep ",
    "docker ps", "docker inspect", "docker exec",
    "select ", "with ", "--", "#",
    "psql -c \"select", "psql -c 'select",
)

FORBIDDEN_MUTATION = (
    "supabase db push", "supabase migration up", "supabase migration new",
    "supabase migration repair", "supabase migration squash",
    "supabase db reset", "supabase db pull", "supabase db diff", "supabase db commit",
    "supabase functions deploy", "supabase secrets set",
    "supabase start", "supabase stop", "supabase restart",
    "docker restart", "docker compose up", "docker compose down", "docker compose restart",
    "insert ", "update ", "delete ", "truncate ", "alter ", "drop ", "create ",
    "grant ", "revoke ", "pg_dump", "set role",
)

FORBIDDEN_SECRETS = (
    "cat .env", "cat ~/.supabase",
    "jwt_secret=", "anon_key=", "service_role_key=",
    "password=", "token=", "authorization: bearer", "-----begin", "pgpassword=",
)

SECRET_VALUE = re.compile(
    r"(?i)(secret|token|password|jwt[_-]?secret|anon[_-]?key|service[_-]?role[_-]?key)\s*[:=]\s*\S+"
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
        for token in FORBIDDEN_MUTATION:
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
                elif lowered.startswith("docker exec") and not (
                    "psql" in lowered and "-c" in lowered and "select" in lowered
                ):
                    # docker exec permitido solo como psql ... -c "SELECT ..."
                    blocked.append(f"[out-of-scope] {line}")
    print({"status": "FAILED" if blocked else "PASSED", "lines": len(lines), "blocked": blocked})
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())