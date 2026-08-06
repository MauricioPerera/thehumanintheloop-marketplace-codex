"""Reject log-retention audit plans that delete, truncate, rotate, restart or reconfigure; allow read-only inspection only."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

# journald mutation + log file destruction/truncation/rotation.
#   - `rm`/`truncate`/`logrotate` use bounded lookbehind/lookahead so they match the
#     command but NOT a path token like `--rm` or `/etc/logrotate.d/...`.
FORBIDDEN_MUTATION = re.compile(
    r"("
    r"journalctl\s+--vacuum(?:-size|-time|-files)?"
    r"|journalctl\s+--rotate"
    r"|journalctl\s+--flush"
    r"|journalctl\s+--sync"
    r"|(?<![\w/-])rm(?![\w-])"
    r"|\btruncate\b"
    r"|(?<![\w/])logrotate\b"
    r"|systemctl\s+(?:restart|reload|stop|start|daemon-reload|enable|disable|mask|unmask)\b"
    r"|docker\s+(?:system|container|image|volume|network|builder)\s+prune\b"
    r"|docker\s+prune\b"
    r"|docker\s+(?:restart|exec|stop|start|rm|kill|run|create|pause|unpause|update|rename|cp|rmi)\b"
    r"|docker\s+(?:image|container|volume|network)\s+(?:rm|remove)\b"
    r"|docker\s+compose\s+(?:up|down|restart|stop|start|rm|pull|build)\b"
    r"|\bsed\s+-i\b"
    r"|\btee\b"
    r")"
)

# Credential / secret material (config-file presence is reported by name, never read).
FORBIDDEN_SECRETS = (
    "cat .env", "cat ~/.docker/config", "cat /root/.docker/config",
    "cat .docker/config", "docker login", "/etc/shadow", "/etc/gshadow",
    "password=", "passwd=", "token=", "api_key=", "apikey=", "secret=",
    "authorization:", "bearer ", "private_key=", "-----begin",
)

# Detection of installed tools is read-only and may name tools that are otherwise
# forbidden (e.g. `logrotate`). A *pure* detection line (no shell operators beyond a
# trailing `|| true`/`|| :`) is exempt from the mutation check. Any line with pipes,
# `&&`, `;`, redirects or substitution falls through to the normal checks, so a
# compound `command -v logrotate && rm ...` is still caught.
DETECTION_RE = re.compile(
    r"^(?:command\s+-v|which|whereis|type)\b[^\|;&><`$]*(?:\|\|\s*(?:true|:)\s*)?$"
)

# Read-only inspection allowed after mutation/secret checks pass.
ALLOWED_RE = re.compile(
    r"^(?:"
    r"command\s+-v|which\b|whereis\b|type\b"
    r"|journalctl\s"
    r"|docker\s+(?:info|inspect|system\s+df|ps|version|context\s+ls|stats|logs)\b"
    r"|du\b|df\b|ls\b|stat\b|file\b|find\b"
    r"|systemctl\s+(?:status|show|list|is-active|is-enabled|cat)\b"
    r"|cat\s+/etc/"
    r"|grep\b|awk\b|sed\s(?!-i)"
    r"|#|--"
    r")"
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
        if line.startswith("#"):
            continue
        if DETECTION_RE.match(line):
            continue
        if FORBIDDEN_MUTATION.search(line.lower()):
            blocked.append(f"[mutation] {line}")
        elif any(term in line.lower() for term in FORBIDDEN_SECRETS):
            blocked.append(f"[secret] {line}")
        elif not ALLOWED_RE.match(line.lower()):
            blocked.append(f"[out-of-scope] {line}")
    print({"status": "FAILED" if blocked else "PASSED", "lines": len(lines), "blocked": blocked})
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())