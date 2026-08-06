#!/usr/bin/env python3
"""Check that every marketplace plugin has a matching static page under docs/plugins/."""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PLUGINS_DIR = DOCS / "plugins"


def load_catalog_by_name():
    html_text = (DOCS / "index.html").read_text(encoding="utf-8")
    marker = '<script type="application/ld+json">'
    start = html_text.index(marker) + len(marker)
    end = html_text.index("</script>", start)
    structured = json.loads(html_text[start:end].strip())
    result = {}
    for entry in structured["mainEntity"]["itemListElement"]:
        app = entry["item"]
        name = app["url"].rstrip("/").split("/")[-1]
        result[name] = app
    return result


def main():
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    expected = {entry["name"] for entry in marketplace["plugins"]}
    catalog = load_catalog_by_name()
    errors = []

    existing_dirs = {p.name for p in PLUGINS_DIR.iterdir() if p.is_dir()} if PLUGINS_DIR.exists() else set()
    orphans = existing_dirs - expected
    if orphans:
        errors.append(f"Orphan plugin page directories (no matching marketplace entry): {sorted(orphans)}")

    for name in sorted(expected):
        page_path = PLUGINS_DIR / name / "index.html"
        if not page_path.exists():
            errors.append(f"Missing plugin page: docs/plugins/{name}/index.html")
            continue
        page = page_path.read_text(encoding="utf-8")
        app = catalog.get(name)
        if app is None:
            errors.append(f"Plugin not found in JSON-LD ItemList: {name}")
            continue
        display_name = app["name"]
        expected_canonical = f"https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/plugins/{name}/"
        if f"<title>{html.escape(display_name)} ·" not in page:
            errors.append(f"Title mismatch in docs/plugins/{name}/index.html")
        if f'rel="canonical" href="{expected_canonical}"' not in page:
            errors.append(f"Canonical URL mismatch in docs/plugins/{name}/index.html")
        marker = '<script type="application/ld+json">'
        start = page.index(marker) + len(marker)
        end = page.index("</script>", start)
        page_json_ld = json.loads(page[start:end].strip())
        if page_json_ld.get("name") != display_name:
            errors.append(f"JSON-LD name mismatch in docs/plugins/{name}/index.html")

    if errors:
        print(json.dumps({"status": "FAILED", "errors": errors}, indent=2, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "PASSED", "pages": len(expected)}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
