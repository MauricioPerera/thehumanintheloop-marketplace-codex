#!/usr/bin/env python3
"""Validate a GitHub commit signing audit."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("commit",r"(?i)\b(?:commit|commits)\b"),("signature",r"(?i)\b(?:sign|signature|firma|signed)\b"),("verification",r"(?i)\b(?:verification|verified|verificaci[oó]n)\b"),("coverage",r"(?i)\b(?:coverage|cobertura|policy|pol[ií]tica)\b"),("impact",r"(?i)\b(?:impact|impacto|rollback|revert)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<65: errors.append("Signing audit must contain at least 65 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
