# Summary prompt (shared by interactive and batch paths)

Write **one sentence** for a corpus entry: what it does or claims, and why
someone building agents would care. Then stop.

Format the finished line as:

```
- [Title](url) — What it is, in a clause. Why it matters, in a clause. `PROVENANCE`
```

## Source of truth

Write from the **abstract** (papers) or **README** (tools). Never from a seed
list's description — those are the curators' editorial work and must not be
reproduced or reworded. If no abstract/README is reachable, output the literal
`NEEDS-SOURCE` instead of guessing. A wrong summary is worse than a missing one:
nothing downstream catches it.

## Voice

Uniform across the whole pass — an engineer telling a colleague why to open the
link. Lead with the load-bearing claim.

Include a number only when it *is* the point ("84% token reduction on a 100-turn
eval"), never as decoration ("state-of-the-art results").

Banned register (the source lists' voice, zero information):
"this paper proposes", "introduces a novel framework", "leverages", "utilizes",
"cutting-edge", "revolutionary", "state-of-the-art results".

- Weak: "Proposes a novel framework for context management in agents."
- Good: "Moves compression from threshold-triggered to agent-triggered, avoiding
  the failure where compaction interrupts a subtask mid-flight."
