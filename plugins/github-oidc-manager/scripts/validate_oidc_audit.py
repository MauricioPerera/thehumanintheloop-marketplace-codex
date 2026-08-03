#!/usr/bin/env python3
"""Validate a GitHub OIDC trust audit."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("OIDC",r"(?i)\b(?:OIDC|openid)\b"),("subject",r"(?i)\b(?:subject|claim|repo:)\b"),("audience",r"(?i)\b(?:audience|audiencia)\b"),("provider",r"(?i)\b(?:provider|proveedor|cloud)\b"),("least privilege",r"(?i)\b(?:least privilege|m[ií]nimo privilegio|rollback|revert)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<65: errors.append("OIDC audit must contain at least 65 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
