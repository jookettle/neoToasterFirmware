#!/usr/bin/env python3
from pathlib import Path
import difflib
DOCS = Path('docs')
for c in DOCS.glob('*.conflict'):
    orig = DOCS / c.stem
    print('\n=== DIFF for', orig.name, 'vs', c.name, '===')
    a = orig.read_text(encoding='utf-8').splitlines()
    b = c.read_text(encoding='utf-8').splitlines()
    for line in difflib.unified_diff(a,b,fromfile=str(orig),tofile=str(c),n=3):
        print(line)
