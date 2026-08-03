#!/usr/bin/env python3
"""Check that the static JSON-LD catalog matches the Claude marketplace manifest."""
import json
import re
import sys
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    html = (root / "docs" / "index.html").read_text(encoding="utf-8")
    marker = '<script type="application/ld+json">'
    start = html.index(marker) + len(marker)
    end = html.index("</script>", start)
    structured = json.loads(html[start:end].strip())
    marketplace = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    readme = (root / "README.md").read_text(encoding="utf-8")
    expected = {entry["name"] for entry in marketplace["plugins"]}
    actual = {
        item["item"]["url"].rstrip("/").split("/")[-1]
        for item in structured["mainEntity"]["itemListElement"]
    }
    errors = []
    if structured["mainEntity"]["numberOfItems"] != len(expected):
        errors.append("JSON-LD numberOfItems does not match marketplace")
    if expected != actual:
        errors.append(f"JSON-LD plugin mismatch: expected={sorted(expected)}, actual={sorted(actual)}")
    category_counts = {}
    for entry in marketplace["plugins"]:
        category_counts[entry["category"]] = category_counts.get(entry["category"], 0) + 1
    for category, count in category_counts.items():
        pattern = rf"^- {re.escape(category)} — {count} plugin(?:s)?$"
        if not re.search(pattern, readme, re.MULTILINE):
            errors.append(f"README category count is stale: {category} should be {count}")
    if errors:
        print(json.dumps({"status": "FAILED", "errors": errors}, indent=2, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "PASSED", "plugins": len(expected)}, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
