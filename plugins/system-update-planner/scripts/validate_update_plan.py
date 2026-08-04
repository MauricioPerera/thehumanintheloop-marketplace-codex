"""Require a change plan for system update mutations."""
from pathlib import Path
import argparse
REQUIRED=('preflight:','packages:','reboot:','rollback:','confirmation:')
def main():
 p=argparse.ArgumentParser();p.add_argument('--plan',required=True);a=p.parse_args();t=Path(a.plan).read_text(encoding='utf-8').lower();m=any(x in t for x in ('apt upgrade','apt install','dnf update','reboot'));missing=[x for x in REQUIRED if x not in t] if m else [];print({'status':'FAILED' if missing else 'PASSED','missing':missing});return 1 if missing else 0
if __name__=='__main__':raise SystemExit(main())
