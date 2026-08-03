#!/usr/bin/env python3
"""Validate a Mercado Pago Checkout Preference payment plan."""
import argparse,json,re,sys
from pathlib import Path
def validate(text):
    errors=[]
    for label,p in [("items",r"(?i)\b(?:items?|art[ií]culos?)\b"),("quantity",r"(?i)\b(?:quantity|cantidad)\b"),("currency",r"(?i)\b(?:currency|moneda|currency_id)\b"),("unit price",r"(?i)\b(?:unit price|precio unitario|unit_price)\b"),("reference",r"(?i)\b(?:external_reference|external reference|referencia)\b"),("HTTPS callbacks",r"(?i)\bhttps://\S+\b"),("confirmation",r"(?i)\b(?:confirmation|confirmaci[oó]n|approval|aprobaci[oó]n)\b")]:
        if not re.search(p,text): errors.append(f"Missing {label} information.")
    if len(text.split())<90: errors.append("Payment plan must contain at least 90 words.")
    if re.search(r"(?i)(access[_ -]?token|bearer|password|api[_ -]?key)\s*[:=]\s*\S+",text): errors.append("Possible exposed credential.")
    if re.search(r"(?i)http://",text): errors.append("Callbacks must use HTTPS.")
    return {"status":"PASSED" if not errors else "FAILED","word_count":len(text.split()),"errors":errors}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--json',dest='json_path',type=Path);a=p.parse_args();r=validate(a.input.read_text(encoding='utf-8'))
    if a.json_path:a.json_path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2));return 0 if r['status']=='PASSED' else 1
if __name__=='__main__':sys.exit(main())
