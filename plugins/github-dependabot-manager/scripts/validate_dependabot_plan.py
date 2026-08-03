#!/usr/bin/env python3
"""Validate a Dependabot upgrade plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("package",r"(?i)\b(?:package|dependenc|paquete)\b"),("severity",r"(?i)\b(?:severity|severidad|critical|high|medium|low)\b"),("fixed version",r"(?i)\b(?:fixed|fix|version|versi[oó]n)\b"),("tests",r"(?i)\b(?:test|prueba|ci)\b"),("rollback",r"(?i)\b(?:rollback|revert|revers)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Dependabot plan must contain at least 60 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]",text):errors.append("Possible credential in plan.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
