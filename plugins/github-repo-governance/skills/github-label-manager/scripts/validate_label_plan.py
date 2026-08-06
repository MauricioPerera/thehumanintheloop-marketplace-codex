#!/usr/bin/env python3
"""Validate a GitHub label taxonomy plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("labels",r"(?i)\b(?:label|labels|etiqueta)\b"),("purpose",r"(?i)\b(?:purpose|prop[oó]sito|description|descripci[oó]n)\b"),("color",r"(?i)\b(?:color|#[0-9a-f]{6})\b"),("migration",r"(?i)\b(?:migration|migraci[oó]n|mapping|mapa)\b"),("commands",r"(?i)\b(?:gh\s+label|command|comando)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Label plan must contain at least 60 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]",text):errors.append("Possible credential in plan.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
