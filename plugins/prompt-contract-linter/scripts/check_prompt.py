import argparse, json, re, sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser(); p.add_argument('prompt'); a=p.parse_args(); t=Path(a.prompt).read_text(encoding='utf-8',errors='ignore'); keys={'objective':r'(?i)(objetivo|goal|task|tarea)','inputs':r'(?i)(entrada|input|contexto)','output':r'(?i)(salida|output|formato)','constraints':r'(?i)(restric|limit|no debes|must not)','acceptance':r'(?i)(aceptación|acceptance|criterio|success)'}; missing=[k for k,v in keys.items() if not re.search(v,t)]; result={'status':'FAILED' if missing else 'PASSED','missing':missing,'wordCount':len(t.split())}; print(json.dumps(result,indent=2,ensure_ascii=False)); return 1 if missing else 0
if __name__=='__main__': sys.exit(main())
