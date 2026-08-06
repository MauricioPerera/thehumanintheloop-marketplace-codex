#!/usr/bin/env python3
"""Validate a GitHub team access audit."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("team",r"(?i)\b(?:team|equipo)\b"),("members",r"(?i)\b(?:member|miembro)\b"),("repository",r"(?i)\b(?:repository|repositorio)\b"),("permissions",r"(?i)\b(?:permission|permiso|role|rol)\b"),("least privilege",r"(?i)\b(?:least privilege|m[ií]nimo privilegio|rollback|revert)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<70: errors.append("Team access audit must contain at least 70 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
