#!/usr/bin/env python3
"""Validate a merge queue diagnosis."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("queue",r"(?i)\b(?:queue|cola|merge)\b"),("pull request",r"(?i)\b(?:pull request|PR|solicitud)\b"),("checks",r"(?i)\b(?:check|checks|validaci[oó]n)\b"),("evidence",r"(?i)\b(?:evidence|evidencia|status|estado)\b"),("verification",r"(?i)\b(?:verification|verificaci[oó]n|validate|validar)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<65: errors.append("Merge queue report must contain at least 65 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
