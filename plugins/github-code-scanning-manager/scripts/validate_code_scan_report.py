#!/usr/bin/env python3
"""Validate a Code Scanning report."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("alert",r"(?i)\b(?:alert|alerta)\b"),("severity",r"(?i)\b(?:severity|severidad|critical|high|medium|low)\b"),("rule",r"(?i)\b(?:rule|regla|query)\b"),("location",r"(?i)\b(?:location|ubicaci[oó]n|file|archivo)\b"),("remediation",r"(?i)\b(?:remediation|remediaci[oó]n|fix|correcci[oó]n)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<65: errors.append("Code Scanning report must contain at least 65 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
