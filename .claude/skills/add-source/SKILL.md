---
name: add-source
description: Add a new seed list to the corpus and reconcile it. Use when the user wants to ingest a new awesome-list, paper list, or feed into the wiki corpus, or says "add <repo> as a source".
---

# Adding a source

## 1. Register it

Create `sources/<key>.yaml`:

```yaml
key: <short-key>
repo: owner/name
branch: main
path: README.md
kind: papers | tools | mixed | course
era: "<span you observe after reading, e.g. 2024-2026>"
tier: 1 | 2 | 3
```

Set `tier` from currency and fit, not stars. Tier 1 = actively maintained and
aligned with the wiki's engineering focus. Tier 3 = historical value only.
Set `era` only after actually reading the list — do not infer it from the repo
description, which is frequently stale.

## 2. Read before you ingest

Fetch the raw README (`raw.githubusercontent.com`, never the rendered page — the
HTML pulls ~200 nav links). Read enough to answer:

- What is its actual date span? Check the oldest and newest entries, not the README's claims.
- Does it have metadata nobody else has? (venue labels, dates, categories)
- What does it cover that the existing corpus does not?

Record the answers in `sources/<key>.yaml` under `notes:`. This is the step that
gets skipped and it is the step that matters — two of the seven current sources
were mis-tiered until they were read properly.

## 3. Ingest and inspect

```bash
python tools/merge_agent_lists.py --out corpus
python tools/validate_corpus.py
```

Then read, in this order:

1. `corpus/report.md` → **title collisions first.** These are wrong links in the
   source. Resolve by checking which source has it right; never auto-merge.
2. `corpus/by-category/unsorted.md` → if more than ~5% of the new entries landed
   here, the taxonomy needs a rule, not the entries need moving. Edit
   `docs/TAXONOMY.md` and re-run.
3. `corpus/report.md` → cross-source overlap. Near-zero overlap with everything
   else usually means a generation gap, which is informative, not a problem.

## 4. Reconcile with the curated layer

New entries arrive with `summary: TODO`. Do not bulk-generate summaries yet —
see the `write-summaries` skill, and only after the taxonomy has settled.

## Do not

- Do not hand-edit `corpus/by-category/*.md`. Regenerate.
- Do not raise a tier to make an entry sort higher. Fix the ranking instead.
- Do not add a source without reading it. A registered-but-unread source is worse
  than an absent one, because it looks covered.
