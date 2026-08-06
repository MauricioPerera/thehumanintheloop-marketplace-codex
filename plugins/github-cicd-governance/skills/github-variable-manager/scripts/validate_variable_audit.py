#!/usr/bin/env python3
"""Validate a GitHub Actions variable audit."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("scope",r"(?i)\b(?:scope|alcance|repository|environment|organization)\b"),("names",r"(?i)\b(?:variable|variables|name|nombre)\b"),("references",r"(?i)\b(?:references?|referencias?|workflow)\b"),("secret safety",r"(?i)\b(?:secret|secreto|value|valor|redact|not exposed)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<60:errors.append("Variable audit must contain at least 60 words.")
    if re.search(r"(?i)(secret|token|password|api[_ -]?key)\s*[:=]\s*\S+",text):errors.append("Possible exposed variable secret.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
