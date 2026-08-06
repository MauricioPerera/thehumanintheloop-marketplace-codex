#!/usr/bin/env python3
"""Validate a GitHub Project planning document."""
import argparse, json, re, sys
from pathlib import Path

def validate(text):
    errors=[]
    for label, pattern in [("owner/project",r"(?i)\b(?:owner|org|organization|project)\b"),("items",r"(?i)\b(?:items?|issues?|pull requests?|tareas?)\b"),("status",r"(?i)\b(?:status|estado)\b"),("dependencies",r"(?i)\b(?:dependenc|bloquead|blocked)"),("decisions",r"(?i)\b(?:decision|decisi[oó]n|open|pendiente)")]:
        if not re.search(pattern,text): errors.append(f"Missing {label} information.")
    if len(text.split())<60: errors.append("Project plan must contain at least 60 words.")
    if re.search(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]",text): errors.append("Possible credential in plan.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True,type=Path); p.add_argument("--json",dest="json_path",type=Path); a=p.parse_args(); r=validate(a.input.read_text(encoding="utf-8"));
    if a.json_path: a.json_path.write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["status"]=="PASSED" else 1
if __name__=="__main__": sys.exit(main())
