#!/usr/bin/env python3
"""
add_summaries.py — persist hand-written summaries (or other per-entry fields,
like a fetched date) into corpus/curated.jsonl.

Values written straight into corpus.jsonl do not survive: the merge overlays
summary/date onto the crawl by matching id against the --seed (curated.jsonl).
So a crawl-only entry keeps a value only once it lives in the curated layer.

This upserts {id: value} pairs into curated.jsonl for the given --field
(default "summary"). For an id already there, it updates that field in place.
For a crawl-only id, it appends a full curated record built from that entry
in corpus.jsonl (url/title/category/sources), so validate_corpus.py's schema
+ provenance checks still pass.

    python tools/add_summaries.py --values batch.json
    # batch.json: {"arxiv:2601.06606": "One sentence.", ...}

    python tools/add_summaries.py --values dates.json --field date
    # dates.json: {"gh:owner/repo": "2022-03", ...}

Then rebuild and validate:
    python tools/merge_agent_lists.py --out corpus --max-tier 1 --seed corpus/curated.jsonl
    python tools/validate_corpus.py --jsonl corpus.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--values", "--summaries", dest="values", type=Path, required=True,
                    help="JSON file: {canonical_id: value}")
    ap.add_argument("--field", default="summary",
                    help="curated.jsonl field to write the values into (default: summary)")
    ap.add_argument("--corpus", type=Path, default=Path("corpus/corpus.jsonl"))
    ap.add_argument("--curated", type=Path, default=Path("corpus/curated.jsonl"))
    args = ap.parse_args()
    field = args.field

    new = json.loads(args.values.read_text(encoding="utf-8"))
    corpus = {r["id"]: r for r in load_jsonl(args.corpus)}
    curated = load_jsonl(args.curated)
    by_id = {r["id"]: r for r in curated}

    updated, added, missing = 0, 0, []
    for cid, value in new.items():
        value = value.strip()
        if not value:
            continue
        if cid in by_id:
            by_id[cid][field] = value
            updated += 1
            continue
        src = corpus.get(cid)
        if src is None:
            missing.append(cid)
            continue
        rec = {
            "id": src["id"],
            "id_type": src.get("id_type", ""),
            "url": src["url"],
            "title": src["title"],
            "summary": "TODO",
            "category": src["category"],
            "subsection": "",
            "sources": src.get("sources", []),
            "origin": "crawl",
            "also_in": src.get("categories", []),
        }
        rec[field] = value
        curated.append(rec)
        by_id[cid] = rec
        added += 1

    if missing:
        print(f"  !! {len(missing)} id(s) not found in {args.corpus}:", file=sys.stderr)
        for m in missing:
            print(f"     {m}", file=sys.stderr)

    with args.curated.open("w", encoding="utf-8") as fh:
        for r in curated:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"curated.jsonl: {updated} updated, {added} added, {len(curated)} total ({field})")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
