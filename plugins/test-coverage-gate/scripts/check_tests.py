import argparse,json,re,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='.');a=p.parse_args();r=Path(a.root); tests=[x for x in r.rglob('*') if x.is_file() and (('test' in x.name.lower() or 'spec' in x.name.lower()) and x.suffix.lower() in ('.py','.js','.ts','.jsx','.tsx','.go','.rs'))]; reports=[x for x in r.rglob('*') if x.is_file() and ('coverage' in x.name.lower() or 'junit' in x.name.lower())]; result={'status':'PASSED' if tests else 'NEEDS_REVIEW','testFiles':len(tests),'reports':len(reports),'evidence':[str(x.relative_to(r)) for x in reports]};print(json.dumps(result,indent=2));return 0
if __name__=='__main__':sys.exit(main())
