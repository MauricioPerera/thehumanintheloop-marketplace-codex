import argparse,json,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('contract');a=p.parse_args();path=Path(a.contract); errors=[]
 try: data=json.loads(path.read_text(encoding='utf-8'))
 except Exception as e: print(json.dumps({'status':'FAILED','errors':[str(e)]},indent=2));return 1
 if not data.get('openapi') and not data.get('swagger'): errors.append('Missing openapi or swagger version')
 paths=data.get('paths',{})
 if not paths: errors.append('Contract has no paths')
 operations=sum(len([k for k in v if k.lower() in ('get','post','put','patch','delete','head','options')]) for v in paths.values() if isinstance(v,dict))
 print(json.dumps({'status':'FAILED' if errors else 'PASSED','paths':len(paths),'operations':operations,'errors':errors},indent=2));return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
