#!/usr/bin/env python3
"""Validate a GitHub repository migration plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("source",r"(?i)\b(?:source|origen)\b"),("destination",r"(?i)\b(?:destination|destino)\b"),("dependencies",r"(?i)\b(?:dependencies?|integrations?|webhooks?|secrets?)\b"),("validation",r"(?i)\b(?:validation|validaci[oó]n|smoke)\b"),("rollback",r"(?i)\b(?:rollback|revert|revers)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<75: errors.append("Migration plan must contain at least 75 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
