#!/usr/bin/env python3
import subprocess,sys
p = subprocess.run(['git','ls-files'], capture_output=True, text=True)
files = p.stdout.splitlines()
hash_map = {}
for f in files:
    try:
        h = subprocess.run(['git','hash-object',f], capture_output=True, text=True).stdout.strip()
    except Exception:
        continue
    hash_map.setdefault(h,[]).append(f)

dups = {h:ps for h,ps in hash_map.items() if len(ps)>1}
if dups:
    for h,ps in dups.items():
        print('==',h, '(%d)'%len(ps))
        for p in ps:
            print(p)
        print()
else:
    print('No exact duplicate files found')

# Also report duplicate basenames across different directories
from collections import defaultdict
bases = defaultdict(list)
for f in files:
    import os
    bases[os.path.basename(f)].append(f)
dup_basenames = {b:ps for b,ps in bases.items() if len(ps)>1}
if dup_basenames:
    print('\nDuplicate basenames across repo:')
    for b,ps in sorted(dup_basenames.items(), key=lambda x: -len(x[1]))[:50]:
        print(f"-- {b} ({len(ps)})")
        for p in ps:
            print(f"   {p}")
        print()
else:
    print('No duplicate basenames found')
