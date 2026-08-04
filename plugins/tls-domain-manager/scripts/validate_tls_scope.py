"""Reject TLS plans that renew or rewrite configuration implicitly."""
from pathlib import Path
import argparse
FORBIDDEN=('certbot renew','certbot certonly','nginx -s reload','systemctl reload','tee /etc/nginx','rm ')
def main():
    p=argparse.ArgumentParser(); p.add_argument('--command-file',required=True); a=p.parse_args(); lines=Path(a.command_file).read_text(encoding='utf-8').splitlines(); blocked=[x for x in lines if any(t in x.lower() for t in FORBIDDEN)]; print({'status':'FAILED' if blocked else 'PASSED','blocked':blocked}); return 1 if blocked else 0
if __name__=='__main__': raise SystemExit(main())
