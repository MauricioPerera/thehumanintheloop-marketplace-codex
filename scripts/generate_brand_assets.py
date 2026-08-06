#!/usr/bin/env python3
"""Generate favicon and Open Graph image assets for the marketplace site.

Uses the same color palette as docs/styles.css (--ink/--lime/--orange/--cream).
Re-run after changing the brand palette or copy; these are static generated
files, not regenerated automatically by scripts/generate_plugin_pages.py.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FONT_DIR = Path("C:/Windows/Fonts")

INK = (23, 33, 29)
LIME = (215, 243, 106)
ORANGE = (255, 112, 78)
CREAM = (245, 245, 239)
MUTED = (183, 196, 189)
RING = (71, 85, 79)


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def make_favicon_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#17211d"/>
  <text x="32" y="45" font-family="Arial, Helvetica, sans-serif" font-weight="800" font-size="36" fill="#d7f36a" text-anchor="middle">T</text>
  <circle cx="50" cy="15" r="5" fill="#ff704e"/>
</svg>
"""
    (DOCS / "favicon.svg").write_text(svg, encoding="utf-8")


def make_apple_touch_icon():
    size = 180
    img = Image.new("RGB", (size, size), INK)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=38, fill=INK)
    f = font("segoeuib.ttf", 108)
    bbox = draw.textbbox((0, 0), "T", font=f)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1] - 8), "T", font=f, fill=LIME)
    draw.ellipse([size - 48, 12, size - 12, 48], fill=ORANGE)
    img.save(DOCS / "apple-touch-icon.png")


def make_og_image():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), INK)
    draw = ImageDraw.Draw(img)
    draw.ellipse([760, -200, 1400, 440], outline=RING, width=2)
    draw.ellipse([880, -70, 1260, 310], outline=RING, width=2)

    eyebrow_font = font("segoeuib.ttf", 26)
    title_font = font("segoeuib.ttf", 74)
    sub_font = font("segoeui.ttf", 32)
    domain_font = font("segoeui.ttf", 24)

    draw.text((80, 86), "THL · MARKETPLACE", font=eyebrow_font, fill=ORANGE)
    draw.text((77, 148), "TheHumanInTheLoop", font=title_font, fill=CREAM)
    draw.text((77, 240), "Marketplace", font=title_font, fill=LIME)
    draw.text((80, 350), "Plugins para Claude Code + Codex", font=sub_font, fill=MUTED)
    draw.text((80, 396), "Design System Analyses · validadores deterministas", font=sub_font, fill=MUTED)
    draw.text((80, 526), "mauricioperera.github.io/thehumanintheloop-marketplace-codex", font=domain_font, fill=RING)

    img.save(DOCS / "og-image.png")


def main():
    make_favicon_svg()
    make_apple_touch_icon()
    make_og_image()
    print("Generated docs/favicon.svg, docs/apple-touch-icon.png, docs/og-image.png")


if __name__ == "__main__":
    main()
