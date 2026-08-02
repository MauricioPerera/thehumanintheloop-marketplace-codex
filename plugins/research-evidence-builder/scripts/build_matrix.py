import argparse,json,re,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('document');a=p.parse_args();t=Path(a.document).read_text(encoding='utf-8',errors='ignore'); lines=[x.strip() for x in t.splitlines() if x.strip() and not x.startswith('#')]; rows=[]
 for line in lines:
  if len(line.split())>=8: rows.append({'claim':line[:240],'hasDate':bool(re.search(r'\b(?:19|20)\d{2}\b',line)),'hasSource':bool(re.search(r'https?://|según|fuente',line,re.I))})
 print(json.dumps({'status':'PASSED' if rows else 'NEEDS_REVIEW','claims':rows,'count':len(rows)},indent=2,ensure_ascii=False)); return 0
if __name__=='__main__':sys.exit(main())
