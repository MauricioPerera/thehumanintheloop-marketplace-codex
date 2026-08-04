"""Require recovery evidence for backup mutations."""
from pathlib import Path
import argparse
REQUIRED=('source:','destination:','retention:','restore-test:','confirmation:')
def main():
    p=argparse.ArgumentParser(); p.add_argument('--plan',required=True); a=p.parse_args(); text=Path(a.plan).read_text(encoding='utf-8').lower(); mutation=any(x in text for x in ('backup','restore','prune','delete')); missing=[x for x in REQUIRED if x not in text] if mutation else []; print({'status':'FAILED' if missing else 'PASSED','missing':missing}); return 1 if missing else 0
if __name__=='__main__': raise SystemExit(main())
