#!/usr/bin/env python3
"""Validate a GitHub Actions incident report."""
import argparse, json, re, sys
from pathlib import Path

def validate(text):
    errors=[]
    for label, pattern in [("run", r"(?i)\b(?:run|execution|ejecuci[oó]n)\b"),("workflow",r"(?i)\bworkflow\b"),("evidence",r"(?i)\b(?:evidence|evidencia|log)\b"),("hypotheses",r"(?i)\b(?:hypothes|hip[oó]tesis|possible cause|causa posible)"),("next action",r"(?i)\b(?:next action|siguiente acci[oó]n|recommendation|recomendaci[oó]n)\b")]:
        if not re.search(pattern,text): errors.append(f"Missing {label} section or evidence.")
    if len(text.split())<60: errors.append("Report must contain at least 60 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]",text): errors.append("Possible credential in report.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True,type=Path); p.add_argument("--json",dest="json_path",type=Path); a=p.parse_args(); r=validate(a.input.read_text(encoding="utf-8"));
    if a.json_path: a.json_path.write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["status"]=="PASSED" else 1
if __name__=="__main__": sys.exit(main())
