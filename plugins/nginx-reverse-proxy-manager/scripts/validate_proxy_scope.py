"""Reject proxy audit plans that edit or reload Nginx."""
from pathlib import Path
import argparse
FORBIDDEN=('tee /etc/nginx','sed -i','nginx -s reload','systemctl reload nginx','systemctl restart nginx','rm /etc/nginx')
def main():
 p=argparse.ArgumentParser();p.add_argument('--command-file',required=True);a=p.parse_args();xs=Path(a.command_file).read_text(encoding='utf-8').splitlines();b=[x for x in xs if any(t in x.lower() for t in FORBIDDEN)];print({'status':'FAILED' if b else 'PASSED','blocked':b});return 1 if b else 0
if __name__=='__main__':raise SystemExit(main())
