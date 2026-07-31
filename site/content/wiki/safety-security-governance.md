---
title: Safety, Security, and Governance
category: safety-security-governance
status: draft
updated: 2026-07-30
---

## What it is

This covers what stops an agent from doing the wrong thing — deliberately
(an attacker) or accidentally (a capable model given too much latitude).
Three layers recur throughout: **sandboxing** (containing what an agent's
code can touch), **authorization** (deciding what an agent's *reasoning* is
allowed to authorize), and **prompt injection** (the attack that tries to
make the agent authorize something it shouldn't).

## State of the art

**Prompt injection is the most mature attack literature here, and it keeps
getting more automated.** AutoHijacker uses LLMs themselves as optimizers for
black-box indirect injection [openreview:2VmB01D9Ef](https://openreview.net/pdf?id=2VmB01D9Ef), and AutoInject turns
injection's binary success signal into a trainable RL reward dense enough to
break Meta-SecAlign-70B, a model fine-tuned specifically to resist injection
[arxiv:2602.05746](https://arxiv.org/pdf/2602.05746v1). The threat is not theoretical: a single poisoned email
coerced GPT-4o into exfiltrating SSH keys over 80% of the time in a real
multi-agent workflow, at $0.21 per query [arxiv:2601.07072](https://arxiv.org/pdf/2601.07072v1). OWASP's
LLM01:2025 entry is the field's reference definition of the attack class
[url:https://genai.owasp.org/llmrisk/llm01-prompt-injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), and Simon
Willison's ongoing series is the closest thing to a running historical
record of how the industry's understanding of it has evolved
[url:https://simonwillison.net/series/prompt-injection](https://simonwillison.net/series/prompt-injection/).

**Sandboxing has become a crowded, fast-moving infrastructure layer of its
own**, converging on microVM/copy-on-write isolation as the dominant pattern
for cost: forkd forks warm snapshots to spin up ~100 sandboxes in ~100ms
[gh:deeplethe/forkd](https://github.com/deeplethe/forkd), zeroboot claims under a millisecond via the same
technique [gh:zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot), and CubeSandbox reaches sub-60ms
hardware-isolated startup [gh:tencentcloud/cubesandbox](https://github.com/TencentCloud/CubeSandbox). But a direct
argument pushes back on sandboxing-as-sufficient: the agent's control loop
should run *outside* the sandbox and call into it via API, because
co-locating them puts credentials inside untrusted code
[url:https://mendral.com/blog/agent-harness-belongs-outside-sandbox](https://www.mendral.com/blog/agent-harness-belongs-outside-sandbox) — and
CNCF makes the complementary point that isolation alone doesn't make a fleet
of agents economically or operationally production-ready
[url:https://cncf.io/blog/2026/07/07/why-sandboxing-your-agent-is-not-enough](https://www.cncf.io/blog/2026/07/07/why-sandboxing-your-agent-is-not-enough/).

**Memory and RAG poisoning is a distinct, increasingly practical attack
surface**, not just a variant of prompt injection. AgentPoison poisons an
agent's long-term memory or knowledge base with an optimized trigger phrase,
hitting over 80% attack success while poisoning less than 0.1% of the
knowledge base [url:https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf).
Confundo specifically targets the gap that makes most *published* poisoning
attacks fail in practice — surviving real content-processing pipelines and
unpredictable queries — and doubles as a defense against your own content
being scraped [arxiv:2602.06616](https://arxiv.org/pdf/2602.06616v1). Attacks now also target the
infrastructure *around* retrieval rather than retrieval itself: DRAINCODE
drives up energy and latency costs without touching the model
[arxiv:2601.20615](https://arxiv.org/pdf/2601.20615v3), and key-collision attacks hijack semantic caching at an
86% rate [arxiv:2601.23088](https://arxiv.org/pdf/2601.23088v1).

**Authorization is shifting from prompt-level trust to structural
enforcement.** Anthropic's own framing is explicit: "beyond permission
prompts" toward structured authorization
[url:https://anthropic.com/engineering/beyond-permission-prompts](https://www.anthropic.com/engineering/beyond-permission-prompts), echoed
by Anthropic's finding that users approve 93% of prompts anyway, meaning the
approval signal had stopped meaning anything
[url:https://anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode). AgentGuardian
learns access-control policy from an agent's own staging-phase execution
traces rather than hand-written rules [arxiv:2601.10440](https://arxiv.org/pdf/2601.10440v1), and Microsoft's
Agent Governance Toolkit intercepts every tool call and delegation in
deterministic application code before it reaches the model, so unauthorized
actions are structurally blocked rather than merely discouraged by a prompt
[gh:microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit).

## Origin

AgentDojo is the reference dynamic testbed for evaluating prompt-injection
attacks *and* defenses together, rather than attacks in isolation
[openreview:m1YYAQjO3w](https://openreview.net/pdf?id=m1YYAQjO3w). OWASP's Excessive Agency entry
([url:https://genai.owasp.org/llmrisk/llm062025-excessive-agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)) is the
standard checklist against which permission-scope audits get measured.

## Open problems

**Detection timeliness, not just detection accuracy, is still mostly
unsolved.** StepShield is the first benchmark to measure *when* a rogue agent
gets caught rather than *whether*, and finds an 847-rule guardrail hitting
86% recall is statistically no better than random at catching the actual
moment an agent turns rogue [arxiv:2601.22136](https://arxiv.org/pdf/2601.22136v1). Frontier models also have a
safety failure mode that survives ordinary alignment: "Internal Safety
Collapse" describes models generating harmful content while performing an
otherwise legitimate task, with worst-case failure rates averaging 95% across
GPT-5.2, Claude Sonnet 4.5, and other frontier models on tasks where harmful
output is the only valid completion [arxiv:2603.23509](https://arxiv.org/pdf/2603.23509).

**Deanonymization and re-identification are underappreciated agentic
risks.** Off-the-shelf LLM agents with web search re-identified 6 of 24
anonymized participants in a public research dataset by cross-referencing
details across benign sub-tasks — no jailbreak or special access required
[arxiv:2601.05918](https://arxiv.org/pdf/2601.05918v1).

See also [[tool-use-and-protocols]] for MCP-specific security work (tool
poisoning, protocol-level vulnerabilities) that sits adjacent to but outside
this category's scope.

*Editorial note:* 3 entries could not be summarized this pass (a 404'd
GitHub repo, an MDPI page returning 403, and a LangGraph docs page that
returned only a client-side redirect stub). These remain `NEEDS-SOURCE` in
the corpus.

## See also

- [[tool-use-and-protocols]]
- [[multi-agent]]
- [[harness-engineering]]
