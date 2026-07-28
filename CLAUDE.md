# agentic-ai-wiki

A wiki of state-of-the-art and best practices in agentic AI, built to be queried
by AI assistants as well as read by humans. Distinct from my Obsidian second brain.

## Layout

- `sources/` — one YAML per seed list: repo, branch, kind, era, tier
- `corpus/corpus.jsonl` — canonical deduplicated entries, one per line
- `corpus/by-category/*.md` — generated per-category views. **Generated. Never hand-edit.**
- `wiki/` — topic pages. Hand-written. Entries from the corpus attach as evidence.
- `tools/` — pipeline (`merge_agent_lists.py`, `validate_corpus.py`)
- `docs/TAXONOMY.md` — category definitions and classification rules. **Authoritative.**

## Invariants

These are not preferences. Breaking them corrupts the corpus.

1. **Summaries are written from scratch.** Never copy or lightly reword a source
   list's description. They are the curators' editorial work, and their voices are
   mutually incompatible. Write from the abstract or the repo README.
2. **Dedup by canonical ID, never by URL.** `arxiv:2210.03629`, `gh:owner/repo`,
   `openreview:<id>`, `acl:<id>`, `url:<normalized>`. See `docs/TAXONOMY.md` §2.
3. **Never auto-merge a title collision.** Two dissimilar titles under one ID means
   a source has a wrong link, not that they're the same thing. Report it.
   Real case: `XI` points FireAct at Voyager's arXiv ID; `LJ` has it right.
4. **Provenance is required on every entry.** Codes: `HE` `KY` `XI` `BK` `VA` `ZJ` `LJ`.
   An entry with no source is not an entry.
5. **Facts from sources, opinions marked as mine.** Editorial judgement (tiering,
   "this is the best entry point") is fine but must be visibly mine, not implied
   to be the source's.

## Commands

- `python tools/merge_agent_lists.py --out corpus --max-tier 1` — rebuild from tier-1
- `python tools/validate_corpus.py` — schema, dedup and collision checks. Run before commit.

## Style

French/English both fine in commit messages; wiki prose in English.
Concise. No em-dash-heavy filler. Don't restate what the code already says.
