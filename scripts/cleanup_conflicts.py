#!/usr/bin/env python3
from pathlib import Path
DOCS = Path('docs')
removed = []
for c in DOCS.glob('*.conflict'):
    orig = DOCS / c.stem
    try:
        if orig.exists() and c.read_bytes() == orig.read_bytes():
            c.unlink()
            removed.append(c.name)
    except Exception as e:
        print('error checking', c, e)
if removed:
    print('removed conflicts:', removed)
else:
    print('no identical conflicts removed')
