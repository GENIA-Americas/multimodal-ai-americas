#!/usr/bin/env python3
"""Convert a spreadsheet export (CSV) of AmeriNLI examples to validated JSONL.

Columns: premise, hypothesis, label, region, domain, notes (notes optional).
Spanish headers and labels are accepted. Handles Excel exports (UTF-8 with
BOM, comma or semicolon separators).

Usage:
  python3 tools/csv_to_jsonl.py examples.csv --contributor <github-username> \
      --out datasets/amerinli/submissions/<github-username>_<region>.jsonl

Nothing is written if any row has a problem.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_amerinli import check_record, load_schema  # noqa: E402

HEADERS = {
    "premisa": "premise", "hipotesis": "hypothesis", "hipótesis": "hypothesis",
    "etiqueta": "label", "region": "region", "región": "region",
    "dominio": "domain", "notas": "notes",
}
LABELS = {
    "implicacion": "entailment", "implicación": "entailment",
    "contradiccion": "contradiction", "contradicción": "contradiction",
    "neutral": "neutral", "neutro": "neutral",
}
DOMAINS = {
    "noticias": "news", "legal": "legal", "agricultura": "agriculture",
    "salud": "health", "educacion": "education", "educación": "education",
    "comercio": "commerce", "cultura": "culture", "ambiente": "environment",
    "medio ambiente": "environment",
}


def read_rows(path):
    text = Path(path).read_text(encoding="utf-8-sig")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def normalize(row, contributor):
    rec = {}
    for key, value in row.items():
        if key is None:
            continue
        name = key.strip().lower()
        name = HEADERS.get(name, name)
        value = (value or "").strip()
        if value:
            rec[name] = value
    if "label" in rec:
        low = rec["label"].lower()
        rec["label"] = LABELS.get(low, low)
    if "domain" in rec:
        low = rec["domain"].lower()
        rec["domain"] = DOMAINS.get(low, low)
    if "region" in rec:
        rec["region"] = rec["region"].upper()
    if contributor:
        rec["contributor"] = contributor
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_file")
    ap.add_argument("--contributor", help="GitHub username or name to credit")
    ap.add_argument("--out", required=True, help="output .jsonl path")
    args = ap.parse_args()

    required, props, allow_extra = load_schema()
    records, errors = [], 0
    for i, row in enumerate(read_rows(args.csv_file), start=2):  # row 1 is the header
        if not any((v or "").strip() for v in row.values() if v is not None):
            continue
        rec = normalize(row, args.contributor)
        problems = check_record(rec, required, props, allow_extra)
        for p in problems:
            print(f"row {i}: {p}")
        errors += len(problems)
        records.append(rec)

    if errors:
        sys.exit(f"{errors} problem(s) found, nothing written")
    if not records:
        sys.exit("no rows found")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} record(s) to {out}")
    print(f"next: python3 tools/validate_amerinli.py {out}")


if __name__ == "__main__":
    main()
