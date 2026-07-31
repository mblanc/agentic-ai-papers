---
title: Context Compaction
category: context-engineering
status: draft
updated: 2026-07-28
---

## What it is

As an agent's session runs long, its context window fills with tool output,
old turns, and superseded plans. Compaction is the practice of compressing or
discarding that history so the agent can keep working without hitting the
context limit or paying for tokens it no longer needs.

## State of the art

Anthropic's Claude API compacts server-side, summarizing older context and
reporting an 84% token reduction on a 100-turn eval [url:https://platform.claude.com/docs/en/build-with-claude/compaction](https://platform.claude.com/docs/en/build-with-claude/compaction).
LangChain's approach differs in *when* compaction triggers: rather than a
fixed threshold, the agent itself decides when to consolidate, which avoids
the failure mode where compression interrupts a subtask mid-flight
[url:https://blog.langchain.com/autonomous-context-compression](https://blog.langchain.com/autonomous-context-compression/). The same
idea appears in the research literature as a "Focus Agent" that decides when
to consolidate and prune, cutting tokens 22.7% with no accuracy loss
[arxiv:2601.07190](https://arxiv.org/abs/2601.07190).

## Origin

The framing that context is a finite curated resource — not just prompt
wording — comes from [url:https://anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

## Open problems

What survives compaction and what silently doesn't is still mostly
undocumented per-harness; critical rules need to live in the system prompt
rather than conversation history precisely because compaction can't be
trusted to preserve them.

## See also

- [[context-engineering]]
- [[memory]]
- [[harness-engineering]]
