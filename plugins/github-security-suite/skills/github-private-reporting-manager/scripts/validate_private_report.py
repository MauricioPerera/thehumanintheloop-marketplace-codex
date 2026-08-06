#!/usr/bin/env python3
"""Validate a private vulnerability report."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("impact",r"(?i)\b(?:impact|impacto)\b"),("reproduction",r"(?i)\b(?:reproduc|steps|pasos)\b"),("versions",r"(?i)\b(?:versions?|versiones?)\b"),("mitigation",r"(?i)\b(?:mitigation|mitigaci[oó]n)\b"),("disclosure",r"(?i)\b(?:disclosure|divulgaci[oó]n|private|privado)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<70: errors.append("Private report must contain at least 70 words.")
    if re.search(r"(?i)(secret|token|password|api[_ -]?key)\s*[:=]\s*\S+",text): errors.append("Possible exposed secret.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
