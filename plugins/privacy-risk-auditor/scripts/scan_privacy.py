import argparse, json, re, sys
from pathlib import Path
PATTERNS={'secret':r'(?i)(api[_-]?key|secret|token|password)\s*[=:]\s*["\'][^"\']{8,}', 'email':r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', 'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'}
def main():
 p=argparse.ArgumentParser(); p.add_argument('root',nargs='?',default='.'); a=p.parse_args(); root=Path(a.root); findings=[]
 for f in root.rglob('*'):
  if not f.is_file() or '.git' in f.parts or f.stat().st_size>2_000_000: continue
  text=f.read_text(encoding='utf-8',errors='ignore')
  for kind,pat in PATTERNS.items():
   for m in re.finditer(pat,text): findings.append({'type':kind,'file':str(f.relative_to(root)),'line':text[:m.start()].count('\n')+1})
 result={'status':'FAILED' if findings else 'PASSED','findings':findings}; print(json.dumps(result,indent=2)); return 1 if findings else 0
if __name__=='__main__': sys.exit(main())
