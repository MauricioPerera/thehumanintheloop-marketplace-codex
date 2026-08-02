#!/usr/bin/env python3
"""Static SEO/GEO linter for Markdown or HTML articles."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from html import unescape

HEDGING = re.compile(r"\b(probablemente|tal vez|podr[ií]a|quiz[aá]|posiblemente|likely|perhaps|maybe|could)\b", re.I)
GENERIC = re.compile(r"\b(en el mundo actual|es importante destacar|cabe mencionar|sin duda|en conclusi[oó]n)\b", re.I)
ANCHOR_BLACKLIST = re.compile(r"^(haz clic aqu[ií]|leer m[aá]s|este enlace|click here)$", re.I)
DATE = r"(?:19|20)\d{2}|\d{1,2}[/-]\d{1,2}[/-](?:19|20)\d{2}"

def strip_markup(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#*_>`~-]", " ", text)
    return re.sub(r"\s+", " ", unescape(text)).strip()

def words(text):
    return re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", strip_markup(text), re.UNICODE)

def headings(text):
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m: out.append({"level": len(m.group(1)), "text": strip_markup(m.group(2)), "line": i})
    for m in re.finditer(r"<h([1-6])\b[^>]*>(.*?)</h\1>", text, re.I | re.S):
        out.append({"level": int(m.group(1)), "text": strip_markup(m.group(2)), "line": text[:m.start()].count("\n") + 1})
    return sorted(out, key=lambda x: x["line"])

def section_capsules(text, hs):
    lines, result = text.splitlines(), []
    targets = [h for h in hs if h["level"] in (1, 2)]
    for idx, h in enumerate(targets):
        start = h["line"]; end = targets[idx + 1]["line"] if idx + 1 < len(targets) else len(lines) + 1
        body = "\n".join(lines[start:end-1]); body = re.sub(r"^\s{0,3}#{1,6}\s+.*$", "", body, flags=re.M)
        first = next((p.strip() for p in re.split(r"\n\s*\n", body) if strip_markup(p)), "")
        count = len(words(first)); hedging = HEDGING.findall(first)
        result.append({"heading": h["text"], "line": h["line"], "words": count, "hedging": hedging, "passed": 40 <= count <= 75 and not hedging})
    return result

def links(text):
    found = []
    pattern = r"\[([^]]+)\]\((https?://[^)\s]+|/[^)\s]+)\)|<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>"
    for m in re.finditer(pattern, text, re.I | re.S):
        found.append({"anchor": strip_markup(m.group(1) or m.group(4) or ""), "url": m.group(2) or m.group(3)})
    return found

def faq_and_glossary(text):
    faq = re.search(r"(?:^|\n)\s{0,3}#{1,6}\s*(?:faq|preguntas frecuentes|preguntas y respuestas)\b", text, re.I)
    faq_count, bad = 0, []
    if faq:
        block = text[faq.end():]
        for part in re.split(r"\n(?=\s{0,3}(?:#{3,6}\s+|\*\*?Pregunta|Q\s*[:：]))", block, flags=re.I):
            if "?" in part:
                faq_count += 1; answer = part.split("?", 1)[1]
                sentences = len(re.findall(r"[^.!?]+[.!?]+", answer))
                if not 2 <= sentences <= 4: bad.append(sentences)
    glossary = re.search(r"(?:^|\n)\s{0,3}#{1,6}\s*(?:glosario|mini glosario)\b", text, re.I)
    terms = 0
    if glossary: terms = len(re.findall(r"(?:^|\n)\s*(?:[-*]\s+|\*\*[^*]+\*\*\s*[:—-])", text[glossary.end():], re.M))
    return {"faq_section": bool(faq), "faq_pairs": faq_count, "faq_bad_sentence_counts": bad, "glossary_section": bool(glossary), "glossary_terms": terms}

def infer_format(text):
    low = text.lower()
    if re.search(r"\b(faq|preguntas frecuentes|glosario)\b", low) and len(words(text)) <= 1000: return "faq"
    if re.search(r"\b(precio|comprar|caracter[ií]sticas|producto|especificaciones)\b", low): return "product"
    if re.search(r"\b(gu[ií]a completa|gu[ií]a definitiva|pillar page|paso a paso)\b", low): return "guide"
    return "standard"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--input", type=Path); ap.add_argument("--keyword"); ap.add_argument("--format", choices=["guide","standard","product","faq"]); ap.add_argument("--json", type=Path); ap.add_argument("--markdown", type=Path)
    a = ap.parse_args(); text = a.input.read_text(encoding="utf-8") if a.input else sys.stdin.buffer.read().decode("utf-8", errors="replace")
    hs, plain = headings(text), strip_markup(text); wc, fmt = len(words(text)), a.format or infer_format(text); ranges = {"guide": (2500,5000), "standard": (1500,2500), "product": (800,1500), "faq": (300,800)}; kw = a.keyword; intro = " ".join(words(text)[:100]); ls = links(text)
    stats = re.findall(r"\b\d+(?:[.,]\d+)?\s*(?:%|por ciento|millones|mil|usuarios|personas|casos|veces)\b[^.]{0,180}", plain, re.I); cited = [s for s in stats if re.search(DATE, s) and re.search(r"\b(?:seg[uú]n|informe|estudio|datos de|fuente)\b", s, re.I)]
    quotes = re.findall(r"[\"“].{20,300}?[\"”]", plain); attributed = [q for q in quotes if re.search(r"\b[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑ-]+\s+[A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑ-]+\b.{0,100}\b(?:CEO|director|directora|analista|profesor|profesora|fundador|especialista|chief)\b", plain, re.I)]
    internal = [x for x in ls if x["url"].startswith("/") or not x["url"].startswith(("http://","https://"))]; external = [x for x in ls if x["url"].startswith(("http://","https://"))]; bad_anchors = [x for x in ls if ANCHOR_BLACKLIST.fullmatch(x["anchor"].strip())]
    imgs = re.findall(r"!\[([^]]*)\]\([^)]*\)|<img\b([^>]*?)>", text, re.I | re.S); missing_alt = [x for x in imgs if x[0] == "" and not re.search(r"\balt\s*=\s*[\"'][^\"']+[\"']", x[1], re.I)]; caps = section_capsules(text, hs); faq = faq_and_glossary(text)
    rules = {
      "rule_1": {"passed": ranges[fmt][0] <= wc <= ranges[fmt][1], "word_count": wc, "format": fmt, "target_range": ranges[fmt], "commodity_signals": len(GENERIC.findall(plain))},
      "rule_2": {"passed": bool(caps) and all(x["passed"] for x in caps), "capsules": caps},
      "rule_3": {"passed": len(cited) >= 3 and len(attributed) >= 2, "statistics_detected": len(stats), "statistics_with_source_date": len(cited), "quotes_detected": len(quotes), "quotes_with_attribution": len(attributed)},
      "rule_4": {"passed": faq["faq_pairs"] in range(5,9) and not faq["faq_bad_sentence_counts"] and faq["glossary_terms"] >= 5, **faq},
      "rule_5": {"passed": 2 <= len(internal) <= 3 and len(external) >= 3 and not bad_anchors, "internal_links": len(internal), "external_links": len(external), "blacklisted_anchors": bad_anchors},
      "rule_6": {"passed": len([h for h in hs if h["level"] == 1]) == 1 and bool(kw) and kw.lower() in " ".join(h["text"] for h in hs if h["level"] == 1).lower() and kw.lower() in intro.lower() and any(kw.lower() in h["text"].lower() for h in hs if h["level"] == 2) and not missing_alt, "h1_count": len([h for h in hs if h["level"] == 1]), "keyword": kw, "keyword_in_intro": bool(kw and kw.lower() in intro.lower()), "keyword_in_h2": bool(kw and any(kw.lower() in h["text"].lower() for h in hs if h["level"] == 2)), "images": len(imgs), "images_missing_alt": len(missing_alt)}
    }
    report = {"skill": "linter-seo-geo-2026", "rules": rules}; out = json.dumps(report, ensure_ascii=False, indent=2)
    if a.json: a.json.write_text(out + "\n", encoding="utf-8")
    if a.markdown:
        labels = ["Longitud y profundidad","Cápsulas de respuesta","Densidad de datos y E-E-A-T","FAQ y glosario","Topic clusters","Metadatos y estructura"]; md = "# Reporte Linter SEO/GEO 2026\n\n| Regla | Estado | Valor detectado |\n|---|---|---|\n"
        for i, label in enumerate(labels, 1): md += f"| {i}. {label} | {'[PASSED]' if rules[f'rule_{i}']['passed'] else '[FAILED]'} | {json.dumps(rules[f'rule_{i}'], ensure_ascii=False)} |\n"
        a.markdown.write_text(md, encoding="utf-8")
    print(out)

if __name__ == "__main__": main()
