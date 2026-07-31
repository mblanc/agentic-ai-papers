# tool-use-and-protocols

103 entries.

- [A2A Protocol](https://github.com/a2aproject/A2A)
  - `gh:a2aproject/a2a` · cited by 1: HE
  - summary: Agent-to-agent JSON-RPC with Agent Card discovery and task/message/artifact model.

- [AG-UI](https://github.com/ag-ui-protocol/ag-ui)
  - `gh:ag-ui-protocol/ag-ui` · cited by 1: HE
  - summary: Event protocol for agent-to-frontend streaming, tool rendering and HITL interrupts.

- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/pdf/2601.10338v1)
  - `arxiv:2601.10338` · cited by 1: VA
  - summary: The first large-scale security study of agent 'skills' (42,447 collected, 31,132 analyzed) finds 26.1% contain a vulnerability across prompt injection, data exfiltration, privilege escalation, and supply-chain risk, and that skills bundling executable scripts are 2.12x more likely to be vulnerable than instruction-only ones.

- [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)
  - `gh:aws/agent-toolkit-for-aws` · cited by 1: HE
  - summary: Official AWS MCP servers, skills and plugins for provisioning and querying resources.

- [agent-device](https://github.com/callstackincubator/agent-device)
  - `gh:callstackincubator/agent-device` · cited by 1: HE
  - summary: MCP-native iOS/Android control with semantic targeting and replayable workflows.

- [agentgateway](https://github.com/agentgateway/agentgateway)
  - `gh:agentgateway/agentgateway` · cited by 1: HE
  - summary: Unifies LLM, MCP and A2A gateways into one control plane.

- [agentic-stack](https://github.com/codejunkie99/agentic-stack)
  - `gh:codejunkie99/agentic-stack` · cited by 1: HE
  - summary: Portable `.agent/` folder with adapters, addressing harness vendor lock-in.

- [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781)
  - `arxiv:2606.04781` · cited by 1: HE
  - summary: Compiles skills to typed execution graphs; pass rate 53%→67% and skills become auditable.

- [Announcing Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)
  - `url:https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services` · cited by 1: HE
  - summary: Managed MCP endpoints with IAM, audit logging and discovery as platform primitives.

- [Announcing the Agentic Resource Discovery specification](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/)
  - `url:https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification` · cited by 1: HE
  - summary: Runtime discovery of MCP servers and A2A agents via domain catalogs and trust manifests.

- [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills)
  - `gh:sickn33/antigravity-awesome-skills` · cited by 1: HE
  - summary: 1,400+ installable skills with npm installer and role bundles.

- [API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://aclanthology.org/2023.emnlp-main.187/)
  - `acl:2023.emnlp-main.187` · cited by 1: LJ
  - summary: A 73-tool runnable benchmark plus 1,888-dialogue training set for tool-augmented LLMs, showing GPT-4 leads on planning while a fine-tuned Alpaca-based model (Lynx) closes most of the gap to GPT-3.5 on tool use.

- [AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness](https://arxiv.org/abs/2603.03329)
  - `arxiv:2603.03329` · cited by 1: HE
  - summary: Synthesizes runtime constraint guards from tool schemas; smaller model beats larger.

- [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)
  - `gh:appcypher/awesome-mcp-servers` · cited by 1: HE
  - summary: A curated directory of production and experimental MCP servers spanning file access, databases, APIs, and communication platforms, useful as a lookup when wiring an agent to a new external system.

- [AWS Bedrock AgentCore with WebRTC Support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-webrtc/)
  - `url:https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-webrtc` · cited by 1: HE
  - summary: P2P UDP streaming for sub-800ms voice turn-around.

- [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](https://arxiv.org/pdf/2601.10955v1)
  - `arxiv:2601.10955` · cited by 1: VA
  - summary: A stealthy multi-turn denial-of-service attack at the MCP tool layer that edits only text-visible fields to steer agents into verbose tool-calling chains, pushing per-query cost up to 658x and GPU cache occupancy to 35-74% while evading standard prompt filters and output monitors.

- [Beyond Rule-Based Workflows: An Information-Flow-Orchestrated Multi-Agents Paradigm via A2A Communication from CORAL](https://arxiv.org/pdf/2601.09883v1)
  - `arxiv:2601.09883` · cited by 1: VA
  - summary: Replaces predefined multi-agent workflow rules with an orchestrator that monitors task progress and routes agents dynamically via natural-language A2A communication, beating a workflow-based baseline 63.64% vs 55.15% on GAIA at comparable token cost.

- [Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning](https://arxiv.org/pdf/2601.07782v1)
  - `arxiv:2601.07782` · cited by 1: VA
  - summary: Models tool retrieval as iterative query planning instead of single-shot dense matching, decomposing a request into sub-tasks and generating targeted queries per sub-task, trained via RL with verifiable rewards for state-of-the-art zero-shot retrieval generalization.

- [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification](https://arxiv.org/pdf/2601.17549v1)
  - `arxiv:2601.17549` · cited by 1: VA
  - summary: The first formal security analysis of the MCP specification itself, finding architectural vulnerabilities (no capability attestation, unauthenticated bidirectional sampling, implicit multi-server trust) that raise attack success 23-41% over non-MCP integrations, then proposes a backward-compatible extension cutting attack success from 52.8% to 12.4% at 8.3ms overhead.

- [Chain of Tools: Large Language Model is an Automatic Multi-tool Learner](http://arxiv.org/abs/2405.16533)
  - `arxiv:2405.16533` · cited by 1: LJ
  - summary: Black-box probing so the model learns unfamiliar tools without demos.

- [ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models](https://aclanthology.org/2023.findings-emnlp.985/)
  - `acl:2023.findings-emnlp.985` · cited by 1: LJ
  - summary: Lets a chat-based LLM alternate between invoking tools and reasoning within one multi-turn conversation rather than a fixed pipeline, improving ~7.9% over baselines on MATH and HotpotQA.

- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)
  - `gh:chromedevtools/chrome-devtools-mcp` · cited by 1: HE
  - summary: Exposes network, profiling, console and Lighthouse as structured tools.

- [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
  - `gh:hkuds/cli-anything` · cited by 1: HE
  - summary: Generates agent-native CLIs for software never designed for automation.

- [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp)
  - `url:https://anthropic.com/engineering/code-execution-with-mcp` · cited by 1: HE
  - summary: Have agents write code against MCP servers rather than calling tools directly; up to 98.7% token cut.

- [Composio](https://github.com/ComposioHQ/composio)
  - `gh:composiohq/composio` · cited by 1: HE
  - summary: 250+ SaaS APIs as agent-ready actions with managed OAuth.

- [Corpus2Skill: Don't Retrieve, Navigate — Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/pdf/2604.14572)
  - `arxiv:2604.14572` · cited by 1: VA
  - summary: Compiles a corpus into a navigable skill tree, replacing retrieval with traversal.

- [CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models](https://aclanthology.org/2023.findings-emnlp.462/)
  - `acl:2023.findings-emnlp.462` · cited by 1: LJ
  - summary: Separates tool creation from tool use: the LLM writes its own tool via documentation and code when no existing API fits, then executes it, outperforming chain-of-thought and program-of-thought baselines on math and tabular reasoning.

- [CUA-Skill: Develop Skills for Computer Using Agent](https://arxiv.org/pdf/2601.21123v2)
  - `arxiv:2601.21123` · cited by 1: VA
  - summary: A large skill library encoding how humans operate Windows applications as parameterized, composable execution graphs, giving a computer-using agent reusable skills plus memory-aware failure recovery for state-of-the-art 57.5% success on WindowsAgentArena.

- [DALIA: Towards a Declarative Agentic Layer for Intelligent Agents in MCP-Based Server Ecosystems](https://arxiv.org/pdf/2601.17435v1)
  - `arxiv:2601.17435` · cited by 1: VA
  - summary: A declarative architectural layer that formalizes capabilities, exposes tasks via discovery protocol, and builds deterministic task graphs grounded only in declared operations, aiming to fix hallucinated actions and brittle coordination that stem from missing structure rather than model limits.

- [Dataverse Skills: Your Coding Agent Now Speaks Dataverse](https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse)
  - `url:https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse` · cited by 1: HE
  - summary: Domain skills as curated execution strategies across MCP, SDK and raw API.

- [Design Patterns for Deploying AI Agents with Model Context Protocol](https://arxiv.org/abs/2603.13417)
  - `arxiv:2603.13417` · cited by 1: HE
  - summary: Three protocol gaps that break production: identity, tool budgeting, error semantics.

- [Developer's Guide to AI Agent Protocols](https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/)
  - `url:https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols` · cited by 1: HE
  - summary: Maps six interop protocols (MCP, A2A, UCP, AP2, A2UI, AG-UI) to boundary problems.

- [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](http://arxiv.org/abs/2401.06201)
  - `arxiv:2401.06201` · cited by 1: LJ
  - summary: Compresses verbose tool docs into concise instructions.

- [EigentSearch-Q+](https://arxiv.org/abs/2604.07927)
  - `arxiv:2604.07927` · cited by 1: HE
  - summary: Dedicated reasoning tools that externalize intermediate decisions as typed arguments.

- [Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration](https://arxiv.org/pdf/2601.11595v2)
  - `arxiv:2601.11595` · cited by 1: VA
  - summary: Adds a shared context store to MCP so otherwise-stateless servers can read and write shared memory instead of routing everything back through the LLM, cutting redundant LLM calls and response failures on TravelPlanner and REALM-Bench.

- [ET-Agent: Incentivizing Effective Tool-Integrated Reasoning Agent via Behavior Calibration](https://arxiv.org/pdf/2601.06860v2)
  - `arxiv:2601.06860` · cited by 1: VA
  - summary: Trains a tool-integrated reasoning agent to fix its own behavior patterns (redundant or insufficient tool calls) via a self-evolving data flywheel plus two-phase behavior-calibration training, rather than optimizing only for answer accuracy.

- [From Self-Evolving Synthetic Data to Verifiable-Reward RL: Post-Training Multi-turn Interactive Tool-Using Agents](https://arxiv.org/pdf/2601.22607v2)
  - `arxiv:2601.22607` · cited by 1: VA
  - summary: A hierarchical multi-agent engine that synthesizes tool-grounded multi-turn dialogues with executable per-instance checkers, then post-trains on that data with verifier-based RL, matching or beating frontier models on tau^2-bench (73.0% Airline, 98.3% Telecom).

- [Function Calling — OpenAI Docs](https://platform.openai.com/docs/guides/function-calling)
  - `url:https://platform.openai.com/docs/guides/function-calling` · cited by 1: HE
  - summary: The de facto JSON Schema conventions and parallel calling.

- [GEAR: Augmenting Language Models with Generalizable and Efficient Tool Resolution](https://arxiv.org/pdf/2307.08775)
  - `arxiv:2307.08775` · cited by 1: LJ
  - summary: Generalizable, efficient tool resolution decoupled from the main model.

- [Google Developers: Closing the Knowledge Gap with Agent Skills](https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/)
  - `url:https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills` · cited by 1: HE
  - summary: ADK skills with a 117-prompt evaluation harness.

- [Gorilla: Large Language Model Connected with Massive APIs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e4c61f578ff07830f5c37378dd3ecb0d-Abstract-Conference.html)
  - `url:https://proceedings.neurips.cc/paper_files/paper/2024/hash/e4c61f578ff07830f5c37378dd3ecb0d-Abstract-Conference.html` · cited by 1: LJ
  - summary: Gorilla is a fine-tuned LLaMA model trained with Retriever-Aware Training that beats GPT-4 at writing correct API calls and adapts to documentation changes at test time via a paired retriever, substantially reducing hallucinated API usage.

- [GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e393677793767624f2821cec8bdd02f1-Abstract-Conference.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=email&utm_source=Artificial_Intelligence_Weekly_411)
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/e393677793767624f2821cec8bdd02f1-Abstract-Conference.html` · cited by 1: LJ
  - summary: GPT4Tools self-generates instruction-following data (via self-instruction plus LoRA) to teach open-source models like LLaMA to use multimodal tools, improving both known-tool accuracy and zero-shot generalization to unseen tools.

- [Hermes Agent: Unified Streaming for Real-Time Agent Workflows](https://juliangoldie.com/hermes-agent-unified-streaming/)
  - `url:https://juliangoldie.com/hermes-agent-unified-streaming` · cited by 1: HE
  - summary: Token-by-token streaming for sub-second reactive decision loops.

- [instructor](https://python.useinstructor.com/)
  - `url:https://python.useinstructor.com/` · cited by 1: HE
  - summary: Pydantic models for structured extraction with retry and validation feedback.

- [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/pdf/2601.05214v1)
  - `arxiv:2601.05214` · cited by 1: VA
  - summary: Detects wrong-tool, wrong-parameter and bypass errors from a single forward pass.

- [LARGE LANGUAGE MODELS AS TOOL MAKERS](https://arxiv.org/abs/2305.17126)
  - `arxiv:2305.17126` · cited by 1: LJ
  - summary: Closed loop where the model creates its own reusable tools.

- [LLMs in the Imaginarium: Tool Learning through Simulated Trial and Error](https://aclanthology.org/2024.acl-long.570/)
  - `acl:2024.acl-long.570` · cited by 1: LJ
  - summary: Biologically inspired trial, imagination and memory loop.

- [Making Language Models Better Tool Learners with Execution Feedback](https://aclanthology.org/2024.naacl-long.195/)
  - `acl:2024.naacl-long.195` · cited by 1: LJ
  - summary: Learns *when* to use a tool from execution outcomes, not just how.

- [Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study](https://arxiv.org/pdf/2602.06547v1)
  - `arxiv:2602.06547` · cited by 1: VA
  - summary: A security study of 98,380 agent skills finds 157 deliberately malicious ones spanning 632 vulnerabilities, dominated by credential theft via remote code execution and adversarial instructions hidden in documentation, over half traced to one threat actor impersonating brands at scale.

- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
  - `gh:modelcontextprotocol/inspector` · cited by 1: HE
  - summary: Interactive debugging UI for MCP servers without wiring a full agent.

- [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
  - `url:https://modelcontextprotocol.io/specification/2025-11-25/basic/transports` · cited by 1: HE
  - summary: Remote MCP deployment; session headers fight horizontal scaling.

- [mcp-agent](https://github.com/lastmile-ai/mcp-agent)
  - `gh:lastmile-ai/mcp-agent` · cited by 1: HE
  - summary: Composable workflows, observability and provider-agnostic routing over MCP.

- [MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP](https://arxiv.org/pdf/2601.07395v1)
  - `arxiv:2601.07395` · cited by 1: VA
  - summary: An automated black-box optimization framework that plants malicious instructions in tool metadata (not the tool itself) to trick an MCP agent into misusing a legitimate high-privilege tool, reaching 84.2% attack success while keeping malicious-tool detection under 0.3%.

- [MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools](https://arxiv.org/pdf/2601.01241v1)
  - `arxiv:2601.01241` · cited by 1: VA
  - summary: An audit framework that runs MCP tools under WebAssembly sandboxing or unmodified over stdio to trace source-to-sink data flows, recovering security-sensitive capability declarations for 886 of 1,127 profiled tools across 71 real repositories.

- [Microsoft Skills Framework](https://github.com/microsoft/skills)
  - `gh:microsoft/skills` · cited by 1: HE
  - summary: Defining, versioning and distributing skills across platforms.

- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
  - `gh:microsoft/playwright-mcp` · cited by 1: HE
  - summary: Browser automation via accessibility tree rather than screenshots.

- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
  - `url:https://modelcontextprotocol.io/introduction` · cited by 1: HE
  - summary: Open protocol standardizing agent access to tools, data and services.

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
  - `gh:modelcontextprotocol/servers` · cited by 1: HE
  - summary: Official reference server implementations; the structural baseline.

- [MultiTool-CoT: GPT-3 Can Use Multiple External Tools with Chain of Thought Prompting](https://aclanthology.org/2023.acl-short.130/)
  - `acl:2023.acl-short.130` · cited by 1: LJ
  - summary: Uses chain-of-thought prompting to let GPT-3 call multiple external tools (calculator, retriever) mid-reasoning on numerical-plus-knowledge tasks, beating strong baselines on NumGLUE.

- [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/pdf/2606.00135)
  - `arxiv:2606.00135` · cited by 1: VA
  - summary: Shows tool-calling benchmark results are highly sensitive to undocumented implementation choices (seed, system prompt, multi-turn template), making leaderboard rankings unreliable without standardization, then introduces two RL efficiency fixes that cut wasted rollouts and update cost.

- [On the Tool Manipulation Capability of Open-source Large Language Models](http://arxiv.org/abs/2305.16504)
  - `arxiv:2305.16504` · cited by 1: LJ
  - summary: Boosts open-source LLMs' tool-manipulation ability via curated training examples, in-context demonstration retrievers, and generation-style regulation, closing most of the gap to GPT-4 on a new benchmark (ToolBench) with about one developer-day of data curation per tool.

- [outlines](https://github.com/dottxt-ai/outlines)
  - `gh:dottxt-ai/outlines` · cited by 1: HE
  - summary: Constrains sampling by regex/CFG/JSON Schema at the decoding layer.

- [Ponytail](https://github.com/DietrichGebert/ponytail)
  - `gh:dietrichgebert/ponytail` · cited by 1: HE
  - summary: A skill system enforcing a 'laziness ladder' that checks whether code needs to exist or can be reused before an agent writes anything new, cutting code output ~54% and cost ~20% while keeping safety guardrails.

- [Re-Invoke: Tool Invocation Rewriting for Zero-Shot Tool Retrieval](http://arxiv.org/abs/2408.01875)
  - `arxiv:2408.01875` · cited by 1: LJ
  - summary: Unsupervised retrieval via query synthesis and multi-view ranking.

- [RestGPT: Connecting Large Language Models with Real-World RESTful APIs](http://arxiv.org/abs/2306.06624)
  - `arxiv:2306.06624` · cited by 1: LJ
  - summary: RestGPT connects an LLM to real-world RESTful APIs via coarse-to-fine online planning for task decomposition and API selection, plus a dedicated API executor for parameter formulation and response parsing, evaluated on a new benchmark (RestBench) of real-world scenarios with gold solution paths.

- [SAGE: Tool-Augmented LLM Task Solving Strategies in Scalable Multi-Agent Environments](https://arxiv.org/pdf/2601.09750v1)
  - `arxiv:2601.09750` · cited by 1: VA
  - summary: A conversational tool-use interface built on the OPACA framework for dynamic tool discovery and integration, letting new domain-specific tools be added without retraining and comparing several agentic prompting strategies for selecting and executing them.

- [Scaling Parallel Tool Calling for Efficient Deep Research](https://arxiv.org/abs/2602.07359)
  - `arxiv:2602.07359` · cited by 1: HE
  - summary: Concurrent execution as the main latency lever in multi-step research.

- [SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/pdf/2601.03555v1)
  - `arxiv:2601.03555` · cited by 1: VA
  - summary: Grounds reward modeling in a curated library of skill prototypes rather than open-ended LLM judging, cutting reward-signal noise in multi-step tool use and lifting a small model's AIME25 accuracy from 43.3% to 63.3%.

- [Shell + Skills + Compaction: Tips for Long-Running Agents](https://developers.openai.com/blog/skills-shell-tips)
  - `url:https://developers.openai.com/blog/skills-shell-tips` · cited by 1: HE
  - summary: Versioned skill bundles; negative examples raised routing accuracy 73%→85%.

- [SkillNet & SkillsBench: Infrastructure for AI Agent Skills at Scale](https://github.com/skillmatic-ai/awesome-agent-skills)
  - `gh:skillmatic-ai/awesome-agent-skills` · cited by 1: HE
  - summary: Skill creation/evaluation infrastructure with an 86-task, 11-domain benchmark.

- [SkillOpt](https://github.com/microsoft/SkillOpt)
  - `gh:microsoft/skillopt` · cited by 1: HE
  - summary: Treats skills as optimizable parameters improved by trajectory feedback.

- [Skills-in-Context: Unlocking Compositionality in Large Language Models](https://aclanthology.org/2024.findings-emnlp.812/)
  - `acl:2024.findings-emnlp.812` · cited by 1: LJ
  - summary: Unlocks compositional generalization by putting basic skills in the prompt.

- [SkillTester: Benchmarking Utility and Security of Agent Skills](https://arxiv.org/abs/2603.28815)
  - `arxiv:2603.28815` · cited by 1: HE
  - summary: Evaluates skills on capability, robustness and security before deployment.

- [SMCP: Secure Model Context Protocol](https://arxiv.org/pdf/2602.01129v1)
  - `arxiv:2602.01129` · cited by 1: VA
  - summary: Extends MCP with unified identity management, mutual authentication, security-context propagation, and audit logging to close the unauthorized-access, tool-poisoning, and privilege-escalation gaps the base protocol leaves open.

- [superpowers](https://github.com/obra/superpowers)
  - `gh:obra/superpowers` · cited by 1: HE
  - summary: Cross-harness skills packaging TDD, subagent development and review gates.

- [The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
  - `url:https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap` · cited by 1: HE
  - summary: Scaling transport, `.well-known` discovery, Tasks primitive, enterprise extensions.

- [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
  - `url:https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate` · cited by 1: HE
  - summary: The MCP spec's 2026-07-28 release candidate moves to a stateless core that scales over ordinary HTTP and adds extensions for server-rendered UIs (MCP Apps) and long-running work (Tasks).

- [Think-Augmented Function Calling: Improving LLM Parameter Accuracy Through Embedded Reasoning](https://arxiv.org/pdf/2601.18282v2)
  - `arxiv:2601.18282` · cited by 1: VA
  - summary: Adds a universal 'think' parameter to function-calling schemas so a model can articulate its reasoning before filling in complex, interdependent arguments, improving parameter accuracy with no architecture changes and full API compatibility.

- [Tool Annotations as Risk Vocabulary](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/)
  - `url:https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations` · cited by 1: HE
  - summary: Four annotation hints as permission inputs; the "lethal trifecta" framing.

- [Tool Use — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
  - `url:https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview` · cited by 1: HE
  - summary: Client vs server execution models and strict schema enforcement.

- [ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/pdf/2601.08276v1)
  - `arxiv:2601.08276` · cited by 1: VA
  - summary: Trains a lightweight, history-aware router that generalizes from MCP tool selection to the broader Agent Web, scaling to massive candidate-tool spaces and multi-agent collaboration with minimal adaptation.

- [ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](http://arxiv.org/abs/2306.05301)
  - `arxiv:2306.05301` · cited by 1: LJ
  - summary: Auto-generates a 3,938-instance tool-use corpus from a multi-agent simulation covering 400+ real APIs, then fine-tunes 7B/13B models to reach generalized tool-use ability on unseen tools comparable to GPT-3.5, without needing GPT-4-scale models.

- [ToolCoder: A Systematic Code-Empowered Tool Learning Framework for Large Language Models](http://arxiv.org/abs/2502.11404)
  - `arxiv:2502.11404` · cited by 1: LJ
  - summary: Recasts tool learning as code generation with reusable Python scaffolds.

- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html` · cited by 1: LJ
  - summary: Trains a model to decide which API to call, when, and with what arguments in a fully self-supervised way from a handful of demonstrations per tool, the origin point for teaching LLMs tool use without manual annotation.

- [ToolGen: Unified Tool Retrieval and Calling via Generation](http://arxiv.org/abs/2410.03439)
  - `arxiv:2410.03439` · cited by 1: LJ
  - summary: Bakes tools into the vocabulary as tokens, making retrieval a generation step.

- [ToolGym: an Open-world Tool-using Environment for Scalable Agent Testing and Data Curation](https://arxiv.org/pdf/2601.06328v1)
  - `arxiv:2601.06328` · cited by 1: VA
  - summary: 5,571 tools across 204 apps with injected failures for robustness testing.

- [ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html)
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html` · cited by 1: LJ
  - summary: Represents each of many tools as a learned 'toolken' embedding a frozen LLM can emit like a token, adding new tools without fine-tuning or in-context demos across numerical reasoning, KBQA, and embodied tasks.

- [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](http://arxiv.org/abs/2307.16789)
  - `arxiv:2307.16789` · cited by 1: LJ
  - summary: Large-scale API corpus plus a DFS-based decision strategy for tool selection.

- [ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph](http://arxiv.org/abs/2403.00839)
  - `arxiv:2403.00839` · cited by 1: LJ
  - summary: Organizes thousands of tools as a graph the model traverses.

- [ToolPlanner: A Tool Augmented LLM for Multi Granularity Instructions with Path Planning and Feedback](http://arxiv.org/abs/2409.14826)
  - `arxiv:2409.14826` · cited by 1: LJ
  - summary: Path planning plus feedback over multi-granularity instructions.

- [ToolQA: A Dataset for LLM Question Answering with External Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9cb2a7495900f8b602cb10159246a016-Abstract-Datasets_and_Benchmarks.html)
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/9cb2a7495900f8b602cb10159246a016-Abstract-Datasets_and_Benchmarks.html` · cited by 1: LJ
  - summary: ToolQA tests genuine tool-use reasoning (not memorization) by minimizing overlap with pretraining data and providing 13 specialized external-knowledge tools, exposing specific gaps in existing tool-augmented LLMs on hallucination and numerical reasoning.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/pdf/2602.02548v1)
  - `arxiv:2602.02548` · cited by 1: VA
  - summary: Represents GUI operations as a sequence of learnable tool-token embeddings instead of raw coordinates, using semantic anchoring and a curriculum to reach performance competitive with a 235B model using under 1% of its training data.

- [TopoCurate: Modeling Interaction Topology for Tool-Use Agent Training](https://arxiv.org/abs/2603.01714)
  - `arxiv:2603.01714` · cited by 1: HE
  - summary: Learns topological priors over tool chaining, not just individual calls.

- [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/pdf/2601.08012v1)
  - `arxiv:2601.08012` · cited by 1: VA
  - summary: Applies System-Theoretic Process Analysis to derive formal safety specifications for agent tool sequences, then enforces them via an MCP extension requiring structured capability, confidentiality, and trust labels, moving tool safety from ad hoc reliability fixes to a designed guarantee.

- [tui-use](https://github.com/onesuper/tui-use)
  - `gh:onesuper/tui-use` · cited by 1: HE
  - summary: Programmable interaction with REPLs, debuggers and ncurses apps.

- [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255)
  - `arxiv:2505.19255` · cited by 1: LJ
  - summary: Trains VLMs for multimodal thought chains with visual tools in the RL loop.

- [vurb.ts](https://github.com/vinkius-labs/vurb.ts)
  - `gh:vinkius-labs/vurb.ts` · cited by 1: HE
  - summary: TypeScript framework for *authoring* MCP servers with PII redaction and state-gated visibility.

- [What's New with GitHub Copilot Coding Agent](https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent/)
  - `url:https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent` · cited by 1: HE
  - summary: `.github/agents/` files, self-review and security scanning as harness primitives.

- [When Agents Fail to Act: A Diagnostic Framework for Tool Invocation Reliability in Multi-Agent LLM Systems](https://arxiv.org/pdf/2601.16280v1)
  - `arxiv:2601.16280` · cited by 1: VA
  - summary: 12-category error taxonomy for multi-agent tool-use failures.

- [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](https://arxiv.org/pdf/2601.04748v2)
  - `arxiv:2601.04748` · cited by 1: VA
  - summary: Scaling limits and phase transitions in skill selection as libraries grow.

- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-effective-tools-for-agents)
  - `url:https://anthropic.com/engineering/writing-effective-tools-for-agents` · cited by 1: HE
  - summary: Tool design as agent UX: naming, schemas, error surfaces, return conventions.

- [You can't whisper at an AI agent](https://stripe.dev/blog/ai-steering-experiments)
  - `url:https://stripe.dev/blog/ai-steering-experiments` · cited by 1: HE
  - summary: Stripe's steering experiments find 'hard' constraints (errors, explicit blocking instructions) reliably redirect agent tool use while 'soft' cues (warnings, hints) get ignored, because agents pursue a narrow goal-directed path rather than exploring context the way a human developer would.

- [zerolang](https://github.com/vercel-labs/zerolang)
  - `gh:vercel-labs/zerolang` · cited by 1: HE
  - summary: Agents edit code through a compiler-derived ProgramGraph instead of text patches.
