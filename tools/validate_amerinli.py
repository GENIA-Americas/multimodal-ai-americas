#!/usr/bin/env python3
"""Check AmeriNLI JSONL files against the rules in datasets/amerinli/README.md."""
import json
import sys

REQUIRED = ["premise", "hypothesis", "label", "region", "domain"]
LABELS = {"entailment", "neutral", "contradiction"}
DOMAINS = {"news", "legal", "agriculture", "health", "education",
           "commerce", "culture", "environment"}


def check(path):
    errors = 0
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"{path}:{n}: invalid JSON ({e})")
                errors += 1
                continue
            for key in REQUIRED:
                if not isinstance(rec.get(key), str) or not rec[key].strip():
                    print(f"{path}:{n}: missing or empty '{key}'")
                    errors += 1
            if rec.get("label") not in LABELS:
                print(f"{path}:{n}: label must be one of {sorted(LABELS)}")
                errors += 1
            if rec.get("domain") not in DOMAINS:
                print(f"{path}:{n}: domain must be one of {sorted(DOMAINS)}")
                errors += 1
            region = rec.get("region")
            if not (isinstance(region, str) and len(region) == 2 and region.isupper()):
                print(f"{path}:{n}: region must be a 2-letter uppercase ISO 3166-1 code")
                errors += 1
    return errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: validate_amerinli.py file.jsonl [more.jsonl ...]")
    total = sum(check(p) for p in sys.argv[1:])
    print("OK" if total == 0 else f"{total} problem(s)")
    sys.exit(1 if total else 0)
