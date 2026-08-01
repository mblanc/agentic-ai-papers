---
title: Tool Use and Protocols
category: tool-use-and-protocols
status: draft
updated: 2026-08-01
---

## What it is

Tool use is how an agent extends past its parametric knowledge — calling
calculators, search engines, APIs, or other agents mid-generation, rather
than answering from what it memorized during training. This category spans
the whole stack that makes that work in practice: choosing which tool to
call among thousands, generating a well-formed call, verifying and recovering
from the result, and — increasingly — the standardized wire protocols (MCP,
A2A, and a widening set of neighbors) and packaged "skills" that make tool
access portable across agents and vendors rather than bespoke per project.

## State of the art

**Tool selection has moved from single-shot dense retrieval to something
closer to planning.** Early systems like ToolLLM organized selection as a
DFS-based decision strategy over a corpus of 16,000+ real APIs
{{arxiv:2307.16789}}, and ToolGen collapsed retrieval into generation itself
by baking tools directly into the model's vocabulary as tokens
{{arxiv:2410.03439}}. The current direction treats a request as something to
decompose first: modeling tool retrieval as iterative query planning —
breaking a request into sub-tasks and issuing a targeted retrieval query per
sub-task, trained with RL against verifiable rewards — for state-of-the-art
zero-shot generalization {{arxiv:2601.07782}}. ToolACE-MCP generalizes the
same history-aware routing idea beyond MCP tool lists to the broader
"Agent Web" of arbitrary agent-callable services {{arxiv:2601.08276}}.

**Call quality spans a spectrum from zero-training prompting to RL, and the
benchmarks measuring it are shakier than the leaderboards suggest.**
Think-Augmented Function Calling adds a universal "think" parameter so a
model can articulate reasoning before filling in complex, interdependent
arguments, with zero architecture change {{arxiv:2601.18282}}. Further up the
training-effort scale, SCRIBE grounds reward modeling in a curated
skill-prototype library instead of open-ended LLM judging, cutting reward
noise enough to take a Qwen3-4B model's AIME25 accuracy from 43.3% to 63.3%
{{arxiv:2601.03555}} (verified against the abstract). AWO takes a different
lever entirely, mining an agent's own execution traces for repeated
tool-call sequences and compiling them into single deterministic
"meta-tools," cutting LLM calls up to 11.9% and lifting task success up to
4.2 points {{arxiv:2601.22037}}. A companion finding is a methodological
warning that should discount all of the above somewhat: tool-calling
benchmark results are highly sensitive to undocumented implementation
choices — seed, system prompt, multi-turn template — making cross-paper
leaderboard comparisons unreliable without standardization
{{arxiv:2606.00135}}.

**Structured output has become a decoding-layer guarantee, not a prompting
convention.** `outlines` constrains sampling by regex, CFG, or JSON Schema at
the token level rather than hoping the model complies {{gh:dottxt-ai/outlines}},
and `instructor` layers Pydantic models with retry-on-validation-failure over
any provider's function calling {{url:https://python.useinstructor.com/}}.
XGrammar-2 pushes this into agent-workload territory specifically, handling
requests that switch output structure mid-generation via tag-triggered
dispatch and cross-request grammar caching, compiling over 6x faster than
prior structured-generation engines {{arxiv:2601.04426}}.

**MCP is now both the default integration layer and a subject of formal
scrutiny.** Anthropic's own guidance argues for having agents write and run
code against MCP servers rather than issuing tool calls one at a time — in
their worked example this cut a 150,000-token workflow to 2,000 tokens, a
98.7% reduction {{url:https://anthropic.com/engineering/code-execution-with-mcp}}
(verified against the post). The protocol keeps moving structurally: the
2026-07-28 release candidate shifts to a stateless core that scales over
ordinary HTTP and adds server-rendered UI and long-running-task extensions
{{url:https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate}}.
The first rigorous security analysis of the specification itself found
architectural gaps — no capability attestation, unauthenticated bidirectional
sampling, implicit multi-server trust — that amplify attack success by
23-41% over non-MCP integrations, and a proposed backward-compatible
extension cuts that from 52.8% to 12.4% at a median 8.3ms overhead per
message {{arxiv:2601.17549}} (verified against the abstract). SMCP takes a
broader systems approach across the same surface, adding identity
management, mutual authentication, and audit logging {{arxiv:2602.01129}}.

**A2A and a widening set of interop protocols now sit alongside MCP rather
than replacing it.** A2A defines JSON-RPC agent-to-agent messaging with
Agent Card discovery and a task/message/artifact model
{{gh:a2aproject/a2a}}; a CORAL-based paradigm shows what dynamic A2A routing
buys over hand-written workflow rules — an orchestrator that monitors task
progress and routes via natural-language A2A messages beats a workflow-based
baseline 63.64% vs 55.15% on GAIA at comparable token cost
{{arxiv:2601.09883}}. Google's developer guide maps six coexisting protocols
(MCP, A2A, UCP, AP2, A2UI, AG-UI) to distinct boundary problems rather than
competing standards
{{url:https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols}}.
agentgateway unifies LLM, MCP, and A2A traffic into one control plane
rather than three {{gh:agentgateway/agentgateway}}.

**Agent "skills" have emerged as the field's answer to packaging
tool-adjacent knowledge that doesn't fit a function schema** — instructions,
scripts, and reference material bundled and versioned together. superpowers
packages TDD, subagent development, and review gates as cross-harness skills
{{gh:obra/superpowers}}, and Microsoft's Skills Framework standardizes
defining, versioning, and distributing them across platforms
{{gh:microsoft/skills}}. OpenAI's own guidance on long-running agents found
that adding negative examples to versioned skill bundles raised routing
accuracy from 73% to 85%
{{url:https://developers.openai.com/blog/skills-shell-tips}}, and Ponytail
enforces a "laziness ladder" — checking whether code needs to exist at all
before an agent writes anything new — cutting code output roughly 54% and
cost roughly 20% while keeping guardrails intact
{{gh:dietrichgebert/ponytail}}. AIP compiles skills into typed, auditable
execution graphs rather than loose instruction bundles, moving one
benchmark's pass rate from 53% to 67% {{arxiv:2606.04781}}. Whether skills
should replace multi-agent decomposition is contested: one study finds real
scaling limits and phase transitions in skill selection as a library grows
— single-agent-with-skills doesn't just keep winning as libraries scale
{{arxiv:2601.04748}}.

## Origin

Toolformer is the clear origin point for *learned* tool use: a model trained
self-supervised, from a handful of demonstrations per API, to decide which
tool to call, when, and with what arguments, with no manual annotation
pipeline {{arxiv:2302.04761}}. WebGPT predates and narrows this to one tool —
a browser — trained by imitation then preference optimization, and is
arguably the ancestor of today's deep-research agents
{{arxiv:2112.09332}}. API-Bank and ToolAlpaca are the early instances of
scaling the idea past closed frontier models: API-Bank pairs a 73-tool
runnable benchmark with an 1,888-dialogue training set showing a fine-tuned
Alpaca-based model closes most of the gap to GPT-3.5
{{acl:2023.emnlp-main.187}}, and ToolAlpaca auto-generates a 3,938-instance
corpus from multi-agent simulation across 400+ real APIs to bring 7B/13B
models to comparable generalized tool use without GPT-4-scale parameters
{{arxiv:2306.05301}}.

## Open problems

**Skills and MCP tools are now a measured attack surface, not a
hypothetical one, and the numbers are worse than intuition suggests.** The
first large-scale study of agent skills found 26.1% of 31,132 analyzed
skills carried at least one vulnerability, with 5.2% showing patterns
strongly suggestive of malicious intent, and skills bundling executable
scripts were 2.12x more likely to be vulnerable than instruction-only ones
{{arxiv:2601.10338}} (verified against the abstract). A follow-up study of
98,380 skills confirmed this isn't incidental: it found 157 deliberately
malicious skills spanning 632 vulnerabilities, over half traced to a single
threat actor running templated brand impersonation at scale
{{arxiv:2602.06547}}. At the protocol layer, tool poisoning — planting
malicious instructions in tool *metadata* rather than the tool itself —
reaches 84.2% attack success while keeping detection under 0.3% in one
demonstrated framework {{arxiv:2601.07395}}, and a related multi-turn
denial-of-service attack can push per-query cost up to 658x while evading
standard prompt filters {{arxiv:2601.10955}}. None of this is settled:
MCP-SandboxScan's own audit of 71 real MCP repositories recovered
security-sensitive capability declarations for 886 of 1,127 tools it could
profile {{arxiv:2601.01241}}, implying most deployed MCP tooling has not
been audited at all. See [[safety-security-governance]] for the broader
threat landscape this connects to.

**Reliability failures are being diagnosed rather than just observed.** A
diagnostic framework proposes a 12-category error taxonomy specifically for
tool-invocation failures in multi-agent settings {{arxiv:2601.16280}}, and a
separate line shows hallucinated tool selection — wrong tool, wrong
parameter, or a bypass entirely — is detectable from a model's internal
representations in a single forward pass, before the call is even issued
{{arxiv:2601.05214}}.

**Steering an agent's tool use requires hard constraints, not soft ones.**
Stripe's own experiments found warnings and hints get ignored while errors
and explicit blocking instructions reliably redirect behavior, because
agents pursue a narrow goal-directed path rather than exploring context the
way a human developer does
{{url:https://stripe.dev/blog/ai-steering-experiments}}. Design Patterns for
Deploying AI Agents with MCP names three protocol-level gaps that break
production specifically — identity, tool budgeting, and error semantics —
that no amount of prompt engineering fixes {{arxiv:2603.13417}}.

## See also

- [[safety-security-governance]]
- [[coding-agents]]
- [[harness-engineering]]
- [[frameworks-and-sdks]]
