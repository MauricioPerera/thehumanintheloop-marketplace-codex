#!/usr/bin/env python3
"""Validate a GitHub branch operation plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("branch",r"(?i)\b(?:branch|rama)\b"),("operation",r"(?i)\b(?:operation|operaci[oó]n|create|delete|merge|compare)\b"),("impact",r"(?i)\b(?:impact|impacto|risk|riesgo)\b"),("rollback",r"(?i)\b(?:rollback|revert|revers)\b"),("command",r"(?i)\b(?:git|gh)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Branch plan must contain at least 60 words.")
    if re.search(r"(?i)force[- ]?push|--force",text):errors.append("Force push requires a separate explicit safety review.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
