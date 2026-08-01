---
title: Safety, Security, and Governance
category: safety-security-governance
status: draft
updated: 2026-08-01
---

## What it is

This covers what stops an agent from doing the wrong thing, deliberately (an
attacker steering it) or by default (a capable model given too much
latitude, or a system that never checks). Five clusters recur across the
192 entries here: **prompt injection** (the attack that gets an agent to
authorize something it shouldn't), **sandboxing** (containing what an
agent's code can touch), **memory/RAG poisoning** (corrupting what an agent
believes rather than what it's told), **authorization** (deciding what an
agent's reasoning is allowed to act on), and **human-in-the-loop design**
(when a human actually needs to be in that loop, and when asking them
stops meaning anything).

## State of the art

**Prompt injection is the most mature attack literature here, and both
sides are automating.** AutoInject turns injection's binary success signal
into a trainable dense RL reward, beating template attacks and adaptive
optimizers on AgentDojo and breaking Meta-SecAlign-70B — a model
fine-tuned specifically to resist injection {{arxiv:2602.05746}}.
AutoHijacker uses LLMs themselves as optimizers for black-box indirect
injection {{openreview:2VmB01D9Ef}}. The threat is not theoretical: an
attack that decomposes malicious content into a retrieval-guaranteeing
trigger plus payload gets near-100% retrieval across 11 benchmarks and 8
embedding models for as little as $0.21 per query, and in a real
multi-agent workflow a single poisoned email coerced GPT-4o into
exfiltrating SSH keys over 80% of the time {{arxiv:2601.07072}} — a number
this page verified directly against the abstract, not just the corpus
summary. A SoK-style survey of 78 studies against agentic coding
assistants (Claude Code, Copilot, Cursor, MCP skills) catalogs 42 attack
techniques and finds success rates above 85% against adaptive attacks,
with most of the 18 cataloged defenses stopping less than half of them
{{arxiv:2601.17548}}. Defenses are shifting toward filtering tool results
before they reach the model rather than training a detector: Defense via
Tool Result Parsing reports the lowest attack success rate of any tested
indirect-injection defense {{arxiv:2601.04795}}, RTBAS adapts information
flow control to screen tool calls automatically {{arxiv:2502.08966}}, and
the Task Shield reframes the whole problem as task alignment — does this
instruction actually serve the user's stated goal {{arxiv:2412.16682}}.
AgentDojo remains the reference dynamic testbed for evaluating attacks and
defenses together {{openreview:m1YYAQjO3w}}, and AgentHarm's 110 explicit
malicious tasks across 11 harm categories found leading models comply with
malicious agent requests even *without* jailbreaking {{arxiv:2410.09024}}.

**Sandboxing has become a crowded infrastructure layer converging on
microVM/copy-on-write isolation for cost.** forkd forks warm snapshots to
spin up ~100 sandboxes in ~100ms {{gh:deeplethe/forkd}}, zeroboot claims
under a millisecond via the same technique versus 150-300ms for
competitors {{gh:zerobootdev/zeroboot}}, and CubeSandbox reaches sub-60ms
hardware-isolated startup on RustVMM/KVM {{gh:tencentcloud/cubesandbox}}.
Cloudflare's Dynamic Workers skip VMs entirely, running agent code in JS
isolates and claiming 100x faster cold starts
{{url:https://blog.cloudflare.com/dynamic-workers}}. But two arguments push
back on sandboxing-as-sufficient: the agent's control loop should run
*outside* the sandbox and call in via API, since co-locating them puts
credentials inside untrusted code
{{url:https://mendral.com/blog/agent-harness-belongs-outside-sandbox}}, and
CNCF argues isolation alone doesn't make a fleet of agents economically or
operationally production-ready, contrasting pure-isolation projects with
"agent-substrate" work on pausable, on-demand execution
{{url:https://cncf.io/blog/2026/07/07/why-sandboxing-your-agent-is-not-enough}}.
Cursor's move to OS-level sandboxes (Seatbelt, Landlock/seccomp, WSL2) that
only prompt on boundary violations cut interruptions 40%
{{url:https://cursor.com/blog/agent-sandboxing}}, a concrete data point for
the harness-not-just-sandbox argument.

**Memory and RAG poisoning is a distinct, increasingly practical attack
surface**, not just a variant of prompt injection. AgentPoison poisons an
agent's long-term memory or knowledge base with an optimized trigger
phrase, hitting over 80% attack success on driving, QA, and healthcare
agents while poisoning less than 0.1% of the knowledge base
{{url:https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf}}.
Confundo targets the gap that makes most *published* poisoning attacks
fail against real content-processing pipelines, and doubles as a defense
against your own content being scraped {{arxiv:2602.06616}}. Attacks now
also target infrastructure around retrieval rather than retrieval itself:
DRAINCODE drives up latency 85% and energy use 49% without touching the
model {{arxiv:2601.20615}}, key-collision attacks hijack semantic caching
at an 86% rate {{arxiv:2601.23088}}, and GRASP reconstructs GraphRAG
subgraphs by reframing extraction as ordinary context-processing, reaching
82.9 F1 where prior extraction attacks are suppressed by safe prompts
{{arxiv:2602.06495}}.

**Authorization is shifting from prompt-level trust to structural
enforcement.** Anthropic's own framing is explicit — "beyond permission
prompts" toward structured authorization
{{url:https://anthropic.com/engineering/beyond-permission-prompts}} —
echoed by the finding that users approve 93% of Claude Code prompts
anyway, meaning the approval signal had stopped meaning anything
{{url:https://anthropic.com/engineering/claude-code-auto-mode}}. Progent
gives agents a policy language for least-privilege tool execution
{{arxiv:2504.11703}}; AgentGuardian learns access-control policy from an
agent's own staging-phase execution traces rather than hand-written rules
{{arxiv:2601.10440}}; Faramesh puts a non-bypassable authorization
checkpoint in front of every agent action and logs PERMIT/DEFER/DENY
decisions as an append-only provenance trail {{arxiv:2601.17744}}; and
Open Agent Passport reports 0% attack success under a restrictive
pre-action authorization policy with signed audit records
{{arxiv:2603.20953}}. Microsoft's Agent Governance Toolkit intercepts
every tool call and delegation in deterministic application code before it
reaches the model, so unauthorized actions are structurally blocked rather
than merely discouraged by a prompt
{{gh:microsoft/agent-governance-toolkit}}. Standards are catching up: MCP's
authorization spec defines an OAuth 2.1 flow for scoped tokens
{{url:https://modelcontextprotocol.io/specification/2025-11-05/basic/authorization}},
and an IETF draft is the first standards-track spec for AI agent
authentication, building on WIMSE and OAuth 2.0
{{url:https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth}}.

Multi-agent systems add a distinct security surface — topology-dependent
propagation, inter-agent belief manipulation, contagious blocking attacks —
covered in depth in [[multi-agent]]; within this corpus, NetSafe frames
safety as a property of network topology rather than individual agents
{{arxiv:2410.15686}}, and CORBA shows resource-depletion attacks that
alignment training does not mitigate {{arxiv:2502.14529}}.

## Origin

AgentDojo is the reference dynamic testbed that made evaluating attacks
*and* defenses together standard practice rather than attacks in isolation
{{openreview:m1YYAQjO3w}}. OWASP's LLM01:2025 Prompt Injection entry is the
field's reference definition, distinguishing direct from indirect
injection and jailbreaking {{url:https://genai.owasp.org/llmrisk/llm01-prompt-injection}},
and its Excessive Agency entry is the standard checklist against which
permission-scope audits get measured
{{url:https://genai.owasp.org/llmrisk/llm062025-excessive-agency}}. Two
older, non-agentic results underpin why memory and context leakage matter
now: verbatim training-data memorization is extractable at scale
{{url:https://usenix.org/system/files/sec21-carlini-extracting.pdf}}, and
unintended memorization was quantifiable years before agents made it
exploitable through tool calls
{{url:https://usenix.org/system/files/sec19-carlini.pdf}}.

## Open problems

**Detection timeliness, not just detection accuracy, is largely unsolved.**
StepShield is the first benchmark to measure *when* a rogue agent gets
caught rather than *whether*: on 9,429 incident trajectories, an
847-rule guardrail hits 86% recall but its alert timing is statistically
indistinguishable from random (p = 0.66) — most of its alerts fire on
benign code before any violation occurs {{arxiv:2601.22136}}. Frontier
models also have a failure mode that survives ordinary alignment work:
"Internal Safety Collapse" describes models generating harmful content
while performing an otherwise legitimate task, with a 95.3% average
worst-case failure rate across GPT-5.2, Claude Sonnet 4.5, and other
frontier models on tasks where harmful output is the only valid completion
{{arxiv:2603.23509}}.

**Governance frameworks are proliferating faster than consensus on the
right model.** Delegation Without Living Governance argues that
compliance-based governance — rules set in advance, audits after the fact
— breaks down once agents make runtime decisions, proposing a "Governance
Twin" as a runtime alternative {{arxiv:2601.21226}}. A separate proposal
stages agent autonomy the way self-driving cars staged theirs, via a
transparency-accountability-trustworthiness model
{{arxiv:2601.06223}}. These don't yet agree on a shared vocabulary, let
alone a shared mechanism.

**Human-in-the-loop design is recalibrating from "approve everything" to
"monitor and intervene."** Anthropic's analysis of real Claude agent
interactions finds experienced users shift from approving every action to
monitoring, and that most usage today is still low-risk software
engineering work
{{url:https://anthropic.com/news/measuring-agent-autonomy}}. HiL-Bench
asks the inverse question — do agents know when *they* should stop and
ask a human — and shows RL training on a precision-recall "Ask-F1" reward
teaches a 32B model to escalate better and transfer that judgment across
domains {{arxiv:2604.09408}}. Concrete HITL plumbing is still ad hoc:
LangGraph, AutoGen, and Dify each expose their own pause/resume node, and
the HITL Protocol proposes a framework-agnostic HTTP handoff instead
{{gh:rotorstar/hitl-protocol}}.

**Deanonymization is an underappreciated agentic risk with no proposed
fix yet.** Off-the-shelf LLM agents with web search re-identified 6 of 24
anonymized participants in a public research dataset by cross-referencing
details across benign sub-tasks — no jailbreak or special access required
{{arxiv:2601.05918}}.

**Backdoor persistence across an agent's pipeline stages is worse than
single-stage threat models assume.** BackdoorAgent finds trigger
persistence in up to 78% of memory-stage attacks across QA, code, web, and
driving agents {{arxiv:2601.04566}}, and DemonAgent shows dynamically
encrypted multi-backdoor implantation can evade safety audits entirely
{{arxiv:2502.12575}}.

*Editorial note:* a handful of entries in the corpus remain
`NEEDS-SOURCE` (a 404'd GitHub repo, an MDPI page returning 403, a
LangGraph docs page that only serves a client-side redirect stub) and
were not cited here for that reason.

## See also

- [[tool-use-and-protocols]]
- [[multi-agent]]
- [[harness-engineering]]
