---
title: Context Engineering
category: context-engineering
status: draft
updated: 2026-08-01
---

## What it is

Context engineering is the discipline of deciding what enters an agent's
context window on a given turn — which tool outputs, memories, documents,
and instructions get assembled, in what form, and when — rather than
treating the problem as one of prompt wording. It sits above
[[context-compaction]], which handles what to discard once the window
fills; this page covers the broader problem of curating input in the first
place: window management, caching, convention files, and general token
reduction.

## State of the art

**Context is now explicitly framed as a finite, curated resource rather
than a prompt-wording problem**, per Anthropic's own engineering guidance
{{url:https://anthropic.com/engineering/effective-context-engineering-for-ai-agents}}.
That framing has produced a convergent architectural move across
independent tools: give the agent a filesystem-shaped view of its world
instead of stuffing everything into the prompt. Context7 injects
version-specific library docs on demand to stop hallucinated APIs from
stale training data {{gh:upstash/context7}}, Mirage mounts S3, Slack,
Gmail, GitHub, and Redis as one virtual filesystem so the agent can use
bash against all of them {{gh:strukto-ai/mirage}}, and OpenViking unifies
memory, resources, and skills behind the same filesystem paradigm
{{gh:volcengine/openviking}}. A Microsoft field report on an Azure SRE
agent found the same pattern paid off concretely: replacing 100+ bespoke
tools with a filesystem interface raised its "Intent Met" metric from 45%
to 75%
{{url:https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200}}.

**But the filesystem-as-context pattern is not a universal win — it's
model-tier-dependent.** A 9,649-experiment study across 11 models, 4
serialization formats, and schemas from 10 to 10,000 tables found
file-based retrieval helps frontier models by a modest +2.7% but actively
*hurts* open-source models by -7.7%, with model capability dwarfing any
architectural or format choice {{arxiv:2602.05447}}. Serialization format
(YAML vs JSON vs Markdown vs TOON) barely moved aggregate accuracy in the
same study — which cuts against a lot of prescriptive advice about "the
right format" for structured context. This directly complicates the
harness-tools cluster above: "mount it as a filesystem" is a lever that
can backfire below the frontier tier, not a default best practice.

**A second cluster attacks context size from the output side, compressing
what tools and retrieval produce before it ever reaches the window.**
LLMLingua compresses prompts up to 20x, with the LLMLingua-2 variant
adding a 3-6x latency speedup on top {{gh:microsoft/llmlingua}}; headroom
cuts tool, log, and RAG output 60-95% before it hits context
{{gh:chopratejas/headroom}}; dirac uses hash-anchored edits and AST
manipulation for surgical curation, claiming 50-80% cost reduction
{{gh:dirac-run/dirac}}; and in the coding-agent-specific case,
SWE-Pruner uses a small 0.6B "skimmer" model to keep only lines relevant
to the current step, cutting 23-54% of tokens on SWE-Bench Verified while
*raising* success rates rather than trading accuracy for size
{{arxiv:2601.16746}}.

**Convention files (CLAUDE.md/AGENTS.md) are also being rethought as
structure rather than one flat blob.** Trellis replaces a monolithic
CLAUDE.md with progressive spec loading and cross-platform adapters
{{gh:mindfold-ai/trellis}}, and harness-experimental turns a whole repo
into an agent-ready workspace via structured AGENTS/HARNESS/FEATURE_INTAKE
files rather than a single instructions file
{{gh:hoangnb24/harness-experimental}}. On the serving side, Vercel argues
the same curation problem exists one layer down the stack: serve agents
`text/markdown` via content negotiation so page boilerplate never enters
context to begin with
{{url:https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation}}.

**Prompt caching is the other lever, orthogonal to what content is
selected: it controls what it costs to keep re-sending the same context.**
Anthropic's guidance frames cache-breakpoint placement as the main cost
lever in multi-turn sessions
{{url:https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching}}.
This is a distinct concern from pruning or compaction — a well-cached
context can be large and cheap, while a poorly-pruned one is small but
still expensive per turn if caching isn't set up to exploit repetition.

**A third thread treats context engineering itself as something to
automate rather than hand-design.** Meta Context Engineering evolves the
context-engineering skills and artifacts together in a bi-level loop — a
meta-agent evolves the skills while a base-agent applies them, optimizing
context as editable files and code — averaging 16.9% over prior agentic
methods {{arxiv:2601.21557}}. CEDAR applies a narrower version of the same
idea to agentic data science specifically: interleaved plan-and-code
context blocks written by separate LLM agents, keeping raw data local and
injecting only aggregate statistics so Kaggle-style tasks stay within
context limits {{arxiv:2601.06606}}.

## Origin

Harness Engineering names the surrounding discipline this all sits
inside — the idea that the agent loop and its scaffolding are themselves a
first-class design surface, not incidental plumbing
{{url:https://openai.com/index/harness-engineering}}. Claude Code's
compaction work is the applied instance most people encounter first
{{url:https://platform.claude.com/docs/en/build-with-claude/compaction}},
and is covered in depth on its own page: [[context-compaction]].

## Open problems

The filesystem/file-native pattern's benefit is model-dependent, not
universal {{arxiv:2602.05447}}, and there is no settled guidance yet on
when to reach for it versus keeping context flat and inline. Per-harness
behavior on *what specifically* survives context assembly versus what
silently gets dropped or truncated remains undocumented outside vendor
blog posts, with no cross-harness comparison yet — a gap that shows up
concretely in Claude Code's own compaction behavior, covered in
[[context-compaction]]. Convention-file structure (Trellis, AGENTS.md
patterns) is being actively redesigned by multiple independent tools
right now, which suggests the flat-CLAUDE.md convention that dominated
2024-2025 is being recognized as a bottleneck, but no format has emerged
as a clear standard.

## See also

- [[context-compaction]]
- [[memory]]
- [[harness-engineering]]
- [[rag-and-retrieval]]
