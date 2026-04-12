#!/usr/bin/env python3
"""Normalize filenames in docs/ to kebab-case and unify .md/.txt appropriately.

Behavior:
- Target name: lowercase, spaces/underscores -> hyphens, multiple hyphens collapsed.
- If a `.txt` file appears to be markdown (starts with '#' or '---' frontmatter), convert to `.md`.
- If target file already exists and contents match, remove the source duplicate.
- If target exists and contents differ, leave both and write a `.conflict` log.

Run from repo root: `python scripts/normalize_docs_names.py`
"""
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'

def kebab(name: str) -> str:
    name = name.strip()
    name = name.replace(' ', '-')
    name = name.replace('_', '-')
    name = re.sub(r'[^a-z0-9\-\.]+', '', name.lower())
    name = re.sub(r'-{2,}', '-', name)
    return name

def should_convert_txt_to_md(path: Path) -> bool:
    try:
        with path.open('r', encoding='utf-8') as f:
            head = ''.join([next(f) for _ in range(5)])
    except Exception:
        return False
    if head.lstrip().startswith('#'):
        return True
    if head.lstrip().startswith('---'):
        return True
    return False

def file_contents(path: Path):
    try:
        return path.read_bytes()
    except Exception:
        return None

def safe_rename(src: Path, dst: Path):
    dst_parent = dst.parent
    dst_parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if file_contents(src) == file_contents(dst):
            print(f"Duplicate identical: removing {src.name}")
            src.unlink()
            return
        else:
            conflict = dst.with_suffix(dst.suffix + '.conflict')
            print(f"Conflict: {src.name} -> {dst.name} (saving as {conflict.name})")
            src.rename(conflict)
            return
    # On Windows, renaming case-only requires temp
    if src.resolve() == dst.resolve():
        print(f"No-op for {src.name}")
        return
    tmp = dst.with_suffix(dst.suffix + '.tmp')
    src.replace(tmp)
    tmp.replace(dst)
    print(f"Renamed: {src.name} -> {dst.name}")

def main():
    if not DOCS.exists():
        print('docs/ not found')
        return
    for p in sorted(DOCS.iterdir()):
        if p.is_dir():
            continue
        orig = p.name
        stem = p.stem
        suffix = p.suffix  # includes leading dot
        # decide new suffix for .txt
        if suffix.lower() == '.txt' and should_convert_txt_to_md(p):
            new_suffix = '.md'
        else:
            new_suffix = suffix.lower()
        new_stem = kebab(stem)
        new_name = new_stem + new_suffix
        dst = DOCS / new_name
        if p.name == new_name:
            print(f"OK: {p.name}")
            continue
        safe_rename(p, dst)

if __name__ == '__main__':
    main()
