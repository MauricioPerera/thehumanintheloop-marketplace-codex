#!/usr/bin/env python3
"""Validate a GitHub milestone plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("goal",r"(?i)\b(?:goal|objetivo|outcome|resultado)\b"),("criteria",r"(?i)\b(?:criteria|criterio|exit|done)\b"),("owner",r"(?i)\b(?:owner|responsable)\b"),("date",r"(?i)\b(?:date|fecha|deadline|due)\b"),("issues",r"(?i)\b(?:issue|issues|tarea)\b"),("risk",r"(?i)\b(?:risk|riesgo|dependency|dependencia)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Milestone plan must contain at least 60 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
