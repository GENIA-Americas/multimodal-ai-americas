#!/usr/bin/env python3
"""Validate AmeriNLI JSONL files against datasets/amerinli/schema.json.

The schema file is the single source of truth for required fields, allowed
values, and length limits. Also reports duplicate premise/hypothesis pairs.

Usage: python3 tools/validate_amerinli.py file.jsonl [more.jsonl ...]
"""
import json
import re
import sys
from pathlib import Path

SCHEMA = Path(__file__).resolve().parent.parent / "datasets" / "amerinli" / "schema.json"


def load_schema():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return schema["required"], schema["properties"], schema.get("additionalProperties", True)


def check_record(rec, required, props, allow_extra):
    """Return a list of problems for one record."""
    if not isinstance(rec, dict):
        return ["record must be a JSON object"]
    problems = []
    for key in required:
        if key not in rec:
            problems.append(f"missing '{key}'")
    for key, value in rec.items():
        if key not in props:
            if not allow_extra:
                problems.append(f"unknown field '{key}'")
            continue
        spec = props[key]
        if spec.get("type") == "string" and not isinstance(value, str):
            problems.append(f"'{key}' must be a string")
            continue
        if not isinstance(value, str):
            continue
        if "minLength" in spec and len(value.strip()) < spec["minLength"]:
            problems.append(f"'{key}' must be at least {spec['minLength']} characters")
        if "enum" in spec and value not in spec["enum"]:
            problems.append(f"'{key}' must be one of {spec['enum']}")
        if "pattern" in spec and not re.search(spec["pattern"], value):
            problems.append(f"'{key}' must match {spec['pattern']}")
    return problems


def check_file(path, required, props, allow_extra, seen):
    errors = 0
    count = 0
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            count += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"{path}:{n}: invalid JSON ({e})")
                errors += 1
                continue
            for p in check_record(rec, required, props, allow_extra):
                print(f"{path}:{n}: {p}")
                errors += 1
            if isinstance(rec, dict):
                key = (str(rec.get("premise", "")).strip().lower(),
                       str(rec.get("hypothesis", "")).strip().lower())
                if key in seen:
                    print(f"{path}:{n}: duplicate of {seen[key]}")
                    errors += 1
                else:
                    seen[key] = f"{path}:{n}"
    return errors, count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: validate_amerinli.py file.jsonl [more.jsonl ...]")
    required, props, allow_extra = load_schema()
    seen, total_err, total_rec = {}, 0, 0
    for path in sys.argv[1:]:
        e, c = check_file(path, required, props, allow_extra, seen)
        total_err += e
        total_rec += c
    print(f"{total_rec} record(s), " + ("OK" if total_err == 0 else f"{total_err} problem(s)"))
    sys.exit(1 if total_err else 0)
