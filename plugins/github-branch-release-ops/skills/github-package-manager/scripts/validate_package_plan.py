#!/usr/bin/env python3
"""Validate a GitHub package plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("package",r"(?i)\b(?:package|paquete|container|artifact)\b"),("version",r"(?i)\b(?:version|versi[oó]n|tag)\b"),("consumers",r"(?i)\b(?:consumer|consumidor|dependency|dependencia)\b"),("retention",r"(?i)\b(?:retention|retenci[oó]n|cleanup|limpieza)\b"),("rollback",r"(?i)\b(?:rollback|revert|revers)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<70:errors.append("Package plan must contain at least 70 words.")
    if re.search(r"(?i)(token|password|secret|api[_ -]?key)\s*[:=]\s*\S+",text):errors.append("Possible exposed package credential.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
