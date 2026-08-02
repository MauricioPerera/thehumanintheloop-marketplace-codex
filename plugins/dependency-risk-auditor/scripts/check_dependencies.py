import argparse,json,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='.');a=p.parse_args();r=Path(a.root); manifests=[x for x in r.rglob('*') if x.name in ('package.json','pyproject.toml','requirements.txt','go.mod','Cargo.toml') and '.git' not in x.parts]; locks=[x for x in r.rglob('*') if 'lock' in x.name.lower() and '.git' not in x.parts]; result={'status':'PASSED' if locks else 'NEEDS_REVIEW','manifests':[str(x.relative_to(r)) for x in manifests],'lockfiles':[str(x.relative_to(r)) for x in locks]};print(json.dumps(result,indent=2));return 0
if __name__=='__main__':sys.exit(main())
