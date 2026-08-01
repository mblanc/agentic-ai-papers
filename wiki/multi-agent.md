---
title: Multi-Agent Systems
category: multi-agent
status: draft
updated: 2026-08-01
---

## What it is

Multi-agent systems coordinate more than one LLM-driven agent toward a shared
or contested goal — through debate, role division, hierarchical orchestration,
learned topology, or peer negotiation — rather than relying on one model call
to do everything. The category spans two layers that the corpus keeps
returning to: the coordination *mechanisms* researchers study (does debate
help, how should a team be shaped, who talks to whom) and the *orchestration
frameworks and harnesses* that implement those mechanisms in production. A
recurring, uncomfortable finding threads through both layers: adding agents is
not free, and it is not always a win.

## State of the art

**Debate is the most-studied coordination primitive, and the corpus's own
evidence complicates a simple "debate helps" story.** The foundational result
showed multi-agent debate improves factuality and reasoning
{{arxiv:2305.14325}}, and early follow-ups refined *why*: debating with more
persuasive models yields more truthful answers even for a non-expert judge
{{arxiv:2402.06782}}, and round-table consensus with confidence-weighted
voting beats single- and multi-agent baselines by up to 11.4%
{{arxiv:2309.13007}}. Recent 2026 work pushes back on the mechanism itself:
diversity of initialization and confidence-modulated updates matter more than
raw debate rounds {{arxiv:2601.19921}}, DynaDebate finds debating agents tend
to collapse into homogeneous positions and fixes it by forcing divergent
solution paths before a verifier resolves deadlocks {{arxiv:2601.05746}}, and
dynamic role assignment via proposal-and-peer-review beats fixed debater/judge
roles {{arxiv:2601.17152}}. A direct cross-domain benchmark asking whether
debate helps at all — tracking token cost and latency alongside accuracy
across nine base models, five domains, and both text and vision-language
settings — found the picture far less uniform than the earlier literature
suggested {{arxiv:2601.02854}}. That caution is backed by a starker, separate
finding: self-organizing multi-agent teams often *underperform their own
single best member* {{arxiv:2602.01011}}, echoing an applied result that a
single-shot recommender pipeline is often Pareto-efficient and multi-agent
decomposition only pays off on high-diversity inputs {{arxiv:2507.02097}}.

**Team composition and communication topology are increasingly learned, not
fixed by the researcher.** Adaptive Graph Pruning jointly optimizes agent
count (hard-pruning) and communication topology (soft-pruning) per task,
cutting token consumption more than 90% while improving performance
2.58-9.84% across six benchmarks — verified against the abstract, not just
the paraphrase {{arxiv:2506.02951}}. TopoDIM has decentralized agents
construct heterogeneous topologies in one shot, with no iterative
coordination step at all {{arxiv:2601.10120}}. Confidence-aware routing (send
each reasoning step to the cheapest sufficient model rather than running every
role on the largest LLM) cuts cost up to 79.78% while *improving* accuracy up
to 12.88% {{arxiv:2601.04861}}, and CASTER routes with a lightweight combination
of semantic embeddings and structural meta-features instead of a heavier
learned router {{arxiv:2601.19793}}. A large empirical study across 12 tested
multi-agent systems found architecture choice — not backend model or tool
config — is the dominant factor in cost, latency, and run-to-run reliability
{{arxiv:2601.00481}}, which argues for treating topology as a first-class,
measured design variable rather than an afterthought.

**The orchestration-framework ecosystem is large and still consolidating.**
General-purpose frameworks — AutoGen {{gh:microsoft/autogen}}, CrewAI
{{gh:crewaiinc/crewai}}, LangGraph {{gh:langchain-ai/langgraph}}, Google ADK
{{gh:google/adk-python}}, OpenAI Agents SDK
{{gh:openai/openai-agents-python}} — compete alongside newer entrants that
explicitly consolidate prior tools: Microsoft Agent Framework 1.0 merges
Semantic Kernel and AutoGen into one SDK
{{url:https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0}},
and its BUILD 2026 update adds CodeAct, where the model writes executable
Python instead of emitting tool calls, for 52% faster runs and 64% fewer
tokens
{{url:https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce}}.
Cross-language interop is now a stated goal, not a gap: Google demonstrates a
Python extraction agent and a Go compliance agent collaborating over ADK's A2A
abstraction
{{url:https://developers.googleblog.com/en/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a}}.
A distinct, newer layer has emerged around *deterministic* orchestration and
*fanning out coding agents in parallel*, rather than open-ended conversational
coordination: Conductor executes version-controlled YAML workflows without an
LLM making routing decisions {{gh:microsoft/conductor}}; Orca runs one prompt
across multiple coding agents in parallel git worktrees for comparison
{{gh:stablyai/orca}}; Sandcastle and bernstein isolate and audit many
concurrent coding agents so they don't step on each other's changes
{{gh:mattpocock/sandcastle}} {{gh:sipyourdrink-ltd/bernstein}}. That this
scales past toy demos is documented directly: a researcher ran 16 parallel
Claude instances across roughly 2,000 sessions to build a 100,000-line Rust
C compiler capable of building the Linux kernel on x86, ARM, and RISC-V, for
under $20,000 in inference cost
{{url:https://anthropic.com/engineering/building-c-compiler}}. Separately, a
large-scale study of 42K commits and 4.7K issues across eight production
multi-agent frameworks catalogs what actually breaks when teams build these
systems, as opposed to what papers assume breaks {{arxiv:2601.07136}}.

## Origin

CAMEL is the foundational instance of role-playing multi-agent collaboration
— a user/assistant pair driven by inception prompting to generate cooperative
task-solving data with no human in the loop {{arxiv:2303.17760}}. MetaGPT
extended the idea by encoding standard operating procedures as agent roles,
so a one-line requirement yields a full PRD, design, task breakdown, and code
{{arxiv:2308.00352}}, and ChatDev packaged the same idea as a "virtual
software company" staffed by role-playing agents moving through a structured
chat chain {{arxiv:2307.07924}}.

## Open problems

**Coordination failure is now a named, measured phenomenon, not an
anecdote.** MAST provides an LLM-judge-based failure taxonomy for why
multi-agent systems fail at all {{arxiv:2503.13657}}. "Agent drift" names the
progressive degradation of behavior and inter-agent coherence over extended
interactions, decomposed into semantic, coordination, and behavioral drift
with a 12-dimension stability index {{arxiv:2601.04170}}. The Mandela
effect — collective false-memory formation across agents — is measurable
across four task types and five interaction protocols, and only partially
defensible against: prompt- and alignment-level defenses cut it by an
average of 74.40%, not to zero — verified against the abstract
{{arxiv:2602.00428}}.

**Multi-agent systems are also a distinct, harder-to-govern security
surface**, addressed in depth in [[safety-security-governance]]. Within this
category specifically: LLM agents can manipulate a victim's beliefs using
only true evidence fragments posted in the open — no covert channel required
— at 74.4% success against proprietary models, and the attack gets *more*
effective as the target model's reasoning improves {{arxiv:2601.01685}}.
Multi-agent Cournot price-fixing drops from 50% to 5.6% incidence only once
prompt-only bans are replaced with an enforcing public governance graph —
prompt bans alone did nothing, per the same paper — verified against the
abstract {{arxiv:2601.11369}}. INFA-Guard treats an agent "infected" by an
attacker as a distinct threat category from the attacker itself, since binary
clean-vs-attacker framing misses the propagation step and localizing/
rehabilitating infected agents cuts attack success 33% on average
{{arxiv:2601.14667}}. Distributed systems add a third failure mode besides
malice and drift: free riding and outright malicious participation among
otherwise-cooperative agents {{arxiv:2504.07461}}.

**Cost- and risk-aware orchestration is emerging as its own subfield**, not
just an efficiency footnote. Framing multi-LLM ensembles as likelihood models
for cost-asymmetric sequential decisions (hiring, triage, fraud) cut
resume-screening cost by $294K (34%) and improved demographic parity 45%
versus the best single-LLM baseline — verified against the abstract
{{arxiv:2601.01522}}. Whether this generalizes past the benchmarked domains,
and how it composes with the routing and topology-pruning work above, is
open.

## See also

- [[safety-security-governance]]
- [[planning-and-reasoning]]
- [[harness-engineering]]
- [[evaluation-and-benchmarks]]
- {{gh:google/adk-python}} — production multi-agent framework with A2A interop
