---
title: Coding Agents
category: coding-agents
status: draft
updated: 2026-07-28
---

## What it is

Coding agents are LLM agents whose job is writing, reviewing, or fixing code
directly against a real repository — opening pull requests, running tests,
and iterating on failures — rather than answering a one-off code-generation
prompt.

## State of the art

SWE-agent established the reference pattern: a purpose-built
agent-computer interface that lets the model autonomously fix issues in real
GitHub repos, and it remains the configurable, documented baseline much
SWE-bench research builds on {{gh:swe-agent/swe-agent}}. Around it sits a
cluster of similarly-shaped open harnesses — OpenHands as a self-hosted control
center wiring agents into GitHub and Slack {{gh:openhands/openhands}}, OpenCode
with separate full-access and read-only modes {{gh:anomalyco/opencode}}, and
Open SWE, which composes on Deep Agents and LangGraph rather than forking, to
keep an upgrade path as those libraries improve
{{url:https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents}}.

The more interesting frontier right now isn't the harnesses themselves but a
wave of empirical studies asking whether agent-authored code actually holds up
in practice, and the answers complicate the benchmark story. Message-code
inconsistency is measurable — PR descriptions don't always match the actual
diff {{arxiv:2601.04886}}. Core and peripheral developers use agents
differently, with real differences in review and verification behavior
{{arxiv:2601.20106}}. A 40,214-PR comparison of developer versus agentic PRs
looked at merge outcomes and review features directly {{arxiv:2601.18749}}, and
a study of 8,106 fix-related agent PRs catalogued *why* they stay unmerged
{{arxiv:2602.00164}} — a very different question from "does the agent pass the
benchmark."

Anthropic's own trends report is blunt about a confound underneath all of
this: harness configuration alone can swing benchmark results by 5+ points
{{url:https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf}}
— meaning cross-tool comparisons that don't control for harness setup aren't
comparing the models at all.

## Origin

ToolCoder is an early instance of the underlying idea — teach a code-generation
model to call an external tool (API search) mid-generation rather than
hallucinate signatures from training data, which is the same shape every
modern coding agent's tool loop now takes {{arxiv:2305.04032}}.

## Open problems

The gap between benchmark performance and real-world adoption friction is the
open problem, not model capability. CooperBench found current coding agents
still can't function as teammates across 600+ collaborative tasks with varied
coordination structures {{arxiv:2601.13295}} — the individual-task success
story doesn't transfer to working alongside other agents or people. Separately,
reviewer sentiment toward AI-generated PRs and their actual code quality don't
always move together {{arxiv:2601.21276}}, and "silent" agent PRs with no
commentary carry measurable complexity and vulnerability implications
{{arxiv:2601.21102}} — trust calibration for agent-authored code is still an
open, mostly qualitative problem.

## See also

- [[harness-engineering]]
- [[tool-use-and-protocols]]
- [[evaluation-and-benchmarks]]
