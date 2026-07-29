# harness-engineering

79 entries.

- [A Scheduler-Theoretic Framework for LLM Agent Execution](https://arxiv.org/abs/2604.11378)
  - `arxiv:2604.11378` · cited by 1: HE
  - summary: Surveys 70 projects; 60% use the plain agent loop, and maps the alternatives' trade-offs.

- [Agent Harness Design: 3 Patterns for Harnessing Claude's Intelligence](https://claude.com/blog/harnessing-claudes-intelligence)
  - `url:https://claude.com/blog/harnessing-claudes-intelligence` · cited by 1: HE
  - summary: Anthropic's own harness-design guidance: lean on tools Claude already understands well, strip out harness assumptions as the model gets more capable, and reserve explicit boundaries for security, cost, and UX rather than over-constraining behavior.

- [agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering)
  - `gh:china-qijizhifeng/agentic-harness-engineering` · cited by 1: HE
  - summary: An observability system that evolves a coding agent's harness (prompts, tools, memory) through iterative evaluate-analyze-improve cycles while keeping the base model fixed, lifting GPT-5.4 from 69.7% to 77.0% pass rate with evolved harnesses transferring across models.

- [Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics](https://arxiv.org/abs/2603.01209)
  - `arxiv:2603.01209` · cited by 1: HE
  - summary: Mismatching runtime persistence to training-time semantics costs either correctness or 3.5× tokens.

- [AgentSPEX](https://github.com/ScaleML/AgentSPEX)
  - `gh:scaleml/agentspex` · cited by 1: HE
  - summary: Declarative YAML spec language for agent workflows with sandbox, checkpointing and trajectory logs.

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - `gh:alibaba/open-code-review` · cited by 1: HE
  - summary: An LLM-based CLI that reviews Git diffs under deterministic engineering constraints for precise line-level comments, reaching higher precision and F1 than general-purpose review agents while using about 1/9 the tokens.

- [AOHP](https://github.com/aohp-os/aohp)
  - `gh:aohp-os/aohp` · cited by 1: HE
  - summary: An OS-level agent harness on Android letting agents compose personalized services by orchestrating system APIs, CLIs, and app GUIs directly, instead of being limited to fixed developer-defined app interfaces.

- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071)
  - `arxiv:2604.18071` · cited by 1: HE
  - summary: Empirical study of 70 public agent systems across five recurring design dimensions.

- [AutoAgent](https://github.com/kevinrgu/autoagent)
  - `gh:kevinrgu/autoagent` · cited by 1: HE
  - summary: A meta-agent that iteratively modifies an agent's own configuration, prompts, and tools based on benchmark scores, automating the harness-tuning loop instead of requiring manual tweak-and-test cycles.

- [autocontext](https://github.com/greyhaven-ai/autocontext)
  - `gh:greyhaven-ai/autocontext` · cited by 1: HE
  - summary: A recursive self-improving harness that accumulates playbooks, datasets, and training artifacts across runs so an agent (and its future iterations) keeps getting better at a task over time.

- [AutoJunjie/awesome-agent-harness](https://github.com/AutoJunjie/awesome-agent-harness)
  - `gh:autojunjie/awesome-agent-harness` · cited by 1: HE
  - summary: A curated reference collection spanning orchestrators, runtimes, spec tools, and knowledge-management systems for the full harness-engineering stack.

- [Awesome Code as Agent Harness Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)
  - `gh:yennning/awesome-code-as-agent-harness-papers` · cited by 1: HE
  - summary: A paper collection organized around 'Code as Agent Harness', covering how code serves as an executable interface for agent reasoning, action, environment modeling, and coordination across coding, GUI automation, science, and robotics.

- [browser-harness](https://github.com/browser-use/browser-harness)
  - `gh:browser-use/browser-harness` · cited by 1: HE
  - summary: A thin CDP-based harness that connects LLMs directly to real browsers, writing missing helper code on the fly during execution so repetitive browser-interaction patterns get automated away rather than re-solved each time.

- [Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned](https://arxiv.org/abs/2603.05344)
  - `arxiv:2603.05344` · cited by 1: HE
  - summary: Practitioner paper on eager-construction scaffolding and compound multi-model architecture.

- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
  - `url:https://platform.claude.com/docs/en/agent-sdk/overview` · cited by 1: HE
  - summary: The Agent SDK exposes the same tools, agent loop, and context management that power Claude Code as a library (Python/TypeScript), so builders get autonomous tool execution, hooks, subagents, and MCP support without implementing a tool loop themselves.

- [ClawGUI](https://github.com/ZJU-REAL/ClawGUI)
  - `gh:zju-real/clawgui` · cited by 1: HE
  - summary: A GUI-agent framework unifying online RL training, standardized evaluation, and real-device deployment into one system, so training environments, benchmarks, and production deployment don't have to be solved as three separate problems.

- [Code as Agent Harness](https://arxiv.org/abs/2605.18747)
  - `arxiv:2605.18747` · cited by 1: HE
  - summary: Survey arguing code is the substrate unifying harness interface, mechanism and multi-agent scaling.

- [CodeWhale](https://github.com/Hmbown/CodeWhale)
  - `gh:hmbown/codewhale` · cited by 1: HE
  - summary: An open-source terminal coding agent supporting 30+ model providers with a unified runtime, read-only safety modes, and resumable local-first execution.

- [coleam00/your-claude-engineer](https://github.com/coleam00/your-claude-engineer)
  - `gh:coleam00/your-claude-engineer` · cited by 1: HE
  - summary: A harness built on top of the Anthropic harness for long-running tasks, letting Claude autonomously manage multi-tool software projects (Linear, GitHub, Slack) via coordinated subagents without exhausting the context window.

- [Continual Harness](https://github.com/sethkarten/continual-harness)
  - `gh:sethkarten/continual-harness` · cited by 1: HE
  - summary: A reference implementation letting agents refine their own prompts, sub-agents, skills, and memory mid-episode via online adaptation, evaluated on Pokémon games as part of the PokeAgent benchmark for long-horizon reasoning.

- [cua](https://github.com/trycua/cua)
  - `gh:trycua/cua` · cited by 1: HE
  - summary: An open-source computer-use platform with a unified API for agents that see screens and drive native applications across macOS, Windows, Linux, and Android, including sandboxing and training-data generation.

- [danielrosehill/AI-Harnesses](https://github.com/danielrosehill/AI-Harnesses)
  - `gh:danielrosehill/ai-harnesses` · cited by 1: HE
  - summary: A curated, dated snapshot (April 2026) of projects self-describing as AI agent harnesses, for surveying the orchestration-layer landscape that manages tool dispatch, permissions, and agent lifecycle.

- [deepclaude](https://github.com/aattaran/deepclaude)
  - `gh:aattaran/deepclaude` · cited by 1: HE
  - summary: Ports a full agent loop to other backends, isolating loop architecture from model identity.

- [DeerFlow](https://github.com/bytedance/deer-flow)
  - `gh:bytedance/deer-flow` · cited by 1: HE
  - summary: An open-source agent orchestration platform with sandboxed execution, persistent memory, extensible skills, and sub-agent decomposition, providing the runtime infrastructure for multi-step tasks rather than just a prompting layer.

- [desloppify](https://github.com/peteromallet/desloppify)
  - `gh:peteromallet/desloppify` · cited by 1: HE
  - summary: A harness combining mechanical detectors and LLM review across 29 languages to systematically score, prioritize, and improve codebase quality over time rather than relying on ad hoc agent judgment.

- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
  - `gh:affaan-m/everything-claude-code` · cited by 1: HE
  - summary: A coordinated engineering system of 67 specialized agents and 281 reusable skills implementing a plan-test-implement-review-verify-remember-improve workflow with security scanning across Claude Code, Codex, and Cursor.

- [Extended Thinking — Claude API Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  - `url:https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking` · cited by 1: HE
  - summary: Reasoning-budget control; thinking blocks must survive tool-result round-trips.

- [Getting started with loops](https://claude.com/blog/getting-started-with-loops)
  - `url:https://claude.com/blog/getting-started-with-loops` · cited by 1: HE
  - summary: Categorizes agent loops into turn-based, goal-based, time-based, and proactive types with different trigger conditions, as a framework for choosing the right loop primitive and managing token usage.

- [GitHub Agentic Workflows](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/)
  - `url:https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview` · cited by 1: HE
  - summary: GitHub Agentic Workflows let developers automate repository tasks via AI agents running inside GitHub Actions, described in plain Markdown instead of YAML, with read-only-by-default permissions.

- [Goose](https://github.com/aaif-goose/goose)
  - `gh:aaif-goose/goose` · cited by 1: HE
  - summary: A general-purpose Rust-based agent that runs locally with a desktop app, CLI, and API, supporting 15+ LLM providers and 70+ MCP extensions for tasks beyond coding (research, writing, data analysis).

- [grok-build](https://github.com/xai-org/grok-build)
  - `gh:xai-org/grok-build` · cited by 1: HE
  - summary: A terminal-based coding agent that understands a codebase, edits files, and executes commands, usable interactively, headlessly for CI, or embedded in editors via the Agent Client Protocol.

- [Harness Books](https://github.com/wquguru/harness-books)
  - `gh:wquguru/harness-books` · cited by 1: HE
  - summary: Two guides on how production coding agents (Claude Code, Codex) are actually engineered — constraint structures, runtime control, query loops, permissions, error recovery, and multi-agent verification patterns.

- [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
  - `url:https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html` · cited by 1: HE
  - summary: Martin Fowler's synthesis: context curation, architectural constraints, entropy management, humans *on* the loop.

- [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)
  - `url:https://martinfowler.com/articles/harness-engineering.html` · cited by 1: HE
  - summary: Böckeler's feedforward-guides / feedback-sensors model; separates computational from inferential controls.

- [Harness Engineering: How to Build Reliable AI Agents by Engineering the System, Not the Model](https://www.deepset.ai/blog/harness-engineering)
  - `url:https://deepset.ai/blog/harness-engineering` · cited by 1: HE
  - summary: Failure-classification framework mapping each failure mode to a harness component.

- [Harness Engineering: Structured Workflows for AI-Assisted Development](https://developers.redhat.com/articles/2026/04/07/harness-engineering-structured-workflows-ai-assisted-development)
  - `url:https://developers.redhat.com/articles/2026/04/07/harness-engineering-structured-workflows-ai-assisted-development` · cited by 1: HE
  - summary: Red Hat's enterprise four-pillar model: vibes, specs, skills, agents.

- [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness)
  - `gh:hkuds/openharness` · cited by 1: HE
  - summary: A lightweight Python framework providing the core harness layer (tools, skills, memory, multi-agent coordination) with safety boundaries and observability built in, so builders don't reimplement it per project.

- [How Middleware Lets You Customize Your Agent Harness](https://blog.langchain.com/how-middleware-lets-you-customize-your-agent-harness/)
  - `url:https://blog.langchain.com/how-middleware-lets-you-customize-your-agent-harness` · cited by 1: HE
  - summary: Six composable hooks for cross-cutting concerns without touching agent logic.

- [HyperAgents: Self-Improving AI Systems](https://pooya.blog/blog/hyperagents-self-improving-ai-meta-research-2026/)
  - `url:https://pooya.blog/blog/hyperagents-self-improving-ai-meta-research-2026` · cited by 1: HE
  - summary: NEEDS-SOURCE

- [Improving Deep Agents with Harness Engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)
  - `url:https://blog.langchain.com/improving-deep-agents-with-harness-engineering` · cited by 1: HE
  - summary: Harness-only changes moved a coding agent from rank 30 to top 5 on Terminal Bench 2.0.

- [jiji262/awesome-harness-engineering](https://github.com/jiji262/awesome-harness-engineering)
  - `gh:jiji262/awesome-harness-engineering` · cited by 1: HE
  - summary: A curated resource list for harness engineering and AI-native engineering, covering foundational design patterns, open-source frameworks (LangGraph, OpenHands), and evaluation benchmarks.

- [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)
  - `gh:langchain-ai/deepagents` · cited by 1: HE
  - summary: An opinionated agent harness that works out of the box with filesystem access, sub-agents, and context management for any tool-calling LLM, meant as a production-ready foundation rather than a from-scratch build.

- [LangGraph — Low Level Concepts](https://langchain-ai.github.io/langgraph/concepts/low_level/)
  - `url:https://langchain-ai.github.io/langgraph/concepts/low_level` · cited by 1: HE
  - summary: Models the loop as a typed-state graph with conditional edges and checkpointing.

- [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/)
  - `url:https://walkinglabs.github.io/learn-harness-engineering/en` · cited by 1: HE
  - summary: Teaches harnesses as closed-loop working systems that keep coding agents reliable by constraining behavior with explicit rules and maintaining context across long-running tasks via state management and verification.

- [Life-Harness](https://github.com/Tianshi-Xu/Life-Harness)
  - `gh:tianshi-xu/life-harness` · cited by 1: HE
  - summary: Lifecycle-aware runtime layer; gains transfer across 18 model backbones.

- [Live-SWE-agent: Autonomous Software Agent with Self-Evolving Harness](https://arxiv.org/html/2511.13646v3)
  - `arxiv:2511.13646` · cited by 1: HE
  - summary: The first agent that autonomously evolves its own scaffold at runtime while solving real software problems, starting from a minimal bash-only agent and reaching 77.4% on SWE-bench Verified without test-time scaling, beating all existing software agents including proprietary ones.

- [Loop Engineering](https://github.com/cobusgreyling/loop-engineering)
  - `gh:cobusgreyling/loop-engineering` · cited by 1: HE
  - summary: A framework for designing the control systems that orchestrate coding agents over time, providing CLI tools (loop-audit, loop-init, loop-cost) and safety checklists to move from manual prompting toward L1-L3 autonomy.

- [lopopolo/harness-engineering](https://github.com/lopopolo/harness-engineering)
  - `gh:lopopolo/harness-engineering` · cited by 1: HE
  - summary: A guide and context bundle arguing agent output improves by shaping the surrounding environment (context and tools), not the model, focused on making organizational knowledge and operational context retrievable to coding agents.

- [meta-agent](https://github.com/canvas-org/meta-agent)
  - `gh:canvas-org/meta-agent` · cited by 1: HE
  - summary: A harness optimizer that reads execution traces from the current harness, proposes a targeted change, evaluates it on a held-out split, and keeps it only if the score improves, rewriting prompts and control flow around a frozen model.

- [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052)
  - `arxiv:2603.28052` · cited by 1: HE
  - summary: Meta-Harness searches over an LLM application's harness code itself (not just prompts) using an agentic proposer with filesystem access to prior candidates' traces, improving a context-management baseline by 7.7 points at 4x fewer tokens and beating hand-engineered baselines on TerminalBench-2.

- [metaharness](https://github.com/SuperagenticAI/metaharness)
  - `gh:superagenticai/metaharness` · cited by 1: HE
  - summary: An open-source library for optimizing the executable harness code around agentic coding systems (repo instructions, validation logic, test flows) through an iterative loop that stores evidence per proposal, making harness engineering repeatable and inspectable.

- [Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents](http://arxiv.org/abs/2306.03314)
  - `arxiv:2306.03314` · cited by 1: LJ
  - summary: An early multi-agent collaboration framework built around case studies of Auto-GPT, BabyAGI, and API-integrating Gorilla, explicitly cataloguing looping, security, scalability, evaluation, and ethics as the open challenges for multi-agent LLM systems.

- [nanobot](https://github.com/HKUDS/nanobot)
  - `gh:hkuds/nanobot` · cited by 1: HE
  - summary: ~4,000-line personal assistant framework with MCP and skills.

- [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723)
  - `arxiv:2603.25723` · cited by 1: HE
  - summary: Externalizes control logic as portable natural-language artifacts run by a shared runtime.

- [neosigmaai/auto-harness](https://github.com/neosigmaai/auto-harness)
  - `gh:neosigmaai/auto-harness` · cited by 1: HE
  - summary: Wraps an existing agent to build a self-improving system that mines failures, optimizes the harness, and gates changes against regressions across benchmarks (Terminal-Bench, BIRD-Interact, tau-bench) automatically.

- [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
  - `gh:yeachan-heo/oh-my-claudecode` · cited by 1: HE
  - summary: Zero-configuration multi-agent orchestration for Claude Code with specialized team-based agents for parallel task delegation and persistent completion with minimal setup.

- [Omnigent](https://github.com/omnigent-ai/omnigent)
  - `gh:omnigent-ai/omnigent` · cited by 1: HE
  - summary: An open-source meta-harness providing a common orchestration layer across multiple coding agents (Claude Code, Codex, Cursor) in unified sessions, letting teams swap model backends and enforce governance across devices.

- [Pi](https://github.com/earendil-works/pi)
  - `gh:earendil-works/pi` · cited by 1: HE
  - summary: A self-extensible agent toolkit with a unified multi-provider LLM API, an agent runtime with tool calling, and an interactive coding agent CLI, for building agents without rebuilding foundational infrastructure per platform.

- [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness)
  - `gh:picrew/awesome-agent-harness` · cited by 1: HE
  - summary: A large curated collection (338 entries across 9 categories) of harness-engineering resources spanning orchestration, execution, evaluation, and security infrastructure for agents.

- [Pipecat: Python Framework for Real-Time Voice Agent Pipelines](https://github.com/pipecat-ai/pipecat)
  - `gh:pipecat-ai/pipecat` · cited by 1: HE
  - summary: Voice and multimodal conversational AI pipelines.

- [raphaelchristi/harness-evolver](https://github.com/raphaelchristi/harness-evolver)
  - `gh:raphaelchristi/harness-evolver` · cited by 1: HE
  - summary: A Claude Code plugin that autonomously evolves prompts, routing, and architecture via multi-agent optimization backed by LangSmith, proposing, evaluating, and merging harness changes through a self-organizing loop.

- [Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents](https://arxiv.org/pdf/2601.15322v1)
  - `arxiv:2601.15322` · cited by 1: VA
  - summary: Measures trajectory determinism and evidence-conditioned faithfulness.

- [retro-harness](https://github.com/wbopan/retro-harness)
  - `gh:wbopan/retro-harness` · cited by 1: HE
  - summary: RHO (Retrospective Harness Optimization) improves an agent's harness purely from its own past trajectories with no labels or validation set, lifting SWE-Bench Pro performance from 59% to 78% in the reported case.

- [revfactory/harness](https://github.com/revfactory/harness)
  - `gh:revfactory/harness` · cited by 1: HE
  - summary: A team-architecture factory for Claude Code that generates specialized agent teams and their skills from a domain description using six pre-defined architectural patterns, automating team decomposition for complex tasks.

- [RUCAIBox/awesome-agent-harness](https://github.com/RUCAIBox/awesome-agent-harness)
  - `gh:rucaibox/awesome-agent-harness` · cited by 1: HE
  - summary: Academic survey and 500+ reference reading list on harness engineering.

- [RyanAlberts/best-of-Agent-Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses)
  - `gh:ryanalberts/best-of-agent-harnesses` · cited by 1: HE
  - summary: A curated, ranked list of 140+ agent harnesses — the orchestration infrastructure converting model reasoning into sustained, tool-using, error-recovering behavior — comparable by autonomy level and recovery tier.

- [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)
  - `arxiv:2606.09498` · cited by 1: HE
  - summary: Self-Harness lets an agent improve its own operating harness with no human engineer via a three-stage loop (mine model-specific weaknesses from traces, propose minimal harness edits, validate via regression testing before accepting), lifting held-out pass rates by 15-21 points across three different base model families on Terminal-Bench-2.0.

- [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)
  - `url:https://humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents` · cited by 1: HE
  - summary: Frames harness engineering as systematically using configuration points (system prompts, tools, MCP servers, skills, hooks) to improve reliability now, rather than waiting on better base models.

- [SmallCode](https://github.com/Doorman11991/smallcode)
  - `gh:doorman11991/smallcode` · cited by 1: HE
  - summary: A coding agent specifically optimized for small (8B-35B parameter) LLMs on consumer hardware, using budget-managed context, forgiving tool parsing, and search-and-replace editing to compensate for weaker models.

- [Squad](https://github.com/bradygaster/squad)
  - `gh:bradygaster/squad` · cited by 1: HE
  - summary: A framework giving a repository a team of specialist agents (frontend, backend, tester, lead) inside GitHub Copilot, automating coordination and execution while keeping humans accountable for approvals and priorities.

- [stanford-iris-lab/meta-harness](https://github.com/stanford-iris-lab/meta-harness)
  - `gh:stanford-iris-lab/meta-harness` · cited by 1: HE
  - summary: A framework for automated search over task-specific harnesses — the code deciding what a fixed base model stores, retrieves, and sees — automating what would otherwise be manual prompting and retrieval-logic engineering.

- [statewright](https://github.com/statewright/statewright)
  - `gh:statewright/statewright` · cited by 1: HE
  - summary: State-machine guardrails restricting tool availability per phase; shrinking tool space fixed local-model failures.

- [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)
  - `url:https://blog.langchain.com/the-anatomy-of-an-agent-harness` · cited by 1: HE
  - summary: Five composing primitives: filesystem, code execution, sandbox, memory, context management.

- [The Coding Harness Behind GitHub Copilot in VS Code](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode)
  - `url:https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode` · cited by 1: HE
  - summary: Three loop responsibilities, multi-provider routing, PR-gated eval suite.

- [The Design Space of Today's and Future AI Agent Systems](https://arxiv.org/abs/2604.14228)
  - `arxiv:2604.14228` · cited by 1: HE
  - summary: Reverse-engineers a production agent's five-stage progressive compaction and hook pipeline.

- [Tuning the harness, not the model: a Nemotron 3 Ultra playbook](https://blog.langchain.com/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook)
  - `url:https://blog.langchain.com/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook` · cited by 1: HE
  - summary: Achieves near-frontier performance by tuning Nemotron 3 Ultra's harness (system prompt, tool descriptions, middleware) instead of its weights, mining execution traces for failure patterns to iteratively refine the scaffolding until the model stops fighting its own infrastructure.

- [Unlocking the Codex Harness: How We Built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
  - `url:https://openai.com/index/unlocking-the-codex-harness` · cited by 1: HE
  - summary: The Item/Turn/Thread protocol, and why MCP's tool-oriented model was insufficient.

- [Unrolling the Codex Agent Loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
  - `url:https://openai.com/index/unrolling-the-codex-agent-loop` · cited by 1: HE
  - summary: Step-by-step decomposition of one loop iteration and where each component plugs in.

- [What makes a harness a harness: necessary and sufficient conditions for an agent harness](https://arxiv.org/abs/2606.10106)
  - `arxiv:2606.10106` · cited by 1: HE
  - summary: Constitutive definition via four necessary elements; applied as an inclusion test to real harnesses.
