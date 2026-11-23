#!/usr/bin/env python3
"""Fail if any relative link in a tracked Markdown file points to a missing path."""
import pathlib
import re
import subprocess
import sys

files = subprocess.check_output(["git", "ls-files", "*.md"], text=True).split()
broken = 0
for f in files:
    p = pathlib.Path(f)
    text = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.S)
    for m in re.finditer(r"\]\(([^)\s]+)\)", text):
        url = m.group(1)
        if re.match(r"(https?:|mailto:|#)", url):
            continue
        if not (p.parent / url.split("#")[0]).resolve().exists():
            print(f"{f}: broken link -> {url}")
            broken += 1
print(f"{len(files)} files checked, {broken} broken link(s)")
sys.exit(1 if broken else 0)
