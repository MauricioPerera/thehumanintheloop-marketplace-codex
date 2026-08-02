import argparse,json,re,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('guide');p.add_argument('text');a=p.parse_args();g=Path(a.guide).read_text(encoding='utf-8',errors='ignore');t=Path(a.text).read_text(encoding='utf-8',errors='ignore'); banned=re.findall(r'(?i)(?:prohibid[oa]s?|avoid|no usar)[:\-]\s*([^\n]+)',g); terms=[]
 for group in banned: terms += re.findall(r'[\w-]+',group.lower())
 hits=[x for x in terms if re.search(r'\b'+re.escape(x)+r'\b',t,re.I)]; result={'status':'FAILED' if hits else 'PASSED','bannedHits':sorted(set(hits)),'wordCount':len(t.split()),'sentences':len(re.findall(r'[.!?]+',t))}; print(json.dumps(result,indent=2,ensure_ascii=False)); return 1 if hits else 0
if __name__=='__main__':sys.exit(main())
