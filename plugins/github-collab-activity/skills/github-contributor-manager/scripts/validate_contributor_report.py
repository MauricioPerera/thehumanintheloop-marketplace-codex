#!/usr/bin/env python3
"""Validate a contributor analysis report."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("scope",r"(?i)\b(?:scope|alcance|repository|repositorio)\b"),("activity",r"(?i)\b(?:activity|actividad|commit|pull request|review)\b"),("evidence",r"(?i)\b(?:evidence|evidencia|https?://)\b"),("confidence",r"(?i)\b(?:confidence|confianza|high|medium|low|alta|media|baja)\b"),("limitations",r"(?i)\b(?:limitations?|limitaci[oó]n(?:es)?|caveat(?:s)?)\b")]:
        if not re.search(p,text):errors.append(f"Missing {label} information.")
    if len(text.split())<70:errors.append("Contributor report must contain at least 70 words.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
