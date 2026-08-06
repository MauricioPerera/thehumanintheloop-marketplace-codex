#!/usr/bin/env python3
"""Validate a GitHub notification digest."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("thread link",r"https?://github\.com/"),("priority",r"(?i)\b(?:urgent|today|scheduled|reference|noise|urgente|hoy|programado)\b"),("reason",r"(?i)\b(?:reason|reasoning|raz[oó]n)\b"),("next action",r"(?i)\b(?:next action|siguiente acci[oó]n|action|acci[oó]n)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<50:errors.append("Notification digest must contain at least 50 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]\s*\S+",text):errors.append("Possible exposed credential.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
