#!/usr/bin/env python3
"""Validate a manual workflow dispatch plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("workflow",r"(?i)\b(?:workflow|workflow_dispatch)\b"),("ref",r"(?i)\b(?:ref|branch|rama|tag)\b"),("inputs",r"(?i)\b(?:input|inputs|par[aá]metro)\b"),("permissions",r"(?i)\b(?:permission|permiso|environment|entorno)\b"),("verification",r"(?i)\b(?:verification|verificaci[oó]n|monitoring|monitoreo)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<65: errors.append("Dispatch plan must contain at least 65 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
