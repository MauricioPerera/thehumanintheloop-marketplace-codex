import argparse,json,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('root');a=p.parse_args();r=Path(a.root); files=[x for x in r.rglob('*') if x.is_file() and x.suffix.lower() in ('.js','.css','.png','.jpg','.jpeg','.webp','.woff','.woff2')]; large=[{'file':str(x.relative_to(r)),'bytes':x.stat().st_size} for x in files if x.stat().st_size>500_000]; result={'status':'NEEDS_REVIEW' if large else 'PASSED','assets':len(files),'largeAssets':large}; print(json.dumps(result,indent=2));return 0
if __name__=='__main__':sys.exit(main())
