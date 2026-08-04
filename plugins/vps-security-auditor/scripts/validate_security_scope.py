"""Reject security audit plans that mutate access controls."""
from pathlib import Path
import argparse
FORBIDDEN = ("ufw allow", "ufw deny", "iptables -a", "useradd", "userdel", "passwd", "systemctl restart", "apt install")
def main():
    p=argparse.ArgumentParser(); p.add_argument('--command-file',required=True); a=p.parse_args(); lines=[x.strip() for x in Path(a.command_file).read_text(encoding='utf-8').splitlines() if x.strip()]; blocked=[x for x in lines if any(t in x.lower() for t in FORBIDDEN)]; print({'status':'FAILED' if blocked else 'PASSED','blocked':blocked}); return 1 if blocked else 0
if __name__=='__main__': raise SystemExit(main())
