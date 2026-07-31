---
title: Multi-Agent Systems
category: multi-agent
status: draft
updated: 2026-07-30
---

## What it is

Multi-agent systems coordinate more than one LLM-driven agent toward a shared
goal — through debate, role division, hierarchical orchestration, or peer
negotiation — rather than relying on one model to do everything. This covers
both the coordination *mechanisms* (debate, dynamic team selection, topology)
and the *orchestration frameworks* that implement them in production.

## State of the art

**Debate and structured disagreement remain the most-studied coordination
primitive**, but the corpus's own evidence complicates a simple "debate helps"
story. The foundational result showed multi-agent debate improves factuality
and reasoning [arxiv:2305.14325](https://arxiv.org/abs/2305.14325), and follow-ups refined *why*: debating
with more persuasive models yields more truthful answers even for a
non-expert judge [arxiv:2402.06782](https://arxiv.org/abs/2402.06782), diversity and confidence-modulated
updates matter more than raw debate rounds [arxiv:2601.19921](https://arxiv.org/pdf/2601.19921v1), and
round-table consensus with confidence-weighted voting beats single- and
multi-agent baselines by up to 11.4% [arxiv:2309.13007](https://arxiv.org/abs/2309.13007). But a direct
benchmark asking whether debate actually helps across domains and modalities
found the picture is far less uniform than the earlier literature suggested,
tracking token cost and latency alongside accuracy rather than accuracy alone
[arxiv:2601.02854](https://arxiv.org/pdf/2601.02854v1) — and a separate finding states this even more starkly:
multi-agent teams often *underperform* their own single best member
[arxiv:2602.01011](https://arxiv.org/pdf/2602.01011v3).

**Team composition and topology are increasingly learned, not fixed.** DyLAN
selects which agents to include per task from an unsupervised importance
score, improving MMLU accuracy up to 25% over static teams
[arxiv:2310.02170](https://arxiv.org/abs/2310.02170), and Adaptive Graph Pruning jointly optimizes agent count
and communication topology per task, cutting token consumption 90%+ while
improving performance [arxiv:2506.02951](https://arxiv.org/abs/2506.02951). TopoDIM goes further, having
decentralized agents construct heterogeneous topologies without any iterative
coordination step at all.

**The orchestration-framework ecosystem is large and still consolidating.**
General-purpose frameworks (AutoGen [gh:microsoft/autogen](https://github.com/microsoft/autogen), CrewAI
[gh:crewaiinc/crewai](https://github.com/crewAIInc/crewAI), LangGraph [gh:langchain-ai/langgraph](https://github.com/langchain-ai/langgraph), Google ADK
[gh:google/adk-python](https://github.com/google/adk-python), OpenAI Agents SDK
[gh:openai/openai-agents-python](https://github.com/openai/openai-agents-python)) compete alongside newer entrants
consolidating prior tools — Microsoft Agent Framework 1.0 explicitly merges
Semantic Kernel and AutoGen into one SDK
[url:https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/).
A second, distinct layer has emerged around *fanning out coding agents in
parallel* rather than long-running conversational coordination: Orca runs one
prompt across multiple coding agents in parallel git worktrees for comparison
[gh:stablyai/orca](https://github.com/stablyai/orca), and Sandcastle isolates multiple agents so they don't
step on each other's changes [gh:mattpocock/sandcastle](https://github.com/mattpocock/sandcastle).

## Origin

CAMEL is the foundational instance of role-playing multi-agent
collaboration — a user/assistant pair driven by inception prompting to
generate cooperative task-solving data with no human in the loop
[arxiv:2303.17760](https://arxiv.org/abs/2303.17760). MetaGPT extended the idea into encoded standard
operating procedures, so a one-line requirement yields a full PRD, design,
task breakdown, and code [arxiv:2308.00352](https://arxiv.org/abs/2308.00352).

## Open problems

**Coordination failure is now a named, measured phenomenon, not an
anecdote.** MAST provides an LLM-judge-based failure taxonomy for why
multi-agent systems fail at all [arxiv:2503.13657](https://arxiv.org/abs/2503.13657). "Agent drift" names the
progressive degradation of behavior and inter-agent coherence over extended
interactions, decomposed into semantic, coordination, and behavioral drift
with a 12-dimension stability index [arxiv:2601.04170](https://arxiv.org/pdf/2601.04170v1). The Mandela effect
— collective false-memory formation across agents — is measurable and only
partially defensible against (74.4% average reduction, not elimination)
[arxiv:2602.00428](https://arxiv.org/pdf/2602.00428v1).

**Multi-agent systems are also a distinct, harder-to-govern security
surface**, addressed in depth in [[safety-security-governance]]. Within this
category specifically: LLM agents can manipulate a victim's beliefs using
only true evidence fragments posted in the open — no covert channel required
— at 74.4% success against proprietary models [arxiv:2601.01685](https://arxiv.org/pdf/2601.01685v1), and
multi-agent Cournot price-fixing drops from 50% to 5.6% only once you replace
prompt-only bans with an enforcing governance graph, since prompt bans alone
did nothing [arxiv:2601.11369](https://arxiv.org/pdf/2601.11369v2). INFA-Guard treats an agent "infected" by an
attacker as a distinct threat category from the attacker itself, since
binary clean-vs-attacker framing misses the propagation step entirely
[arxiv:2601.14667](https://arxiv.org/pdf/2601.14667v1).

## See also

- [[safety-security-governance]]
- [[planning-and-reasoning]]
- [[harness-engineering]]
