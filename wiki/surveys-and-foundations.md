---
title: Surveys and Foundations
category: surveys-and-foundations
status: draft
updated: 2026-08-01
---

## What it is

This category holds the field's survey papers, foundation-model papers, and
position papers — entries that map a subfield or argue a stance rather than
propose one new technique. Read it for framing and terminology, not detail:
where a survey here establishes the taxonomy a topic uses, the topic's own
wiki page is where the mechanics live. It's the right first stop when a term
elsewhere in the wiki (agentic RL, self-evolving agents, agent AI) needs to
be traced back to whoever coined or systematized it.

## State of the art

**Two 2023 surveys are still the field's reference taxonomies, and a 2025
entry reframes rather than replaces them.** One proposes a unified
construction framework for LLM-based autonomous agents
{{arxiv:2308.11432}}; the other traces "agent" from its philosophical origins
into a brain/perception/action framework and works outward into single-agent,
multi-agent, and human-agent cooperation {{arxiv:2309.07864}}. A 2025
methodology-centered pass doesn't try to out-taxonomize either — it links
architectural choices directly to collaboration mechanisms and evolutionary
pathways, treating structure and behavior as one axis instead of two
{{arxiv:2503.21460}}. A separate, terminology-first entry from early 2024 sets
out to unify fragmented agent-design vocabulary across single- and
multi-agent architecture, cognitive/planning components, tool use, and
inter-agent communication {{arxiv:2401.03428}} — worth citing specifically
when a term's definition, not its mechanism, is what's in question.

**Subfield surveys increasingly serve as the first systematic entry point for
topics with their own dedicated wiki pages.** Planning gets its first
systematic taxonomy here {{arxiv:2402.02716}} (see
[[planning-and-reasoning]]); evaluation methodology gets a two-dimensional
taxonomy plus enterprise-specific failure modes {{arxiv:2507.21504}} (see
[[evaluation-and-benchmarks]]); self-evolving agents get a survey explicitly
positioned as bridging foundation models and lifelong agentic systems, folding
in safety and evaluation rather than treating them as separate concerns
{{arxiv:2508.07407}} (see [[training-and-optimization]]); and agentic
reinforcement learning gets a dual taxonomy of capabilities (planning, tool
use, memory, reasoning, self-improvement, perception) and applications,
synthesizing over 500 works into one map of the RL-for-agents landscape
{{arxiv:2509.02547}}.

**Domain-specific surveys extend the general framework rather than replace
it, and their evidentiary weight varies a lot.** The code intelligence survey
is unusually well-scoped: 680+ papers, 50+ models, 20+ task categories,
tracing the field from RNN-era code models through current LLMs
{{arxiv:2403.14734}}. The scientific-LLM survey is similarly quantified —
270+ pre-/post-training datasets and 190+ benchmarks — and argues the field's
progress tracks its data substrate at least as much as model architecture,
with the trend line pointing from static exams toward closed-loop agents that
experiment and validate {{arxiv:2508.21148}}. Scientific discovery
{{arxiv:2503.24047}} and materials science {{arxiv:2506.20743}} get their own
narrower treatments; both flag interpretability and multimodal fusion as open
rather than closed. Multimodal coverage is thinner and more fragmented across
this corpus: a vision-language-model survey names hallucination, alignment,
fairness, and safety as unresolved {{arxiv:2501.02189}}, and two 2024 entries
cover multimodal/multi-agent interaction more generally without converging on
shared terminology {{arxiv:2401.03568}}, {{arxiv:2402.15116}}.

**Security, privacy, and ethics surveys disagree on how far along the field
is, which is itself informative.** One combined taxonomy treats security,
privacy, and ethics threats in LLM-based agents as inventory-complete enough
to unify {{arxiv:2411.09523}}, while a case-study-driven survey the same year
frames the same ground as still needing worked examples to be legible at all
{{arxiv:2407.19354}} — read together, the disagreement is less about the
threats than about whether cataloguing them counts as understanding them.

## Origin

LLaMA is the release that made "match a much larger proprietary model on
public data alone" credible: LLaMA-13B outperforms GPT-3 (175B parameters) on
most benchmarks, and LLaMA-65B is competitive with Chinchilla-70B and
PaLM-540B, with weights released to researchers — a large part of why an open
agent ecosystem exists to survey at all {{url:https://ai.meta.com/research/publications/llama-open-and-efficient-foundation-language-models}}.
"On the Opportunities and Risks of Foundation Models" is the paper that named
the category, and its framing still does the work: scale produces new
emergent capabilities, and because the same model gets adapted across so many
downstream tasks, its defects are inherited by everything built on it —
homogenization as risk, not just efficiency {{arxiv:2108.07258}}. Not every
entry from that era treated the emergence story as settled: a 2020 evaluation
of GPT-3 against mathematical, semantic (Turing Test), and ethical criteria
found it failed all three despite fluent output, and is worth keeping as the
counterweight whenever a later survey states emergent capability as
uncontested fact {{url:https://link.springer.com/article/10.1007/s11023-020-09548-1}}.

## Open problems

**Alignment and security surveys here are explicit that they're cataloguing,
not solving.** The alignment survey splits the problem into outer (specifying
the right objective) and inner (getting the model to pursue it) alignment and
says plainly that neither is solved, just better categorized
{{arxiv:2309.15025}}. A 2026 position paper goes further and argues a
specific failure mode — LLM agents laundering unwarranted claims into trusted
facts by having them cross an architecturally-trusted tool boundary — can't
be fixed by scaling, better models, or LLM-as-judge checks under standard
architectural assumptions, which if right undercuts a fair amount of current
verification work {{arxiv:2601.08333}}.

**The 2026 position papers in this category converge on organizational and
architectural framing more than new technique.** One survey frames the shift
from passive LLMs to agentic systems around a reasoning-action-reflection
loop and names verifiable planning, multi-agent coordination, and governance
as the open priorities, without claiming any of the three is close to solved
{{arxiv:2601.02749}}. A field-experience writeup on organizational rollout
argues the real blockers aren't technical — they're treating agent workflows
like ordinary software projects and leaving AI task ownership ambiguous
{{arxiv:2602.10122}}. Verification design specifically is still being unified
rather than settled: a survey of verifier training for test-time scaling
frames the space as fragmented enough to need one {{arxiv:2508.16665}}.

*Editorial note:* three entries in this category — an IJCAI multi-agent
survey, an ACM security survey, and TaskMatrix.AI — remain marked
`NEEDS-SOURCE` in the corpus because their sources were login-walled or
returned unreadable binaries. That's a corpus gap, not a claim they're
unimportant; check `corpus/by-category/surveys-and-foundations.md` before
assuming this page's coverage of the category is exhaustive.

## See also

- [[training-and-optimization]]
- [[planning-and-reasoning]]
- [[evaluation-and-benchmarks]]
- [[safety-security-governance]]
- [[multi-agent]]
- [[domain-applications]]
