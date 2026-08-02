#!/usr/bin/env python3
"""Report factual claims that need named sources and dates."""
import argparse, json, re, sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("document"); args=parser.parse_args()
    text=Path(args.document).read_text(encoding="utf-8")
    stats=re.findall(r"\b\d+(?:[.,]\d+)?\s*(?:%|por ciento|millones?|mil millones?)\b", text, re.I)
    dates=re.findall(r"\b(?:19|20)\d{2}\b", text)
    urls=re.findall(r"https?://\S+", text)
    source_markers=re.findall(r"\b(?:según|de acuerdo con|fuente|source|reportado por|citado por)\b", text, re.I)
    result={"status":"PASSED" if len(stats)>=3 and len(dates)>=3 and len(urls)>=1 else "FAILED", "statistics":len(stats), "dates":len(dates), "urls":len(urls), "sourceMarkers":len(source_markers), "claimsNeedReview":max(0, len(stats)-len(source_markers))}
    print(json.dumps(result, indent=2, ensure_ascii=False)); return 0 if result["status"]=="PASSED" else 1
if __name__ == "__main__": sys.exit(main())
