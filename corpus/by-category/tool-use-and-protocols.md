# tool-use-and-protocols

134 entries.

## Timeline

120 dated entries, oldest first.

- [WebGPT: Browser-assisted question-answering with human feedback](http://arxiv.org/abs/2112.09332) · 2021-12
  - `arxiv:2112.09332` · cited by 2: LJ, ZJ
  - summary: Browsing agent trained by imitation then preference optimization; the ancestor of deep research.

- [TALM: Tool Augmented Language Models](https://arxiv.org/abs/2205.12255) · 2022-05
  - `arxiv:2205.12255` · cited by 1: ZJ
  - summary: Combines non-differentiable tools with LMs for real-time/private data.

- [API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://aclanthology.org/2023.emnlp-main.187/) · 2023
  - `acl:2023.emnlp-main.187` · cited by 1: LJ
  - summary: A 73-tool runnable benchmark plus 1,888-dialogue training set for tool-augmented LLMs, showing GPT-4 leads on planning while a fine-tuned Alpaca-based model (Lynx) closes most of the gap to GPT-3.5 on tool use.

- [ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models](https://aclanthology.org/2023.findings-emnlp.985/) · 2023
  - `acl:2023.findings-emnlp.985` · cited by 1: LJ
  - summary: Lets a chat-based LLM alternate between invoking tools and reasoning within one multi-turn conversation rather than a fixed pipeline, improving ~7.9% over baselines on MATH and HotpotQA.

- [CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models](https://aclanthology.org/2023.findings-emnlp.462/) · 2023
  - `acl:2023.findings-emnlp.462` · cited by 1: LJ
  - summary: Separates tool creation from tool use: the LLM writes its own tool via documentation and code when no existing API fits, then executes it, outperforming chain-of-thought and program-of-thought baselines on math and tabular reasoning.

- [GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e393677793767624f2821cec8bdd02f1-Abstract-Conference.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=email&utm_source=Artificial_Intelligence_Weekly_411) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/e393677793767624f2821cec8bdd02f1-Abstract-Conference.html` · cited by 1: LJ
  - summary: GPT4Tools self-generates instruction-following data (via self-instruction plus LoRA) to teach open-source models like LLaMA to use multimodal tools, improving both known-tool accuracy and zero-shot generalization to unseen tools.

- [MultiTool-CoT: GPT-3 Can Use Multiple External Tools with Chain of Thought Prompting](https://aclanthology.org/2023.acl-short.130/) · 2023
  - `acl:2023.acl-short.130` · cited by 1: LJ
  - summary: Uses chain-of-thought prompting to let GPT-3 call multiple external tools (calculator, retriever) mid-reasoning on numerical-plus-knowledge tasks, beating strong baselines on NumGLUE.

- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html` · cited by 1: LJ
  - summary: Trains a model to decide which API to call, when, and with what arguments in a fully self-supervised way from a handful of demonstrations per tool, the origin point for teaching LLMs tool use without manual annotation.

- [ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html` · cited by 1: LJ
  - summary: Represents each of many tools as a learned 'toolken' embedding a frozen LLM can emit like a token, adding new tools without fine-tuning or in-context demos across numerical reasoning, KBQA, and embodied tasks.

- [ToolQA: A Dataset for LLM Question Answering with External Tools](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9cb2a7495900f8b602cb10159246a016-Abstract-Datasets_and_Benchmarks.html) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/9cb2a7495900f8b602cb10159246a016-Abstract-Datasets_and_Benchmarks.html` · cited by 1: LJ
  - summary: ToolQA tests genuine tool-use reasoning (not memorization) by minimizing overlap with pretraining data and providing 13 specialized external-knowledge tools, exposing specific gaps in existing tool-augmented LLMs on hallucination and numerical reasoning.

- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) · 2023-02
  - `arxiv:2302.04761` · cited by 1: ZJ
  - summary: Self-supervised API-call insertion; showed tool use can be learned from a handful of demos.

- [ART: Automatic multi-step reasoning and tool-use for large language models](https://arxiv.org/abs/2303.09014) · 2023-03
  - `arxiv:2303.09014` · cited by 1: ZJ
  - summary: Retrieves reasoning-program demonstrations from a task library.

- [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) · 2023-03
  - `arxiv:2303.17580` · cited by 1: ZJ
  - summary: LLM as controller routing subtasks to specialist models.

- [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381) · 2023-03
  - `arxiv:2303.11381` · cited by 1: ZJ
  - summary: Prompting for multimodal reasoning and action.

- [outlines](https://github.com/dottxt-ai/outlines) · 2023-03
  - `gh:dottxt-ai/outlines` · cited by 1: HE
  - summary: Constrains sampling by regex/CFG/JSON Schema at the decoding layer.

- [TaskMatrix.AI: Completing Tasks by Connecting Foundation Models with Millions of APIs](https://arxiv.org/abs/2303.16434) · 2023-03
  - `arxiv:2303.16434` · cited by 1: ZJ
  - summary: Connecting foundation models to millions of APIs.

- [Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671) · 2023-03
  - `arxiv:2303.04671` · cited by 1: ZJ
  - summary: Wires ChatGPT up to a set of vision models (Stable Diffusion, ViT, etc.) via a prompt-based dispatcher so it can take and generate images and chain multi-step visual edits, not just text — an early, hacky but influential template for LLM-as-orchestrator-of-tools.

- [Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842) · 2023-04
  - `arxiv:2304.09842` · cited by 1: ZJ
  - summary: Plug-and-play compositional reasoning over heterogeneous modules.

- [ChemCrow: Augmenting large-language models with chemistry tools](https://arxiv.org/abs/2304.05376) · 2023-04
  - `arxiv:2304.05376` · cited by 2: LJ, ZJ
  - summary: 13 expert chemistry tools augmenting an LLM for synthesis planning.

- [ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models](https://arxiv.org/abs/2305.14323) · 2023-05
  - `arxiv:2305.14323` · cited by 1: ZJ
  - summary: Reframes chain-of-thought tool use as a multi-turn chat rather than a single long prompt, letting a chat LLM alternate between reasoning and tool calls turn-by-turn and picking up 7.9% over the prior best on MATH and HotpotQA.

- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/pdf/2305.11738.pdf) · 2023-05
  - `arxiv:2305.11738` · cited by 1: ZJ
  - related: <https://github.com/microsoft/ProphetNet/tree/master/CRITIC>
  - summary: Verify-then-correct using external tools rather than self-judgment alone.

- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) · 2023-05
  - `arxiv:2305.15334` · cited by 1: ZJ
  - summary: Retriever-aware training over a large API corpus; reduced hallucinated calls.

- [Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning](https://arxiv.org/abs/2305.14909) · 2023-05
  - `arxiv:2305.14909` · cited by 1: ZJ
  - summary: Has an LLM generate PDDL domain models instead of acting as the planner itself, so a proper symbolic planner does the actual search and guarantees plan correctness while the LLM just handles translating problems into and out of PDDL — the authors get it producing usable models for 40+ actions and solving 48 non-trivial household planning tasks.

- [Making Language Models Better Tool Learners with Execution Feedback](https://arxiv.org/abs/2305.13068) · 2023-05
  - `arxiv:2305.13068` · cited by 1: ZJ
  - summary: Trains models to call tools selectively rather than reflexively, using execution feedback from actual tool runs (TRICE) to teach them when a tool helps versus when it just adds failure modes on tasks the model could already solve alone.

- [On the Tool Manipulation Capability of Open-source Large Language Models](http://arxiv.org/abs/2305.16504) · 2023-05
  - `arxiv:2305.16504` · cited by 1: LJ
  - summary: Boosts open-source LLMs' tool-manipulation ability via curated training examples, in-context demonstration retrievers, and generation-style regulation, closing most of the gap to GPT-4 on a new benchmark (ToolBench) with about one developer-day of data curation per tool.

- [Data-Copilot: Bridging Billions of Data and Humans with Autonomous Workflow](https://arxiv.org/abs/2306.07209) · 2023-06
  - `arxiv:2306.07209` · cited by 1: ZJ
  - summary: Autonomous workflow bridging large data sources and humans.

- [ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](http://arxiv.org/abs/2306.05301) · 2023-06
  - `arxiv:2306.05301` · cited by 1: LJ
  - summary: Auto-generates a 3,938-instance tool-use corpus from a multi-agent simulation covering 400+ real APIs, then fine-tunes 7B/13B models to reach generalized tool-use ability on unseen tools comparable to GPT-3.5, without needing GPT-4-scale models.

- [GEAR: Augmenting Language Models with Generalizable and Efficient Tool Resolution](https://arxiv.org/pdf/2307.08775) · 2023-07
  - `arxiv:2307.08775` · cited by 2: LJ, ZJ
  - summary: Generalizable, efficient tool resolution decoupled from the main model.

- [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](http://arxiv.org/abs/2307.16789) · 2023-07
  - `arxiv:2307.16789` · cited by 2: LJ, ZJ
  - summary: Large-scale API corpus plus a DFS-based decision strategy for tool selection.

- [Gentopia: A Collaborative Platform for Tool-Augmented LLMs](https://arxiv.org/abs/2308.04030) · 2023-08
  - `arxiv:2308.04030` · cited by 1: ZJ
  - summary: Collaborative platform for tool-augmented agents.

- [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) · 2023-09
  - `arxiv:2309.17452` · cited by 1: ZJ
  - related: <https://github.com/microsoft/ToRA>
  - summary: Tool-integrated reasoning for mathematical problem solving.

- [Symbol-LLM: Towards Foundational Symbol-centric Interface For Large Language Models](https://arxiv.org/abs/2311.09278) · 2023-11
  - `arxiv:2311.09278` · cited by 1: ZJ
  - summary: Symbol-centric interface as a foundation for tool interaction.

- [CLOVA: A Closed-LOop Visual Assistant with Tool Usage and Update](https://arxiv.org/abs/2312.10908) · 2023-12
  - `arxiv:2312.10908` · cited by 1: ZJ
  - summary: Closed-loop visual assistant that updates its tools from feedback.

- [GitAgent: Facilitating Autonomous Agent with GitHub by Tool Extension](https://arxiv.org/pdf/2312.17294.pdf) · 2023-12
  - `arxiv:2312.17294` · cited by 1: ZJ
  - summary: Autonomously extends its own toolset from GitHub repositories.

- [Gorilla: Large Language Model Connected with Massive APIs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e4c61f578ff07830f5c37378dd3ecb0d-Abstract-Conference.html) · 2024
  - `url:https://proceedings.neurips.cc/paper_files/paper/2024/hash/e4c61f578ff07830f5c37378dd3ecb0d-Abstract-Conference.html` · cited by 1: LJ
  - summary: Gorilla is a fine-tuned LLaMA model trained with Retriever-Aware Training that beats GPT-4 at writing correct API calls and adapts to documentation changes at test time via a paired retriever, substantially reducing hallucinated API usage.

- [LLMs in the Imaginarium: Tool Learning through Simulated Trial and Error](https://aclanthology.org/2024.acl-long.570/) · 2024
  - `acl:2024.acl-long.570` · cited by 1: LJ
  - summary: Biologically inspired trial, imagination and memory loop.

- [Making Language Models Better Tool Learners with Execution Feedback](https://aclanthology.org/2024.naacl-long.195/) · 2024
  - `acl:2024.naacl-long.195` · cited by 1: LJ
  - summary: Learns *when* to use a tool from execution outcomes, not just how.

- [Skills-in-Context: Unlocking Compositionality in Large Language Models](https://aclanthology.org/2024.findings-emnlp.812/) · 2024
  - `acl:2024.findings-emnlp.812` · cited by 1: LJ
  - summary: Unlocks compositional generalization by putting basic skills in the prompt.

- [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](http://arxiv.org/abs/2401.06201) · 2024-01
  - `arxiv:2401.06201` · cited by 2: LJ, ZJ
  - summary: Compresses verbose tool docs into concise instructions.

- [Composio](https://github.com/ComposioHQ/composio) · 2024-02
  - `gh:composiohq/composio` · cited by 1: HE
  - summary: 250+ SaaS APIs as agent-ready actions with managed OAuth.

- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) · 2024-02
  - `arxiv:2402.01030` · cited by 1: LJ
  - summary: CodeAct has LLM agents emit executable Python instead of JSON or text actions and run it through a real interpreter to react to feedback, beating traditional action formats by up to 20% across 17 models, with an open dataset (CodeActInstruct) that fine-tunes Llama2/Mistral into agents that can debug themselves without losing general ability.

- [ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph](http://arxiv.org/abs/2403.00839) · 2024-03
  - `arxiv:2403.00839` · cited by 1: LJ
  - summary: Organizes thousands of tools as a graph the model traverses.

- [Agentic Skill Discovery](https://arxiv.org/abs/2405.15019) · 2024-05
  - `arxiv:2405.15019` · cited by 1: ZJ
  - related: <https://github.com/xf-zhao/Agentic-Skill-Discovery>
  - summary: Bootstraps a robot's skill library from nothing by having an LLM propose tasks from a scene description, spin up RL runs with LLM-authored reward functions, and have a vision-language model check whether the resulting behavior actually worked — no hand-designed skill list required.

- [Chain of Tools: Large Language Model is an Automatic Multi-tool Learner](http://arxiv.org/abs/2405.16533) · 2024-05
  - `arxiv:2405.16533` · cited by 1: LJ
  - summary: Black-box probing so the model learns unfamiliar tools without demos.

- [Tulip Agent -- Enabling LLM-Based Agents to Solve Tasks Using Large Tool Libraries](https://arxiv.org/abs/2407.21778) · 2024-07
  - `arxiv:2407.21778` · cited by 1: ZJ
  - summary: Solves tasks against tool libraries too large to fit in context.

- [Re-Invoke: Tool Invocation Rewriting for Zero-Shot Tool Retrieval](http://arxiv.org/abs/2408.01875) · 2024-08
  - `arxiv:2408.01875` · cited by 1: LJ
  - summary: Unsupervised retrieval via query synthesis and multi-view ranking.

- [OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs](https://arxiv.org/abs/2409.05152) · 2024-09
  - `arxiv:2409.05152` · cited by 1: ZJ
  - summary: One-pass unified generation and retrieval.

- [ToolPlanner: A Tool Augmented LLM for Multi Granularity Instructions with Path Planning and Feedback](http://arxiv.org/abs/2409.14826) · 2024-09
  - `arxiv:2409.14826` · cited by 1: LJ
  - summary: Path planning plus feedback over multi-granularity instructions.

- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) · 2024-10
  - `gh:modelcontextprotocol/inspector` · cited by 1: HE
  - summary: Interactive debugging UI for MCP servers without wiring a full agent.

- [ToolGen: Unified Tool Retrieval and Calling via Generation](http://arxiv.org/abs/2410.03439) · 2024-10
  - `arxiv:2410.03439` · cited by 1: LJ
  - summary: Bakes tools into the vocabulary as tokens, making retrieval a generation step.

- [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) · 2024-11
  - `gh:appcypher/awesome-mcp-servers` · cited by 1: HE
  - summary: A curated directory of production and experimental MCP servers spanning file access, databases, APIs, and communication platforms, useful as a lookup when wiring an agent to a new external system.

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · 2024-11
  - `gh:modelcontextprotocol/servers` · cited by 1: HE
  - summary: Official reference server implementations; the structural baseline.

- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) · 2024-12
  - `gh:lastmile-ai/mcp-agent` · cited by 1: HE
  - summary: Composable workflows, observability and provider-agnostic routing over MCP.

- [ToolCoder: A Systematic Code-Empowered Tool Learning Framework for Large Language Models](http://arxiv.org/abs/2502.11404) · 2025-02
  - `arxiv:2502.11404` · cited by 1: LJ
  - summary: Recasts tool learning as code generation with reusable Python scaffolds.

- [A2A Protocol](https://github.com/a2aproject/A2A) · 2025-03
  - `gh:a2aproject/a2a` · cited by 1: HE
  - summary: Agent-to-agent JSON-RPC with Agent Card discovery and task/message/artifact model.

- [agentgateway](https://github.com/agentgateway/agentgateway) · 2025-03
  - `gh:agentgateway/agentgateway` · cited by 1: HE
  - summary: Unifies LLM, MCP and A2A gateways into one control plane.

- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 2025-03
  - `gh:microsoft/playwright-mcp` · cited by 1: HE
  - summary: Browser automation via accessibility tree rather than screenshots.

- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) · 2025-05
  - `gh:ag-ui-protocol/ag-ui` · cited by 1: HE
  - summary: Event protocol for agent-to-frontend streaming, tool rendering and HITL interrupts.

- [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255) · 2025-05
  - `arxiv:2505.19255` · cited by 1: LJ
  - summary: Trains VLMs for multimodal thought chains with visual tools in the RL loop.

- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) · 2025-09
  - `gh:chromedevtools/chrome-devtools-mcp` · cited by 1: HE
  - summary: Exposes network, profiling, console and Lighthouse as structured tools.

- [superpowers](https://github.com/obra/superpowers) · 2025-10
  - `gh:obra/superpowers` · cited by 1: HE
  - summary: Cross-harness skills packaging TDD, subagent development and review gates.

- [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) · 2025-11
  - `url:https://anthropic.com/engineering/code-execution-with-mcp` · cited by 1: HE
  - summary: Have agents write code against MCP servers rather than calling tools directly; up to 98.7% token cut.

- [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) · 2025-11
  - `url:https://modelcontextprotocol.io/specification/2025-11-25/basic/transports` · cited by 1: HE
  - summary: Remote MCP deployment; session headers fight horizontal scaling.

- [SkillNet & SkillsBench: Infrastructure for AI Agent Skills at Scale](https://github.com/skillmatic-ai/awesome-agent-skills) · 2025-12
  - `gh:skillmatic-ai/awesome-agent-skills` · cited by 1: HE
  - summary: Skill creation/evaluation infrastructure with an 86-task, 11-domain benchmark.

- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/pdf/2601.10338v1) · 2026-01
  - `arxiv:2601.10338` · cited by 1: VA
  - summary: The first large-scale security study of agent 'skills' (42,447 collected, 31,132 analyzed) finds 26.1% contain a vulnerability across prompt injection, data exfiltration, privilege escalation, and supply-chain risk, and that skills bundling executable scripts are 2.12x more likely to be vulnerable than instruction-only ones.

- [agent-device](https://github.com/callstackincubator/agent-device) · 2026-01
  - `gh:callstackincubator/agent-device` · cited by 1: HE
  - summary: MCP-native iOS/Android control with semantic targeting and replayable workflows.

- [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills) · 2026-01
  - `gh:sickn33/antigravity-awesome-skills` · cited by 1: HE
  - summary: 1,400+ installable skills with npm installer and role bundles.

- [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](https://arxiv.org/pdf/2601.10955v1) · 2026-01
  - `arxiv:2601.10955` · cited by 1: VA
  - summary: A stealthy multi-turn denial-of-service attack at the MCP tool layer that edits only text-visible fields to steer agents into verbose tool-calling chains, pushing per-query cost up to 658x and GPU cache occupancy to 35-74% while evading standard prompt filters and output monitors.

- [Beyond Rule-Based Workflows: An Information-Flow-Orchestrated Multi-Agents Paradigm via A2A Communication from CORAL](https://arxiv.org/pdf/2601.09883v1) · 2026-01
  - `arxiv:2601.09883` · cited by 1: VA
  - summary: Replaces predefined multi-agent workflow rules with an orchestrator that monitors task progress and routes agents dynamically via natural-language A2A communication, beating a workflow-based baseline 63.64% vs 55.15% on GAIA at comparable token cost.

- [Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning](https://arxiv.org/pdf/2601.07782v1) · 2026-01
  - `arxiv:2601.07782` · cited by 1: VA
  - summary: Models tool retrieval as iterative query planning instead of single-shot dense matching, decomposing a request into sub-tasks and generating targeted queries per sub-task, trained via RL with verifiable rewards for state-of-the-art zero-shot retrieval generalization.

- [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification](https://arxiv.org/pdf/2601.17549v1) · 2026-01
  - `arxiv:2601.17549` · cited by 1: VA
  - summary: The first formal security analysis of the MCP specification itself, finding architectural vulnerabilities (no capability attestation, unauthenticated bidirectional sampling, implicit multi-server trust) that raise attack success 23-41% over non-MCP integrations, then proposes a backward-compatible extension cutting attack success from 52.8% to 12.4% at 8.3ms overhead.

- [CUA-Skill: Develop Skills for Computer Using Agent](https://arxiv.org/pdf/2601.21123v2) · 2026-01
  - `arxiv:2601.21123` · cited by 1: VA
  - summary: A large skill library encoding how humans operate Windows applications as parameterized, composable execution graphs, giving a computer-using agent reusable skills plus memory-aware failure recovery for state-of-the-art 57.5% success on WindowsAgentArena.

- [DALIA: Towards a Declarative Agentic Layer for Intelligent Agents in MCP-Based Server Ecosystems](https://arxiv.org/pdf/2601.17435v1) · 2026-01
  - `arxiv:2601.17435` · cited by 1: VA
  - summary: A declarative architectural layer that formalizes capabilities, exposes tasks via discovery protocol, and builds deterministic task graphs grounded only in declared operations, aiming to fix hallucinated actions and brittle coordination that stem from missing structure rather than model limits.

- [Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration](https://arxiv.org/pdf/2601.11595v2) · 2026-01
  - `arxiv:2601.11595` · cited by 1: VA
  - summary: Adds a shared context store to MCP so otherwise-stateless servers can read and write shared memory instead of routing everything back through the LLM, cutting redundant LLM calls and response failures on TravelPlanner and REALM-Bench.

- [ET-Agent: Incentivizing Effective Tool-Integrated Reasoning Agent via Behavior Calibration](https://arxiv.org/pdf/2601.06860v2) · 2026-01
  - `arxiv:2601.06860` · cited by 1: VA
  - summary: Trains a tool-integrated reasoning agent to fix its own behavior patterns (redundant or insufficient tool calls) via a self-evolving data flywheel plus two-phase behavior-calibration training, rather than optimizing only for answer accuracy.

- [From Self-Evolving Synthetic Data to Verifiable-Reward RL: Post-Training Multi-turn Interactive Tool-Using Agents](https://arxiv.org/pdf/2601.22607v2) · 2026-01
  - `arxiv:2601.22607` · cited by 1: VA
  - summary: A hierarchical multi-agent engine that synthesizes tool-grounded multi-turn dialogues with executable per-instance checkers, then post-trains on that data with verifier-based RL, matching or beating frontier models on tau^2-bench (73.0% Airline, 98.3% Telecom).

- [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/pdf/2601.05214v1) · 2026-01
  - `arxiv:2601.05214` · cited by 1: VA
  - summary: Detects wrong-tool, wrong-parameter and bypass errors from a single forward pass.

- [MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP](https://arxiv.org/pdf/2601.07395v1) · 2026-01
  - `arxiv:2601.07395` · cited by 1: VA
  - summary: An automated black-box optimization framework that plants malicious instructions in tool metadata (not the tool itself) to trick an MCP agent into misusing a legitimate high-privilege tool, reaching 84.2% attack success while keeping malicious-tool detection under 0.3%.

- [MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools](https://arxiv.org/pdf/2601.01241v1) · 2026-01
  - `arxiv:2601.01241` · cited by 1: VA
  - summary: An audit framework that runs MCP tools under WebAssembly sandboxing or unmodified over stdio to trace source-to-sink data flows, recovering security-sensitive capability declarations for 886 of 1,127 profiled tools across 71 real repositories.

- [Microsoft Skills Framework](https://github.com/microsoft/skills) · 2026-01
  - `gh:microsoft/skills` · cited by 1: HE
  - summary: Defining, versioning and distributing skills across platforms.

- [Optimizing Agentic Workflows using Meta-tools](https://arxiv.org/pdf/2601.22037v2) · 2026-01
  - `arxiv:2601.22037` · cited by 1: VA
  - summary: AWO mines an agent's own execution traces for repeated tool-call sequences and compiles them into single deterministic 'meta-tools,' cutting LLM calls by up to 11.9% and lifting task success by up to 4.2 points.

- [SAGE: Tool-Augmented LLM Task Solving Strategies in Scalable Multi-Agent Environments](https://arxiv.org/pdf/2601.09750v1) · 2026-01
  - `arxiv:2601.09750` · cited by 1: VA
  - summary: A conversational tool-use interface built on the OPACA framework for dynamic tool discovery and integration, letting new domain-specific tools be added without retraining and comparing several agentic prompting strategies for selecting and executing them.

- [SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/pdf/2601.03555v1) · 2026-01
  - `arxiv:2601.03555` · cited by 1: VA
  - summary: Grounds reward modeling in a curated library of skill prototypes rather than open-ended LLM judging, cutting reward-signal noise in multi-step tool use and lifting a small model's AIME25 accuracy from 43.3% to 63.3%.

- [Think-Augmented Function Calling: Improving LLM Parameter Accuracy Through Embedded Reasoning](https://arxiv.org/pdf/2601.18282v2) · 2026-01
  - `arxiv:2601.18282` · cited by 1: VA
  - summary: Adds a universal 'think' parameter to function-calling schemas so a model can articulate its reasoning before filling in complex, interdependent arguments, improving parameter accuracy with no architecture changes and full API compatibility.

- [ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/pdf/2601.08276v1) · 2026-01
  - `arxiv:2601.08276` · cited by 1: VA
  - summary: Trains a lightweight, history-aware router that generalizes from MCP tool selection to the broader Agent Web, scaling to massive candidate-tool spaces and multi-agent collaboration with minimal adaptation.

- [ToolGym: an Open-world Tool-using Environment for Scalable Agent Testing and Data Curation](https://arxiv.org/pdf/2601.06328v1) · 2026-01
  - `arxiv:2601.06328` · cited by 1: VA
  - summary: 5,571 tools across 204 apps with injected failures for robustness testing.

- [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/pdf/2601.08012v1) · 2026-01
  - `arxiv:2601.08012` · cited by 1: VA
  - summary: Applies System-Theoretic Process Analysis to derive formal safety specifications for agent tool sequences, then enforces them via an MCP extension requiring structured capability, confidentiality, and trust labels, moving tool safety from ad hoc reliability fixes to a designed guarantee.

- [When Agents Fail to Act: A Diagnostic Framework for Tool Invocation Reliability in Multi-Agent LLM Systems](https://arxiv.org/pdf/2601.16280v1) · 2026-01
  - `arxiv:2601.16280` · cited by 1: VA
  - summary: 12-category error taxonomy for multi-agent tool-use failures.

- [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](https://arxiv.org/pdf/2601.04748v2) · 2026-01
  - `arxiv:2601.04748` · cited by 1: VA
  - summary: Scaling limits and phase transitions in skill selection as libraries grow.

- [XGrammar 2: Dynamic and Efficient Structured Generation Engine for Agentic LLMs](https://arxiv.org/pdf/2601.04426v1) · 2026-01
  - `arxiv:2601.04426` · cited by 1: VA
  - summary: XGrammar-2 speeds up structured generation for agent workloads that switch output structure mid-request, using tag-triggered dispatch and cross-request grammar caching to compile over 6x faster than prior structured-generation engines with near-zero serving overhead.

- [Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study](https://arxiv.org/pdf/2602.06547v1) · 2026-02
  - `arxiv:2602.06547` · cited by 1: VA
  - summary: A security study of 98,380 agent skills finds 157 deliberately malicious ones spanning 632 vulnerabilities, dominated by credential theft via remote code execution and adversarial instructions hidden in documentation, over half traced to one threat actor impersonating brands at scale.

- [Scaling Parallel Tool Calling for Efficient Deep Research](https://arxiv.org/abs/2602.07359) · 2026-02
  - `arxiv:2602.07359` · cited by 1: HE
  - summary: Concurrent execution as the main latency lever in multi-step research.

- [SMCP: Secure Model Context Protocol](https://arxiv.org/pdf/2602.01129v1) · 2026-02
  - `arxiv:2602.01129` · cited by 1: VA
  - summary: Extends MCP with unified identity management, mutual authentication, security-context propagation, and audit logging to close the unauthorized-access, tool-poisoning, and privilege-escalation gaps the base protocol leaves open.

- [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/pdf/2602.02548v1) · 2026-02
  - `arxiv:2602.02548` · cited by 1: VA
  - summary: Represents GUI operations as a sequence of learnable tool-token embeddings instead of raw coordinates, using semantic anchoring and a curriculum to reach performance competitive with a 235B model using under 1% of its training data.

- [vurb.ts](https://github.com/vinkius-labs/vurb.ts) · 2026-02
  - `gh:vinkius-labs/vurb.ts` · cited by 1: HE
  - summary: TypeScript framework for *authoring* MCP servers with PII redaction and state-gated visibility.

- [What's New with GitHub Copilot Coding Agent](https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent/) · 2026-02
  - `url:https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent` · cited by 1: HE
  - summary: `.github/agents/` files, self-review and security scanning as harness primitives.

- [AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness](https://arxiv.org/abs/2603.03329) · 2026-03
  - `arxiv:2603.03329` · cited by 1: HE
  - summary: Synthesizes runtime constraint guards from tool schemas; smaller model beats larger.

- [AWS Bedrock AgentCore with WebRTC Support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-webrtc/) · 2026-03
  - `url:https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-webrtc` · cited by 1: HE
  - summary: P2P UDP streaming for sub-800ms voice turn-around.

- [CLI-Anything](https://github.com/HKUDS/CLI-Anything) · 2026-03
  - `gh:hkuds/cli-anything` · cited by 1: HE
  - summary: Generates agent-native CLIs for software never designed for automation.

- [Design Patterns for Deploying AI Agents with Model Context Protocol](https://arxiv.org/abs/2603.13417) · 2026-03
  - `arxiv:2603.13417` · cited by 1: HE
  - summary: Three protocol gaps that break production: identity, tool budgeting, error semantics.

- [Developer's Guide to AI Agent Protocols](https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/) · 2026-03
  - `url:https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols` · cited by 1: HE
  - summary: Maps six interop protocols (MCP, A2A, UCP, AP2, A2UI, AG-UI) to boundary problems.

- [Google Developers: Closing the Knowledge Gap with Agent Skills](https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/) · 2026-03
  - `url:https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills` · cited by 1: HE
  - summary: ADK skills with a 117-prompt evaluation harness.

- [SkillTester: Benchmarking Utility and Security of Agent Skills](https://arxiv.org/abs/2603.28815) · 2026-03
  - `arxiv:2603.28815` · cited by 1: HE
  - summary: Evaluates skills on capability, robustness and security before deployment.

- [The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) · 2026-03
  - `url:https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap` · cited by 1: HE
  - summary: Scaling transport, `.well-known` discovery, Tasks primitive, enterprise extensions.

- [Tool Annotations as Risk Vocabulary](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/) · 2026-03
  - `url:https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations` · cited by 1: HE
  - summary: Four annotation hints as permission inputs; the "lethal trifecta" framing.

- [TopoCurate: Modeling Interaction Topology for Tool-Use Agent Training](https://arxiv.org/abs/2603.01714) · 2026-03
  - `arxiv:2603.01714` · cited by 1: HE
  - summary: Learns topological priors over tool chaining, not just individual calls.

- [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) · 2026-04
  - `gh:aws/agent-toolkit-for-aws` · cited by 1: HE
  - summary: Official AWS MCP servers, skills and plugins for provisioning and querying resources.

- [agentic-stack](https://github.com/codejunkie99/agentic-stack) · 2026-04
  - `gh:codejunkie99/agentic-stack` · cited by 1: HE
  - summary: Portable `.agent/` folder with adapters, addressing harness vendor lock-in.

- [Corpus2Skill: Don't Retrieve, Navigate — Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/pdf/2604.14572) · 2026-04
  - `arxiv:2604.14572` · cited by 1: VA
  - summary: Compiles a corpus into a navigable skill tree, replacing retrieval with traversal.

- [Dataverse Skills: Your Coding Agent Now Speaks Dataverse](https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse) · 2026-04
  - `url:https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse` · cited by 1: HE
  - summary: Domain skills as curated execution strategies across MCP, SDK and raw API.

- [EigentSearch-Q+](https://arxiv.org/abs/2604.07927) · 2026-04
  - `arxiv:2604.07927` · cited by 1: HE
  - summary: Dedicated reasoning tools that externalize intermediate decisions as typed arguments.

- [tui-use](https://github.com/onesuper/tui-use) · 2026-04
  - `gh:onesuper/tui-use` · cited by 1: HE
  - summary: Programmable interaction with REPLs, debuggers and ncurses apps.

- [SkillOpt](https://github.com/microsoft/SkillOpt) · 2026-05
  - `gh:microsoft/skillopt` · cited by 1: HE
  - summary: Treats skills as optimizable parameters improved by trajectory feedback.

- [You can't whisper at an AI agent](https://stripe.dev/blog/ai-steering-experiments) · 2026-05
  - `url:https://stripe.dev/blog/ai-steering-experiments` · cited by 1: HE
  - summary: Stripe's steering experiments find 'hard' constraints (errors, explicit blocking instructions) reliably redirect agent tool use while 'soft' cues (warnings, hints) get ignored, because agents pursue a narrow goal-directed path rather than exploring context the way a human developer would.

- [zerolang](https://github.com/vercel-labs/zerolang) · 2026-05
  - `gh:vercel-labs/zerolang` · cited by 1: HE
  - summary: Agents edit code through a compiler-derived ProgramGraph instead of text patches.

- [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781) · 2026-06
  - `arxiv:2606.04781` · cited by 1: HE
  - summary: Compiles skills to typed execution graphs; pass rate 53%→67% and skills become auditable.

- [Announcing the Agentic Resource Discovery specification](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/) · 2026-06
  - `url:https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification` · cited by 1: HE
  - summary: Runtime discovery of MCP servers and A2A agents via domain catalogs and trust manifests.

- [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/pdf/2606.00135) · 2026-06
  - `arxiv:2606.00135` · cited by 1: VA
  - summary: Shows tool-calling benchmark results are highly sensitive to undocumented implementation choices (seed, system prompt, multi-turn template), making leaderboard rankings unreliable without standardization, then introduces two RL efficiency fixes that cut wasted rollouts and update cost.

- [Ponytail](https://github.com/DietrichGebert/ponytail) · 2026-06
  - `gh:dietrichgebert/ponytail` · cited by 1: HE
  - summary: A skill system enforcing a 'laziness ladder' that checks whether code needs to exist or can be reused before an agent writes anything new, cutting code output ~54% and cost ~20% while keeping safety guardrails.

- [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) · 2026-07
  - `url:https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate` · cited by 1: HE
  - summary: The MCP spec's 2026-07-28 release candidate moves to a stateless core that scales over ordinary HTTP and adds extensions for server-rendered UIs (MCP Apps) and long-running work (Tasks).

## Tools & Undated

14 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Announcing Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)
  - `url:https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services` · cited by 1: HE
  - summary: Managed MCP endpoints with IAM, audit logging and discovery as platform primitives.

- [BMTools](https://github.com/OpenBMB/BMTools)
  - `gh:openbmb/bmtools` · cited by 1: ZJ
  - summary: An open-source toolkit for building and chaining ChatGPT-plugin-style tools, letting a model call external APIs (search, weather, code execution, etc.) through a common plugin interface.

- [Function Calling — OpenAI Docs](https://platform.openai.com/docs/guides/function-calling)
  - `url:https://platform.openai.com/docs/guides/function-calling` · cited by 1: HE
  - summary: The de facto JSON Schema conventions and parallel calling.

- [Hermes Agent: Unified Streaming for Real-Time Agent Workflows](https://juliangoldie.com/hermes-agent-unified-streaming/)
  - `url:https://juliangoldie.com/hermes-agent-unified-streaming` · cited by 1: HE
  - summary: Token-by-token streaming for sub-second reactive decision loops.

- [instructor](https://python.useinstructor.com/)
  - `url:https://python.useinstructor.com/` · cited by 1: HE
  - summary: Pydantic models for structured extraction with retry and validation feedback.

- [joinly](https://github.com/joinly-ai/joinly)
  - `gh:joinly-ai/joinly` · cited by 1: KY
  - summary: Drops an MCP-speaking agent into a live Zoom/Meet/Teams call so it can listen, transcribe, and act on meeting content in real time instead of summarizing a recording after the fact.

- [LLama Cpp Agent](https://github.com/Maximilian-Winter/llama-cpp-agent)
  - `gh:maximilian-winter/llama-cpp-agent` · cited by 1: KY
  - summary: Wrapper around llama.cpp that gets structured function calls and JSON output working even from local models that were never fine-tuned for tool use, including parallel calls.

- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
  - `url:https://modelcontextprotocol.io/introduction` · cited by 1: HE
  - summary: Open protocol standardizing agent access to tools, data and services.

- [Pilot Protocol](https://github.com/TeoSlayer/pilotprotocol)
  - `gh:teoslayer/pilotprotocol` · cited by 1: KY
  - summary: Peer-to-peer overlay network for agents — permanent addresses, NAT traversal through a rendezvous service, and AES-256-GCM-encrypted UDP tunnels for direct agent-to-agent traffic — built so no central platform sits in the data path between two agents talking to each other.

- [RestGPT](https://github.com/Yifan-Song793/RestGPT)
  - `gh:yifan-song793/restgpt` · cited by 1: KY
  - summary: Agent that plans and executes multi-step tasks by calling real-world RESTful APIs directly, instead of relying on a fixed toolset wrapped as functions.

- [Shell + Skills + Compaction: Tips for Long-Running Agents](https://developers.openai.com/blog/skills-shell-tips)
  - `url:https://developers.openai.com/blog/skills-shell-tips` · cited by 1: HE
  - summary: Versioned skill bundles; negative examples raised routing accuracy 73%→85%.

- [Tool Use — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
  - `url:https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview` · cited by 1: HE
  - summary: Client vs server execution models and strict schema enforcement.

- [WorkGPT](https://github.com/team-openpm/workgpt)
  - `gh:team-openpm/workgpt` · cited by 1: ZJ
  - summary: Small TypeScript library that hands GPT-4 a directive plus an array of OpenAPI-described APIs and lets it converse back and forth until the task is done, leaning on the OpenPM registry for ready-made API wrappers.

- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-effective-tools-for-agents)
  - `url:https://anthropic.com/engineering/writing-effective-tools-for-agents` · cited by 1: HE
  - summary: Tool design as agent UX: naming, schemas, error surfaces, return conventions.
