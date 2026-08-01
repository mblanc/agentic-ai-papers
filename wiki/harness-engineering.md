---
title: Harness Engineering
category: harness-engineering
status: draft
updated: 2026-08-01
---

## What it is

A harness is the code around a model that decides what it stores, retrieves,
sees, and is allowed to do: the agent loop, tool definitions, permissions,
memory, and control flow, as distinct from the model weights themselves.
Harness engineering treats that layer as a deliberate design surface rather
than an afterthought, on the premise that harness quality is often a bigger
lever on measured performance than which model sits inside it.

## State of the art

**There is no single canonical definition yet, but the attempts are
converging on similar shapes.** "What makes a harness a harness" proposes
four necessary and sufficient conditions and tests them against real systems
as an inclusion criterion, not just a metaphor {{arxiv:2606.10106}}. The
Anatomy of an Agent Harness names five composing primitives — filesystem,
code execution, sandbox, memory, context management
{{url:https://blog.langchain.com/the-anatomy-of-an-agent-harness}}. Martin
Fowler's two entries split the concept differently: one frames it as context
curation, architectural constraints, and entropy management, with humans kept
*on* the loop rather than *in* it
{{url:https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html}},
the other (Böckeler) separates feedforward guides from feedback sensors and
distinguishes computational from inferential controls
{{url:https://martinfowler.com/articles/harness-engineering.html}}. Red Hat's
enterprise framing is a four-pillar model — vibes, specs, skills, agents
{{url:https://developers.redhat.com/articles/2026/04/07/harness-engineering-structured-workflows-ai-assisted-development}}
— while deepset's is a failure-classification table mapping each observed
failure mode to the harness component responsible for it
{{url:https://deepset.ai/blog/harness-engineering}}. These don't contradict
each other so much as slice the same object along different axes; there's no
sign yet of one framing winning out.

**The load-bearing empirical claim is that harness changes alone move
benchmark scores by double digits, holding the model fixed.** LangChain's
Deep Agents writeup reports a coding agent moving from Terminal-Bench-2.0
rank ~30 to top 5 through harness changes only, a score gain from 52.8% to
66.5% {{url:https://blog.langchain.com/improving-deep-agents-with-harness-engineering}}
— verified against the source, which states the figures directly rather than
as a rounded headline. Their companion Nemotron 3 Ultra playbook reports
near-frontier performance from tuning the system prompt, tool descriptions,
and middleware, mining execution traces for failure patterns rather than
retraining {{url:https://blog.langchain.com/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook}}.
Anthropic's own harness-design guidance argues the opposite emphasis over
time: lean on what the model already does well, and strip out harness
assumptions as the model gets more capable, reserving explicit constraints
for security, cost, and UX rather than over-engineering scaffolding around a
model that no longer needs it {{url:https://claude.com/blog/harnessing-claudes-intelligence}}.

**The dominant emerging pattern is harnesses that improve themselves**, and
independent teams converge on a strikingly similar loop: mine failures from
execution traces, propose a targeted harness change, accept it only if it
survives held-out evaluation. Self-Harness runs exactly this three-stage
loop (mine model-specific weaknesses → propose minimal edits → validate via
regression testing) with no human engineer, reporting held-out pass-rate
gains on Terminal-Bench-2.0 of 21.4, 14.3, and 14.2 points across three base
model families (MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5) — verified against the
abstract, which gives per-model before/after numbers rather than a single
blended figure {{arxiv:2606.09498}}. Meta-Harness generalizes the same idea
to harness code broadly, not just prompts: a 7.7-point improvement over a
state-of-the-art context-management baseline at 4x fewer context tokens on
one task, plus a separate 4.7-point gain on IMO-level math reasoning across
five held-out models — both confirmed against the abstract
{{arxiv:2603.28052}}. RHO (Retrospective Harness Optimization) removes the
labeled validation set entirely, learning purely from an agent's own past
trajectories, and its repository reports one SWE-Bench Pro run moving from
59% to 78% (+19 points), plus smaller gains on Terminal-Bench-2 (0.71→0.76)
and GAIA-2 (0.29→0.37) — the repo also claims it beats Meta-Harness
head-to-head on SWE-Bench Pro, 0.78 vs 0.62 {{gh:wbopan/retro-harness}}.
agentic-harness-engineering runs the same evaluate-analyze-improve cycle and
reports GPT-5.4 moving from 69.7% to 77.0% pass@1 over ten iterations, with
the evolved harness transferring across models rather than being tied to the
one it was tuned on {{gh:china-qijizhifeng/agentic-harness-engineering}}.
Live-SWE-agent is the extreme version — an agent that evolves its own
scaffold *during* runtime while solving real problems, starting from a
bash-only baseline and reaching 77.4% on SWE-bench Verified without
test-time scaling (and 45.8% on the harder SWE-bench Pro), which the authors
state beats every existing software agent including proprietary ones —
both figures confirmed against the abstract {{arxiv:2511.13646}}. This has
produced a small ecosystem of general-purpose harness optimizers built as
products rather than papers: meta-agent {{gh:canvas-org/meta-agent}},
metaharness {{gh:superagenticai/metaharness}}, auto-harness
{{gh:neosigmaai/auto-harness}}, harness-evolver
{{gh:raphaelchristi/harness-evolver}}, AutoAgent {{gh:kevinrgu/autoagent}},
and Stanford IRIS Lab's own meta-harness
{{gh:stanford-iris-lab/meta-harness}} all implement some version of
propose-evaluate-keep against a frozen base model. Life-Harness reports the
resulting gains transfer across 18 model backbones
{{gh:tianshi-xu/life-harness}} — a striking claim from a single GitHub repo
that I have not independently verified beyond its own README.

**A parallel line treats the agent loop itself as a design-space problem to
be surveyed, not assumed.** A Scheduler-Theoretic Framework analyzes 70
surveyed systems on controllability, expressiveness, and implementability
{{arxiv:2604.11378}} — the by-category summary additionally claims 60% of
those 70 use a plain agent loop, a figure I could not confirm from the
abstract text alone and am flagging as unverified rather than dropping, since
it may be in the paper body. Architectural Design Decisions in AI Agent
Harnesses runs a similar empirical study, independently landing on 70 public
agent systems across five recurring design dimensions
{{arxiv:2604.18071}}. Anthropic's own loop taxonomy splits triggers into
turn-based, goal-based, time-based, and proactive, as a framework for
choosing a loop primitive and managing token budget rather than defaulting
to one shape {{url:https://claude.com/blog/getting-started-with-loops}}.
OpenAI's "Unrolling the Codex Agent Loop" and "Unlocking the Codex Harness"
give the concrete production counterpart: a step-by-step decomposition of
one loop iteration, and the reasoning behind an Item/Turn/Thread protocol
built because MCP's tool-oriented model was insufficient for their case
{{url:https://openai.com/index/unrolling-the-codex-agent-loop}}
{{url:https://openai.com/index/unlocking-the-codex-harness}}. VS Code's own
writeup on the Copilot harness names three loop responsibilities and a
PR-gated eval suite behind multi-provider routing
{{url:https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode}}.

**Concrete architectural techniques recur across otherwise unrelated
projects.** State-machine guardrails that shrink the available tool set per
phase fixed local-model failures in one report
{{gh:statewright/statewright}}; SmallCode compensates for small (8B-35B)
models with budget-managed context and forgiving tool parsing rather than
assuming a large-model-shaped harness works at any scale
{{gh:doorman11991/smallcode}}. OpenCodeReview constrains an LLM code
reviewer with deterministic engineering rules and reports higher precision
and F1 than general-purpose review agents at roughly 1/9 the token cost —
a vendor-reported figure, unverified here beyond the repo's own claim
{{gh:alibaba/open-code-review}}. "Code as Agent Harness" argues code itself
is the substrate that unifies the interface, execution mechanism, and
multi-agent scaling problem, rather than treating code execution as one tool
among many {{arxiv:2605.18747}}.

## Origin

The oldest entry in this category frames the underlying idea before "harness"
was the word for it: Language Model Cascades models chains of LLM calls with
control flow — chain-of-thought, verifiers, STaR, selection-inference, tool
use — as probabilistic-programming graphical models, giving a common
formalism for reasoning about multi-step, multi-model pipelines
{{arxiv:2207.10342}}.

## Open problems

**Harness design is still model-specific, which is a scaling problem, not a
one-time cost.** Self-Harness's own framing states that effective harness
design is inherently tied to a particular model's behavior, and as models
proliferate and evolve rapidly, hand-engineering a harness per model does not
scale {{arxiv:2606.09498}} — the direct motivation for the self-improving
approaches above, but also the reason there is no single "correct" harness to
converge on, only ones fit to a specific model at a specific time.

**Runtime semantics can silently cost tokens or correctness if mismatched to
training.** Agents Learn Their Runtime finds that mismatching interpreter
persistence to training-time semantics costs either correctness or a 3.5x
token overhead {{arxiv:2603.01209}} — a reminder that harness changes are not
free even when they measurably help on one metric.

**Determinism and verifiability remain open even in narrow domains.**
Replayable Financial Agents measures trajectory determinism and
evidence-conditioned faithfulness for tool-using agents specifically because
neither is guaranteed by default {{arxiv:2601.15322}}, and CaveAgent's
approach — keeping a persistent runtime as the actual state store so its
verifiable state can double as an RL reward signal — is presented as a way
around needing human labels for that verification, not evidence that the
underlying problem is solved {{arxiv:2601.01569}}.

*Editorial note:* this category is dominated by a single provenance code
(`HE`) across nearly all 90 entries, unlike more balanced categories in this
corpus — treat it as reflecting one curator's coverage of a fast-moving
GitHub ecosystem rather than independently corroborated consensus. It also
contains at least six overlapping meta-lists that curate the same space
recursively (`AutoJunjie/awesome-agent-harness`, `Picrew/awesome-agent-harness`
with 338 entries, `RUCAIBox/awesome-agent-harness` with 500+, `RyanAlberts
/best-of-Agent-Harnesses` with 140+, `jiji262/awesome-harness-engineering`,
`danielrosehill/AI-Harnesses`) — worth knowing about as an entry point into
the wider ecosystem, but they are indexes, not primary findings, and I have
not cited them as evidence above. Tool-specific performance numbers
throughout this page (token-reduction percentages, precision gains) are
self-reported by the tool's own repository unless otherwise noted; treat them
as vendor claims pending independent replication.

## See also

- [[context-engineering]]
- [[coding-agents]]
- [[observability-and-ops]]
- [[tool-use-and-protocols]]
- [[multi-agent]]
