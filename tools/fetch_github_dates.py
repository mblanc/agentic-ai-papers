#!/usr/bin/env python3
"""
fetch_github_dates.py — fetch repo creation dates for gh: corpus entries and
persist them via add_summaries.py --field date.

A repo's creation date is a proxy for "when this tool entered the ecosystem",
not a guarantee — a repo can sit dark for years before the fork/rewrite that
made it notable. It's the best signal available without per-repo commit-log
archaeology, and it's free public metadata (no token permissions needed; a
token here only lifts the unauthenticated 60/hr rate limit to 5,000/hr).

Reads GITHUB_TOKEN from the environment, or from .env.local if present
(never printed, never logged).

    python tools/fetch_github_dates.py --out /tmp/gh_dates.json
    python tools/add_summaries.py --values /tmp/gh_dates.json --field date
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_token() -> str | None:
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    env_file = ROOT / ".env.local"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("GITHUB_TOKEN="):
                return line.split("=", 1)[1].strip()
    return None


def fetch_created_at(owner: str, repo: str, token: str) -> str | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "agentic-ai-papers-corpus-tool",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            created = data.get("created_at", "")  # e.g. "2015-06-23T12:34:56Z"
            return created[:7] if created else None  # "YYYY-MM"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # renamed/deleted repo
        raise


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path, default=ROOT / "corpus" / "corpus.jsonl")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    token = load_token()
    if not token:
        print("!! no GITHUB_TOKEN in env or .env.local", file=sys.stderr)
        return 1

    rows = [json.loads(l) for l in args.corpus.read_text().splitlines() if l.strip()]
    targets = [r for r in rows if r["id_type"] == "github" and not r.get("date")]
    print(f"{len(targets)} undated github entries to fetch")

    results: dict[str, str] = {}
    not_found: list[str] = []
    for i, r in enumerate(targets, 1):
        owner_repo = r["id"].split(":", 1)[1]
        owner, _, repo = owner_repo.partition("/")
        try:
            date = fetch_created_at(owner, repo, token)
        except Exception as exc:  # noqa: BLE001
            print(f"  !! {r['id']}: {exc}", file=sys.stderr)
            continue
        if date:
            results[r["id"]] = date
        else:
            not_found.append(r["id"])
        if i % 50 == 0:
            print(f"  ...{i}/{len(targets)}", file=sys.stderr)

    args.out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"fetched {len(results)} dates -> {args.out}")
    if not_found:
        print(f"{len(not_found)} repos returned 404 (renamed/deleted), left undated:", file=sys.stderr)
        for cid in not_found:
            print(f"  {cid}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
