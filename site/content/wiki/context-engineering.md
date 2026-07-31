---
title: Context Engineering
category: context-engineering
status: draft
updated: 2026-07-28
---

## What it is

Context engineering is the discipline of deciding what enters an agent's context
window on a given turn — not just how a prompt is worded, but which tool
outputs, memories, documents, and instructions get assembled, in what form, and
when. It sits above [[context-compaction]] (which handles what to discard once
the window fills) and covers the harder problem of curating input in the first
place.

## State of the art

The framing that context is a finite, curated resource rather than a prompt-
wording problem comes from Anthropic's engineering guidance
[url:https://anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
A cluster of harness-layer tools has converged on the same underlying move:
give the agent a filesystem-shaped view of its world instead of stuffing
everything into the prompt. Context7 injects version-specific docs on demand
[gh:upstash/context7](https://github.com/upstash/context7), Mirage mounts S3/Slack/Gmail/GitHub/Redis as one
virtual filesystem so the agent can use bash [gh:strukto-ai/mirage](https://github.com/strukto-ai/mirage), and
OpenViking unifies memory, resources and skills behind the same paradigm
[gh:volcengine/openviking](https://github.com/volcengine/OpenViking). Token-reduction tools attack the same problem from
the output side: LLMLingua compresses prompts up to 20x
[gh:microsoft/llmlingua](https://github.com/microsoft/LLMLingua), headroom cuts tool/log/RAG output 60-95% before it
hits context [gh:chopratejas/headroom](https://github.com/chopratejas/headroom), and dirac uses hash-anchored edits and
AST manipulation for 50-80% cost reduction [gh:dirac-run/dirac](https://github.com/dirac-run/dirac).

There's a real empirical caution on the filesystem-as-context idea, though: a
9,649-experiment study found file-based retrieval only helps frontier-tier
models (+2.7%) and actively hurts open-source models (-7.7%), with model
capability dwarfing any architectural or format choice
[arxiv:2602.05447](https://arxiv.org/pdf/2602.05447v1). Structure isn't free, and "give the agent files" is not a
universal best practice — it's a lever that works differently by model tier.

A second thread treats context engineering itself as something to automate.
Meta Context Engineering evolves the context-engineering skills and artifacts
together in a bi-level loop rather than hand-crafting a fixed harness
[arxiv:2601.21557](https://arxiv.org/pdf/2601.21557v2), and CEDAR applies structured, interleaved plan/code
context specifically to agentic data science [arxiv:2601.06606](https://arxiv.org/pdf/2601.06606v1).

## Origin

Harness Engineering names the surrounding discipline — the idea that the agent
loop and its scaffolding are themselves a first-class design surface, not
incidental plumbing [url:https://openai.com/index/harness-engineering](https://openai.com/index/harness-engineering/). Claude
Code's compaction work is the applied instance most people encounter first
[url:https://platform.claude.com/docs/en/build-with-claude/compaction](https://platform.claude.com/docs/en/build-with-claude/compaction), and is
covered on its own page: [[context-compaction]].

## Open problems

The filesystem/file-native pattern's benefit is model-dependent, not universal
[arxiv:2602.05447](https://arxiv.org/pdf/2602.05447v1) — there is no settled guidance yet on when to reach for it.
Serialization format choice (YAML/JSON/Markdown/TOON) barely moves aggregate
accuracy in that same study, which cuts against a lot of prescriptive advice on
"the right format" for structured context. Separately, per-harness behavior on
*what specifically* survives context assembly versus what silently gets
dropped or truncated remains undocumented outside vendor blog posts — there's
no cross-harness comparison yet.

## See also

- [[context-compaction]]
- [[memory]]
- [[harness-engineering]]
