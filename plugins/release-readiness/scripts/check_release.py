import argparse, json, sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser(); p.add_argument('root',nargs='?',default='.'); a=p.parse_args(); r=Path(a.root); names={x.name.lower() for x in r.rglob('*') if x.is_file() and '.git' not in x.parts}; missing=[]
 for required in ('readme.md','license'):
  if required not in names and not any(n.startswith(required+'.') for n in names): missing.append(required)
 checks={'readme':not any(n.startswith('readme') for n in names),'license':not any(n.startswith('license') for n in names),'changelog':not any(n.startswith('changelog') for n in names)}
 result={'status':'NEEDS_REVIEW' if missing else 'PASSED','missing':missing,'checks':checks}; print(json.dumps(result,indent=2)); return 0
if __name__=='__main__': sys.exit(main())
