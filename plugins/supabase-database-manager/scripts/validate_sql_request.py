"""Classify SQL and block destructive statements unless explicitly planned."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

MUTATIONS = re.compile(r"\b(drop|truncate|delete|update|alter|insert|create\s+extension|vacuum\s+full)\b", re.I)
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sql-file", required=True)
    parser.add_argument("--allow-mutation", action="store_true")
    args = parser.parse_args()
    sql = Path(args.sql_file).read_text(encoding="utf-8")
    mutation = bool(MUTATIONS.search(sql))
    blocked = mutation and not args.allow_mutation
    print({"status": "FAILED" if blocked else "PASSED", "classification": "MUTATION" if mutation else "READ_ONLY", "mutation_allowed": args.allow_mutation})
    return 1 if blocked else 0
if __name__ == "__main__":
    raise SystemExit(main())
