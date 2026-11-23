#!/usr/bin/env python3
"""Summarize AmeriNLI JSONL files: balance by label, domain, region, and a
negation-shortcut check. Run it before opening a pull request.

Usage: python3 tools/amerinli_stats.py file.jsonl [more.jsonl ...]
"""
import json
import re
import sys
from collections import Counter

NEGATION = re.compile(r"\b(no|nunca|jam[aá]s|ning[uú]n|ninguna|ninguno|nadie|tampoco)\b", re.I)


def load(paths):
    rows = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return rows


def show(title, counter, total):
    print(f"\n{title}")
    for key, n in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {key:<14} {n:>5}  {100 * n / total:5.1f}%")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: amerinli_stats.py file.jsonl [more.jsonl ...]")
    rows = [r for r in load(sys.argv[1:]) if isinstance(r, dict)]
    if not rows:
        sys.exit("no records found")
    total = len(rows)
    print(f"{total} record(s)")
    labels = Counter(r.get("label", "?") for r in rows)
    show("By label", labels, total)
    show("By domain", Counter(r.get("domain", "?") for r in rows), total)
    show("By region", Counter(r.get("region", "?") for r in rows), total)

    print("\nHypotheses containing a negation word, by label")
    for label in sorted(labels):
        hyp = [str(r.get("hypothesis", "")) for r in rows if r.get("label") == label]
        hits = sum(1 for h in hyp if NEGATION.search(h))
        print(f"  {label:<14} {hits:>3} of {len(hyp):<4} ({100 * hits / len(hyp):.0f}%)")

    if total >= 20 and len(labels) > 1:
        most, least = max(labels.values()), min(labels.values())
        if most > 2 * least:
            print("\nNote: label counts are uneven. Aim for roughly equal numbers.")
        contra = [str(r.get("hypothesis", "")) for r in rows if r.get("label") == "contradiction"]
        if contra and sum(1 for h in contra if NEGATION.search(h)) / len(contra) > 0.6:
            print("Note: most contradictions use a negation word. Vary how you write them.")
