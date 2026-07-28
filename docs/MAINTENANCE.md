# Maintaining the wiki

There's no scheduled job here — this repo has no CI configured, so "maintain"
means running these by hand or via a Claude Code session, on whatever cadence
you want. What follows is the loop, not an automation.

## The four things that go stale, and how each is caught

| what stales | how you'd notice | fix |
|---|---|---|
| a source repo gets new entries | nothing — silent unless you re-run | re-ingest that source (see below) |
| a wiki page's "Open problems" section | reading it and knowing it's wrong | manual edit, no tooling for this |
| a summary reads like the source's voice | `validate_corpus.py`'s BANNED-phrase check | flagged automatically, fix by hand |
| a wiki citation points at a deleted/renamed entry | `validate_corpus.py`'s citation check | flagged automatically, fix by hand |

Only the last two have automated detection. The first two are why this file
exists — they need a person to decide it's time.

## Refresh loop (run this periodically)

```bash
python tools/merge_agent_lists.py --out corpus --max-tier 1 --seed corpus/curated.jsonl
python tools/validate_corpus.py --jsonl corpus.jsonl
```

Then read `corpus/report.md` for two things specifically:

- **New title collisions.** A source changed a link and it now points at the
  wrong paper. Never auto-resolve — see `docs/TAXONOMY.md` §2 for why.
- **Seed coverage dropped.** The report prints what fraction of entries kept a
  seed summary. If a source rewrote its README structure, ids can shift and
  summaries you already wrote stop matching. A sudden drop is the tell.

If `unsorted.md` grew past ~5%, the taxonomy missed something new — add a
pattern to `TAXONOMY` in `tools/merge_agent_lists.py`, not a one-off fix to
the entry.

## When you add a wiki page

1. Copy `wiki/_TEMPLATE.md`.
2. Pull ids from `corpus/by-category/<category>.md` — don't hand-type them.
3. `python tools/validate_corpus.py` before committing. It will catch a typo'd
   id immediately instead of leaving a dead citation for someone to find later.

## When tier-1 sources change their inclusion rules

VoltAgent's list is arXiv-only from Jan 2026 forward by its own stated rule —
if that changes, `era` in `sources/voltagent.yaml` goes stale and your
generation-chain reasoning (see `docs/TAXONOMY.md`) stops holding. Re-read the
source's own README occasionally, not just its entries — the *rules* drift too.

## What's still manual, on purpose

Summary writing (`.claude/skills/write-summaries`) and category-fit review
(`.claude/agents/corpus-reviewer.md`) stay human-in-the-loop deliberately —
both are exactly the kind of judgment call that produced the FireAct/Voyager
catch, which no purely mechanical check would have found on its own.
