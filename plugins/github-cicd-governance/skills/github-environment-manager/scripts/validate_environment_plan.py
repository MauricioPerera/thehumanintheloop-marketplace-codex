#!/usr/bin/env python3
"""Validate a GitHub environment plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("environment",r"(?i)\b(?:environment|entorno)\b"),("branches",r"(?i)\b(?:branch|rama|deployment)\b"),("reviewers",r"(?i)\b(?:reviewers?|revisors?|approval|aprobaci[oó]n)\b"),("impact",r"(?i)\b(?:impact|impacto|risk|riesgo)\b"),("rollback",r"(?i)\b(?:rollback|revert|revers)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<70:errors.append("Environment plan must contain at least 70 words.")
    if re.search(r"(?i)(secret|token|password|api[_ -]?key)\s*[:=]\s*\S+",text):errors.append("Possible exposed environment secret.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
