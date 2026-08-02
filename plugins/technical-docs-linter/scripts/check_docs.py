import argparse, json, re, sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('root',nargs='?',default='.'); a=p.parse_args(); root=Path(a.root); docs=[x for x in root.rglob('*') if x.is_file() and x.suffix.lower() in ('.md','.mdx','.rst')]
    errors=[]; links=0; code=0
    for f in docs:
        text=f.read_text(encoding='utf-8',errors='ignore'); links+=len(re.findall(r'https?://\S+',text)); code+=len(re.findall(r'```',text))
        if f.name.lower()=='readme.md' and len(text.strip())<100: errors.append(f'{f}: README is too short')
    result={'status':'FAILED' if errors else 'PASSED','documents':len(docs),'links':links,'codeFences':code,'errors':errors}; print(json.dumps(result,indent=2)); return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
