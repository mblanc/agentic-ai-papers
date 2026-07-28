---
title: Tool Use and Protocols
category: tool-use-and-protocols
status: draft
updated: 2026-07-28
---

## What it is

Tool use is how an agent extends past its parametric knowledge — calling
calculators, search engines, APIs, or other agents mid-generation. Protocols
are the standardized wire formats for that calling, principally the Model
Context Protocol (MCP), which has become the field's de facto standard for
connecting agents to external tools and servers.

## State of the art

Toolformer established the now-standard shape: a model trained
self-supervised, from a handful of demonstrations per API, to decide which
tool to call, when, and with what arguments {{url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html}}.
Everything downstream refines one of three axes: what to call, how to
generate the call, or how to verify the result.

**Retrieval over massive tool libraries** has moved from single-shot dense
matching to iterative query planning, decomposing a request into sub-tasks and
generating a targeted retrieval query per sub-task {{arxiv:2601.07782}}, and
ACE-Router generalizes the same history-aware routing idea from MCP tools to
the broader "Agent Web" of arbitrary agent-callable services
{{arxiv:2601.08276}}.

**Call-quality and training** work spans a spectrum from prompting to RL. TAFC
adds a universal "think" parameter so a model can articulate its reasoning
before filling in complex, interdependent arguments, with zero architecture
change {{arxiv:2601.18282}}. Further up the training-effort scale, SCRIBE
grounds reward modeling in a curated skill-prototype library instead of
open-ended LLM judging, cutting reward noise enough to take a small model's
AIME25 accuracy from 43.3% to 63.3% {{arxiv:2601.03555}}. A companion finding
is a methodological warning: tool-calling benchmark results are highly
sensitive to undocumented implementation choices (seed, system prompt,
multi-turn template), making cross-paper leaderboard comparisons unreliable
without standardization {{arxiv:2606.00135}}.

**Tool creation**, not just tool selection, is its own thread: CREATOR lets an
LLM write its own tool via documentation and code when nothing existing fits,
separating abstract creation from concrete execution
{{acl:2023.findings-emnlp.462}}, and CUA-Skill takes the same idea to computer-
use, encoding human GUI-interaction knowledge as a large library of composable
skills reaching state-of-the-art 57.5% on WindowsAgentArena
{{arxiv:2601.21123}}.

**MCP itself has become a subject of formal scrutiny**, not just an
implementation detail. The first rigorous security analysis of the protocol
specification found architectural vulnerabilities — no capability attestation,
unauthenticated bidirectional sampling, implicit multi-server trust — that
amplify attack success 23-41% over non-MCP integrations, and proposed a
backward-compatible fix cutting that back to 12.4% at 8.3ms overhead
{{arxiv:2601.17549}}. SMCP takes a broader systems approach, adding identity
management, mutual authentication, and audit logging across the whole protocol
workflow {{arxiv:2602.01129}}. The protocol itself keeps moving: its
2026-07-28 release candidate shifts to a stateless core that scales over
ordinary HTTP and adds server-rendered UI and long-running-task extensions
{{url:https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate}}.

## Origin

Toolformer is the clear origin point — the first demonstration that a model
can teach itself which external tool to invoke and how, with no more
supervision than a few examples per API
{{url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html}}.
ToolAlpaca and the API-Bank benchmark are the early instances of scaling that
idea to compact, open models rather than closed frontier APIs
{{arxiv:2306.05301}} {{acl:2023.emnlp-main.187}}.

## Open problems

Agent "skills" — the packaged, shareable extensions this ecosystem has
converged on — are now a measured attack surface, not a hypothetical one. The
first large-scale study found 26.1% of 31,132 analyzed skills carried at least
one vulnerability, and skills bundling executable scripts were 2.12x more
likely to be vulnerable than instruction-only ones {{arxiv:2601.10338}}. A
follow-up study of 98,380 skills confirmed this isn't accidental: it identified
157 deliberately malicious skills, over half traced to a single threat actor
running templated brand impersonation at scale {{arxiv:2602.06547}}. Tool
poisoning specifically — planting malicious instructions in tool *metadata*
rather than the tool itself — reaches 84.2% attack success while keeping
detection under 0.3% in one demonstrated framework {{arxiv:2601.07395}}, and a
related multi-turn denial-of-service attack can push per-query cost up to
658x while evading standard prompt filters {{arxiv:2601.10955}}. None of this
is settled: `SandScope`'s own audit of 71 real MCP repositories found
security-sensitive capabilities in 886 of 1,127 tools it could profile
{{arxiv:2601.01241}}, meaning most deployed MCP tooling has not been audited
at all. See also [[safety-security-governance]] for the broader threat
landscape this connects to.

Separately, a lower-stakes but very concrete finding: steering an agent's tool
use requires hard constraints, not soft ones. Stripe's own experiments found
warnings and hints get ignored while errors and explicit blocking instructions
work, because agents pursue a narrow goal-directed path rather than exploring
context the way a human developer does
{{url:https://stripe.dev/blog/ai-steering-experiments}}.

## See also

- [[safety-security-governance]]
- [[coding-agents]]
- [[harness-engineering]]
