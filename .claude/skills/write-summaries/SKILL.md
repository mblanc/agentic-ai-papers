---
name: write-summaries
description: Generate the one-line summaries for corpus entries marked summary TODO. Use when the user asks to fill in summaries, write descriptions for corpus entries, or do the summary pass.
---

# Writing corpus summaries

## Preconditions

Do not start until **both** are true:

- `corpus/by-category/unsorted.md` is under ~5% of total entries
- the taxonomy has not changed in the last two ingests

Summarizing before the taxonomy settles means re-summarizing. This ordering is
the single most expensive mistake available here.

## The form

One sentence. What it does or claims, and why someone building agents would care.
Then stop.

```
- [Title](url) — What it is, in a clause. The reason it matters, in a clause. `PROVENANCE`
```

Include a number only when it is the point of the paper: "84% token reduction on a
100-turn eval" earns its place; "achieves state-of-the-art results" does not.

## Voice

Uniform across all entries — that is the entire reason for doing this as a pass
rather than per-entry. Write as an engineer telling a colleague why to open the
link.

Avoid: "This paper proposes...", "Introduces a novel framework for...", "leverages",
"utilizes", "cutting-edge", "revolutionary". These are the source lists' register,
not ours, and they carry zero information.

Prefer the load-bearing claim. Compare:

- Weak: "Proposes a novel framework for context management in agents."
- Good: "Moves compression from threshold-triggered to agent-triggered, avoiding
  the failure where compaction interrupts a subtask mid-flight."

## Source of truth

Write from the **abstract** (papers) or **README** (tools). Not from the seed
list's description — those are the curators' work and must not be reproduced or
lightly reworded. If the abstract is unavailable, mark `summary: NEEDS-SOURCE`
rather than guessing. A wrong summary is worse than a missing one because nothing
downstream will catch it.

## Batching

Work one category file at a time so voice stays consistent within a topic. After
each file, re-read the first and last five entries together — drift shows up there
before anywhere else.

For volume, this is a good candidate for a batch API job rather than an
interactive pass. Keep the prompt in `tools/prompts/summary.md` so the
interactive and batch paths cannot diverge.
