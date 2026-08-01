---
title: Coding Agents
category: coding-agents
status: draft
updated: 2026-08-01
---

## What it is

Coding agents are LLM agents that write, review, or fix code directly against
a real repository — reading files, running tests, opening pull requests, and
iterating on failures — rather than answering a one-off code-generation
prompt. The corpus here splits cleanly into two very different kinds of
evidence: harnesses and tools that implement the pattern, and a growing wave
of 2026 empirical studies asking whether the code these tools produce actually
holds up once it's merged.

## State of the art

**SWE-agent set the reference pattern that most open harnesses still follow.**
Its companion paper argues the *interface* the model sees — search, file
viewer, edit commands scoped to what an LLM can reliably use — matters as much
as the underlying model, coining the "agent-computer interface" (ACI)
{{arxiv:2405.15793}}; the tool itself remains the configurable, documented
baseline much SWE-bench research builds on {{gh:swe-agent/swe-agent}}. Around
it sits a cluster of similarly-shaped open harnesses: OpenHands gives agents a
sandboxed shell, browser, and editor and wires them into GitHub and Slack as a
self-hosted control center {{arxiv:2407.16741}} {{gh:openhands/openhands}},
OpenCode ships separate full-access "build" and read-only "plan" modes
{{gh:anomalyco/opencode}}, and Open SWE composes on Deep Agents and LangGraph
rather than forking, trading some control for an upgrade path as those
libraries evolve
{{url:https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents}}.
Terminal-native agents in the same lineage include Aider, built around a
repo-map and git-aware diffs {{gh:aider-ai/aider}}, and Cline, which exposes
every model action for inspection {{gh:cline/cline}}.

**A second, distinct cluster has formed around running many coding agents at
once rather than perfecting one.** Cate and Dorothy give each parallel agent
its own git worktree on a visual canvas or kanban board
{{gh:0-ai-ug/cate}} {{gh:charlie85270/dorothy}}, fractal lets a running agent
loop spawn child loops for separable subtasks in their own worktrees, bounded
by hard caps since it runs without permission prompts by default
{{gh:plasma-ai/fractal}}, amux multiplexes dozens of sessions behind a
dashboard and an A2A REST API {{gh:mixpeek/amux}}, and zeroshot refuses to
ship code without sign-off from independent reviewer agents first
{{gh:the-open-engine/zeroshot}}. This is worktree-per-agent isolation solving
a coordination problem, not a code-generation one — see [[multi-agent]] for
the orchestration layer these tools sit on top of.

**The more interesting frontier right now is a wave of empirical studies
asking whether agent-authored code holds up, and the answers complicate the
benchmark story.** PR descriptions don't always match the actual diff
{{arxiv:2601.04886}}, and core and peripheral developers use agents with
measurably different review and verification habits {{arxiv:2601.20106}}. At
scale: a 40,214-PR comparison of developer versus agentic PRs looked directly
at merge outcomes and review features {{arxiv:2601.18749}}, mining 19,450
inline review comments across 3,177 agent-authored PRs found reviewers mostly
flag documentation gaps, refactoring needs, and style — with an LLM annotator
matching human exact-match labels 78.63% of the time
{{arxiv:2601.19287}} — and a build-code-specific study found 364
maintainability and security smells in agent-authored PRs, yet also cases of
agents *cleaning up* existing smells, alongside the harder finding that over
61% of these PRs are approved and merged with minimal human review
{{arxiv:2601.16839}}. Tracking 200,000+ code units across 201 open-source
projects, one study found AI-authored code survives 15.8 percentage points
longer before modification than human code — not because it's better, but
because it draws more corrective fixes and fewer adaptive changes, pointing at
review practice rather than generation quality as the real bottleneck
{{arxiv:2601.16809}}. A separate study of 8,106 fix-related agent PRs
catalogued why the rest stay unmerged {{arxiv:2602.00164}} — a different
question from "does the agent pass the benchmark."

**Harness configuration is a confound underneath all of this.** Anthropic's
own 2026 trends report states plainly that harness configuration alone can
swing benchmark results by 5+ points
{{url:https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf}}
— meaning cross-tool comparisons that don't control for harness setup aren't
actually comparing the underlying models.

**Vulnerability discovery and program repair form a smaller, separate
cluster.** Tooling, not model scale, drove the gains in one study of
agent-based vulnerability discovery {{arxiv:2409.16165}}, and Google Project
Zero's agent found real memory-safety bugs in production code, reported as
the successor to their earlier Naptime project
{{url:https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html}}.

## Origin

Tool-augmented code generation predates the agent framing: ToolCoder teaches a
code model to call an API-search tool mid-generation instead of hallucinating
signatures, adding at least 6.21% average pass@1 over prior methods and
letting a small model rival GPT-3.5 on library-heavy tasks
{{arxiv:2305.04032}} — the same shape every modern coding agent's tool loop
now takes. PanGu-Coder2 took a different precursor path, fine-tuning by
ranking sampled completions against test execution and teacher feedback
rather than plain supervised fine-tuning, reaching 62.20% pass@1 on HumanEval
{{arxiv:2307.14936}}. On the "generate a whole codebase from a prompt" side,
GPT Engineer is the direct, now-archived precursor to today's app-builder
agents {{gh:antonosika/gpt-engineer}}, followed by Devika's
research-then-code decomposition {{gh:stitionai/devika}} and GPT Pilot's
checkpointed step-by-step builds {{gh:pythagora-io/gpt-pilot}}.

## Open problems

**Individual-task success doesn't transfer to working alongside others.**
CooperBench found current coding agents still can't function as teammates
across 600+ collaborative tasks with varied coordination structures
{{arxiv:2601.13295}}.

**Reviewer sentiment and actual code quality don't reliably move together**
— a genuine disagreement in the evidence, not a rounding error: one study
finds AI-generated PRs get less code reuse alongside sentiment that doesn't
track quality {{arxiv:2601.21276}}, while "silent" agent PRs with no
commentary carry measurably higher complexity and vulnerability risk
{{arxiv:2601.21102}}, and yet the survival-rate study above found agent code
sticks around *longer* than human code {{arxiv:2601.16809}}. Read together,
these don't resolve into "agent code is good" or "agent code is bad" — they
say review scrutiny, not generation quality, is the variable actually moving.

**Cost accounting is thin.** Where tokens actually go across the SDLC —
which stages are the real cost drivers — is only just being measured
{{arxiv:2601.14470}}, and as agent-authored PRs become harder to tell from
human ones, attribution itself is now a research question: one study builds
behavioral fingerprints to identify which agent produced a given PR
{{arxiv:2601.17406}}.

## See also

- [[harness-engineering]]
- [[tool-use-and-protocols]]
- [[evaluation-and-benchmarks]]
- [[multi-agent]]
- {{gh:swe-agent/swe-agent}} — the ACI pattern implemented, not just described
