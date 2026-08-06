#!/usr/bin/env python3
"""Validate a public repository funding audit."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("funding",r"(?i)\b(?:funding|financiaci[oó]n|sponsor)\b"),("provider",r"(?i)\b(?:provider|proveedor|github sponsors)\b"),("link",r"(?i)\b(?:link|enlace|URL)\b"),("consistency",r"(?i)\b(?:consistency|consistencia|README|documentation)\b"),("validation",r"(?i)\b(?:validation|validaci[oó]n|broken|roto)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<60: errors.append("Funding audit must contain at least 60 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
