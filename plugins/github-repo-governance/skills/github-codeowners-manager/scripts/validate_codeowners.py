#!/usr/bin/env python3
"""Validate CODEOWNERS syntax and ownership coverage."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]; rules=0
    for line in text.splitlines():
        line=line.strip()
        if not line or line.startswith('#'):continue
        parts=line.split()
        if len(parts)<2:errors.append(f"Invalid CODEOWNERS rule: {line}")
        else:
            rules+=1
            if not any(x.startswith('@') or '@' in x for x in parts[1:]):errors.append(f"Rule has no user or team owner: {line}")
    if rules==0:errors.append("No CODEOWNERS rules found.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]\s*\S+",text):errors.append("Possible credential in CODEOWNERS.")
    return {"status":"PASSED" if not errors else "FAILED","rules":rules,"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
