#!/usr/bin/env python3
"""Ensure the AI-readable catalog covers the published plugin inventory."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    llms = (root / "docs" / "llms.txt").read_text(encoding="utf-8")
    names = [entry["name"] for entry in manifest.get("plugins", [])]
    errors = [f"Missing plugin in docs/llms.txt: {name}" for name in names if f"`{name}`" not in llms]
    for entry in manifest.get("plugins", []):
        expected = f"- `{entry['name']}` — {entry.get('category')} —"
        if expected not in llms:
            errors.append(f"Missing category in docs/llms.txt: {entry['name']}")
    if "Productivity" in llms:
        errors.append("docs/llms.txt contains obsolete category: Productivity")
    for analysis in (root / "docs" / "analyses").glob("*/index.html"):
        if f"`{analysis.parent.name}`" not in llms:
            errors.append(f"Missing analysis in docs/llms.txt: {analysis.parent.name}")
    result = {"status": "FAILED" if errors else "PASSED", "plugins": len(names), "errors": errors}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
