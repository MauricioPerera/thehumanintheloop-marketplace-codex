#!/usr/bin/env python3
"""Validate a Terraform plan review."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("resource",r"(?i)\b(?:resource|recurso)\b"),("action",r"(?i)\b(?:create|update|delete|replace|crear|actualizar|eliminar|reemplazar)\b"),("risk",r"(?i)\b(?:risk|riesgo)\b"),("evidence",r"(?i)\b(?:evidence|evidencia|plan line|l[ií]nea)\b"),("recommendation",r"(?i)\b(?:recommendation|recomendaci[oó]n)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<60: errors.append("Plan review must contain at least 60 words.")
    if re.search(r"(?i)\bterraform\s+(apply|destroy|import)\b",text): errors.append("Review must not instruct terraform apply/destroy/import.")
    if re.search(r"(?i)-auto-approve",text): errors.append("Review must not suggest -auto-approve.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
