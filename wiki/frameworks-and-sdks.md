---
title: Frameworks and SDKs
category: frameworks-and-sdks
status: draft
updated: 2026-08-01
---

## What it is

A framework or SDK in this sense is the general-purpose layer a team reaches
for before building anything specific: model access, tool-calling plumbing,
memory/state primitives, and a composition model for chaining or branching
agent steps. It's distinct from a harness — a framework's opinions become a
harness only once they're locked into one product's execution loop (see
[[harness-engineering]]) — and distinct from a single coordination mechanism
like debate or team-selection, which belongs to [[multi-agent]] even when it
ships as a library. This page covers the frameworks themselves: what they bet
on, where they cluster, and where the category is thin.

## State of the art

**There is no consensus architecture, and 71 entries in this category is
itself evidence of that.** LangChain remains the earliest and most widely
adopted framework, standardizing model access and tool integration with
built-in monitoring {{gh:langchain-ai/langchain}} — and its own early
history is preserved as a separate corpus entry under the pre-rename
`hwchase17/langchain` path {{gh:hwchase17/langchain}}. Almost everything
else in this category positions itself relative to that default, either by
composing on it (DemoGPT generates a working LangChain app from a plain-English
prompt {{gh:melih-unsal/demogpt}}) or by rejecting its weight: smolagents bets
on minimal code-writing agents in very few lines {{gh:huggingface/smolagents}},
and AutoChain keeps agent, tool, and chain code deliberately small and
unit-testable, built by a support-automation company for production
customer-facing agents rather than research demos {{gh:forethought-technologies/autochain}}.

**AgentForge's efficiency claim is the sharpest number in the category, and
it comes with the sharpest caveat.** Its composable-skill, declarative-YAML
alternative reports cutting agent development time 62% versus LangChain and
78% versus direct API integration, across four benchmark scenarios
{{arxiv:2601.13383}} — verified against the abstract, which frames this
explicitly as the authors' own experimental evaluation, not an independent or
third-party comparison. Read it as one team's benchmark of their own tool
against LangChain, not a settled ranking.

**A more foundational critique targets the whole category's taxonomy, not
any one framework.** Agentic Design Patterns argues that most framework
taxonomies are convenience-based rather than grounded in systems theory, and
instead decomposes an agent into five interacting subsystems (reasoning,
perception, action, learning, communication) to derive 12 reusable design
patterns, demonstrating the approach by identifying structural gaps in ReAct
itself {{arxiv:2601.19752}}.

**Consolidation and language diversification are the two clearest ecosystem
trends.** AG2 is the explicit successor framework from the AutoGen creators
{{gh:ag2ai/ag2}}. Phidata renamed itself Agno and now ships an AgentOS
runtime with a Postgres-backed control plane, web UI, and JWT access control
— an SDK-plus-hosting bet rather than a library alone
{{gh:phidatahq/phidata}}. Outside Python, trpc-agent-go answers LangGraph
with graph-based multi-agent workflows plus MCP/A2A/AG-UI protocol support
and built-in OpenTelemetry tracing for teams whose services are already Go
{{gh:trpc-group/trpc-agent-go}}; Agency does the same for teams wiring LLM
calls, memory, and RAG into idiomatic Go pipelines {{gh:neurocult/agency}};
and Modus offers a serverless framework for agents and APIs in Go or
AssemblyScript {{gh:hypermodeinc/modus}}.

**A separate, larger cluster has abandoned code entirely in favor of visual
or no-code composition.** Dify offers a drag-and-drop workspace for agentic
workflows and RAG pipelines with MCP support, deployable self-hosted or on
managed cloud {{gh:langgenius/dify}}; Giselle is a no-code studio for wiring
together multi-model, multi-agent workflows visually, positioned as an app
builder rather than a coding library {{gh:giselles-ai/giselle}}; ix targets
the same audience with parallel, talking-to-each-other agent workflows
{{gh:kreneskyp/ix}}. This cluster overlaps with chat-platform products more
than with agent libraries — Botpress, for instance, is closer to a hosted
assistant platform with an integrations hub than a bare agent SDK
{{gh:botpress/botpress}}.

**Domain-specific frameworks are emerging rather than everything converging
on one general tool.** InfiAgent externalizes agent state to a file-centric
workspace it reconstructs each step, keeping reasoning context strictly
bounded on arbitrarily long tasks — the paper reports a 20B open model
competitive with larger proprietary systems on DeepResearch-style and
80-paper literature-review tasks specifically because of this bounded-context
property, not fine-tuning {{arxiv:2601.03204}}. OS-Symphony is purpose-built
for computer-use agents, pairing milestone-driven reflection memory for
long-horizon self-correction with tool agents that synthesize live visual
tutorials for unseen apps, reaching 65.84% on OSWorld and claiming new
state-of-the-art results on three online benchmarks — verified against the
abstract {{arxiv:2601.07779}}. Vectara-agentic narrows further still: a thin
wrapper around LlamaIndex's agent classes that turns a Vectara RAG corpus
into a one-line callable tool, with prebuilt finance/legal tools and
hallucination checking against the retrieved corpus {{gh:vectara/py-vectara-agentic}}.

**The long tail is real and worth naming as a tail, not pretending each entry
is a distinct architectural bet.** A large share of the 54 undated tool
entries are single-maintainer frameworks with one-line differentiators —
Upsonic (reliability-focused, MCP support) {{gh:upsonic/upsonic}}, ConnectOnion
(12 lifecycle hooks, multi-agent networking) {{gh:openonion/connectonion}},
ConnectOnion-adjacent Ailoy (WASM, runs anywhere) {{gh:brekkylab/ailoy}},
ConnectOnion-adjacent Astron (enterprise workflow platform)
{{gh:iflytek/astron-agent}}. None of these has enough independent evidence in
the corpus to say whether the differentiator matters in practice; they're
listed here as the category's shape, not individually endorsed.

## Origin

LangChain is both the earliest and the most cited entry in this category
{{gh:langchain-ai/langchain}}, predating most of what it's now compared
against. Hugging Face's Transformer Agents offered an early alternative
framing — a natural-language API layered directly over transformers tooling
rather than a standalone orchestration library
{{url:https://huggingface.co/docs/transformers/transformers_agents}}. For
understanding what a framework actually does under the abstractions, the
`LLM Agents` repo strips a ReAct loop (Thought/Action/Observation) down from
LangChain's machinery to a few hundred lines — useful as a reading reference,
not production infrastructure {{gh:mpaepper/llm_agents}}.

## Open problems

**Project Ariadne's finding is a category-wide problem, not a
framework-specific bug.** Running causal interventions on reasoning steps, it
finds agents reach identical conclusions regardless of contradictory internal
logic — a "faithfulness gap" with violation density up to 0.77 in factual and
scientific domains, confirmed against the abstract {{arxiv:2601.02314}}. Any
framework in this category whose debugging or observability story leans on
inspecting the chain-of-thought trace is, per this finding, potentially
inspecting a rationalization rather than the decision process that actually
produced the output. No framework here claims to have solved this.

**The category has more frameworks than differentiated ideas.** Multiple
entries describe themselves in near-identical terms — "lightweight,"
"minimal," "production-ready," "MCP support" — with no benchmark or
independent citation distinguishing one from the next. That's consistent with
a market still picking winners rather than a taxonomy with real gaps in it;
whether consolidation (AG2 absorbing AutoGen's userbase, Agno absorbing
Phidata's) continues or reverses is not something the corpus can currently
answer.

**Category boundaries with [[multi-agent]] are genuinely blurry, not just an
indexing artifact.** Frameworks whose primary pitch is agent-to-agent
coordination — AgentVerse's dual scaffolds for pipelines and simulations
{{gh:openbmb/agentverse}}, Swarms' enterprise multi-agent orchestration
{{gh:kyegomez/swarms}} — are filed here as general frameworks but are argued
for almost entirely on multi-agent grounds. Per this repo's taxonomy,
multi-agent is the more specific category and should win those cases; treat
their presence here as a sign the classifier scored them close, not as a firm
claim that they belong primarily in this category.

## See also

- [[harness-engineering]]
- [[multi-agent]]
- [[tool-use-and-protocols]]
- [[planning-and-reasoning]]
