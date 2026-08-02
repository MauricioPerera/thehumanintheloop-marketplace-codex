import argparse, json, re, sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('path'); a=p.parse_args(); root=Path(a.path); files=[root] if root.is_file() else list(root.rglob('*.html')); errors=[]; images=buttons=labels=0
    for f in files:
        t=f.read_text(encoding='utf-8',errors='ignore'); images+=len(re.findall(r'<img\b',t,re.I)); buttons+=len(re.findall(r'<button\b',t,re.I)); labels+=len(re.findall(r'<label\b',t,re.I))
        for m in re.finditer(r'<img\b([^>]*)>',t,re.I):
            if not re.search(r'\balt\s*=',m.group(1),re.I): errors.append(f'{f}: image without alt')
        for m in re.finditer(r'<button\b([^>]*)>(.*?)</button>',t,re.I|re.S):
            attrs, body = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
            if not body and not re.search(r'aria-label\s*=|title\s*=', attrs, re.I): errors.append(f'{f}: button without accessible name')
    result={'status':'FAILED' if errors else 'PASSED','files':len(files),'images':images,'buttons':buttons,'labels':labels,'errors':errors}; print(json.dumps(result,indent=2)); return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
