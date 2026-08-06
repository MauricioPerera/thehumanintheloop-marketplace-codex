#!/usr/bin/env python3
"""Generate a static, shareable page per plugin under docs/plugins/<name>/.

Source of truth: the SoftwareApplication ItemList already embedded as
JSON-LD in docs/index.html, which scripts/validate_catalog_metadata.py
keeps in sync with .claude-plugin/marketplace.json. Regenerating from
that block avoids introducing a third, driftable copy of plugin text.
"""
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PLUGINS_DIR = DOCS / "plugins"
SITE_URL = "https://mauricioperera.github.io/thehumanintheloop-marketplace-codex"
MARKETPLACE_NAME = "thehumanintheloop-marketplace-claude"


def load_catalog():
    html_text = (DOCS / "index.html").read_text(encoding="utf-8")
    marker = '<script type="application/ld+json">'
    start = html_text.index(marker) + len(marker)
    end = html_text.index("</script>", start)
    structured = json.loads(html_text[start:end].strip())
    return structured["mainEntity"]["itemListElement"]


def load_categories():
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    return {entry["name"]: entry["category"] for entry in marketplace["plugins"]}


def render_page(app, real_category):
    name = app["url"].rstrip("/").split("/")[-1]
    display_name = html.escape(app["name"])
    description = html.escape(app["description"])
    category = html.escape(real_category)
    version = html.escape(app["softwareVersion"])
    repo_url = html.escape(app["url"])
    keywords = html.escape(app.get("keywords", ""))
    page_url = f"{SITE_URL}/plugins/{name}/"
    claude_install = f"claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\nclaude plugin install {name}@{MARKETPLACE_NAME}"

    json_ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": app["name"],
        "applicationCategory": app["applicationCategory"],
        "operatingSystem": app["operatingSystem"],
        "softwareVersion": app["softwareVersion"],
        "description": app["description"],
        "url": app["url"],
        "author": app["author"],
        "keywords": app.get("keywords", ""),
        "isPartOf": {
            "@type": "WebSite",
            "name": "TheHumanInTheLoop Marketplace",
            "url": f"{SITE_URL}/",
        },
    }

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#17211d">
  <link rel="canonical" href="{page_url}">
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="../apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{display_name} · TheHumanInTheLoop Marketplace">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:site_name" content="TheHumanInTheLoop Marketplace">
  <meta property="og:image" content="{SITE_URL}/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE_URL}/og-image.png">
  <script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>
  <title>{display_name} · TheHumanInTheLoop Marketplace</title>
  <link rel="stylesheet" href="../plugin-page.css">
</head>
<body>
  <main class="wrap">
    <a class="back-link" href="../../">← Volver al catálogo completo</a>
    <article class="plugin-detail">
      <span class="badge">Plugin · {category}</span>
      <h1>{display_name}</h1>
      <p class="description">{description}</p>
      <dl class="meta">
        <div><dt>Versión</dt><dd>{version}</dd></div>
        <div><dt>Categoría</dt><dd>{category}</dd></div>
        <div><dt>Keywords</dt><dd>{keywords}</dd></div>
      </dl>
      <div class="actions">
        <a class="button primary" href="{repo_url}" target="_blank" rel="noreferrer">Ver en GitHub ↗</a>
        <a class="button" href="codex://new" target="_blank" rel="noreferrer">Abrir en Codex</a>
      </div>
      <div class="install">
        <p class="install-label">Instalar en Claude Code</p>
        <pre><code>{html.escape(claude_install)}</code></pre>
      </div>
    </article>
  </main>
</body>
</html>
"""


SITEMAP_BEGIN = "  <!-- BEGIN GENERATED PLUGIN PAGES (scripts/generate_plugin_pages.py) -->\n"
SITEMAP_END = "  <!-- END GENERATED PLUGIN PAGES -->\n"


def update_sitemap(names):
    sitemap_path = DOCS / "sitemap.xml"
    text = sitemap_path.read_text(encoding="utf-8")
    if SITEMAP_BEGIN in text:
        start = text.index(SITEMAP_BEGIN)
        end = text.index(SITEMAP_END) + len(SITEMAP_END)
        text = text[:start] + text[end:]
    entries = [SITEMAP_BEGIN]
    for name in sorted(names):
        entries.append(
            f"  <url>\n    <loc>{SITE_URL}/plugins/{name}/</loc>\n"
            "    <changefreq>monthly</changefreq>\n    <priority>0.5</priority>\n  </url>\n"
        )
    entries.append(SITEMAP_END)
    block = "".join(entries)
    text = text.replace("</urlset>", block + "</urlset>")
    sitemap_path.write_text(text, encoding="utf-8")


def main():
    catalog = load_catalog()
    categories = load_categories()
    if PLUGINS_DIR.exists():
        for entry in PLUGINS_DIR.iterdir():
            if entry.is_dir():
                shutil.rmtree(entry)
    PLUGINS_DIR.mkdir(exist_ok=True)
    names = []
    for item in catalog:
        app = item["item"]
        name = app["url"].rstrip("/").split("/")[-1]
        names.append(name)
        page = render_page(app, categories[name])
        page_dir = PLUGINS_DIR / name
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(page, encoding="utf-8")
    update_sitemap(names)
    print(f"Generated {len(catalog)} plugin pages under {PLUGINS_DIR}")


if __name__ == "__main__":
    main()
