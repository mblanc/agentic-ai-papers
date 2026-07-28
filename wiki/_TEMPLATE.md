---
title: <Topic Name>
category: <one taxonomy slug from docs/TAXONOMY.md, e.g. context-engineering>
status: draft | stable
updated: <YYYY-MM-DD>
---

<!--
HOW THIS FILE WORKS

A wiki page is prose written by you, with corpus entries attached as evidence
via {{id}} citations — e.g. {{arxiv:2210.03629}} or {{gh:letta-ai/letta}}.

validate_corpus.py checks every {{...}} against corpus/corpus.jsonl and fails
the build if one doesn't resolve. That's the point: a claim on this page is
either backed by something in the corpus, or it's your own synthesis and
should be flagged as such, not silently unsourced.

Pull the id straight from corpus/by-category/<category>.md — it's printed
under each entry as `id_type:identifier`.

Delete this comment block before publishing the page.
-->

## What it is

One paragraph. What problem this addresses, in plain terms. This is where an
AI assistant querying the wiki should land first — write for that reader as
much as for yourself.

## State of the art

The current best approach, and why it's currently best. Cite the entries that
establish this: {{arxiv:XXXX.XXXXX}}.

Where there's real disagreement between sources rather than one clear best
approach, say so — don't force consensus that isn't there.

## Origin

Where this idea came from, if it matters for understanding it. Often one entry
from `docs/TAXONOMY.md`'s classical-canon section: {{arxiv:XXXX.XXXXX}}.

## Open problems

What isn't solved yet. This section ages fastest — check it every time you
touch the page.

## See also

- [[other-wiki-page]]
- {{gh:owner/repo}} — a tool that implements this, not just discusses it
