#!/usr/bin/env python3
"""Validate the shared Claude Code/Codex marketplace layout."""
import argparse, json, sys
from pathlib import Path

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Invalid JSON: {path}: {exc}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors = []
    claude_path = root / ".claude-plugin" / "marketplace.json"
    codex_path = root / ".agents" / "plugins" / "marketplace.json"
    if not claude_path.exists(): errors.append(f"Missing {claude_path.relative_to(root)}")
    if not codex_path.exists(): errors.append(f"Missing {codex_path.relative_to(root)}")
    manifests = []
    for path in (claude_path, codex_path):
        if path.exists():
            try: manifests.append(load(path))
            except ValueError as exc: errors.append(str(exc))
    names = []
    for manifest in manifests:
        entries = manifest.get("plugins", [])
        names.append({entry.get("name") for entry in entries})
        for entry in entries:
            name = entry.get("name")
            source = entry.get("source")
            relative = source if isinstance(source, str) else (source or {}).get("path")
            if not name or not relative: errors.append("Every plugin entry needs name and source/path")
            elif not (root / relative).is_dir(): errors.append(f"Plugin path does not exist: {relative}")
    if len(names) == 2 and names[0] != names[1]: errors.append(f"Marketplace plugin mismatch: Claude={sorted(names[0])}, Codex={sorted(names[1])}")
    if errors:
        print(json.dumps({"status": "FAILED", "errors": errors}, indent=2, ensure_ascii=False)); return 1
    print(json.dumps({"status": "PASSED", "plugins": sorted(names[0]) if names else []}, indent=2, ensure_ascii=False)); return 0

if __name__ == "__main__": sys.exit(main())
