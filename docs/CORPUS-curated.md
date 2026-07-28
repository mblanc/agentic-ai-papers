# Canonical agentic-AI corpus

Deduplicated and classified across the seven seed lists. Summaries are written
from scratch, not carried over from the source lists.

**Provenance codes** — `HE` ai-boost/awesome-harness-engineering · `KY`
kyrolabs/awesome-agents · `XI` WooooDyy/LLM-Agent-Paper-List · `BK`
arvindcr4/awesome-agents (Berkeley MOOC) · `VA` VoltAgent/awesome-ai-agent-papers ·
`ZJ` zjunlp/LLMAgentPapers · `LJ` luo-junyu/Awesome-Agent-Papers

## Coverage

All seven lists read. Still partial within two of them: the tail of `HE` (task
runners onward) and two of `VA`'s five sections (Agent Tooling 95, Security 82) —
though `LJ` and `ZJ` now fill much of that security gap independently. Every entry
below is something I saw directly, with the URL as it appeared.

## What deduplication actually revealed

The lists do not form one corpus, but they do form a **chain**, and reading the
last two corrected my earlier read of it.

| source | span | role |
| --- | --- | --- |
| `XI` | 2022 – mid-2024 | origin points, frozen |
| `LJ` | 2019 – 2025 | broadest span; **the only source with venue metadata** |
| `ZJ` | 2022 – mid-2026 | bridge across every generation |
| `BK` | 2024 – 2025 | curriculum ordering |
| `VA` | **2026 only** | live arXiv edge, weekly |
| `HE` | 2026 | engineering practice, vendor-heavy |
| `KY` | 2023 – 2026 | tools only, no papers |

**Correction to my first read.** I initially concluded that cross-list agreement
was useless as a quality signal because the generations don't overlap. That holds
for `VA` ∩ `XI` — empty by construction, since `VA` admits only papers from
January 2026 onward. But `ZJ` and `LJ` are connective tissue: `ZJ` carries 2026
entries (CORAL `2604.01658`, ClawBench `2604.08523`, AutoNumerics `2602.17607`)
that also appear in `VA`, while reaching back to 2022 alongside `XI`. So
agreement *is* usable — just along the chain rather than across the whole set.

**A better quality signal exists, and only one source has it.** `LJ` tags every
entry with its venue — ICLR, NeurIPS, ICML, ACL, TMLR, Nature, CVPR. For the
pre-2026 corpus that is strictly more informative than counting how many lists
cite something, because it is peer review rather than curator overlap. Where an
entry below carries `LJ`, venue data is available in the source; the pipeline
should extract it into a field of its own.

---

# 0. The classical canon

Papers that appear across multiple pre-2026 lists. These are the origin points —
worth a wiki page each, and they are what the 2026 work assumes you know.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — Interleaves reasoning traces with actions in a Thought/Action/Observation loop; the structure nearly every agent harness still uses. `HE` `XI` `BK`
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — Agent critiques its own failed attempt in natural language and retries, turning failure into a text-based learning signal. `XI`
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — Explores multiple reasoning branches with lookahead and backtracking instead of committing to one chain. `XI`
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — Showed that prompting for intermediate steps unlocks multi-step reasoning at scale. `XI`
- [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) — Samples many reasoning paths and takes the majority answer; cheap and durable accuracy win. `XI`
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — 25 agents in a sandbox town with memory-stream, reflection and planning; the reference design for believable agent behaviour. `XI`
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — Lifelong Minecraft agent that writes and stores executable skills, building a reusable skill library. `XI` `KY` `BK`
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — Treats context as paged memory with an OS metaphor; the origin of tiered agent memory. `XI` `KY` `HE`
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — Self-supervised API-call insertion; showed tool use can be learned from a handful of demos. `XI`
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — Same model generates, critiques and revises its own output in a loop. `XI`
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — Conversable agents as the primitive; multi-agent systems as structured dialogue. `XI` `BK` `KY`
- [MetaGPT: Meta Programming for Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — Encodes SOPs as agent roles so a one-line requirement yields PRD, design, tasks and code. `XI` `KY`
- [CAMEL: Communicative Agents for "Mind" Exploration](https://arxiv.org/abs/2303.17760) — Role-playing pair (user/assistant) driven by inception prompting to generate cooperative task-solving data. `XI`
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — Argued the *interface* the agent sees matters as much as the model; the ACI concept. `BK` `KY` `HE`
- [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741) — Open platform where agents get a sandboxed shell, browser and editor. `BK` `KY` `HE`
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — Self-hosted realistic websites with functional-correctness grading rather than string match. `XI` `BK`
- [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) — Broad-coverage web-action dataset spanning many real sites and domains. `XI` `BK`
- [WebShop: Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) — Simulated e-commerce site with instruction-following and reward; early practical web-agent benchmark. `XI` `BK`
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — Real OS environments across Ubuntu/Windows/macOS with executable task validation. `XI` `BK`
- [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — Eight distinct environments; documented the open-vs-commercial agentic gap. `XI`
- [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) — Browsing agent trained by imitation then preference optimization; the ancestor of deep research. `XI`
- [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends](https://arxiv.org/abs/2303.17580) — LLM as controller routing subtasks to specialist models. `XI`
- [ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789) — Large-scale API corpus plus a DFS-based decision strategy for tool selection. `XI`
- [Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354) — The framing survey for tool learning as its own research programme. `XI`
- [LATS: Language Agent Tree Search](https://arxiv.org/abs/2310.04406) — MCTS over agent trajectories with environment feedback as the search signal. `HE` `XI`
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) — SayCan: scores LLM proposals against learned skill value functions so plans stay physically feasible. `XI`
- [DSPy: programming — not prompting — foundation models](https://github.com/stanfordnlp/dspy) — Declarative modules with compiled/optimized prompts; treats the pipeline as the thing you tune. `KY` `BK`
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — Preference learning without a separate reward model; now the default alignment recipe. `BK`

---

# 1. Harness engineering

The discipline itself: the scaffolding around the model. Almost entirely `HE`,
almost entirely 2026 — this category barely existed in the older lists.

- [Harness Engineering](https://openai.com/index/harness-engineering/) — OpenAI's framing of harness design as a named discipline for agent-first development. `HE`
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic on composing simple primitives, and when a workflow beats an agent. `HE`
- [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) — Martin Fowler's synthesis: context curation, architectural constraints, entropy management, humans *on* the loop. `HE`
- [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) — Böckeler's feedforward-guides / feedback-sensors model; separates computational from inferential controls. `HE`
- [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) — Five composing primitives: filesystem, code execution, sandbox, memory, context management. `HE`
- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Multi-session harness design; every component encodes an assumption that will expire. `HE`
- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Initializer-then-worker handoff so progress survives across context windows. `HE`
- [What makes a harness a harness](https://arxiv.org/abs/2606.10106) — Constitutive definition via four necessary elements; applied as an inclusion test to real harnesses. `HE`
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071) — Empirical study of 70 public agent systems across five recurring design dimensions. `HE`
- [Code as Agent Harness](https://arxiv.org/abs/2605.18747) — Survey arguing code is the substrate unifying harness interface, mechanism and multi-agent scaling. `HE`
- [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723) — Externalizes control logic as portable natural-language artifacts run by a shared runtime. `HE`
- [Harness Engineering: Build Reliable AI Agents by Engineering the System](https://www.deepset.ai/blog/harness-engineering) — Failure-classification framework mapping each failure mode to a harness component. `HE`
- [Harness Engineering: Structured Workflows for AI-Assisted Development](https://developers.redhat.com/articles/2026/04/07/harness-engineering-structured-workflows-ai-assisted-development) — Red Hat's enterprise four-pillar model: vibes, specs, skills, agents. `HE`
- [2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf?hsLang=en) — Finds harness configuration alone can swing benchmarks by 5+ points. `HE`
- [Building AI Coding Agents for the Terminal](https://arxiv.org/abs/2603.05344) — Practitioner paper on eager-construction scaffolding and compound multi-model architecture. `HE`
- [RUCAIBox/awesome-agent-harness](https://github.com/RUCAIBox/awesome-agent-harness) — Academic survey and 500+ reference reading list on harness engineering. `HE`
- [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) — Orchestration patterns and layered guardrails distilled for production. `HE`
- [What is an AI Agent?](https://www.ibm.com/think/topics/ai-agents) — Definitional anchor; useful for the wiki's entry page. `HE`

## Agent loop

- [Unrolling the Codex Agent Loop](https://openai.com/index/unrolling-the-codex-agent-loop/) — Step-by-step decomposition of one loop iteration and where each component plugs in. `HE`
- [Unlocking the Codex Harness: How We Built the App Server](https://openai.com/index/unlocking-the-codex-harness/) — The Item/Turn/Thread protocol, and why MCP's tool-oriented model was insufficient. `HE`
- [LangGraph — Low Level Concepts](https://langchain-ai.github.io/langgraph/concepts/low_level/) — Models the loop as a typed-state graph with conditional edges and checkpointing. `HE`
- [Improving Deep Agents with Harness Engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) — Harness-only changes moved a coding agent from rank 30 to top 5 on Terminal Bench 2.0. `HE`
- [How Middleware Lets You Customize Your Agent Harness](https://blog.langchain.com/how-middleware-lets-you-customize-your-agent-harness/) — Six composable hooks for cross-cutting concerns without touching agent logic. `HE`
- [Hooks – Codex](https://developers.openai.com/codex/hooks) — Lifecycle hooks for injecting deterministic scripts at loop events. `HE`
- [Extended Thinking — Claude API Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) — Reasoning-budget control; thinking blocks must survive tool-result round-trips. `HE`
- [The Design Space of Today's and Future AI Agent Systems](https://arxiv.org/abs/2604.14228) — Reverse-engineers a production agent's five-stage progressive compaction and hook pipeline. `HE`
- [A Scheduler-Theoretic Framework for LLM Agent Execution](https://arxiv.org/abs/2604.11378) — Surveys 70 projects; 60% use the plain agent loop, and maps the alternatives' trade-offs. `HE`
- [The Coding Harness Behind GitHub Copilot in VS Code](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode) — Three loop responsibilities, multi-provider routing, PR-gated eval suite. `HE`
- [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) — Plan lives in executable JavaScript that fans out to hundreds of parallel subagents. `HE`
- [Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics](https://arxiv.org/abs/2603.01209) — Mismatching runtime persistence to training-time semantics costs either correctness or 3.5× tokens. `HE`
- [Life-Harness](https://github.com/Tianshi-Xu/Life-Harness) — Lifecycle-aware runtime layer; gains transfer across 18 model backbones. `HE`
- [statewright](https://github.com/statewright/statewright) — State-machine guardrails restricting tool availability per phase; shrinking tool space fixed local-model failures. `HE`
- [AgentSPEX](https://github.com/ScaleML/AgentSPEX) — Declarative YAML spec language for agent workflows with sandbox, checkpointing and trajectory logs. `HE`
- [Confucius Code Agent](https://github.com/facebookresearch/cca-swebench) — Production coding agent organized around Agent/User/Developer experience; 59% Resolve@1 on SWE-Bench-Pro. `HE`
- [deepclaude](https://github.com/aattaran/deepclaude) — Ports a full agent loop to other backends, isolating loop architecture from model identity. `HE`
- [Real-Time Deadlines Reveal Temporal Awareness Failures](https://arxiv.org/abs/2601.13206) — Temporal awareness is orthogonal to reasoning; deadlines must be injected into context. `HE`

---

# 2. Context engineering

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Treats the whole context state as a finite curated resource, not prompt wording. `HE`
- [Compaction — Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/compaction) — Server-side summarization of older context; 84% token reduction on a 100-turn eval. `HE`
- [Prompt Caching — Claude API Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — Cache-breakpoint placement as the main cost lever in multi-turn sessions. `HE`
- [Autonomous Context Compression](https://blog.langchain.com/autonomous-context-compression/) — Moves compression from threshold-triggered to agent-triggered, avoiding mid-subtask corruption. `HE`
- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190) — A "Focus Agent" decides when to consolidate and prune; 22.7% token cut, no accuracy loss. `HE` `VA`
- [Context Engineering for Reliable AI Agents: Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/) — Replacing 100+ bespoke tools with a filesystem raised "Intent Met" from 45% to 75%. `HE`
- [Claude Code Compaction: How Context Compression Works](https://okhlopkov.com/claude-code-compaction-explained/) — What survives compaction and what silently doesn't; keep critical rules in the system prompt. `HE`
- [Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning](https://arxiv.org/abs/2605.15315) — Splits relevance into semantic evidence and dependency support instead of one score. `HE`
- [ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](https://arxiv.org/abs/2604.01599) — Model learns to weight information importance across hierarchy levels. `HE`
- [A-RAG: Scaling Agentic RAG via Hierarchical Retrieval Interfaces](https://arxiv.org/abs/2602.03442) — Reframes retrieval as tool calls in the loop rather than pipeline-time injection. `HE`
- [Making Agent-Friendly Pages with Content Negotiation](https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation) — Serve `text/markdown` to agents so boilerplate never enters context. `HE`
- [LLMLingua](https://github.com/microsoft/LLMLingua) — Prompt compression up to 20×; v2 adds 3–6× speedup for latency-sensitive loops. `HE`
- [Token Savior](https://github.com/Mibayy/token-savior) — Symbol-level codebase index so agents navigate by pointer; 77% fewer active tokens. `HE`
- [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — Tree-sitter AST knowledge graph over 66 languages, replacing grep/read cycles. `HE`
- [MinishLab/semble](https://github.com/MinishLab/semble) — Natural-language code search replacing grep+read; ~98% token cut, CPU-only. `HE`
- [headroom](https://github.com/chopratejas/headroom) — Compresses tool outputs, logs and RAG chunks before they hit context; 60–95% reduction. `HE`
- [context-mode](https://github.com/mksglu/context-mode) — Sandboxes bulky tool output outside the window, retrieving fragments via BM25. `HE`
- [dirac](https://github.com/dirac-run/dirac) — Hash-anchored edits and AST manipulation for surgical context curation; 50–80% cost cut. `HE`
- [OpenViking](https://github.com/volcengine/OpenViking) — Context database unifying memory, resources and skills behind a filesystem paradigm. `HE`
- [Mirage](https://github.com/strukto-ai/mirage) — Mounts S3, Slack, Gmail, GitHub and Redis as one virtual filesystem so agents use bash. `HE`
- [Trellis](https://github.com/mindfold-ai/Trellis) — Progressive spec loading to replace monolithic CLAUDE.md, with cross-platform adapters. `HE`
- [harness-experimental](https://github.com/hoangnb24/harness-experimental) — Turns a repo into an agent-ready workspace via structured AGENTS/HARNESS/FEATURE_INTAKE files. `HE`
- [Context7](https://github.com/upstash/context7) — Injects version-specific library docs to stop hallucinated APIs from stale training data. `HE`
- [DESIGN.md](https://github.com/google-labs-code/design.md) — Machine-readable design tokens plus prose rationale so agents respect a design system. `HE`
- [LLM Readiness Harness: Evaluation, Observability, and CI Gates](https://arxiv.org/abs/2603.27355) — Deployment-blocking eval gates and CI patterns for LLM/RAG apps. `HE`
- [Structure and Diversity Aware Context Bubble Construction](https://arxiv.org/abs/2601.10681) — Balances relevance, coverage and redundancy under strict token budgets. `VA`

---

# 3. Memory

- [Letta (MemGPT)](https://github.com/letta-ai/letta) — Reference stateful-agent architecture with core/archival/recall tiers. `HE` `KY`
- [mem0](https://github.com/mem0ai/mem0) — Drop-in universal memory layer; lowest-integration path to cross-session retention. `HE`
- [Zep](https://github.com/getzep/zep) — Agent memory store with automatic summarization, entity extraction and semantic session search. `HE`
- [Stash](https://github.com/alash3al/stash) — Self-hosted memory with an 8-stage consolidation pipeline; single Docker Compose. `HE`
- [TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) — Four-tier local pipeline; 61% token cut and 51% relative pass-rate gain on long-horizon tasks. `HE`
- [engram](https://github.com/Gentleman-Programming/engram) — Single Go binary, SQLite+FTS5, 18 MCP tools for save/search/session lifecycle. `HE`
- [Hindsight](https://github.com/vectorize-io/hindsight) — Self-hostable long-term memory with LangChain/CrewAI/LlamaIndex/MCP integrations. `KY`
- [Cortex Memory](https://github.com/sopaco/cortex-mem) — Extraction, vector search and automated optimization with REST/MCP/CLI and dashboard. `KY`
- [Statewave](https://github.com/smaramwbc/statewave) — Memory runtime turning events into structured memories with consolidation and supersession. `KY`
- [MemClaw](https://github.com/caura-ai/caura-memclaw) — Governed shared memory for agent fleets with permissions and audit trails. `KY`
- [SAGE](https://github.com/l33tdawg/sage) — Institutional memory where each write passes BFT consensus before commit. `KY`
- [piia-engram](https://github.com/Patdolitse/piia-engram) — Local-first cross-tool memory for any MCP-compatible client. `KY`
- [Screenpipe](https://github.com/screenpipe/screenpipe) — Continuous local screen/mic capture with OCR and semantic search as agent context. `KY`
- [Rethinking Memory Mechanisms of Foundation Agents: A Survey](https://arxiv.org/abs/2602.06052) — Organizes memory by substrate, cognitive mechanism and subject. Best 2026 entry point. `VA`
- [The AI Hippocampus: How Far are We From Human Memory?](https://arxiv.org/abs/2601.09113) — Surveys implicit, explicit and agentic memory paradigms including cross-modal. `VA`
- [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2602.05665) — Extraction, storage, retrieval and temporal evolution of graph memory. `VA`
- [Continuum Memory Architectures for Long-Horizon LLM Agents](https://arxiv.org/abs/2601.09913) — Defines persistent temporally-chained state as a class distinct from stateless RAG. `VA`
- [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/abs/2601.08323) — Decomposes memory into CRUD ops and learns the policy via SFT+RL. `VA`
- [FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory](https://arxiv.org/abs/2601.18642) — Adaptive exponential decay with LLM-guided conflict resolution. `VA`
- [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) — Semantic lossless compression, online synthesis, intent-aware retrieval planning. `VA`
- [SwiftMem: Fast Agentic Memory via Query-aware Indexing](https://arxiv.org/abs/2601.08160) — Sub-linear retrieval via temporal/semantic DAG-Tag indexing. `VA`
- [MAGMA: A Multi-Graph based Agentic Memory Architecture](https://arxiv.org/abs/2601.03236) — Orthogonal semantic, temporal, causal and entity graphs with policy-guided traversal. `VA`
- [E-mem: Multi-agent Episodic Context Reconstruction](https://arxiv.org/abs/2601.21714) — Keeps uncompressed contexts in assistants, replacing destructive compression with reconstruction. `VA`
- [Amory: Coherent Narrative-Driven Agent Memory](https://arxiv.org/abs/2601.06282) — Builds episodic narratives from fragments and semanticizes peripheral facts offline. `VA`
- [Membox: Weaving Topic Continuity into Long-Range Memory](https://arxiv.org/abs/2601.03785) — Topic Loom groups same-topic turns into boxes linked by event timelines. `VA`
- [Beyond Dialogue Time: Temporal Semantic Memory](https://arxiv.org/abs/2601.07468) — Organizes by actual occurrence time rather than dialogue order. `VA`
- [HiMeS: Hippocampus-inspired Memory System](https://arxiv.org/abs/2601.06152) — RL-trained short-term extraction fused with partitioned long-term memory. `VA`
- [ProcMEM: Reusable Procedural Memory via Non-Parametric PPO](https://arxiv.org/abs/2602.01869) — Saves step-by-step procedural skills for reuse without retraining. `VA`
- [Learning How to Remember: Meta-Cognitive Memory Management](https://arxiv.org/abs/2601.07470) — Trains a memory copilot via DPO to decide how memories get structured. `VA`
- [Grounding Agent Memory in Contextual Intent](https://arxiv.org/abs/2601.10702) — Indexes trajectory steps by intent cues to cut interference in long-horizon tasks. `VA`
- [BudgetMem: Query-Aware Budget-Tier Routing](https://arxiv.org/abs/2602.06025) — Routes memory queries to processing tiers by difficulty for runtime cost control. `VA`
- [ShardMemo: Masked MoE Routing for Sharded Memory](https://arxiv.org/abs/2601.21545) — Probes only eligible memory shards under a fixed budget. `VA`
- [AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/abs/2601.20352) — Hierarchical granularity with adaptive routing and consistency verification. `VA`
- [Learning to Share: Selective Memory for Parallel Agentic Systems](https://arxiv.org/abs/2602.05965) — Learned controller decides what passes between parallel agent teams. `VA`
- [Beyond Static Summarization: Proactive Memory Extraction](https://arxiv.org/abs/2601.04463) — Self-questioning loops recover information one-off summarization drops. `VA`
- [Controllable Memory Usage in Long-Term Human-Agent Interaction](https://arxiv.org/abs/2601.05107) — Models memory reliance as an explicit user-steerable dimension. `VA`
- [MemCtrl: MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) — Trainable gate decides which observations to retain, update or discard. `VA`
- [HippoRAG: Neurobiologically Inspired Long-Term Memory](https://arxiv.org/abs/2405.14831) — Hippocampal-indexing analogy for single-step multi-hop retrieval. `BK`
- [MemoryBank: Enhancing LLMs with Long-Term Memory](https://arxiv.org/abs/2305.10250) — Ebbinghaus-inspired forgetting curve over stored conversation memory. `XI`
- [ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory](https://arxiv.org/abs/2306.03901) — SQL database as symbolic memory with explicit read/write chains. `XI`
- [Walking Down the Memory Maze](https://arxiv.org/abs/2310.05029) — Interactive tree-structured reading to exceed the context limit. `XI`
- [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) — Extracts cross-task insights from past trajectories without gradient updates. `XI`

---

# 4. Tool use and protocols

- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-effective-tools-for-agents) — Tool design as agent UX: naming, schemas, error surfaces, return conventions. `HE`
- [Tool Use — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) — Client vs server execution models and strict schema enforcement. `HE`
- [Function Calling — OpenAI Docs](https://platform.openai.com/docs/guides/function-calling) — The de facto JSON Schema conventions and parallel calling. `HE`
- [Model Context Protocol](https://modelcontextprotocol.io/introduction) — Open protocol standardizing agent access to tools, data and services. `HE`
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Official reference server implementations; the structural baseline. `HE`
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — Interactive debugging UI for MCP servers without wiring a full agent. `HE`
- [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) — Remote MCP deployment; session headers fight horizontal scaling. `HE`
- [The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — Scaling transport, `.well-known` discovery, Tasks primitive, enterprise extensions. `HE`
- [Tool Annotations as Risk Vocabulary](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/) — Four annotation hints as permission inputs; the "lethal trifecta" framing. `HE`
- [Design Patterns for Deploying AI Agents with MCP](https://arxiv.org/abs/2603.13417) — Three protocol gaps that break production: identity, tool budgeting, error semantics. `HE`
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Have agents write code against MCP servers rather than calling tools directly; up to 98.7% token cut. `HE`
- [A2A Protocol](https://github.com/a2aproject/A2A) — Agent-to-agent JSON-RPC with Agent Card discovery and task/message/artifact model. `HE`
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) — Event protocol for agent-to-frontend streaming, tool rendering and HITL interrupts. `HE`
- [Developer's Guide to AI Agent Protocols](https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/) — Maps six interop protocols (MCP, A2A, UCP, AP2, A2UI, AG-UI) to boundary problems. `HE`
- [Agentic Resource Discovery specification](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/) — Runtime discovery of MCP servers and A2A agents via domain catalogs and trust manifests. `HE`
- [agentgateway](https://github.com/agentgateway/agentgateway) — Unifies LLM, MCP and A2A gateways into one control plane. `HE`
- [Shell + Skills + Compaction: Tips for Long-Running Agents](https://developers.openai.com/blog/skills-shell-tips) — Versioned skill bundles; negative examples raised routing accuracy 73%→85%. `HE`
- [Microsoft Skills Framework](https://github.com/microsoft/skills) — Defining, versioning and distributing skills across platforms. `HE`
- [SkillOpt](https://github.com/microsoft/SkillOpt) — Treats skills as optimizable parameters improved by trajectory feedback. `HE`
- [superpowers](https://github.com/obra/superpowers) — Cross-harness skills packaging TDD, subagent development and review gates. `HE`
- [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills) — 1,400+ installable skills with npm installer and role bundles. `HE`
- [SkillNet & SkillsBench](https://github.com/skillmatic-ai/awesome-agent-skills) — Skill creation/evaluation infrastructure with an 86-task, 11-domain benchmark. `HE`
- [SkillTester: Benchmarking Utility and Security of Agent Skills](https://arxiv.org/abs/2603.28815) — Evaluates skills on capability, robustness and security before deployment. `HE`
- [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781) — Compiles skills to typed execution graphs; pass rate 53%→67% and skills become auditable. `HE`
- [AutoHarness: Automatically Synthesizing a Code Harness](https://arxiv.org/abs/2603.03329) — Synthesizes runtime constraint guards from tool schemas; smaller model beats larger. `HE`
- [outlines](https://github.com/dottxt-ai/outlines) — Constrains sampling by regex/CFG/JSON Schema at the decoding layer. `HE`
- [instructor](https://python.useinstructor.com/) — Pydantic models for structured extraction with retry and validation feedback. `HE`
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — Browser automation via accessibility tree rather than screenshots. `HE`
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Exposes network, profiling, console and Lighthouse as structured tools. `HE`
- [Composio](https://github.com/ComposioHQ/composio) — 250+ SaaS APIs as agent-ready actions with managed OAuth. `HE`
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) — Composable workflows, observability and provider-agnostic routing over MCP. `HE`
- [vurb.ts](https://github.com/vinkius-labs/vurb.ts) — TypeScript framework for *authoring* MCP servers with PII redaction and state-gated visibility. `HE`
- [CLI-Anything](https://github.com/HKUDS/CLI-Anything) — Generates agent-native CLIs for software never designed for automation. `HE`
- [tui-use](https://github.com/onesuper/tui-use) — Programmable interaction with REPLs, debuggers and ncurses apps. `HE`
- [zerolang](https://github.com/vercel-labs/zerolang) — Agents edit code through a compiler-derived ProgramGraph instead of text patches. `HE`
- [agent-device](https://github.com/callstackincubator/agent-device) — MCP-native iOS/Android control with semantic targeting and replayable workflows. `HE`
- [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) — Official AWS MCP servers, skills and plugins for provisioning and querying resources. `HE`
- [Official MCP Support for Google Services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) — Managed MCP endpoints with IAM, audit logging and discovery as platform primitives. `HE`
- [agentic-stack](https://github.com/codejunkie99/agentic-stack) — Portable `.agent/` folder with adapters, addressing harness vendor lock-in. `HE`
- [Scaling Parallel Tool Calling for Efficient Deep Research](https://arxiv.org/abs/2602.07359) — Concurrent execution as the main latency lever in multi-step research. `HE`
- [TopoCurate: Modeling Interaction Topology for Tool-Use Agent Training](https://arxiv.org/abs/2603.01714) — Learns topological priors over tool chaining, not just individual calls. `HE`
- [EigentSearch-Q+](https://arxiv.org/abs/2604.07927) — Dedicated reasoning tools that externalize intermediate decisions as typed arguments. `HE`
- [Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126) — Closed loop where the model creates its own reusable tools. `XI`
- [CREATOR: Disentangling Abstract and Concrete Reasonings through Tool Creation](https://arxiv.org/abs/2305.14318) — Separates tool creation from tool use via documentation and code realization. `XI`
- [Augmented Language Models: a Survey](https://openreview.net/forum?id=jh7wH2AzKK) — Survey of reasoning, tools and actions as LM augmentations. `XI`
- [TALM: Tool Augmented Language Models](https://arxiv.org/abs/2205.12255) — Combines non-differentiable tools with LMs for real-time/private data. `XI`
- [MRKL Systems](https://arxiv.org/abs/2205.00445) — Early modular neuro-symbolic architecture combining LLM, knowledge and discrete reasoning. `XI`
- [When Agents Fail to Act: Tool Invocation Reliability](https://arxiv.org/abs/2601.16280) — 12-category error taxonomy for multi-agent tool-use failures. `VA`
- [Internal Representations as Indicators of Hallucinations in Tool Selection](https://arxiv.org/abs/2601.05214) — Detects wrong-tool, wrong-parameter and bypass errors from a single forward pass. `VA`
- [ToolGym](https://arxiv.org/abs/2601.06328) — 5,571 tools across 204 apps with injected failures for robustness testing. `VA`
- [Arabic Prompts with English Tools: A Benchmark](https://arxiv.org/abs/2601.05101) — First tool-calling benchmark for Arabic agentic workflows. `VA`
- [Corpus2Skill: Don't Retrieve, Navigate](https://arxiv.org/abs/2604.14572) — Compiles a corpus into a navigable skill tree, replacing retrieval with traversal. `VA`

## Scaling to large tool libraries (from `LJ`, `ZJ`)

The problem this cluster addresses — thousands of tools, only a few relevant —
is the same one MCP servers hit in production, but it was studied first here.

- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) — Retriever-aware training over a large API corpus; reduced hallucinated calls. `ZJ`
- [ToolGen: Unified Tool Retrieval and Calling via Generation](http://arxiv.org/abs/2410.03439) — Bakes tools into the vocabulary as tokens, making retrieval a generation step. `LJ`
- [ToolNet: Connecting LLMs with Massive Tools via Tool Graph](http://arxiv.org/abs/2403.00839) — Organizes thousands of tools as a graph the model traverses. `LJ`
- [Re-Invoke: Tool Invocation Rewriting for Zero-Shot Tool Retrieval](http://arxiv.org/abs/2408.01875) — Unsupervised retrieval via query synthesis and multi-view ranking. `LJ`
- [Chain of Tools / Automatic Tool Chain](http://arxiv.org/abs/2405.16533) — Black-box probing so the model learns unfamiliar tools without demos. `LJ`
- [ToolPlanner](http://arxiv.org/abs/2409.14826) — Path planning plus feedback over multi-granularity instructions. `LJ`
- [ToolCoder](http://arxiv.org/abs/2502.11404) — Recasts tool learning as code generation with reusable Python scaffolds. `LJ`
- [EASYTOOL](https://arxiv.org/abs/2401.06201) — Compresses verbose tool docs into concise instructions. `LJ` `ZJ`
- [TRICE / Making LMs Better Tool Learners with Execution Feedback](https://aclanthology.org/2024.naacl-long.195/) — Learns *when* to use a tool from execution outcomes, not just how. `LJ` `ZJ`
- [LLMs in the Imaginarium: Tool Learning through Simulated Trial and Error](https://aclanthology.org/2024.acl-long.570/) — Biologically inspired trial, imagination and memory loop. `LJ`
- [Tulip Agent](https://arxiv.org/abs/2407.21778) — Solves tasks against tool libraries too large to fit in context. `ZJ`
- [GEAR](https://arxiv.org/abs/2307.08775) — Generalizable, efficient tool resolution decoupled from the main model. `ZJ`
- [Chameleon](https://arxiv.org/abs/2304.09842) — Plug-and-play compositional reasoning over heterogeneous modules. `ZJ`
- [ART: Automatic multi-step reasoning and tool-use](https://arxiv.org/abs/2303.09014) — Retrieves reasoning-program demonstrations from a task library. `ZJ`
- [TaskMatrix.AI](https://arxiv.org/abs/2303.16434) — Connecting foundation models to millions of APIs. `ZJ`
- [MM-REACT](https://arxiv.org/abs/2303.11381) — Prompting for multimodal reasoning and action. `ZJ`
- [ToolkenGPT](https://arxiv.org/abs/2305.11554) — Tools as learned embeddings ("toolkens") on a frozen model. `ZJ`
- [Symbol-LLM](https://arxiv.org/abs/2311.09278) — Symbol-centric interface as a foundation for tool interaction. `ZJ`
- [GitAgent](https://arxiv.org/pdf/2312.17294.pdf) — Autonomously extends its own toolset from GitHub repositories. `ZJ`
- [CLOVA](https://arxiv.org/abs/2312.10908) — Closed-loop visual assistant that updates its tools from feedback. `ZJ`
- [Data-Copilot](https://arxiv.org/abs/2306.07209) — Autonomous workflow bridging large data sources and humans. `ZJ`
- [Gentopia](https://arxiv.org/abs/2308.04030) — Collaborative platform for tool-augmented agents. `ZJ`
- [VTool-R1](https://arxiv.org/abs/2505.19255) — Trains VLMs for multimodal thought chains with visual tools in the RL loop. `LJ`
- [Skills-in-Context](https://aclanthology.org/2024.findings-emnlp.812/) — Unlocks compositional generalization by putting basic skills in the prompt. `LJ`
- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) — CodeAct: Python as the unified action space. A load-bearing result for code-as-action designs. `LJ`
- [Chain of Code](https://arxiv.org/abs/2312.04474) — Interleaves real execution with an LM emulating unrunnable code. `ZJ`
- [ToRA](https://arxiv.org/abs/2309.17452) — Tool-integrated reasoning for mathematical problem solving. `ZJ`
- [LLM With Tools: A Survey](http://arxiv.org/abs/2409.18807) — Standardized integration paradigm plus the tool-creation direction. `LJ`
- [A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736) — Classification of agent protocols predating the MCP/A2A consolidation. `LJ`
- [OneGen](https://arxiv.org/abs/2409.05152) — One-pass unified generation and retrieval. `ZJ`

## Key surveys and architecture references

- [Cognitive Architectures for Language Agents (CoALA)](https://arxiv.org/abs/2309.02427) — Modular memory, action space and decision procedure. The most useful organizing framework in the pre-2026 literature. `ZJ` `LJ`
- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — Unified construction framework; the other canonical survey alongside `XI`'s. `ZJ` `LJ`
- [If LLM Is the Wizard, Then Code Is the Wand](https://arxiv.org/abs/2401.00812) — How code specifically empowers agent behaviour. `ZJ`
- [Personal LLM Agents](https://arxiv.org/pdf/2401.05459.pdf) — Capability, efficiency and security for personal agents as a software paradigm. `ZJ` `LJ`
- [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/pdf/2401.03568.pdf) — Multimodal interaction framing. `ZJ` `LJ` `XI`
- [The Landscape of Agentic Reinforcement Learning for LLMs](https://arxiv.org/abs/2509.02547) — Dual taxonomy of capabilities and applications, RL as the integrating mechanism. `ZJ` `LJ`
- [A Survey on Large Language Model based Human-Agent Systems](https://arxiv.org/abs/2505.00753) — The human-in-the-loop literature, surveyed. `ZJ`
- [A Survey on the Memory Mechanism of LLM based Agents](https://arxiv.org/abs/2404.13501) — Design and evaluation of agent memory. `ZJ` `LJ`
- [Understanding the planning of LLM agents: A survey](https://arxiv.org/abs/2402.02716) — First systematic taxonomy of agent planning. `LJ`
- [The Landscape of Emerging AI Agent Architectures](https://arxiv.org/abs/2404.11584) — Reasoning, planning and tool calling across real implementations. `LJ`
- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322) — Collaboration framework, applications and open challenges. `LJ`
- [Large Multimodal Agents: A Survey](https://arxiv.org/abs/2402.15116) — The closest thing in the corpus to multimodal agent coverage. `LJ`
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — MAST failure taxonomy with an LLM-judge pipeline. Pairs directly with the 2026 harness failure work. `LJ`
- [Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime](https://www.preprints.org/manuscript/202603.1756/v2) — `ZJ`'s newest entry; independent 2026 formalization of the harness layer. `ZJ`
- [Interactive Natural Language Processing](https://arxiv.org/abs/2305.13246) — Early framing of interaction as the organizing principle. `ZJ`
- [Trust but Verify! A Survey on Verification Design for Test-time Scaling](https://arxiv.org/abs/2508.16665) — Unified view of verifier training. `LJ`
- [Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047) — How scientific agents differ from general ones. `LJ`

---

# 5. Planning and reasoning

- [Run Long-Horizon Tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex/) — Plan.md / Implement.md / Documentation.md as reusable harness artifacts. `HE`
- [Plan-and-Execute Agents](https://blog.langchain.com/plan-and-execute-agents/) — Separates one-shot planning from execution, replanning only when needed. `HE`
- [Plan-and-Act: Improving Planning for Long-Horizon Tasks](https://arxiv.org/abs/2503.09572) — Independent specialization of planner and executor; 57.58% WebArena-Lite, 81.36% WebVoyager. `HE`
- [microsoft/TaskWeaver](https://github.com/microsoft/TaskWeaver) — Code-first planner/executor split with plugins for domain knowledge. `HE` `KY`
- [Task-Decoupled Planning for Long-Horizon Agents](https://arxiv.org/abs/2601.07577) — Dependency-graph decomposition enabling localized replanning without cascade. `HE`
- [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625) — Decompose then solve sequentially, reusing earlier answers. `XI`
- [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) — RAP: repurposes the LLM as both world model and reasoning agent under MCTS. `XI`
- [LLM+P: Empowering LLMs with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477) — Translates to PDDL and delegates to a classical planner. `XI`
- [SwiftSage](https://arxiv.org/abs/2305.17390) — Fast intuitive module plus slow deliberate module for complex interactive tasks. `XI`
- [Describe, Explain, Plan and Select](https://arxiv.org/abs/2302.01560) — Interactive planning with goal selection for open-world multi-task agents. `XI`
- [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) — Closes the loop by feeding environment feedback back as language. `XI`
- [Chain-of-Verification Reduces Hallucination](https://arxiv.org/abs/2309.11495) — Drafts, plans verification questions, answers them independently, then revises. `HE` `BK`
- [SelfCheck: Zero-Shot Checking of Step-by-Step Reasoning](https://arxiv.org/abs/2308.00436) — Model checks its own reasoning steps without external supervision. `XI`
- [CRITIC: LLMs Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) — Verify-then-correct using external tools rather than self-judgment alone. `XI`
- [Agent-Pro: Learning to Evolve via Policy-Level Reflection](https://arxiv.org/abs/2402.17574) — Reflects at policy level rather than per-action. `XI`
- [Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives](https://arxiv.org/abs/2401.02009) — Contrasts divergent solution attempts to locate real errors. `XI`
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) — The "let's think step by step" result. `XI`
- [Selection-Inference](https://arxiv.org/abs/2205.09712) — Alternates selection and inference steps for interpretable logical reasoning. `XI`
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) — Intrinsic self-correction without external feedback often degrades accuracy. `BK`
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) — Model explains and repairs its own code from execution results. `BK`
- [Chain-of-Thought Reasoning Without Prompting](https://arxiv.org/abs/2402.10200) — Recovers CoT paths by decoding alternatives rather than prompting. `BK`
- [Premise Order Matters in Reasoning with LLMs](https://arxiv.org/abs/2402.08939) — Reordering premises alone changes accuracy substantially. `BK`
- [CoT Empowers Transformers to Solve Inherently Serial Problems](https://arxiv.org/abs/2402.12875) — Theoretical account of why intermediate tokens add expressive power. `BK`
- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) — OPRO: the model proposes successive solutions from an optimization trajectory. `BK`
- [Beyond A*: Better Planning with Transformers via Search Dynamics Bootstrapping](https://arxiv.org/abs/2402.14083) — Trains on search dynamics, not just solutions. `BK`
- [Dualformer: Controllable Fast and Slow Thinking](https://arxiv.org/abs/2410.09918) — Randomized reasoning traces yield a controllable fast/slow switch. `BK`
- [Tree Search for Language Model Agents](https://jykoh.com/search-agents) — Best-first tree search over real interactive web environments. `BK`
- [Is Your LLM Secretly a World Model of the Internet?](https://arxiv.org/abs/2411.06559) — Model-based planning with an LLM world model for web agents. `BK`
- [Grokked Transformers are Implicit Reasoners](https://arxiv.org/abs/2405.15071) — Implicit reasoning emerges past grokking, with sharp generalization limits. `BK`
- [Iterative Reasoning Preference Optimization](https://arxiv.org/abs/2404.19733) — Preference optimization over competing CoT candidates. `BK`
- [ROMA: Recursive Open Meta-Agent Framework](https://arxiv.org/abs/2602.01848) — Subtask trees running in parallel to exceed single-context limits. `VA`
- [LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents](https://arxiv.org/abs/2601.16649) — Oracle counterfactuals measuring which capability actually mattered. `VA`

---

# 6. Multi-agent

- [Choosing the Right Multi-Agent Architecture](https://blog.langchain.com/choosing-the-right-multi-agent-architecture/) — Four patterns with data: subagents process 67% fewer tokens than skills multi-domain. `HE`
- [Multi-Agent Workflows Often Fail. Here's How to Engineer Ones That Don't](https://github.blog/ai-and-ml/generative-ai/multi-agent-workflows-often-fail-heres-how-to-engineer-ones-that-dont/) — Treat handoffs as distributed-system interfaces with typed schemas. `HE`
- [Task-Adaptive Multi-Agent Orchestration (AdaptOrch)](https://arxiv.org/abs/2602.16873) — Selects topology from the task dependency graph; 12–23% over model selection. `HE`
- [Agyn: Multi-Agent System for Team-Based Autonomous Software Engineering](https://arxiv.org/abs/2602.01465) — Role-specialized agents with differing model sizes and tool access. `HE` `VA`
- [Agent Development Kit announcement](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) — Google's multi-agent topology, tool registration and eval pipeline rationale. `HE`
- [Multi-Agent Teams Hold Experts Back](https://arxiv.org/abs/2602.01011) — Self-organizing teams often underperform their single best member. `VA`
- [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](https://arxiv.org/abs/2601.04748) — Scaling limits and phase transitions in skill selection as libraries grow. `VA`
- [Phase Transition for Budgeted Multi-Agent Synergy](https://arxiv.org/abs/2601.17311) — Predicts when systems improve, saturate or collapse from context and error correlation. `VA`
- [Multi-Agent Constraint Factorization Reveals Latent Invariant Solution Structure](https://arxiv.org/abs/2601.15077) — Operator-theoretic account of why decomposition reaches solutions one agent can't. `VA`
- [The Orchestration of Multi-Agent Systems: Architectures, Protocols, Enterprise Adoption](https://arxiv.org/abs/2601.13671) — Unified framework integrating MCP for tools and A2A for peer coordination. `VA`
- [DyTopo: Dynamic Topology Routing via Semantic Matching](https://arxiv.org/abs/2602.06039) — Rewires agent connections each reasoning round instead of fixed topology. `VA`
- [TopoDIM: One-shot Topology Generation of Diverse Interaction Modes](https://arxiv.org/abs/2601.10120) — Decentralized agents construct heterogeneous topologies without iterative coordination. `VA`
- [CASTER: Context-Aware Strategy for Task Efficient Routing](https://arxiv.org/abs/2601.19793) — Lightweight router combining semantic embeddings with structural meta-features. `VA`
- [Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems](https://arxiv.org/abs/2601.10560) — Optimizes the critical path explicitly under parallel execution. `VA`
- [MonoScale: Scaling Multi-Agent System with Monotonic Improvement](https://arxiv.org/abs/2601.23219) — Grows agent pools with guaranteed non-decreasing performance per onboarding round. `VA`
- [ResMAS: Resilience Optimization in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2601.04694) — RL topology generation plus topology-aware prompt optimization under perturbation. `VA`
- [MAS-Orchestra](https://arxiv.org/abs/2601.14652) — Orchestration as function-calling RL, with MASBENCH for controlled evaluation. `VA`
- [CORAL: Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658) — Long-running self-evolving systems with shared memory; 3–10× over evolutionary search. `VA`
- [StackPlanner: Centralized Hierarchical MAS with Task-Experience Memory](https://arxiv.org/abs/2601.05890) — Decouples coordination from execution with RL-driven experience reuse. `VA`
- [CTHA: Constrained Temporal Hierarchical Architecture](https://arxiv.org/abs/2601.10738) — Typed message contracts and authority bounds across layers. `VA`
- [Scaling Multiagent Systems with Process Rewards](https://arxiv.org/abs/2601.23228) — Per-action process rewards for credit assignment when finetuning teams. `VA`
- [Demystifying Multi-Agent Debate: The Role of Confidence and Diversity](https://arxiv.org/abs/2601.19921) — Diversity-aware init and confidence-modulated updates improve debate. `VA`
- [DynaDebate: Breaking Homogeneity with Dynamic Path Generation](https://arxiv.org/abs/2601.05746) — Allocates diverse solution paths and uses a verifier to break deadlocks. `VA`
- [Dynamic Role Assignment for Multi-Agent Debate](https://arxiv.org/abs/2601.17152) — Meta-debate assigning roles by capability through proposal and peer review. `VA`
- [Epistemic Context Learning: Building Trust in Multi-Agent Systems](https://arxiv.org/abs/2601.21742) — Peer reliability profiles from interaction history. `VA`
- [Mixture-of-Models: N-Way Self-Evaluating Deliberation](https://arxiv.org/abs/2601.16863) — Expertise broker and quadratic voting lets small ensembles match frontier. `VA`
- [Do We Always Need Query-Level Workflows?](https://arxiv.org/abs/2601.11147) — Task-level workflow generation as a cheaper alternative to per-query. `VA`
- [Learning to Recommend Multi-Agent Subgraphs from Calling Trees](https://arxiv.org/abs/2601.22209) — Historical calling trees to select agents per subtask. `VA`
- [A Large-Scale Study on Development and Issues of Multi-Agent AI Systems](https://arxiv.org/abs/2601.07136) — 42K commits and 4.7K issues across eight frameworks. `VA`
- [Improving Factuality and Reasoning through Multiagent Debate](https://arxiv.org/abs/2305.14325) — The foundational debate result. `XI`
- [Encouraging Divergent Thinking through Multi-Agent Debate](https://arxiv.org/abs/2305.19118) — Debate as an antidote to degeneration-of-thought. `XI`
- [AgentVerse](https://arxiv.org/abs/2308.10848) — Dynamic team composition with emergent behaviour analysis. `XI` `KY`
- [ChatDev / Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) — Virtual software company staffed by role-playing agents. `XI`
- [AutoAgents: A Framework for Automatic Agent Generation](https://arxiv.org/abs/2309.17288) — Generates the agent roster for a task rather than fixing it upfront. `XI`
- [Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View](https://arxiv.org/abs/2310.02124) — Conformity and consensus dynamics in agent collaboration. `XI`
- [StateFlow: Enhancing LLM Task-Solving through State-Driven Workflows](https://arxiv.org/abs/2403.11322) — Models task solving as explicit state machine transitions. `BK`

---

# 7. Evaluation and benchmarks

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — What to measure and why unit-test-style evals fail for agents. `HE`
- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/pdf/2503.16416) — Broad survey of agent evaluation methodology. `BK`
- [Adding Error Bars to Evals](https://arxiv.org/pdf/2411.00640) — Statistical rigour for model evaluations; treat evals as measurement. `BK`
- [Terminal-Bench](https://arxiv.org/abs/2601.11868) — 89 hard terminal tasks with unique environments and human-written solutions. `VA`
- [τ2-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/pdf/2506.07982) — Both user and agent can act, exposing coordination failures. `BK`
- [ClawBench: Browser Agents on Live Production Websites](https://arxiv.org/abs/2604.08523) — 153 tasks on 144 live sites, intercepting only the final write; top model 33.3%. `VA`
- [APEX-Agents](https://arxiv.org/abs/2601.14242) — 480 long-horizon cross-application tasks authored by bankers, consultants and lawyers. `VA`
- [CooperBench: Why Coding Agents Cannot be Your Teammates Yet](https://arxiv.org/abs/2601.13295) — 600+ collaborative coding tasks under varied coordination structures. `VA`
- [DevOps-Gym](https://arxiv.org/abs/2601.20882) — 700+ tasks across build, monitoring, issue resolution and test generation. `VA`
- [The Hierarchy of Agentic Capabilities](https://arxiv.org/abs/2601.09032) — 150 workplace tasks yielding an empirical capability hierarchy. `VA`
- [Agent Benchmarks Fail Public Sector Requirements](https://arxiv.org/abs/2601.20617) — 1,300+ benchmarks assessed against process-based and realism requirements. `VA`
- [Toward Architecture-Aware Evaluation Metrics for LLM Agents](https://arxiv.org/abs/2601.19583) — Links planner, memory and router components to diagnostic metrics. `VA`
- [Agent-as-a-Judge](https://arxiv.org/abs/2601.05111) — Survey of the shift from LLM-judge to agentic judges with tools and memory. `VA`
- [JAF: Judge Agent Forest](https://arxiv.org/abs/2601.22269) — Judges across a cohort rather than per-instance, using in-context neighbourhoods. `VA`
- [Insider Knowledge: How Much Can RAG Systems Gain from Evaluation Secrets?](https://arxiv.org/abs/2601.13227) — Nugget-based judges are gameable to near-perfect scores. `VA`
- [Agentic Uncertainty Reveals Agentic Overconfidence](https://arxiv.org/abs/2602.06948) — Agents predict their own success rates poorly. `VA`
- [Agentic Confidence Calibration](https://arxiv.org/abs/2601.15778) — Holistic Trajectory Calibration using process-level features across the run. `VA`
- [What Do LLM Agents Know About Their World? Task2Quiz](https://arxiv.org/abs/2601.09503) — Task success is a weak proxy for environment understanding. `VA`
- [Active Evaluation of General Agents](https://arxiv.org/abs/2601.07651) — Chooses which task/agent to sample next to minimize ranking error. `VA`
- [AEMA: Verifiable Evaluation Framework](https://arxiv.org/abs/2601.11903) — Process-aware auditable multi-agent evaluation under human oversight. `VA`
- [Replayable Financial Agents: Determinism-Faithfulness Assurance Harness](https://arxiv.org/abs/2601.15322) — Measures trajectory determinism and evidence-conditioned faithfulness. `VA`
- [Automated Structural Testing of LLM-Based Agents](https://arxiv.org/abs/2601.18827) — OpenTelemetry traces, mocking and automated component assertions. `VA`
- [CAR-bench](https://arxiv.org/abs/2601.22027) — Consistency and limit-awareness under ambiguous multi-turn requests. `VA`
- [ATOD](https://arxiv.org/abs/2601.11854) — Agentic task-oriented dialogue across multi-goal coordination and proactivity. `VA`
- [Mem2ActBench](https://arxiv.org/abs/2601.19935) — Whether agents proactively *act* on long-term memory, not just retrieve. `VA`
- [RealMem](https://arxiv.org/abs/2601.06966) — 2,000+ cross-session dialogues tracking evolving goals. `VA`
- [ES-MemEval](https://arxiv.org/abs/2602.01885) — Personal-information retention across long emotional-support conversations. `VA`
- [IDRBench: Interactive Deep Research Benchmark](https://arxiv.org/abs/2601.06676) — Deep research with on-demand user interaction and cost-aware metrics. `VA`
- [ViDoRe V3](https://arxiv.org/abs/2601.08620) — Multimodal RAG over 26K pages, 3,099 queries, 6 languages. `VA`
- [MiRAGE](https://arxiv.org/abs/2601.15487) — Multi-agent generation of verified multimodal multi-hop QA for RAG eval. `VA`
- [Lost in the Noise: How Reasoning Models Fail with Contextual Distractors](https://arxiv.org/abs/2601.07226) — Robustness across 11 tasks against several noise types. `VA`
- [When Agents Fail: A Comprehensive Study of Bugs in LLM Agents](https://arxiv.org/abs/2601.15232) — 1,187 bug reports across seven frameworks, categorized. `VA`
- [Stalled, Biased, and Confused: Reasoning Failures in Cloud RCA](https://arxiv.org/abs/2601.22208) — 48,000 scenarios producing a 16-failure taxonomy under ReAct and Plan-and-Execute. `VA`
- [Capture the Flags: Family-Based Evaluation of Agentic LLMs](https://arxiv.org/abs/2602.05523) — Equivalent-challenge families to separate understanding from memorization. `VA`
- [AIRS-Bench](https://arxiv.org/abs/2602.06855) — 20 research tasks from real ML papers spanning ideation to refinement. `VA`
- [JADE: Expert-Grounded Dynamic Evaluation](https://arxiv.org/abs/2602.06486) — Decomposes responses into claims checked against expert knowledge. `VA`
- [PieArena](https://arxiv.org/abs/2602.05302) — Negotiation benchmark pitting agents against MBA students. `VA`
- [Benchmarking Agents in Insurance Underwriting Environments](https://arxiv.org/abs/2602.00456) — Multi-turn enterprise conditions with noisy tools and proprietary knowledge. `VA`
- [HumanStudy-Bench](https://arxiv.org/abs/2602.00685) — Replays published human-subject experiments with agents. `VA`
- [M3-BENCH](https://arxiv.org/abs/2601.08462) — Process-aware evaluation of social behaviour in mixed-motive games. `VA`
- [TowerMind](https://arxiv.org/abs/2601.05899) — Low-cost tower-defence environment with hallucination assessment. `VA`
- [MineNPC-Task](https://arxiv.org/abs/2601.05215) — Memory-aware Minecraft tasks with machine-checkable validators. `VA`
- [VirtualEnv](https://arxiv.org/abs/2601.07553) — Unreal Engine 5 platform for embodied navigation and manipulation benchmarks. `VA`
- [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) — Human-validated SWE-bench subset removing unsolvable tasks. `BK`
- [BrowseComp](https://openai.com/index/browsecomp/) — Hard-to-find-information benchmark for browsing agents. `BK`
- [VisualWebArena](https://jykoh.com/vwa) — Visually grounded web tasks requiring image understanding. `BK`
- [WorkArena](https://arxiv.org/abs/2403.07718) — Common knowledge-work tasks on a real enterprise platform. `BK`
- [WorkArena++](https://arxiv.org/abs/2407.05291) — Compositional planning and reasoning extension. `BK`
- [AGUVIS](https://arxiv.org/pdf/2412.04454) — Pure-vision unified GUI agents without accessibility-tree dependence. `BK`
- [MLAgentBench / Benchmarking LLMs As AI Research Agents](https://arxiv.org/abs/2310.03302) — Open-ended ML research tasks with free-form experimentation. `XI`
- [SmartPlay](https://arxiv.org/abs/2310.01557) — Six games isolating distinct agent capabilities. `XI`
- [MAgIC](https://arxiv.org/abs/2311.08562) — Cognition, adaptability, rationality and collaboration in multi-agent settings. `XI`
- [AgentSims](https://arxiv.org/abs/2308.04026) — Open-source sandbox town for task-based LLM evaluation. `XI`
- [ScienceWorld: Is your Agent Smarter than a 5th Grader?](https://arxiv.org/abs/2203.07540) — Interactive text environment requiring grounded science reasoning. `XI`
- [Arize-Phoenix](https://github.com/Arize-ai/phoenix) — Open-source agent tracing, evaluation and observability. `KY`
- [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) — Automated evaluation and evolution of agentic workflows. `KY`
- [Open-RAG-Eval](https://github.com/vectara/open-rag-eval) — RAG evaluation without golden answers. `KY`
- [Voice Lab](https://github.com/saharmor/voice-lab) — Voice-agent evaluation across models, prompts and personas. `KY`
- [agent-qa](https://github.com/vostride/agent-qa) — Self-improving QA harness with natural-language tests that adapt to UI change. `KY`

## Benchmarks from `LJ` and `ZJ` (venue-labelled in `LJ`)

- [TheAgentCompany](https://arxiv.org/pdf/2412.14161) — Simulates a whole software company; consequential long-horizon work tasks. `LJ`
- [MLE-Bench](https://openreview.net/pdf?id=6s5uXNWGIh) — ML engineering tasks from real competitions with baselines. `LJ`
- [DSBench](https://arxiv.org/abs/2409.07703) — How far data-science agents are from expert practice. `LJ`
- [MMAU](https://arxiv.org/pdf/2407.18961) — Five domains × five capabilities, built for interpretability of failures. `LJ`
- [CRAB](https://openreview.net/pdf?id=kyExS4V0H7) — Cross-environment benchmark with graph-based evaluation. `LJ`
- [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf) — Real queries, deployed tools, multimodal inputs. `LJ`
- [AppWorld](https://arxiv.org/abs/2407.18901) — Controllable world of apps and people for interactive coding agents. `LJ` `ZJ`
- [OmniACT](https://arxiv.org/pdf/2402.17553) — Desktop and web task automation dataset. `LJ`
- [macOSWorld](https://arxiv.org/abs/2506.04135) — First macOS GUI benchmark, multilingual, with a safety subset. `LJ`
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) — Broad-coverage multimodal frontier benchmark. `LJ`
- [MCPEval](https://arxiv.org/abs/2507.12806) — MCP-based automated deep evaluation of agent models. `LJ`
- [LiveMCP-101](https://arxiv.org/abs/2508.15760) — 101 real queries needing multi-tool orchestration, graded against ground-truth plans. `LJ`
- [SEC-bench](https://arxiv.org/abs/2506.11791) — Real-world software security tasks with a multi-agent dataset scaffold. `LJ`
- [UserBench](https://arxiv.org/abs/2507.22034) — Simulated users with vague evolving goals; separates task completion from user alignment. `LJ`
- [NewtonBench](https://arxiv.org/abs/2510.07172) — Memorization-resistant scientific law discovery through interactive exploration. `LJ`
- [PillagerBench](https://arxiv.org/abs/2509.06235) — Competitive multi-agent Minecraft with human-readable tactics. `LJ`
- [IDA-Bench](https://arxiv.org/abs/2505.18223) — Multi-round interactive guided data analysis. `LJ`
- [MedAgentBench](https://arxiv.org/pdf/2501.14654) — Virtual EHR environment with clinically derived tasks. `LJ`
- [AI Hospital](https://aclanthology.org/2025.coling-main.680.pdf) — Multi-agent medical interaction simulator with the MVME benchmark. `LJ`
- [DCA-Bench](https://openreview.net/pdf?id=a4sknPttwV) — Whether agents can detect real dataset quality issues in the wild. `LJ`
- [MultiAgentBench](https://arxiv.org/abs/2503.01935) — Evaluates collaboration *and* competition, plus coordination protocols. `LJ`
- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) — ABC guidelines; documents how many existing benchmarks have setup or reward bugs. `LJ`
- [MMSearch-Plus](https://arxiv.org/abs/2508.21475) — Multimodal browsing that genuinely requires multimodal reasoning. `LJ`
- [EgoLife](https://arxiv.org/pdf/2503.03803) — Egocentric life-assistant dataset and QA tasks. `LJ`
- [UnrealZoo](https://arxiv.org/abs/2412.20977) — Photo-realistic virtual worlds; finds environmental diversity is what generalizes. `LJ`
- [CK-Arena / Probe by Gaming](https://arxiv.org/abs/2505.17512) — Conceptual knowledge via interactive description and differentiation. `LJ`
- [DA-Code](https://aclanthology.org/2024.emnlp-main.748.pdf) — Agent-based data-science code generation on real data. `LJ`
- [BLADE](https://aclanthology.org/2024.findings-emnlp.815.pdf) — Evaluates multifaceted analytic approaches in open-ended research. `LJ`
- [DSEval / Benchmarking Data Science Agents](https://aclanthology.org/2024.acl-long.308.pdf) — Evaluation paradigm with bootstrapped coverage. `LJ`
- [CToolEval](https://aclanthology.org/2024.findings-acl.928.pdf) — Chinese-language agent evaluation over 398 real APIs. `LJ`
- [AgentQuest](https://aclanthology.org/2024.naacl-demo.19.pdf) — Modular benchmarks plus two progress-tracking metrics. `LJ`
- [BENCHAGENTS](https://arxiv.org/pdf/2410.22584) — Automates benchmark creation through agent interaction. `LJ`
- [Tapilot-Crossing](https://arxiv.org/pdf/2403.05307) — Interactive data analysis with the AIR self-improvement strategy. `LJ`
- [Tur[k]ingBench](https://arxiv.org/pdf/2403.11905) — Web agents on natural crowdsourcing HTML pages. `LJ`
- [LaMPilot](https://arxiv.org/abs/2312.04372) — Autonomous driving with language model programs. `LJ`
- [Seal-Tools](https://arxiv.org/pdf/2405.08355) — Self-instruct tool-learning dataset with hard instances and strict metrics. `LJ`
- [SheetAgent / SheetRM](https://arxiv.org/abs/2403.03636) — Spreadsheet reasoning and manipulation. `LJ`
- [GenoTEX](https://arxiv.org/abs/2406.15341) — Gene expression analysis benchmark with a self-correcting multi-agent system. `LJ` `ZJ`
- [Embodied Agent Interface](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b631da756d1573c24c9ba9c702fde5a9-Abstract-Datasets_and_Benchmarks_Track.html) — Unifies embodied decision-making tasks, modules and metrics. `LJ`
- [ML Research Benchmark](https://arxiv.org/pdf/2410.22553) — Seven research-level tasks for agents. `LJ`
- [AgentBank](https://aclanthology.org/2024.findings-emnlp.116/) — 50,000+ interaction trajectories for generalized agent tuning. `LJ`
- [AgentOhana](http://arxiv.org/abs/2402.15506) — Unifies heterogeneous trajectory sources into one training pipeline. `LJ`
- [Agent-FLAN](https://aclanthology.org/2024.findings-acl.557/) — Decomposes the agent corpus and uses negatives to reduce hallucination. `LJ`
- [Benchmarking Agentic Workflow Generation](https://arxiv.org/abs/2410.07869) — Evaluates generated workflows rather than final answers. `ZJ`
- [AgentBoard](https://arxiv.org/abs/2401.13178) — Analytical multi-turn evaluation with progress-rate metrics, not just success. `ZJ`
- [BOLAA](https://arxiv.org/abs/2308.05960) — Benchmarks and orchestrates agent architectures side by side. `ZJ`
- [T-Eval](https://arxiv.org/abs/2312.14033) — Decomposes tool-use capability into separately scored steps. `ZJ`
- [TravelPlanner](https://arxiv.org/pdf/2402.01622.pdf) — Real-world constrained planning; famously low success rates. `ZJ` `LJ`
- [UltraTool](https://arxiv.org/abs/2401.17167) — Planning, creation and usage across the whole tool pipeline without a fixed toolset. `LJ`
- [The Tong Test](https://www.sciencedirect.com/science/article/pii/S209580992300293X) — AGI evaluation through dynamic embodied physical and social interaction. `ZJ`
- [PerspectiveGap](https://arxiv.org/abs/2606.08878) — Multi-agent orchestration prompting benchmark (2026). `ZJ`
- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) — Two-dimensional taxonomy plus enterprise-specific challenges. `LJ`

---

# 8. Safety, security and governance

- [Beyond Permission Prompts](https://www.anthropic.com/engineering/beyond-permission-prompts) — Structured authorization instead of prompt-level trust. `HE`
- [Claude Code Auto Mode: A Safer Way to Skip Permissions](https://www.anthropic.com/engineering/claude-code-auto-mode) — Users approve 93% of prompts, so approvals stop meaning anything; two-stage classifier instead. `HE`
- [Claude Agent SDK — Configure Permissions](https://platform.claude.com/docs/en/agent-sdk/permissions) — Five-layer evaluation order and the subagent inheritance warning. `HE`
- [OWASP LLM06:2025 — Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) — The standard checklist for auditing permission scope. `HE`
- [Two Different Types of Agent Authorization](https://blog.langchain.com/two-different-types-of-agent-authorization/) — On-behalf-of vs fixed-credential models have different threat surfaces. `HE`
- [IETF draft-klrc-aiagent-auth](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) — First standards-track agent auth spec, building on WIMSE and OAuth 2.0. `HE`
- [Authorization and Governance for AI Agents](https://techcommunity.microsoft.com/blog/microsoft-security-blog/authorization-and-governance-for-ai-agents-runtime-authorization-beyond-identity/4509161) — PEP/PDP fabric returning ALLOW / DENY / REQUIRE_APPROVAL / MASK. `HE`
- [Open Agent Passport (OAP)](https://arxiv.org/abs/2603.20953) — Pre-action authorization with signed audit records; 0% attack success under restrictive policy. `HE`
- [AgentDoG: Diagnostic Guardrail Framework](https://arxiv.org/abs/2601.18491) — Three-dimensional risk taxonomy with 4B–8B diagnostic models at 91.8% accuracy. `HE`
- [nah](https://github.com/manuelschipper/nah) — Maps tool calls to an intent taxonomy rather than command allow-lists. `HE`
- [GitHub Enterprise — Governing Agents](https://wellarchitected.github.com/library/governance/recommendations/governing-agents/) — MCP registry curation, environment standardization, ephemeral runners, firewall allowlists. `HE`
- [Greywall](https://github.com/GreyhavenHQ/greywall) — Deny-by-default command sandbox with filesystem isolation and transparent network proxy. `KY`
- [Cordum](https://github.com/cordum-io/cordum) — Out-of-process governance plane with pre-dispatch policy and signed audit trails. `KY`
- [AgentRun](https://github.com/Jonathan-Adly/AgentRun) — Safe sandboxed execution of AI-generated Python. `KY`
- [DataSentinel: Game-Theoretic Detection of Prompt Injection](https://arxiv.org/abs/2504.11358) — Detection framed as a minimax game against adaptive injection. `BK`
- [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/abs/2407.12784) — Poisons the memory/KB rather than the prompt. `BK`
- [Progent: Programmable Privilege Control for LLM Agents](https://arxiv.org/html/2504.11703v1) — Policy language for least-privilege tool execution. `BK`
- [DecodingTrust](https://arxiv.org/abs/2306.11698) — Multi-dimensional trustworthiness assessment across eight perspectives. `BK`
- [Representation Engineering](https://arxiv.org/abs/2310.01405) — Top-down transparency via representation reading and control. `BK`
- [Extracting Training Data from Large Language Models](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf) — Verbatim memorization is extractable at scale. `BK`
- [The Secret Sharer](https://www.usenix.org/system/files/sec19-carlini.pdf) — Quantifies unintended memorization with exposure metrics. `BK`
- [Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](https://arxiv.org/abs/2409.16165) — Tooling, not model scale, drove vulnerability-discovery gains. `BK`
- [From Naptime to Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html) — Project Zero's agent finding real memory-safety bugs in production code. `BK`
- [Improving Methodologies for Agentic Evaluations](https://arxiv.org/abs/2601.15679) — Multi-national exercise on leakage, fraud and cyber-threat evaluation. `VA`
- [Sifting the Noise: LLM Agents in Vulnerability False Positive Filtering](https://arxiv.org/abs/2601.22952) — Compares Aider, OpenHands and SWE-agent on triage. `VA`

## Attacks (from `LJ`, `ZJ` — the deepest cluster in the corpus)

- [AgentDojo](https://openreview.net/pdf?id=m1YYAQjO3w) — Dynamic environment for evaluating prompt-injection attacks *and* defenses. The reference testbed. `LJ`
- [Agent Security Bench (ASB)](https://arxiv.org/pdf/2410.02644) — Formalizes and benchmarks attacks and defenses across agent components. `LJ`
- [AgentHarm](https://openreview.net/pdf?id=AC5n7xHuR1) — 110 malicious tasks across 11 harm categories for measuring agent harmfulness. `LJ`
- [AGENT-SAFETYBENCH](https://arxiv.org/pdf/2412.14470) — Broad safety evaluation identifying recurring agent safety flaws. `LJ`
- [INJECAGENT](https://arxiv.org/pdf/2403.02691) — Indirect prompt injection benchmark for tool-integrated agents, by attack intent. `LJ`
- [R-Judge](https://arxiv.org/abs/2401.10019) — Benchmarks whether agents *recognize* safety risk in their own trajectories. `LJ`
- [Prompt Infection](https://arxiv.org/pdf/2410.07283) — LLM-to-LLM injection propagating through a multi-agent system; proposes LLM Tagging. `LJ`
- [Agent Smith](https://arxiv.org/abs/2402.08567) — One image jailbreaks a million multimodal agents exponentially fast via infectious spread. `LJ`
- [CORBA](https://arxiv.org/abs/2502.14529) — Contagious recursive blocking; resource depletion that alignment does not mitigate. `LJ`
- [Breaking ReAct Agents: Foot-in-the-Door Attack](https://arxiv.org/pdf/2410.16950) — Benign first request unlocks a harmful second; proposes a reflection defense. `LJ`
- [WIPI: A New Web Threat for LLM-Driven Web Agents](https://arxiv.org/pdf/2402.16965) — Controls web agents indirectly through instructions planted in pages. `LJ`
- [WebInject](https://arxiv.org/abs/2505.11717) — Pixel-level perturbation as a prompt-injection vector against web agents. `LJ`
- [Web Fraud Attacks on LLM-driven Multi-Agent Systems](https://arxiv.org/abs/2509.01211) — Domain tampering and link camouflage, bypassing jailbreak techniques entirely. `LJ`
- [Imprompter](https://arxiv.org/pdf/2410.14923) — Obfuscated adversarial prompts inducing improper tool use across several agents. `LJ`
- [DemonAgent](https://arxiv.org/abs/2502.12575) — Dynamically encrypted multi-backdoor implantation that evades safety audits. `LJ`
- [Watch Out for Your Agents! Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Abstract-Conference.html) — Formalizes agent-specific backdoor forms. `LJ`
- [AutoHijacker](https://openreview.net/pdf?id=2VmB01D9Ef) — Automatic black-box indirect injection using LLMs as optimizers. `LJ`
- [Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/pdf/2502.14847) — Agent-in-the-Middle: manipulating inter-agent messages. `LJ`
- [Targeting the Core: Attacking RAG-Based Agents via Direct LLM Manipulation](https://arxiv.org/pdf/2412.04415) — Adversarial prefixes defeating RAG agent architectures. `LJ`
- [AEIA-MN](https://arxiv.org/pdf/2502.13053) — Active environmental injection against multimodal mobile agents. `LJ`
- [Advertisement Embedding Attacks](https://arxiv.org/abs/2508.17674) — Hijacks models to inject covert promotional content; two low-cost vectors. `LJ`
- [Evil Geniuses: Delving into the Safety of LLM-based Agents](https://arxiv.org/pdf/2311.11855) — Template-based attack plus a systematic agent-safety probe. `LJ`
- [Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks](https://arxiv.org/abs/2502.08586) — Attack taxonomy executable with no ML knowledge. `LJ`
- [A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents](https://arxiv.org/abs/2402.10196) — First systematic map, 12 scenarios. `LJ`
- [Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/abs/2502.13172) — MEXTRA: black-box extraction of private data from agent memory. `LJ`
- [Beyond Data Privacy: New Privacy Risks for Large Language Models](https://arxiv.org/abs/2509.14278) — Deployment and autonomous reasoning as novel privacy surfaces. `LJ`
- [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817) — ToolEmu: emulated tools to surface risk without real consequences. `ZJ`

## Defenses and architectures (from `LJ`)

- [The Task Shield](https://arxiv.org/pdf/2412.16682) — Reframes agent security as task alignment: verify each instruction contributes to the user's goal. `LJ`
- [SAGA: A Security Architecture for Governing AI Agentic Systems](https://arxiv.org/abs/2504.21034) — User oversight with fine-grained access control for agent deployment. `LJ`
- [RTBAS](https://arxiv.org/pdf/2502.08966) — Information Flow Control adapted to tool-based agents, screening tool calls automatically. `LJ`
- [G-Safeguard](https://arxiv.org/abs/2502.11127) — GNN anomaly detection plus topological intervention on multi-agent graphs. `LJ`
- [NetSafe: Topological Safety of Multi-agent Networks](https://arxiv.org/abs/2410.15686) — Safety as a property of network topology rather than individual agents. `LJ`
- [Firewalls to Secure Dynamic LLM Agentic Networks](https://arxiv.org/pdf/2502.01822) — Derives firewall rules from required communication properties. `LJ`
- [AutoDefense](https://arxiv.org/pdf/2403.04783) — Multi-agent response filtering; small models successfully defending larger ones. `LJ`
- [TrustAgent](https://arxiv.org/abs/2402.01586) — Agent-constitution framework with three safety strategies, and its helpfulness cost. `LJ`
- [PsySafe](https://aclanthology.org/2024.acl-long.812/) — Attack, defense and evaluation framed through agent psychology. `LJ`
- [BlockAgents](https://dl.acm.org/doi/pdf/10.1145/3674399.3674445) — Blockchain proof-of-thought for Byzantine-robust multi-agent coordination. `LJ`
- [Prompt Injection as a Defense Against LLM-driven Cyberattacks](https://arxiv.org/pdf/2410.20911) — Mantis: hacking back autonomously via injection. `LJ`
- [PrivacyChecker / PrivacyLens-Live](https://arxiv.org/abs/2509.17488) — Model-agnostic mitigation plus a dynamic privacy benchmark using contextual integrity. `LJ`
- [PrivWeb](https://arxiv.org/abs/2509.11939) — Local LLM anonymizes on-screen data for web agents by user preference. `LJ`
- [AI Agents Under Threat: A Survey](https://dl.acm.org/doi/pdf/10.1145/3716628) — Four knowledge gaps in agent security. Best survey entry point. `LJ`
- [A Comprehensive Survey in LLM(-Agent) Full Stack Safety](https://arxiv.org/abs/2504.15585) — Data, training and deployment as one safety lifecycle. `LJ`
- [Navigating the Risks: Security, Privacy, and Ethics Threats in LLM-Based Agents](https://arxiv.org/pdf/2411.09523) — Combined taxonomy across all three. `LJ`
- [The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies](https://arxiv.org/pdf/2407.19354) — Threats, impacts and defenses with worked cases. `LJ`
- [Security of AI Agents](https://arxiv.org/pdf/2406.08689) — Systems-level vulnerability view rather than model-level. `LJ`
- [CLAS 2024: The Competition for LLM and Agent Safety](https://openreview.net/pdf?id=GIDw94AlZK) — Three-track community competition; useful for eval design. `LJ`
- [Achilles Heel of Distributed Multi-Agent Systems](https://arxiv.org/abs/2504.07461) — Free riding and malicious participation in distributed agent systems. `LJ` `ZJ`

---

# 9. Observability and ops

- [How We Build Azure SRE Agent with Agentic Workflows](https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-azure-sre-agent-with-agentic-workflows/4508753) — 35,000+ production incidents; time-to-mitigation 40.5 hours → 3 minutes. `HE`
- [Ranking Engineer Agent (REA)](https://engineering.fb.com/2026/03/17/developer-tools/ranking-engineer-agent-rea-autonomous-ai-system-accelerating-meta-ads-ranking-innovation/) — Multi-day ML pipeline automation with hibernate-and-wake checkpointing. `HE`
- [An Update on Recent Claude Code Quality Reports](https://www.anthropic.com/engineering/april-23-postmortem) — Three independent harness-level changes compounding into visible regression. Best postmortem in the corpus. `HE`
- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/abs/2602.06443) — Runtime verifier locating trajectory errors for precise rollback-and-retry. `VA`
- [Tokenomics: Quantifying Where Tokens Are Used](https://arxiv.org/abs/2601.14470) — Token consumption by SDLC stage, identifying cost drivers. `VA`
- [From Features to Actions: Explainability in Traditional and Agentic AI](https://arxiv.org/abs/2602.06841) — Attribution vs trace-based diagnostics for multi-step trajectories. `VA`
- [Interpreting Agentic Systems: Beyond Model Explanations](https://arxiv.org/abs/2601.17168) — Gaps in explaining temporal dynamics and compounding decisions. `VA`
- [The Why Behind the Action: Agentic Attribution](https://arxiv.org/abs/2601.15075) — Hierarchical attribution of actions to internal drivers. `VA`
- [Interpreting Emergent Extreme Events in Multi-Agent Systems](https://arxiv.org/abs/2601.20538) — Shapley attribution across time, agent and behaviour. `VA`
- [TriCEGAR](https://arxiv.org/abs/2601.22997) — Predicate-tree state abstraction from traces for runtime verification. `VA`
- [FROAV](https://arxiv.org/abs/2601.07504) — Visual workflow orchestration plus LLM-judge for RAG pipeline validation. `VA`
- [Balancing Sustainability And Performance](https://arxiv.org/abs/2601.19311) — Whether small models cut energy without quality loss in multi-agent systems. `VA`
- [Manifest](https://github.com/mnfst/manifest) — Local-first cost observability: tokens, costs and model usage with OTLP ingestion. `KY`
- [ctop](https://github.com/aakashadesara/ctop) — htop for coding agents: CPU, memory, tokens, context window, cost. `KY`
- [Hermes Agent: Unified Streaming](https://juliangoldie.com/hermes-agent-unified-streaming/) — Token-by-token streaming for sub-second reactive decision loops. `HE`
- [AWS Bedrock AgentCore with WebRTC Support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-webrtc/) — P2P UDP streaming for sub-800ms voice turn-around. `HE`

---

# 10. Coding agents

- [Aider](https://github.com/Aider-AI/aider) — Terminal pair programming with repo-map context and git-aware edits. `KY`
- [Cline](https://github.com/cline/cline) — Open-source IDE coding agent with full transparency over model actions. `KY`
- [OpenCode](https://github.com/sst/opencode) — Terminal-native coding agent. `KY`
- [Plandex](https://github.com/plandex-ai/plandex) — Coding engine aimed at large multi-file tasks with staged diffs. `KY`
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) — Builds apps step by step with developer checkpoints. `KY`
- [Devika](https://github.com/stitionai/devika) — Decomposes high-level instructions, researches, then writes code. `KY`
- [Codel](https://github.com/semanser/codel) — Autonomous agent with terminal, browser and editor. `KY`
- [RepoAgent](https://github.com/OpenBMB/RepoAgent) — Repository-level documentation generation and comprehension. `KY`
- [Nous](https://github.com/TrafficGuard/nous) — TypeScript platform spanning autonomous, developer and code-review agents. `KY`
- [Stakpak](https://github.com/stakpak/agent) — DevOps agent for securing and deploying production infrastructure. `KY`
- [ReviewCerberus](https://github.com/Kirill89/reviewcerberus) — Branch-diff code review across security, performance and quality. `KY`
- [Frontman](https://github.com/frontman-ai/frontman) — Browser-resident agent reading live DOM and component tree, editing source with hot reload. `KY`
- [Dorothy](https://github.com/Charlie85270/Dorothy) — Desktop orchestration of multiple CLI agents with Kanban and automations. `KY`
- [Maestro (RunMaestro)](https://github.com/RunMaestro/Maestro) — Desktop command centre running parallel agents with event automation and group chat. `KY`
- [Maestro Orchestrate](https://github.com/josstei/maestro-orchestrate) — 22 specialized agents in 4-phase workflows with least-privilege tiers. `KY`
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) — Orchestrates 40+ CLI agents with worktree isolation and an HMAC-chained audit log. `KY`
- [amux](https://github.com/mixpeek/amux) — Multiplexes dozens of parallel sessions with dashboard, watchdog and A2A REST API. `KY`
- [AgentsMesh](https://github.com/AgentsMesh/AgentsMesh) — Remote agent workstations with PTY sandbox and git worktree isolation. `KY`
- [hcom](https://github.com/aannoo/hcom) — Lets agents message, watch and spawn each other across terminals. `KY`
- [What's New with GitHub Copilot Coding Agent](https://github.blog/ai-and-ml/github-copilot/whats-new-with-github-copilot-coding-agent/) — `.github/agents/` files, self-review and security scanning as harness primitives. `HE`
- [Dataverse Skills](https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse) — Domain skills as curated execution strategies across MCP, SDK and raw API. `HE`
- [Why Are AI Agent Involved Pull Requests Remain Unmerged?](https://arxiv.org/abs/2602.00164) — 8,106 fix-related PRs from five agents, with rejection reasons. `VA`
- [More Code, Less Reuse](https://arxiv.org/abs/2601.21276) — Code quality and reviewer sentiment on agent PRs vs human. `VA`
- [Let's Make Every Pull Request Meaningful](https://arxiv.org/abs/2601.18749) — 40,214 PRs compared on merge outcomes and review features. `VA`
- [Understanding Dominant Themes in Reviewing Agentic AI-authored Code](https://arxiv.org/abs/2601.19287) — 19,450 review comments, 12-theme taxonomy. `VA`
- [Will It Survive? Fate of AI-Generated Code in Open Source](https://arxiv.org/abs/2601.16809) — Survival analysis of 200,000+ code units across 201 projects. `VA`
- [The Quiet Contributions: AI-Generated Silent Pull Requests](https://arxiv.org/abs/2601.21102) — Impact of no-comment agent PRs on complexity and vulnerabilities. `VA`
- [When AI Agents Touch CI/CD Configurations](https://arxiv.org/abs/2601.17413) — Modification frequency, merge and build success across 8,031 PRs. `VA`
- [AI builds, We Analyze](https://arxiv.org/abs/2601.16839) — Maintainability and security smells in agent-generated build code. `VA`
- [Fingerprinting AI Coding Agents on GitHub](https://arxiv.org/abs/2601.17406) — Behavioural signatures attributing PRs to specific agents. `VA`
- [Who Writes the Docs in SE 3.0?](https://arxiv.org/abs/2601.20171) — Agent vs human documentation PRs and human intervention patterns. `VA`
- [Are We All Using Agents the Same Way?](https://arxiv.org/abs/2601.20106) — Core vs peripheral developers differ in review and verification behaviour. `VA`
- [Analyzing Message-Code Inconsistency in Agent-Authored PRs](https://arxiv.org/abs/2601.04886) — Whether PR descriptions match the actual diff. `VA`
- [LLM-Based Agentic Systems for Software Engineering](https://arxiv.org/abs/2601.09822) — Review across the SDLC covering frameworks and orchestration challenges. `VA`
- [Adaptive Confidence Gating for Code Generation](https://arxiv.org/abs/2601.21469) — Role-based debate with confidence gating for small-model code generation. `VA`
- [Self-collaboration Code Generation via ChatGPT](https://arxiv.org/abs/2304.07590) — Single model playing analyst/coder/tester roles in sequence. `XI`
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — The Codex paper and HumanEval. `XI`
- [The Hitchhiker's Guide to Program Analysis](https://arxiv.org/abs/2308.00245) — LLMs assisting static analysis to cut false positives. `XI`

---

# 11. Web, GUI and computer use

- [Steel Browser](https://github.com/steel-dev/steel-browser) — Browser infrastructure for agents with session-backed automation and extraction. `KY`
- [Gobii](https://github.com/gobii-ai/gobii-platform) — Deploys and manages browser-use agents at scale with a conversational interface. `KY`
- [Actionbook](https://github.com/actionbook/actionbook) — Parallel action CLI running many actions across many sites at once. `KY`
- [invisible-playwright](https://github.com/feder-cr/invisible_playwright) — Stealth-patched Firefox behind a drop-in Playwright interface. `KY`
- [AgentGPT](https://github.com/reworkd/AgentGPT) — Browser-based autonomous agent runner. `KY`
- [OpenAgents](https://arxiv.org/abs/2310.10634) — Open platform with data, plugin and web agents for real users. `XI`
- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856) — WebAgent: HTML summarization plus program synthesis on live sites. `XI`
- [SYNAPSE: Few-Shot Exemplars for Human-Level Computer Control](https://arxiv.org/abs/2306.07863) — Trajectory-as-exemplar prompting with state abstraction. `XI`
- [Mind2Web / Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://arxiv.org/abs/2305.11854) — WebGUM: instruction-finetuned vision-language web navigation. `XI`
- [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491) — RCI prompting: recursively critique and improve before acting. `XI`
- [Towards Learning a Generalist Model for Embodied Navigation](https://arxiv.org/abs/2312.02010) — NaviLLM: schema-based instruction unifying navigation tasks. `XI`

---

# 12. RAG and retrieval

- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) — Autonomous online research agent producing cited reports. `KY`
- [Storm](https://github.com/stanford-oval/storm) — Perspective-guided question asking to write full Wikipedia-style articles with citations. `KY`
- [Agentset](https://github.com/agentset-ai/agentset) — Production RAG platform with agentic reasoning, hybrid search and multimodal support. `KY`
- [LlamaIndex](https://github.com/jerryjliu/llama_index) — Data framework connecting LLMs to external data. `KY` `BK`
- [Haystack](https://github.com/deepset-ai/haystack) — Composable NLP/LLM pipelines over your data. `KY`
- [Private GPT](https://github.com/imartinez/privateGPT) — Fully local document Q&A. `KY`
- [LLocalSearch](https://github.com/nilsherzig/LLocalSearch) — Local search aggregator with a chain of LLM agents and visible progress. `KY`
- [OpenScholar](https://arxiv.org/abs/2411.14199) — Retrieval-augmented synthesis over scientific literature. `BK`
- [CompactRAG](https://arxiv.org/abs/2602.05728) — Offline atomic QA pairs resolve multi-hop in two LLM calls regardless of hops. `VA`
- [To Retrieve or To Think?](https://arxiv.org/abs/2601.08747) — Decides per step whether to retrieve or reason over existing context. `VA`
- [A2RAG: Adaptive Agentic Graph Retrieval](https://arxiv.org/abs/2601.21162) — Verifies evidence sufficiency and escalates retrieval effort progressively. `VA`
- [Deep GraphRAG](https://arxiv.org/abs/2601.11144) — Global-to-local hierarchical retrieval with beam-search reranking. `VA`
- [Relink: Query-Driven Evidence Graph On-the-Fly](https://arxiv.org/abs/2601.07192) — Builds query-specific evidence graphs, discarding distractor facts. `VA`
- [FastInsight](https://arxiv.org/abs/2601.18579) — Fusion operators combining graph reranking with semantic-topological expansion. `VA`
- [SOPRAG](https://arxiv.org/abs/2602.01858) — Graph experts over entity relations and process flow for SOP documents. `VA`
- [Topo-RAG](https://arxiv.org/abs/2601.10215) — Routes narrative and tabular content through separate retrievers. `VA`
- [Reliable Graph-RAG for Codebases: AST vs LLM-Extracted Graphs](https://arxiv.org/abs/2601.08773) — Benchmarks deterministic against LLM graph construction for code. `VA`
- [Less is More for RAG: Information Gain Pruning](https://arxiv.org/abs/2601.17532) — Generator-aligned reranking filtering harmful passages pre-truncation. `VA`
- [DeepEra](https://arxiv.org/abs/2601.16478) — Reasoning reranker separating semantic similarity from logical relevance. `VA`
- [L-RAG: Entropy-Based Lazy Loading](https://arxiv.org/abs/2601.06551) — Skips retrieval when model uncertainty is low. `VA`
- [When should I search more](https://arxiv.org/abs/2601.21208) — RL decides when to split complex queries and fuse results. `VA`
- [ProRAG](https://arxiv.org/abs/2601.21912) — MCTS step-level rewards to locate flawed reasoning in multi-hop retrieval. `VA`
- [JADE: Strategic-Operational Gap in Dynamic Agentic RAG](https://arxiv.org/abs/2601.21916) — Joint planning/execution optimization as a cooperative team. `VA`
- [PRISMA](https://arxiv.org/abs/2601.05465) — Plan-Retrieve-Inspect-Solve-Memoize with two-stage GRPO against retrieval collapse. `VA`
- [SPARC-RAG](https://arxiv.org/abs/2602.00083) — Sequential and parallel inference-time scaling under unified context management. `VA`
- [DIVERGE](https://arxiv.org/abs/2602.00238) — Reflection and memory refinement for diverse open-ended answers. `VA`
- [CIRAG](https://arxiv.org/abs/2601.06799) — Preserves multiple evidence chains, expanding granularity from triples to passages. `VA`
- [Parallel Context-of-Experts Decoding](https://arxiv.org/abs/2601.08670) — Training-free contrastive decoding treating documents as isolated experts. `VA`
- [Seeing through the Conflict](https://arxiv.org/abs/2601.06842) — Separates semantic match from factual consistency for observable conflict resolution. `VA`
- [Incorporating Q&A Nuggets into RAG](https://arxiv.org/abs/2601.13222) — Nugget bank guiding extraction and report generation with provenance. `VA`
- [Utilizing Metadata for Better RAG](https://arxiv.org/abs/2601.11863) — Compares prefix, suffix, unified-embedding and late-fusion metadata strategies. `VA`
- [OpenDecoder](https://arxiv.org/abs/2601.09028) — Feeds retrieval quality signals into generation for noise robustness. `VA`
- [When Iterative RAG Beats Ideal Evidence](https://arxiv.org/abs/2601.19827) — Diagnoses when retrieval loops beat gold context, and why. `VA`
- [Aggregation Queries over Unstructured Text](https://arxiv.org/abs/2602.01355) — Disambiguation, filtering and aggregation stages for exhaustive-evidence queries. `VA`
- [Mitigating Hallucination in Financial RAG](https://arxiv.org/abs/2602.05723) — Atomic-fact verification against retrieved documents with RL rewards. `VA`
- [Dep-Search](https://arxiv.org/abs/2601.18771) — GRPO-trained dependency-aware decomposition with persistent intermediate results. `VA`

---

# 13. Training and optimization

- [AgentGym: Evolving LLM-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151) — Unified environment suite plus AgentEvol for cross-environment evolution. `XI`
- [AgentTuning](https://arxiv.org/abs/2310.12823) — AgentInstruct data mixed with general instructions to add agent skills without regression. `XI`
- [FireAct: Toward Language Agent Fine-tuning](https://arxiv.org/abs/2310.05915) — Fine-tuning on multi-method agent trajectories. `XI` *(corrected: `XI` links this to arXiv 2305.16291, which is Voyager — see data-quality note below)*
- [Lemur: Harmonizing Natural Language and Code for Language Agents](https://arxiv.org/abs/2310.06830) — Balanced text/code pretraining for agent backbones. `XI`
- [Training LLMs for Reasoning through Reverse Curriculum RL](https://arxiv.org/abs/2402.05808) — R3: reverse curriculum giving step-level signal from outcome-only supervision. `XI`
- [Unpacking DPO and PPO](https://arxiv.org/abs/2406.09279) — Disentangles what actually drives preference-learning gains. `BK`
- [Symbolic Regression with a Learned Concept Library](https://arxiv.org/abs/2409.09359) — Learns reusable abstractions to guide search. `BK`
- [SurCo](https://arxiv.org/abs/2210.12547) — Learned linear surrogates for combinatorial nonlinear optimization. `BK`
- [Composing Global Optimizers to Reasoning Tasks](https://arxiv.org/abs/2410.01779) — Algebraic structure of solutions in small reasoning networks. `BK`
- [ADAS: Automated Design of Agentic Systems](https://github.com/ShengranHu/ADAS) — Meta-agent programming new agent designs in code. `KY`
- [Agentic Context Engine](https://github.com/kayba-ai/agentic-context-engine) — Agents that curate their own context from execution feedback. `KY`
- [AIDE](https://github.com/WecoAI/aideml) — Tree search over ML experiment code against any metric. `KY`
- [MARO: Learning Stronger Reasoning from Social Interaction](https://arxiv.org/abs/2601.12323) — Decomposes social-interaction outcomes into per-behaviour signals. `VA`
- [Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic](https://arxiv.org/abs/2601.21972) — Actor-critic for decentralized collaboration across task types. `VA`
- [Collaborative Multi-Agent Test-Time RL](https://arxiv.org/abs/2601.09667) — Injects structured textual experience at test time, no tuning. `VA`
- [Learning to Collaborate: Peer-to-Peer LLM Federation](https://arxiv.org/abs/2601.17133) — Contextual bandits for matchmaking via secure distillation. `VA`
- [The End of Reward Engineering](https://arxiv.org/abs/2601.08237) — Argues language objectives replace hand-crafted reward functions. `VA`
- [Evolving Interpretable Constitutions for Multi-Agent Coordination](https://arxiv.org/abs/2602.00755) — LLM-driven genetic programming discovering behavioural norms. `VA`

---

# 14. Embodied and robotics

- [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/pdf/2303.03378.pdf) — Interleaves images, state and text into one embodied multimodal model. `XI`
- [Code as Policies](https://arxiv.org/pdf/2209.07753.pdf) — LLM writes policy code calling perception and control primitives. `XI`
- [Language Models as Zero-Shot Planners](https://arxiv.org/abs/2201.07207) — Grounds free-form plans by projecting onto admissible actions. `XI`
- [EmbodiedGPT](https://arxiv.org/pdf/2305.15021.pdf) — Embodied chain-of-thought vision-language pretraining. `XI`
- [An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12871) — LEO: single model across 3D perception, reasoning and action. `XI`
- [JARVIS-1](https://arxiv.org/abs/2311.05997) — Multimodal memory-augmented open-world Minecraft agent. `XI`
- [Ghost in the Minecraft (GITM)](https://arxiv.org/abs/2305.17144) — Text knowledge and memory for open-world capability. `XI`
- [MineDojo](https://papers.nips.cc/paper_files/paper/2022/file/74a67268c5cc5910f64938cac4526a90-Paper-Datasets_and_Benchmarks.pdf) — Internet-scale Minecraft knowledge base plus open-ended benchmark. `XI`
- [Plan4MC](https://arxiv.org/abs/2303.16563) — Skill RL plus planning over a skill graph for Minecraft tasks. `XI`
- [LM-Nav](https://proceedings.mlr.press/v205/shah23b/shah23b.pdf) — Composes pretrained language, vision and navigation models with no fine-tuning. `XI`
- [RoboAgent](https://arxiv.org/abs/2309.01918) — Semantic augmentation and action chunking for multi-task manipulation. `XI`
- [Interactive Language: Talking to Robots in Real Time](https://arxiv.org/abs/2210.06407) — Real-time language-conditioned manipulation. `XI`
- [Eureka: Human-Level Reward Design via Coding LLMs](https://eureka-research.github.io/) — LLM writes and evolves reward code beating human-designed rewards. `BK`
- [DrEureka: Language Model Guided Sim-To-Real Transfer](https://eureka-research.github.io/dr-eureka/) — Automates domain-randomization config for sim-to-real. `BK`
- [Project GR00T](https://www.nvidia.com/en-us/robotics/groot-robot/) — Foundation-model blueprint for generalist humanoid robotics. `BK`
- [SLAC](https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-jiaheng_hu_2025.html) — Simulation-pretrained latent action space for whole-body real-world RL. `BK`
- [Outracing Champion Gran Turismo Drivers with Deep RL](https://www.nature.com/articles/s41586-021-04357-7) — GT Sophy: superhuman racing with RL. `BK`
- [Voyager (repo)](https://github.com/MineDojo/Voyager) — Reference implementation of the skill-library agent. `KY`

---

# 15. Frameworks and SDKs

- [LangChain](https://github.com/hwchase17/langchain) — The original LLM application framework. `KY`
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) — Microsoft's SDK for embedding LLM orchestration in apps. `KY`
- [CrewAI](https://github.com/joaomdmoura/crewai) — Role-playing agent crews with tasks and delegation. `KY`
- [AG2](https://github.com/ag2ai/ag2) — Successor framework from the AutoGen creators. `KY`
- [smolagents](https://github.com/huggingface/smolagents) — Minimal code-writing agents in very few lines. `KY`
- [Mastra](https://github.com/mastra-ai/mastra) — Opinionated TypeScript framework for AI apps and agents. `KY`
- [Strands Agents SDK](https://github.com/strands-agents/sdk-python) — Model-driven agent construction in few lines. `KY`
- [VoltAgent](https://github.com/VoltAgent/voltagent) — TypeScript agent framework with built-in LLM observability. `KY`
- [AgentScope](https://github.com/modelscope/agentscope) — Multi-agent application platform with message-passing model. `KY`
- [Swarms Framework](https://github.com/kyegomez/swarms) — Enterprise multi-agent orchestration. `KY`
- [Swarm](https://github.com/openai/swarm) — OpenAI's educational lightweight handoff-based orchestration. `KY`
- [agency-swarm](https://github.com/VRSEN/agency-swarm) — Agent framework over the Assistants API. `KY`
- [PraisonAI](https://github.com/MervinPraison/PraisonAI) — Multi-agent framework with self-reflection, 100+ LLMs, Python and JS SDKs. `KY`
- [Upsonic](https://github.com/upsonic/upsonic) — Reliability-focused agent framework with MCP support. `KY`
- [Pipecat](https://github.com/pipecat-ai/pipecat) — Voice and multimodal conversational AI pipelines. `KY`
- [Lagent](https://github.com/InternLM/lagent) — Lightweight LLM agent framework. `KY`
- [llama-agents](https://github.com/run-llama/llama-agents) — Async-first multi-agent systems with distributed tool execution. `KY`
- [Phidata](https://github.com/phidatahq/phidata) — Assistants with memory, knowledge and tools. `KY`
- [AgentDock](https://github.com/AgentDock/AgentDock) — Open foundation for building and deploying production agents. `KY`
- [AgentField](https://github.com/Agent-Field/agentfield) — Infrastructure for AI backends with orchestration and identity. `KY`
- [Astron](https://github.com/iflytek/astron-agent) — Enterprise agentic workflow platform. `KY`
- [Modus](https://github.com/hypermodeinc/modus) — Serverless framework for agents and APIs in Go or AssemblyScript. `KY`
- [Ailoy](https://github.com/brekkylab/ailoy) — Agents that run anywhere with local-AI and WASM support. `KY`
- [ConnectOnion](https://github.com/openonion/connectonion) — Python framework with 12 lifecycle hooks and multi-agent networking. `KY`
- [Hive](https://github.com/aden-hive/hive) — Goal-driven self-improving agents auto-generating agent graphs. `KY`
- [LoongFlow](https://github.com/baidu-baige/LoongFlow) — Evolving agent development framework from atomic components up. `KY`
- [open-multi-agent](https://github.com/JackChen-me/open-multi-agent) — One call decomposes a goal into a task DAG and runs it in parallel. `KY`
- [nanobot](https://github.com/HKUDS/nanobot) — ~4,000-line personal assistant framework with MCP and skills. `KY`
- [OpenClaw](https://github.com/openclaw/openclaw) — Persistent proactive personal agent with multi-channel messaging and cron. `KY`
- [SwarmClaw](https://github.com/swarmclawai/swarmclaw) — Self-hosted multi-agent runtime with heartbeats, schedules and delegation. `KY`
- [ClaudeClaw](https://github.com/sbusso/claudeclaw) — Persistent orchestrator plugin with sandbox isolation and webhook triggers. `KY`
- [XAgent](https://github.com/OpenBMB/XAgent) — Autonomous agent with dispatcher/planner/actor separation. `KY`
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) — Dev-first autonomous agent framework. `KY`
- [Agent-LLM](https://github.com/Josh-XT/Agent-LLM) — AI automation platform. `KY`
- [uAgents](https://github.com/fetchai/uAgents) — Lightweight decentralized agents. `KY`
- [Giselle](https://github.com/giselles-ai/giselle) — Visual agentic workflow builder. `KY`
- [e2b](https://github.com/e2b-dev/e2b) — Sandboxed cloud runtime for agent code execution. `KY`
- [Supercharge Your AI Agents: ADK Integrations Ecosystem](https://developers.googleblog.com/en/supercharge-your-ai-agents-adk-integrations-ecosystem/) — ADK ecosystem patterns for wiring external services without losing state coherence. `HE`
- [Closing the Knowledge Gap with Agent Skills](https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/) — ADK skills with a 117-prompt evaluation harness. `HE`
- [Compound AI Systems & DSPy](https://dspy-docs.vercel.app/) — Compound-system framing behind DSPy. `BK`
- [Transformers Agents](https://huggingface.co/docs/transformers/transformers_agents) — Natural-language API over transformers tooling. `KY`

---

# 16. Simulation, social and domain applications

- [Social Simulacra](https://dl.acm.org/doi/10.1145/3526113.3545616) — Populated prototypes to stress-test social system designs pre-launch. `XI`
- [S3: Social-network Simulation System](https://arxiv.org/abs/2307.14984) — Emotion, attitude and behaviour propagation in a simulated network. `XI`
- [Epidemic Modeling with Generative Agents](https://arxiv.org/abs/2307.04986) — Agents reason about their own protective behaviour, producing epidemic curves. `XI`
- [Emergence of Social Norms in LLM-based Agent Societies](https://arxiv.org/abs/2403.08251) — Norm creation, representation, spreading and compliance. `XI`
- [RecAgent](https://arxiv.org/abs/2306.02552) — User-behaviour simulation for recommender research. `XI`
- [Humanoid Agents](https://arxiv.org/abs/2310.05418) — Adds basic needs, emotion and closeness to generative agents. `XI`
- [Lyfe Agents](https://arxiv.org/abs/2310.02172) — Low-cost real-time social agents via option-action and hierarchical memory. `XI`
- [Exploring LLMs for Communication Games: Werewolf](https://arxiv.org/abs/2309.04658) — Tuning-free framework showing emergent deception and trust. `XI`
- [Suspicion Agent](http://arxiv.org/abs/2309.17277) — Theory-of-mind aware play in imperfect-information games. `XI`
- [Hoodwinked](https://arxiv.org/abs/2308.01404) — Deception and cooperation in a text-based social deduction game. `XI`
- [Character-LLM](https://arxiv.org/abs/2310.10158) — Trains agents to embody specific historical characters. `XI`
- [TimeChara](https://arxiv.org/abs/2405.18027) — Point-in-time character hallucination in role-playing models. `XI`
- [Generative Agents (repo)](https://github.com/joonspk-research/generative_agents) — Reference implementation. `XI`
- [MiroShark](https://github.com/aaronjmars/MiroShark) — Swarm engine simulating Twitter, Reddit and prediction markets hour-by-hour. `KY`
- [Enclave](https://github.com/yuanzui0728/enclave) — Self-hosted AI social world with autonomous residents. `KY`
- [SkyAGI](https://github.com/litanlitudan/skyagi) — Human-behaviour simulation in LLM agents. `KY`
- [Gender Dynamics and Homophily in a Social Network of LLM Agents](https://arxiv.org/abs/2602.02606) — 70K+ autonomous agents studied for emergent bias. `VA`
- [Effects of Personality Steering on Cooperative Behavior](https://arxiv.org/abs/2601.05302) — Big Five steering in repeated Prisoner's Dilemma. `VA`
- [Emulating Aggregate Human Choice Behavior and Biases](https://arxiv.org/abs/2602.05597) — Whether agents reproduce aggregate human cognitive biases. `VA`
- [AI Scientist](https://github.com/SakanaAI/AI-Scientist) — End-to-end automated research from ideation to reviewed paper. `KY`
- [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) — Traceable data-to-manuscript pipeline with verification. `KY`
- [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) — Agentic LLM for autonomous data science and analyst-grade reports. `KY`
- [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9) — Agent team producing experimentally validated nanobodies. `BK`
- [Paper2Agent](https://arxiv.org/abs/2509.06917) — Converts research papers into interactive tool-backed agents. `BK`
- [ChemCrow](https://arxiv.org/abs/2304.05376) — 13 expert chemistry tools augmenting an LLM for synthesis planning. `XI`
- [Emergent autonomous scientific research capabilities of LLMs](https://arxiv.org/abs/2304.05332) — Coscientist: autonomous design and execution of real experiments. `XI`
- [GeneGPT](https://arxiv.org/abs/2304.09667) — Teaches API use over NCBI for genomics questions. `XI`
- [ChatMOF](https://arxiv.org/abs/2308.01423) — Predicting and generating metal-organic frameworks. `XI`
- [AlphaProof](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) — RL with formal mathematics at IMO silver-medal level. `BK`
- [LeanDojo](https://arxiv.org/abs/2306.15626) — Retrieval-augmented theorem proving with an open Lean toolkit. `BK`
- [Lean-STaR](https://arxiv.org/abs/2407.10040) — Interleaves informal thought with formal proof steps. `BK`
- [Draft, Sketch, and Prove](https://arxiv.org/abs/2210.12283) — Informal proofs guiding formal provers. `BK`
- [Autoformalization with Large Language Models](https://arxiv.org/abs/2205.12615) — Translating natural-language mathematics into formal statements. `BK`
- [Autoformalizing Euclidean Geometry](https://arxiv.org/abs/2405.17216) — Domain-specific autoformalization with diagrammatic reasoning. `BK`
- [miniCTX](https://www.arxiv.org/pdf/2408.03350) — Long-context theorem proving with real repository context. `BK`
- [ImProver](https://arxiv.org/abs/2410.04753) — Agent-based rewriting of proofs against user-chosen metrics. `BK`
- [An In-Context Learning Agent for Formal Theorem-Proving](https://arxiv.org/abs/2310.04353) — COPRA: in-context proof search with error feedback. `BK`
- [D-Bot: Database Diagnosis System](https://arxiv.org/abs/2312.01454) — LLM diagnosing database performance anomalies from docs and metrics. `XI`
- [LLM As DBA](https://arxiv.org/abs/2308.05481) — Vision for LLM database administration. `XI`
- [RecMind](https://doi.org/10.48550/arXiv.2308.14296) — Planning-and-tools agent for recommendation. `XI`
- [HuatuoGPT](https://doi.org/10.48550/arXiv.2305.15075) — Medical dialogue model blending distilled and real-doctor data. `XI`
- [Zhongjing](https://doi.org/10.48550/arXiv.2308.03549) — Chinese medical LLM with expert feedback and multi-turn dialogue. `XI`
- [H-AdminSim](https://arxiv.org/abs/2602.05407) — Hospital administrative workflow simulation with FHIR integration. `VA`
- [AI Agent Systems for Supply Chains](https://arxiv.org/abs/2602.05524) — Retrieves similar past decisions to adapt inventory ordering. `VA`
- [AgenticPay](https://arxiv.org/abs/2602.06008) — 110+ task benchmark for buyer-seller negotiation. `VA`
- [OptimAI](https://arxiv.org/abs/2504.16918) — Four-agent pipeline turning natural-language optimization into solver code; 88% on NLP4LP. `VA`
- [AutoNumerics](https://arxiv.org/abs/2602.17607) — Writes, debugs and validates classical PDE solvers end-to-end. `VA`
- [AgenticSimLaw](https://arxiv.org/abs/2601.21936) — Role-structured courtroom debate for auditable high-stakes decisions. `VA`
- [OpenLens AI](https://github.com/jarrycyx/openlens-ai) — Autonomous research agent for health informatics. `KY`
- [Autonomous HR Chatbot](https://github.com/stepanogil/autonomous-hr-chatbot) — HR query agent over internal tools. `KY`
- [joinly](https://github.com/joinly-ai/joinly) — Voice-first assistant participating live in online meetings. `KY`
- [Voyager, Camel-AutoGPT and BabyAGI UI](https://github.com/miurla/babyagi-ui) — Early autonomous-loop UIs; useful as historical artifacts. `KY`

---

# 17. Human-in-the-loop

Thin here — this is one of the `HE` sections I did not reach. Placeholder for the
second pass.

- [Beyond Permission Prompts](https://www.anthropic.com/engineering/beyond-permission-prompts) — Also the primary HITL reference; approval design is the HITL surface. `HE`
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) — Carries HITL interrupts as first-class protocol events. `HE`
- [Decision-Oriented Dialogue for Human-AI Collaboration](https://doi.org/10.48550/arXiv.2305.20076) — Human and agent jointly making decisions under partial information. `XI`
- [PEER: A Collaborative Language Model](https://openreview.net/pdf?id=KbYevcLjnc) — Models the write/review/revise loop explicitly. `XI`
- [AI Chains](https://arxiv.org/abs/2110.01691) — Chained prompts as a transparent, steerable interaction unit. `XI`
- [Helping the Helper: Supporting Peer Counselors](https://doi.org/10.48550/arXiv.2305.08982) — AI-assisted practice and feedback for human counselors. `XI`
- [Human-level play in the game of Diplomacy](https://www.science.org/doi/10.1126/science.ade9097) — Cicero: language plus strategic reasoning in human negotiation. `XI`
- [Mastering the Game of No-Press Diplomacy](https://openreview.net/pdf?id=F61FwJTZhb) — Human-regularized RL and planning. `BK`

---

# 18. Courses and learning paths

Unique to `BK` — the only source with structured curriculum.

- [LLM Agents MOOC Fall 2024](https://llmagents-learning.org/f24) — Song & Chen: foundations, reasoning, planning, tool use, infrastructure, robotics, web. `BK`
- [Advanced LLM Agents MOOC Spring 2025](https://llmagents-learning.org/sp25) — Inference-time techniques, post-training, search, code verification, theorem proving. `BK`
- [Agentic AI MOOC Fall 2025](https://agenticai-learning.org/f25) — Foundations through agentic frameworks, robotics and scientific discovery. `BK`
- [Fall 2024 lecture playlist](https://www.youtube.com/playlist?list=PLS01nW3RtgopsNLeM936V4TNSsvvVglLc) · [Spring 2025](https://www.youtube.com/playlist?list=PLS01nW3RtgorL3AW8REU9nGkzhvtn6Egn) · [Fall 2025](https://www.youtube.com/playlist?list=PLS01nW3RtgoqGkm4UeqNeZLccW-OGc1fJ) — Recorded lectures with named guest speakers. `BK`
- [Multi-Agent AI — Noam Brown](https://www.youtube.com/watch?v=SrLcGdVOb9w) — Lecture on multi-agent systems from a game-solving perspective. `BK`
- [Multi-Agent Systems in the Era of LLMs — Oriol Vinyals](https://www.youtube.com/watch?v=ntjOxjZMaac) — DeepMind view on multi-agent directions. `BK`
- [TapeAgents](https://rdi.berkeley.edu/llm-agents-mooc/assets/tapeagents.pdf) — Resumable, granular "tape" abstraction unifying development and optimization. `BK`

---

# 20. Agent evolution and self-improvement

`LJ` has this as a top-level category and **no other source does**. It is the
cleanest example of why reading all seven mattered: this cluster was invisible in
my first pass, and it is directly relevant to any agent meant to improve in place.

- [STaR: Self-Taught Reasoner](https://openreview.net/pdf?id=_3ELRdg2sgI) — Bootstraps reasoning from a handful of rationales plus rationale-free data. The origin of the self-improvement line. `LJ`
- [Self-Rewarding Language Models](https://arxiv.org/pdf/2401.10020) — Model acts as its own judge during training, removing the fixed reward model ceiling. `LJ`
- [V-STaR: Training Verifiers for Self-Taught Reasoners](https://openreview.net/pdf?id=stmqBSW2dV) — Trains a verifier on *both* correct and incorrect self-generated solutions. `LJ`
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/pdf/2404.14387) — Four-phase framework; the entry point for this whole category. `LJ`
- [A Comprehensive Survey of Self-Evolving AI Agents](https://arxiv.org/abs/2508.07407) — Bridges foundation models and lifelong agentic systems; covers safety and evaluation too. `LJ`
- [SELF-INSTRUCT](https://aclanthology.org/2023.acl-long.754.pdf) — Near annotation-free instruction generation from the model itself. `LJ`
- [CREAM: Consistency Regularized Self-Rewarding Language Models](https://openreview.net/pdf?id=Vf6RDObyEF) — Uses reward consistency to filter unreliable self-generated preference data. `LJ`
- [RLCD: RL from Contrastive Distillation](https://openreview.net/pdf?id=v3XXtxWKi6) — Builds preference pairs from contrasting prompts, no human feedback. `LJ`
- [Language Model Self-Improvement by RL Contemplation](https://openreview.net/pdf?id=38E4yUbrgr) — Exploits the gap between evaluating and generating. `LJ`
- [EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079) — Distills past runs into abstract principles that guide later decisions. `LJ`
- [Self-Improving LLM Agents at Test-Time](https://arxiv.org/abs/2510.07841) — Agent spots its own uncertain predictions, synthesizes similar examples, fine-tunes on them. `LJ`
- [SE-Agent: Self-Evolution Trajectory Optimization](https://arxiv.org/abs/2508.02085) — Revision, recombination and refinement to widen the search space across trajectories. `LJ`
- [CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards](https://arxiv.org/abs/2510.08529) — Intrinsic rewards derived from inter-agent discussion, no external supervision. `LJ` `ZJ`
- [Coevolving with the Other You](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c2b1c8f7d317719a9ce32dd7386ba35-Paper-Conference.pdf) — CORY: cooperative multi-agent RL for fine-tuning, beating PPO on real-world refinement. `LJ`
- [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning](https://arxiv.org/abs/2503.15478) — Step-level rewards from a critic with training-time information; introduces ColBench. `LJ`
- [STeCa: Step-level Trajectory Calibration](https://arxiv.org/abs/2502.14276) — Builds calibrated trajectories via step-level reward comparison and reflection. `LJ` `ZJ`
- [PVPO: Pre-Estimated Value-Based Policy Optimization](https://arxiv.org/abs/2508.21104) — Advantage reference anchor plus pre-sampling to cut rollout dependence. `LJ`
- [Atom-Searcher](https://arxiv.org/abs/2508.12800) — Atomic Thought reward units for fine-grained deep-research supervision. `LJ`
- [Memory-R1](https://arxiv.org/abs/2508.19828) — RL framework with two agents learning to manage external memory actively. `LJ`
- [Agents of Change: Self-Evolving LLM Agents for Strategic Planning](https://arxiv.org/abs/2506.04651) — Uses Catan as a strategic benchmark for self-improving architectures. `LJ`
- [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://arxiv.org/abs/2407.06813) — Strategic planning plus self-play evolution without human intervention. `LJ`
- [Motif: Intrinsic Motivation from AI Feedback](https://arxiv.org/pdf/2310.00166) — Turns LLM priors into intrinsic rewards for an RL agent. `LJ`
- [Agent Alignment in Evolving Social Norms](https://arxiv.org/pdf/2401.04620) — Recasts alignment as evolution and selection over agent populations. `LJ`
- [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://arxiv.org/abs/2501.05707) — Specializes models on multiagent-generated data to preserve diversity. `LJ`
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) — Evolutionary coding agent that autonomously improves and discovers algorithms. `LJ`
- [Evolutionary optimization of model merging recipes](https://www.nature.com/articles/s42256-024-00975-8) — Evolutionary search over merge recipes across two spaces. `LJ`
- [Symbolic Learning Enables Self-Evolving Agents](https://arxiv.org/abs/2406.18532v1) — Agent-symbolic learning treating prompts and pipelines as learnable. `ZJ`
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) — Backpropagates natural-language feedback through compound systems. `ZJ`
- [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://arxiv.org/abs/2410.06153) — Searches over modular agent designs automatically. `ZJ`
- [AutoAct: Automatic Agent Learning from Scratch via Self-Planning](https://arxiv.org/abs/2401.05268) — Synthesizes its own trajectories with no external supervision. `ZJ` `LJ`
- [KnowAgent: Knowledge-Augmented Planning](https://arxiv.org/abs/2403.03101) — Action knowledge base plus self-learning to curb planning hallucination. `ZJ` `LJ`
- [Agent Planning with World Knowledge Model](https://arxiv.org/abs/2405.14205) — Parametric world-knowledge model guiding global and local planning. `ZJ` `LJ`
- [ATLaS: Agent Tuning via Learning Critical Steps](https://arxiv.org/abs/2503.02197) — Tunes only on critical expert-trajectory steps, cutting cost. `LJ`
- [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) — GiGPO: hierarchical grouping for credit assignment in agent RL. `ZJ`
- [SPA-RL: Stepwise Progress Attribution](https://arxiv.org/abs/2505.20732) — Attributes final reward to intermediate steps as progress. `ZJ`
- [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) — RL directly on long-horizon interactive tasks. `ZJ`
- [In-the-Flow Agentic System Optimization](https://arxiv.org/abs/2510.05592) — Optimizes planning and tool use inside the running system. `ZJ`
- [Self-Evolved Diverse Data Sampling (DIVERSEEVOL)](https://arxiv.org/pdf/2311.08182) — Self-evolving selection for label-efficient instruction tuning. `LJ`
- [SELFEVOLVE: A Code Evolution Framework](https://arxiv.org/pdf/2306.02907) — Two-step knowledge-provider then self-reflective-programmer pipeline. `LJ`
- [Large Language Models are Better Reasoners with Self-Verification](https://aclanthology.org/2023.findings-emnlp.167.pdf) — Backward verification over CoT conclusions. `LJ`
- [CodeT: Code Generation with Generated Tests](https://openreview.net/pdf?id=ktrw68Cmu9c) — Auto-generates test cases to select among candidate programs. `LJ`
- [AlpacaFarm](https://proceedings.neurips.cc/paper_files/paper/2023/file/5fc47800ee5b30b8777fdd30abcaaf3b-Paper-Conference.pdf) — Cheap simulated feedback for developing and validating RLHF methods. `LJ`
- [Benchmark Self-Evolving](https://arxiv.org/pdf/2402.11443) — Multi-agent framework that extends benchmarks dynamically. `LJ`
- [LLM-Evolve](https://aclanthology.org/2024.emnlp-main.940.pdf) — Extends static benchmarks into sequential settings so models learn from history. `LJ`

---

# 21. Ethics, societal risk and cost

Also unique to `LJ`, and the oldest material in the whole corpus (2019–2022).
Worth keeping separate from security: these are governance and externality
questions, not attack surfaces.

- [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) — The foundational critique of scale-first language modelling. `LJ`
- [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) — Named the category; emergence and homogenization as the two central dynamics. `LJ`
- [Predictability and Surprise in Large Generative Models](https://dl.acm.org/doi/abs/10.1145/3531146.3533229) — Loss is predictable, capabilities are not; the governance problem that follows. `LJ`
- [Ethical and social risks of harm from Language Models](https://arxiv.org/abs/2112.04359) — Six risk areas, 21 named risks; still the clearest taxonomy. `LJ`
- [Foundation Models and Fair Use](https://www.jmlr.org/papers/v24/23-0569.html) — Legal exposure from training on copyrighted data plus technical mitigations. `LJ`
- [Estimating the Carbon Footprint of BLOOM](https://www.jmlr.org/papers/v24/23-0069.html) — Full life-cycle accounting including inference. `LJ`
- [Energy and Policy Considerations for Modern Deep Learning Research](https://ojs.aaai.org/index.php/AAAI/article/view/7123) — Compute cost as an equity problem, not just a budget one. `LJ`
- [Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims](https://arxiv.org/abs/2004.07213) — Ten concrete mechanisms for making claims checkable. `LJ`
- [Actionable Auditing](https://dl.acm.org/doi/abs/10.1145/3306618.3314244) — Evidence that publishing audit results actually changes vendor behaviour. `LJ`
- [PALMS with Values-Targeted Datasets](https://proceedings.neurips.cc/paper_files/paper/2021/hash/2e855f9489df0712b4bd8ea9e2848c5a-Abstract.html) — Small curated datasets can shift model behaviour measurably. `LJ`
- [Defending Against Neural Fake News](https://proceedings.neurips.cc/paper/2019/hash/3e9f0fc9b2f89e043bc6233994dfcf76-Abstract.html) — Grover; generation and detection as two sides of one model. `LJ`
- [Medical LLMs are vulnerable to data-poisoning attacks](https://www.nature.com/articles/s41591-024-03445-1) — Low-ratio poisoning is enough; proposes graph-based mitigation. `LJ`
- [Medical LLMs are susceptible to targeted misinformation attacks](https://doi.org/10.1038/s41746-024-01282-7) — 1.1% weight manipulation injects false facts. `LJ`
- [Deconstructing The Ethics of Large Language Models](https://ui.adsabs.harvard.edu/abs/2024arXiv240605392D/abstract) — Survey from long-standing issues to newly emerging dilemmas. `LJ`

---

# 22. Where this corpus is still thin

Revised now that all seven are read.

1. **`VA`'s Agent Tooling (95) and Security (82) sections remain unread.** The security gap is now largely covered by `LJ` and `ZJ` independently, so the real remaining hole is 2026 tooling papers.
2. **`HE` tail unread**: task runners, verification & CI, debugging/DX, human-in-the-loop, reference implementations, sandbox, templates. Category 17 is still thin as a result.
3. **Vendor primary docs and changelogs are barely present.** For a wiki tracking state of the art, release notes move faster than any curated list. Your existing feed list is the better source.
4. **Multimodal and media generation is absent across all seven.** Nothing covers image/video/audio generation agents. Given what you build, this gap is structural and won't be closed by adding more agent lists — it needs its own sources.
5. **`LJ`'s venue metadata is unexploited.** It's the single best quality signal in the corpus and currently sits unparsed in one README.

## Data-quality note: the source lists contain wrong links

Deduplicating by canonical arXiv ID surfaced a collision that a URL-based dedup
would have missed entirely: `XI` lists **FireAct** with `arxiv.org/abs/2305.16291`,
which is actually **Voyager**. Two different papers, one ID, in the same file.
FireAct is `2310.05915` — and notably, `LJ` links it correctly, which is how the
error is confirmable rather than merely suspicious.

This matters beyond the one entry:

- **Canonical-ID dedup is a correctness check, not just a compression step.** Two
  distinct titles collapsing to one ID means one of them is wrong. The pipeline
  should *report* these rather than silently merge them — merging would have
  deleted FireAct from the corpus.
- **Cited-by counts are corruptible.** Had another list also cited Voyager,
  FireAct's bad link would have inflated Voyager's apparent cross-source
  agreement, and the canon ranking would have been quietly wrong.
- **Cross-source disagreement is the repair mechanism.** Because `LJ` has the
  right link and `XI` has the wrong one, majority-vote on the ID for a given title
  resolves it automatically. That is a second, stronger argument for merging these
  lists rather than picking one.
