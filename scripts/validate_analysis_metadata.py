#!/usr/bin/env python3
"""Validate SEO metadata and sitemap coverage for published analyses."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: dict[str, str] = {}
        self.meta: dict[str, str] = {}
        self.json_ld: list[dict] = []
        self._in_json_ld = False
        self._json_ld_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "link" and values.get("rel") == "canonical" and values.get("href"):
            self.links["canonical"] = values["href"]
        if tag == "meta":
            key = values.get("name") or values.get("property")
            if key and values.get("content"):
                self.meta[key] = values["content"]
        if tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_ld_buffer = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._json_ld_buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_json_ld:
            try:
                self.json_ld.append(json.loads("".join(self._json_ld_buffer)))
            except json.JSONDecodeError:
                self.json_ld.append({})
            self._in_json_ld = False


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    analyses = root / "docs" / "analyses"
    sitemap = (root / "docs" / "sitemap.xml").read_text(encoding="utf-8")
    base = "https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/"
    errors: list[str] = []
    pages = sorted(analyses.glob("*/index.html"))
    for page in pages:
        name = page.parent.name
        for filename in ("DESIGN.md", "design-system.json", "validation-report.json", "styles.css", "app.js"):
            artifact = page.parent / filename
            if not artifact.exists():
                errors.append(f"{name}: missing analysis artifact {filename}")
        for filename in ("design-system.json", "validation-report.json"):
            artifact = page.parent / filename
            if artifact.exists():
                try:
                    json.loads(artifact.read_text(encoding="utf-8"))
                except json.JSONDecodeError as exc:
                    errors.append(f"{name}: invalid JSON in {filename}: {exc}")
        parser = MetadataParser()
        parser.feed(page.read_text(encoding="utf-8"))
        expected = f"{base}{name}/"
        if parser.links.get("canonical") != expected:
            errors.append(f"{name}: canonical must be {expected}")
        if "og:title" not in parser.meta or "og:description" not in parser.meta:
            errors.append(f"{name}: missing Open Graph title or description")
        if len(parser.json_ld) != 1 or parser.json_ld[0].get("@type") != "TechArticle":
            errors.append(f"{name}: missing valid TechArticle JSON-LD")
        if expected not in sitemap:
            errors.append(f"{name}: missing from docs/sitemap.xml")
    result = {"status": "FAILED" if errors else "PASSED", "analyses": len(pages), "errors": errors}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
