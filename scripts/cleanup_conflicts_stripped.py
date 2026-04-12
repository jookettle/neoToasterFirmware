#!/usr/bin/env python3
from pathlib import Path
DOCS = Path('docs')
removed=[]
for c in DOCS.glob('*.conflict'):
    orig = DOCS / c.stem
    try:
        if orig.exists():
            ctxt = c.read_text(encoding='utf-8').strip()
            otxt = orig.read_text(encoding='utf-8').strip()
            if ctxt == otxt:
                c.unlink()
                removed.append(c.name)
    except Exception as e:
        print('err',c,e)
if removed:
    print('removed (stripped):', removed)
else:
    print('no identical (stripped) conflicts removed')
