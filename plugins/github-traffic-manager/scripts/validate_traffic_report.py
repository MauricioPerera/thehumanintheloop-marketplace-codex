#!/usr/bin/env python3
"""Validate a GitHub traffic report."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("repository",r"(?i)\b(?:repository|repo|repositorio)\b"),("window",r"(?i)\b(?:window|ventana|date|fecha|days|d[ií]as)\b"),("views",r"(?i)\b(?:views?|vistas?)\b"),("clones",r"(?i)\b(?:clones?|clonaciones?)\b"),("limitations",r"(?i)\b(?:retention|retenci[oó]n|limitation|limitaci[oó]n|unique users|usuarios únicos|usuarios únicos)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Traffic report must contain at least 60 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
