#!/usr/bin/env python3
"""Validate a reproducible GitHub search report."""
import argparse, json, re, sys
from pathlib import Path

def validate(text):
    errors=[]
    for label, pattern in [("query",r"(?i)\b(?:query|consulta|search)\b"),("scope",r"(?i)\b(?:scope|alcance|repository|repositorio)\b"),("results",r"(?i)\b(?:results?|resultados?|matches|coincidencias|zero)\b"),("links",r"https?://github\.com/"),("limitations",r"(?i)\b(?:limitation|limitaci[oó]n|not exhaustive|no exhaustiv)")]:
        if not re.search(pattern,text): errors.append(f"Missing {label} information.")
    if len(text.split())<50: errors.append("Search report must contain at least 50 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]",text): errors.append("Possible credential in report.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True,type=Path); p.add_argument("--json",dest="json_path",type=Path); a=p.parse_args(); r=validate(a.input.read_text(encoding="utf-8"));
    if a.json_path: a.json_path.write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["status"]=="PASSED" else 1
if __name__=="__main__": sys.exit(main())
