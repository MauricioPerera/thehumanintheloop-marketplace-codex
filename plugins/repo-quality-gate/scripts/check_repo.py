import argparse, json, re, sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('root',nargs='?',default='.'); a=p.parse_args(); root=Path(a.root)
    files=[x for x in root.rglob('*') if x.is_file() and '.git' not in x.parts]
    names={x.name.lower() for x in files}; errors=[]; warnings=[]
    if not any(n in names for n in ('readme.md','readme.txt')): warnings.append('Missing README')
    if not any(n in names for n in ('license','license.md','license.txt')): warnings.append('Missing LICENSE')
    for f in files:
        if f.suffix in ('.env','.key','.pem') or f.name.lower() in ('id_rsa','credentials.json'): errors.append(f'Potential secret file: {f.relative_to(root)}')
    result={'status':'FAILED' if errors else ('NEEDS_REVIEW' if warnings else 'PASSED'),'errors':errors,'warnings':warnings,'fileCount':len(files)}; print(json.dumps(result,indent=2)); return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
