# observability-and-ops

56 entries.

## Timeline

11 dated entries, oldest first.

- [Where LLM Agents Fail and How They Can Learn From Failures (AgentDebug)](https://arxiv.org/abs/2509.25370) · 2025-09
  - `arxiv:2509.25370` · cited by 1: HE
  - summary: Introduces AgentErrorTaxonomy (a modular failure classification across memory, reflection, planning, action, and system layers) and AgentErrorBench (annotated failure trajectories from ALFWorld, GAIA, WebShop), then shows a debugging framework using them lifts task success up to 26% by isolating root causes and generating corrective feedback.

- [Architecting AgentOps Needs CHANGE](https://arxiv.org/pdf/2601.06456v1) · 2026-01
  - `arxiv:2601.06456` · cited by 1: VA
  - summary: Argues DevOps/MLOps operational principles don't transfer to agentic systems because their behavior keeps changing after deployment, and proposes CHANGE, a six-capability framework (Contextualize, Harmonize, Anticipate, Negotiate, Generate, Evolve) for architecting AgentOps around continuous co-evolution rather than fixed control loops.

- [Interpreting Agentic Systems: Beyond Model Explanations to System-Level Accountability](https://arxiv.org/pdf/2601.17168v1) · 2026-01
  - `arxiv:2601.17168` · cited by 1: VA
  - summary: Gaps in explaining temporal dynamics and compounding decisions.

- [Securing LLM-as-a-Service for Small Businesses: An Industry Case Study of a Distributed Chatbot Deployment Platform](https://arxiv.org/pdf/2601.15528v1) · 2026-01
  - `arxiv:2601.15528` · cited by 1: VA
  - summary: An industry case study of a distributed k3s-based platform letting small businesses deploy RAG chatbots with per-tenant isolation and platform-level prompt-injection defenses, validated on a real e-commerce deployment without requiring model retraining.

- [TriCEGAR: A Trace-Driven Abstraction Mechanism for Agentic AI](https://arxiv.org/pdf/2601.22997v1) · 2026-01
  - `arxiv:2601.22997` · cited by 1: VA
  - summary: Predicate-tree state abstraction from traces for runtime verification.

- [When AI Agents Touch CI/CD Configurations: Frequency and Success](https://arxiv.org/pdf/2601.17413v1) · 2026-01
  - `arxiv:2601.17413` · cited by 1: VA
  - summary: Modification frequency, merge and build success across 8,031 PRs.

- [AgentCgroup: Understanding and Controlling OS Resources of AI Agents](https://arxiv.org/abs/2602.09345) · 2026-02
  - `arxiv:2602.09345` · cited by 1: HE
  - summary: Measures OS-level resource behavior in sandboxed coding agents and finds tool-call execution accounts for 55-60% of end-to-end latency with memory (not CPU) as the concurrency bottleneck and up to 15.4x memory spikes, then proposes an eBPF-based controller matched to tool-call-level granularity instead of container-level policies.

- [AgentStepper: Interactive Debugging of Software Development Agents](https://arxiv.org/abs/2602.06593) · 2026-02
  - `arxiv:2602.06593` · cited by 1: HE
  - summary: The first interactive debugger for LLM-based software agents, representing trajectories as structured conversations with breakpoints, stepwise execution, and live prompt/tool editing; a user study found it cut bug-identification success from needing extensive effort to 60% success with frustration dropping from 5.4/7 to 2.4/7.

- [From Features to Actions: Explainability in Traditional and Agentic AI Systems](https://arxiv.org/pdf/2602.06841v1) · 2026-02
  - `arxiv:2602.06841` · cited by 1: VA
  - summary: Attribution vs trace-based diagnostics for multi-step trajectories.

- [TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code](https://arxiv.org/abs/2602.06875) · 2026-02
  - `arxiv:2602.06875` · cited by 2: HE, VA
  - summary: Instruments LLM-generated code with diagnostic probes to capture runtime traces, then runs causal analysis to localize the true root cause of a bug and learns from prior failed repair attempts via a historical-lesson mechanism, improving Pass@1 up to 34.43% over prior automated repair baselines.

- [AgentTrace: Causal Graph Tracing for Root Cause Analysis in Multi-Agent Systems](https://arxiv.org/abs/2603.14688) · 2026-03
  - `arxiv:2603.14688` · cited by 1: HE
  - summary: A lightweight causal-tracing framework that reconstructs causal graphs from multi-agent execution logs and ranks root causes by structural signals without invoking an LLM at debug time, localizing failures faster and more accurately than heuristic or LLM-based baselines.

## Tools & Undated

45 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [5 Production Scaling Challenges for Agentic AI in 2026](https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/)
  - `url:https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026` · cited by 1: HE
  - summary: Names five recurring production-scaling blockers for agentic AI: orchestration complexity under load, immature observability into per-step decisions, unpredictable token cost accumulation, no consensus on non-deterministic evaluation, and guardrails that don't restrict usefulness.

- [A Dev's Guide to Production-Ready AI Agents](https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents)
  - `url:https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents` · cited by 1: HE
  - summary: Recommends agent-specific production infrastructure (session management, persistent memory, authenticated tool integration, real-time logging) plus a staged sandbox-to-canary-to-full-production rollout rather than deploying agents directly.

- [agentacct](https://github.com/mikehasa/agentacct)
  - `gh:mikehasa/agentacct` · cited by 1: HE
  - summary: TODO

- [Agentic Development: What It Means for Engineering Infrastructure in 2026](https://www.bunnyshell.com/guides/agentic-development/)
  - `url:https://bunnyshell.com/guides/agentic-development` · cited by 1: HE
  - summary: Argues infrastructure, not the model, is the bottleneck for agentic workflows, and specifies four requirements: isolated sandboxes for untrusted code, sub-second environment provisioning, automated validation pipelines, and rollback mechanisms to contain failures.

- [AgentOps](https://github.com/AgentOps-AI/agentops)
  - `gh:agentops-ai/agentops` · cited by 1: HE
  - summary: A Python SDK giving session replays, real-time analytics, and cost tracking across agent frameworks (CrewAI, OpenAI Agents, LangChain), positioned as a devtool platform rather than just a logging library.

- [AgentPrism](https://github.com/evilmartians/agent-prism)
  - `gh:evilmartians/agent-prism` · cited by 1: HE
  - summary: An open-source React component library that turns raw JSON agent trace data into hierarchical visual timelines of LLM calls and tool executions, for embedding trace debugging directly into a product's own UI.

- [AgentRx: Systematic Debugging for AI Agents](https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/)
  - `url:https://microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework` · cited by 1: HE
  - summary: Synthesizes constraints from tool schemas and domain policies to automatically pinpoint the first unrecoverable step in an agent's execution, converting heterogeneous logs into a common format and using an LLM judge against a nine-category failure taxonomy.

- [AI Agent Cost Optimization Guide 2026: Reduce Spend by 60-80%](https://moltbook-ai.com/posts/ai-agent-cost-optimization-2026)
  - `url:https://moltbook-ai.com/posts/ai-agent-cost-optimization-2026` · cited by 1: HE
  - summary: NEEDS-SOURCE

- [AI Agent Scaling Gap: Pilot to Production (March 2026)](https://www.digitalapplied.com/blog/ai-agent-scaling-gap-march-2026-pilot-to-production)
  - `url:https://digitalapplied.com/blog/ai-agent-scaling-gap-march-2026-pilot-to-production` · cited by 1: HE
  - summary: Reports 78% of enterprises have agent pilots but only 14% reach production scale, attributing the gap to integration complexity, inconsistent output quality, monitoring deficits, unclear ownership, and insufficient domain-specific training data.

- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
  - `url:https://aws.amazon.com/bedrock/agentcore` · cited by 1: HE
  - summary: AWS's managed platform for deploying, connecting, securing, and scaling production agents across any framework or model without rebuilding infrastructure per project.

- [An Update on Recent Claude Code Quality Reports](https://www.anthropic.com/engineering/april-23-postmortem)
  - `url:https://anthropic.com/engineering/april-23-postmortem` · cited by 1: HE
  - summary: Three independent harness-level changes compounding into visible regression. Best postmortem in the corpus.

- [Arize Phoenix](https://github.com/Arize-ai/phoenix)
  - `gh:arize-ai/phoenix` · cited by 1: HE
  - summary: Open-source agent tracing, evaluation and observability.

- [AWS Agent Registry for Centralized Agent Discovery and Governance](https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview/)
  - `url:https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview` · cited by 1: HE
  - summary: A private, governed catalog for discovering agents, tools, skills, and MCP servers via semantic/keyword search, with approval workflows, CloudTrail audit trails, and IAM/OAuth support.

- [Backtesting AI Agents: How SRE Teams Prove Reliability Before Production](https://drdroid.io/blog/backtesting-ai-agents-how-sre-teams-prove-reliability-before-production)
  - `url:https://drdroid.io/blog/backtesting-ai-agents-how-sre-teams-prove-reliability-before-production` · cited by 1: HE
  - summary: Proposes backtesting agents against synthetic and real incident scenarios before deployment, layering deterministic checks, LLM judges, and human review, in response to 62% of organizations admitting they can't run agents reliably in production.

- [Braintrust](https://www.braintrust.dev)
  - `url:https://braintrust.dev/` · cited by 1: HE
  - summary: An AI observability platform combining real-time trace capture, quality evaluations, and automatic pattern discovery to catch agent issues before they reach users.

- [builderz-labs/mission-control](https://github.com/builderz-labs/mission-control)
  - `gh:builderz-labs/mission-control` · cited by 1: HE
  - summary: A self-hosted control plane for dispatching tasks, inspecting runs, reviewing failures, and tracking spend across multiple agent runtimes from one dashboard.

- [Building Governed Agents: A Framework for Cost, Control, and Compliance](https://www.langchain.com/blog/building-governed-agents-a-framework-for-cost-control-and-compliance)
  - `url:https://langchain.com/blog/building-governed-agents-a-framework-for-cost-control-and-compliance` · cited by 1: HE
  - summary: Frames an LLM gateway as the runtime control plane that turns governance policy into enforceable decisions over model and tool calls, covering token-spend visibility, sensitive-action control, and audit-trail compliance.

- [Building Observable AI Agents: Temporal Now Integrates with Braintrust](https://temporal.io/blog/building-observable-ai-agents-temporal-now-integrates-with-braintrust)
  - `url:https://temporal.io/blog/building-observable-ai-agents-temporal-now-integrates-with-braintrust` · cited by 1: HE
  - summary: Integrates Temporal's durable workflow execution with Braintrust's observability so every Temporal Workflow and Activity becomes a full-context Braintrust span, giving agent tracing that survives infrastructure failures.

- [Claude Code /doctor](https://code.claude.com/docs/en/commands)
  - `url:https://code.claude.com/docs/en/commands` · cited by 1: HE
  - summary: Claude Code's slash commands (`/model`, `/code-review`, `/background`, etc.) let a user configure the assistant, review diffs, and orchestrate large-scale or parallel work through subagents from within a session.

- [Claude Managed Agents: Self-Hosted Sandboxes and MCP Tunnels](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
  - `url:https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes` · cited by 1: HE
  - related: <https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview>
  - summary: Lets Managed Agents execute tools and code inside infrastructure the user controls instead of Anthropic's cloud sandboxes, keeping the agent's filesystem, processes, and network egress inside the user's own boundary while orchestration stays with Anthropic.

- [claude-devtools](https://github.com/matt1398/claude-devtools)
  - `gh:matt1398/claude-devtools` · cited by 1: HE
  - summary: Reads Claude Code's session logs to surface tool calls, token usage, thinking steps, and subagent activity that the terminal UI normally hides, for understanding and optimizing what a coding session actually did.

- [Debugging Deep Agents with LangSmith](https://blog.langchain.com/debugging-deep-agents-with-langsmith/)
  - `url:https://blog.langchain.com/debugging-deep-agents-with-langsmith` · cited by 1: HE
  - summary: Addresses deep agents' hundreds-of-step traces being too complex to inspect manually via Polly, an AI assistant that analyzes traces to identify issues and suggest prompt fixes, plus a Fetch CLI that equips coding agents with debugging access to LangSmith data.

- [Distributed Tracing for Agentic Workflows with OpenTelemetry](https://developers.redhat.com/articles/2026/04/06/distributed-tracing-agentic-workflows-opentelemetry)
  - `url:https://developers.redhat.com/articles/2026/04/06/distributed-tracing-agentic-workflows-opentelemetry` · cited by 1: HE
  - summary: Shows how to implement production-grade distributed tracing for multi-agent systems with OpenTelemetry, propagating context across routing agents, specialist agents, LLM calls, and MCP servers to track requests end-to-end.

- [Enhanced Tool Governance in Vertex AI Agent Builder](https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder)
  - `url:https://cloud.google.com/blog/products/ai-machine-learning/new-enhanced-tool-governance-in-vertex-ai-agent-builder` · cited by 1: HE
  - summary: Integrates a Cloud API Registry into Vertex AI Agent Builder so admins can centrally curate approved tools org-wide, adding a new `ApiRegistry` object to the Agent Development Kit for simplified, governed tool access.

- [FinOps for Agents: Loop Limits, Tool-Call Caps, and the New Unit Economics of Agentic SaaS](https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html)
  - `url:https://infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html` · cited by 1: HE
  - summary: Frames agent cost governance as a FinOps discipline where loop limits, tool-call caps, token budgets, and timeouts are the guardrails that stop runaway costs when an agent hits an edge case and retries excessively.

- [Future AGI](https://github.com/future-agi/future-agi)
  - `gh:future-agi/future-agi` · cited by 1: HE
  - summary: An open-source platform unifying evaluation, tracing, simulation, and guardrails for agents in one system, aimed at replacing a stitched-together stack of separate observability tools with one closed feedback loop.

- [Helicone](https://github.com/Helicone/helicone)
  - `gh:helicone/helicone` · cited by 1: HE
  - summary: An LLM gateway and observability platform giving unified access to 100+ models with built-in cost/latency tracking, prompt management, and automatic provider fallback routing.

- [How My Agents Self-Heal in Production](https://blog.langchain.com/production-agents-self-heal/)
  - `url:https://blog.langchain.com/production-agents-self-heal` · cited by 1: HE
  - summary: Describes a self-healing deployment pipeline that detects regressions via statistical (Poisson) error analysis, triages whether a change caused them, and dispatches an agent to open a fix PR automatically.

- [How We Build Azure SRE Agent with Agentic Workflows](https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-azure-sre-agent-with-agentic-workflows/4508753)
  - `url:https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-azure-sre-agent-with-agentic-workflows/4508753` · cited by 1: HE
  - summary: 35,000+ production incidents; time-to-mitigation 40.5 hours → 3 minutes.

- [Introducing BigQuery Agent Analytics](https://cloud.google.com/blog/products/data-analytics/introducing-bigquery-agent-analytics/)
  - `url:https://cloud.google.com/blog/products/data-analytics/introducing-bigquery-agent-analytics` · cited by 1: HE
  - summary: A single-line-of-code ADK plugin that streams agent interaction data (latency, token use, tool calls) directly into BigQuery for scalable analysis using BigQuery's native AI tooling.

- [KernelEvolve: How Meta's Ranking Engineer Agent Optimizes AI Infrastructure](https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/)
  - `url:https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure` · cited by 1: HE
  - summary: An agentic system that autonomously generates and optimizes production kernels across NVIDIA, AMD, and Meta's own MTIA hardware, used by Meta's Ranking Engineer Agent to make ML-discovered models actually run efficiently at scale.

- [Langfuse](https://github.com/langfuse/langfuse)
  - `gh:langfuse/langfuse` · cited by 1: HE
  - summary: An open-source LLM engineering platform for collaboratively developing, tracing, evaluating, and debugging AI applications, with built-in prompt management alongside observability.

- [mindwalk](https://github.com/cosmtrek/mindwalk)
  - `gh:cosmtrek/mindwalk` · cited by 1: HE
  - summary: Replays a coding agent's session as a 3D map of the codebase that glows where the agent searched, read, or edited, making exploration and decision-making visible without reading logs line by line.

- [Minions: Stripe's one-shot, end-to-end coding agents—Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2)
  - `url:https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2` · cited by 1: HE
  - summary: Stripe's in-house coding agents generate over 1,300 human-reviewed PRs weekly via custom blueprints mixing deterministic workflow nodes with agentic subtasks, run in isolated devboxes with MCP tools.

- [More Visibility into Copilot Coding Agent Sessions](https://github.blog/changelog/2026-03-19-more-visibility-into-copilot-coding-agent-sessions/)
  - `url:https://github.blog/changelog/2026-03-19-more-visibility-into-copilot-coding-agent-sessions` · cited by 1: HE
  - summary: Improves Copilot coding agent session logs with clearer visibility into built-in and custom setup steps and collapsible detail when work is delegated to subagents.

- [OpenLLMetry](https://github.com/traceloop/openllmetry)
  - `gh:traceloop/openllmetry` · cited by 1: HE
  - summary: OpenTelemetry extensions purpose-built for LLM observability, instrumenting model providers, vector databases, and agent frameworks so traces flow into any standard observability backend without vendor lock-in.

- [OpenObserve: Unified Observability for LLM Agents](https://openobserve.ai/)
  - `url:https://openobserve.ai/` · cited by 1: HE
  - summary: A single-binary open-source observability platform unifying logs, metrics, traces, and real-user monitoring, claiming up to 140x lower storage cost than Elasticsearch at similar scale.

- [Opik](https://github.com/comet-ml/opik)
  - `gh:comet-ml/opik` · cited by 1: HE
  - summary: An open-source LLM observability and evaluation platform for tracing multi-step agent workflows, running dataset-based evaluation experiments, and self-hosting production monitoring.

- [OTel GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
  - `url:https://opentelemetry.io/docs/specs/semconv/gen-ai` · cited by 1: HE
  - summary: NEEDS-SOURCE

- [Pydantic Logfire](https://github.com/pydantic/logfire)
  - `gh:pydantic/logfire` · cited by 1: HE
  - summary: A Python-centric observability platform built on OpenTelemetry with native Pydantic integration and SQL querying over trace data, for monitoring LLM and agent behavior in production.

- [Red-Teaming Anthropic's Internal Agent Monitoring Systems — METR](https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring/)
  - `url:https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring` · cited by 1: HE
  - summary: METR's red-team exercise against Anthropic's internal agent-monitoring systems found several novel vulnerabilities (since patched) but nothing that undermined Anthropic's Opus 4.6 sabotage-risk claims, producing a reusable covert-attack trajectory set to strengthen future monitoring.

- [State of Agent Engineering 2026](https://www.langchain.com/state-of-agent-engineering)
  - `url:https://langchain.com/state-of-agent-engineering` · cited by 1: HE
  - summary: A survey of 1,300+ professionals finding 57% of organizations now run agents in production, with quality as the primary remaining barrier and observability (89% adoption) now considered essential rather than optional.

- [Syncause/debug-skill](https://github.com/Syncause/debug-skill)
  - `gh:syncause/debug-skill` · cited by 1: HE
  - summary: An agent debugging skill that captures runtime traces and stack traces before an agent attempts a fix, replacing guesswork about root cause with evidence so repairs are backed by concrete data.

- [Weights & Biases Weave](https://github.com/wandb/weave)
  - `gh:wandb/weave` · cited by 1: HE
  - summary: A toolkit for logging, tracing, and evaluating generative AI applications end to end, bringing structure and reproducibility to agent development from experimentation through production.

- [What Is an Agent Harness? Running Governed Managed Agents in Production](https://www.truefoundry.com/blog/agent-harness-managed-ai-agents)
  - `url:https://truefoundry.com/blog/agent-harness-managed-ai-agents` · cited by 1: HE
  - summary: Argues the agent harness — the runtime layer managing the plan-act-observe loop, tool routing, sandboxing, and approvals — is the real infrastructure decision in agentic AI, and that building it in-house per team is wasteful duplication a managed harness should replace.
