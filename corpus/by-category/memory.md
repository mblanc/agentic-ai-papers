# memory

70 entries.

- [MAGMA: A Multi-Graph based Agentic Memory Architecture](https://arxiv.org/abs/2601.03236)
  - `arxiv:2601.03236` · cited by 2: HE, VA
  - summary: Orthogonal semantic, temporal, causal and entity graphs with policy-guided traversal.

- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)
  - `arxiv:2502.12110` · cited by 1: LJ
  - summary: Organizes agent memory as a Zettelkasten-style network where each new note is auto-tagged and linked to related past memories, and adding a memory can revise existing ones, so the store keeps re-organizing itself instead of being fixed storage.

- [agentmemory](https://github.com/rohitg00/agentmemory)
  - `gh:rohitg00/agentmemory` · cited by 1: HE
  - summary: Drop-in persistent memory for coding agents that captures each session and injects relevant hybrid-searched (BM25 + vector + graph) context into later ones across Claude Code, Copilot, and Cursor, cutting repeated re-explanation.

- [AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval](https://arxiv.org/pdf/2602.05524v1)
  - `arxiv:2602.05524` · cited by 1: VA
  - summary: Retrieves similar past decisions to adapt inventory ordering.

- [AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/pdf/2601.20352v2)
  - `arxiv:2601.20352` · cited by 1: VA
  - summary: Hierarchical granularity with adaptive routing and consistency verification.

- [AMER-RCL: Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices](https://arxiv.org/pdf/2601.02732v1)
  - `arxiv:2601.02732` · cited by 1: VA
  - summary: Localizes microservice failures with a multi-agent recursive-reasoning loop whose agentic memory reuses conclusions from prior alerts, cutting redundant analysis and latency versus schema-bound baselines.

- [Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning](https://arxiv.org/pdf/2601.06282v1)
  - `arxiv:2601.06282` · cited by 1: VA
  - summary: Builds episodic narratives from fragments and semanticizes peripheral facts offline.

- [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/pdf/2601.08323v2)
  - `arxiv:2601.08323` · cited by 1: VA
  - summary: Decomposes memory into CRUD ops and learns the policy via SFT+RL.

- [Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents](https://arxiv.org/pdf/2601.07468v1)
  - `arxiv:2601.07468` · cited by 1: VA
  - summary: Organizes by actual occurrence time rather than dialogue order.

- [Beyond Static Summarization: Proactive Memory Extraction for LLM Agents](https://arxiv.org/pdf/2601.04463v1)
  - `arxiv:2601.04463` · cited by 1: VA
  - summary: Self-questioning loops recover information one-off summarization drops.

- [BudgetMem: Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory](https://arxiv.org/pdf/2602.06025v1)
  - `arxiv:2602.06025` · cited by 1: VA
  - summary: Routes memory queries to processing tiers by difficulty for runtime cost control.

- [Building an Agentic Memory System for GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
  - `url:https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot` · cited by 1: HE
  - summary: GitHub Copilot's cross-agent memory stores learned facts with citations to code locations and re-verifies them just-in-time at recall, so shared memory does not drift as the codebase changes.

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
  - `url:https://anthropic.com/research/building-effective-agents` · cited by 1: HE
  - summary: Anthropic on composing simple primitives, and when a workflow beats an agent.

- [claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler)
  - `gh:coleam00/claude-memory-compiler` · cited by 1: HE
  - summary: Uses Claude Code hooks to distill each conversation's decisions and lessons into compiled articles that feed back into later sessions, giving an agent evolving memory without a vector database.

- [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/abs/2604.10352)
  - `arxiv:2604.10352` · cited by 1: HE
  - summary: Treats the context window as OS-style virtual memory managed by the harness (typed pages with validated writeback at every lifecycle boundary), eliminating the state loss agents suffer after compaction or reset, at under 50 microseconds overhead per turn.

- [Codified Context: Infrastructure for AI Agents in a Complex Codebase](https://arxiv.org/abs/2602.20478)
  - `arxiv:2602.20478` · cited by 1: HE
  - summary: Documents a three-tier 'codified context' setup (a hot-memory constitution of conventions, specialized domain agents, and a cold-memory spec base) built while shipping a 108k-line codebase to stop agents forgetting project conventions across sessions.

- [cognee](https://github.com/topoteretes/cognee)
  - `gh:topoteretes/cognee` · cited by 1: HE
  - summary: An open-source memory layer that ingests an agent's data into a self-hosted knowledge graph, giving persistent cross-session recall instead of flat vector retrieval.

- [Cognitive AI Memory: A Framework for More Human-like Memory in LLMs](https://arxiv.org/abs/2505.13044)
  - `arxiv:2505.13044` · cited by 1: LJ
  - summary: A cognitively-inspired memory framework splitting long-term interaction into a controller, a retrieval filter, and a 'post-thinking' maintenance step, aimed at agents that must adapt to a user across many sessions.

- [Connect the Dots: Knowledge Graph-Guided Crawler Attack on Retrieval-Augmented Generation Systems](https://arxiv.org/pdf/2601.15678v2)
  - `arxiv:2601.15678` · cited by 1: VA
  - summary: Frames stealing a RAG knowledge base as a coverage-maximization problem and builds RAGCrawler, which schedules non-redundant queries to extract 66.8% of a corpus within 1,000 queries, a concrete IP-theft threat against retrieval stores.

- [Continual learning for AI agents](https://blog.langchain.com/continual-learning-for-ai-agents/)
  - `url:https://blog.langchain.com/continual-learning-for-ai-agents` · cited by 1: HE
  - summary: Frames agent improvement as happening across three layers (model weights, the harness, and external context/memory) and argues most teams should target the latter two via trace-driven updates rather than retraining.

- [Continuum Memory Architectures for Long-Horizon LLM Agents](https://arxiv.org/pdf/2601.09913v1)
  - `arxiv:2601.09913` · cited by 1: VA
  - summary: Defines persistent temporally-chained state as a class distinct from stateless RAG.

- [Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction](https://arxiv.org/pdf/2601.05107v1)
  - `arxiv:2601.05107` · cited by 1: VA
  - summary: Models memory reliance as an explicit user-steerable dimension.

- [Dep-Search: Learning Dependency-Aware Reasoning Traces with Persistent Memory](https://arxiv.org/pdf/2601.18771v1)
  - `arxiv:2601.18771` · cited by 1: VA
  - summary: GRPO-trained dependency-aware decomposition with persistent intermediate results.

- [E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/pdf/2601.21714v1)
  - `arxiv:2601.21714` · cited by 1: VA
  - summary: Keeps uncompressed contexts in assistants, replacing destructive compression with reconstruction.

- [engram](https://github.com/Gentleman-Programming/engram)
  - `gh:gentleman-programming/engram` · cited by 1: HE
  - summary: Single Go binary, SQLite+FTS5, 18 MCP tools for save/search/session lifecycle.

- [Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory](https://arxiv.org/abs/2603.17781)
  - `arxiv:2603.17781` · cited by 1: HE
  - summary: Benchmarks prompt-stored facts against hash-addressed 'Knowledge Objects' and shows in-context memory collapses in production (compaction destroys 60% of facts, drift erodes 54% of constraints) while KOs stay 100% accurate at 252x lower cost.

- [FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory](https://arxiv.org/pdf/2601.18642v2)
  - `arxiv:2601.18642` · cited by 1: VA
  - summary: Adaptive exponential decay with LLM-guided conflict resolution.

- [GAAMA: Graph Augmented Associative Memory for Agents](https://arxiv.org/abs/2603.27910)
  - `arxiv:2603.27910` · cited by 1: HE
  - summary: A graph memory that routes retrieval through concept nodes rather than entities to dodge the mega-hub problem of conversational knowledge graphs, plus a post-retrieval repair step, reaching 79.1% on LoCoMo-10.

- [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/pdf/2602.05665v1)
  - `arxiv:2602.05665` · cited by 1: VA
  - summary: Extraction, storage, retrieval and temporal evolution of graph memory.

- [Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures](https://arxiv.org/abs/2603.17244)
  - `arxiv:2603.17244` · cited by 1: HE
  - summary: Grounds agent memory in formal belief-revision (AGM) semantics as a versioned property graph of immutable revisions with typed dependency edges, hitting 93.3% on the implicit-constraint LoCoMo-Plus benchmark where the best baseline scores 45.7%.

- [Grounding Agent Memory in Contextual Intent](https://arxiv.org/pdf/2601.10702v1)
  - `arxiv:2601.10702` · cited by 1: VA
  - summary: Indexes trajectory steps by intent cues to cut interference in long-horizon tasks.

- [HiMeS: Hippocampus-inspired Memory System for Personalized AI Assistants](https://arxiv.org/pdf/2601.06152v1)
  - `arxiv:2601.06152` · cited by 1: VA
  - summary: RL-trained short-term extraction fused with partitioned long-term memory.

- [Hindsight](https://github.com/vectorize-io/hindsight)
  - `gh:vectorize-io/hindsight` · cited by 1: HE
  - summary: Self-hostable long-term memory with LangChain/CrewAI/LlamaIndex/MCP integrations.

- [How We Built Agent Builder's Memory System](https://blog.langchain.com/how-we-built-agent-builders-memory-system/)
  - `url:https://blog.langchain.com/how-we-built-agent-builders-memory-system` · cited by 1: HE
  - summary: Implements LangSmith Agent Builder's memory as plain files the agent reads and edits, betting that models handle filesystems well enough to skip specialized memory tooling.

- [Investigating Tool-Memory Conflicts in Tool-Augmented LLMs](https://arxiv.org/pdf/2601.09760v1)
  - `arxiv:2601.09760` · cited by 1: VA
  - summary: Names and measures 'tool-memory conflict', when an LLM's parametric knowledge contradicts what a tool returns, showing it is common on STEM tasks and that current prompting and RAG mitigations fail to resolve it.

- [Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory](https://arxiv.org/pdf/2601.07470v1)
  - `arxiv:2601.07470` · cited by 1: VA
  - summary: Trains a memory copilot via DPO to decide how memories get structured.

- [Learning to Share: Selective Memory for Efficient Parallel Agentic Systems](https://arxiv.org/pdf/2602.05965v1)
  - `arxiv:2602.05965` · cited by 1: VA
  - summary: Learned controller decides what passes between parallel agent teams.

- [Letta (MemGPT)](https://github.com/letta-ai/letta)
  - `gh:letta-ai/letta` · cited by 1: HE
  - related: <https://www.letta.com/blog/letta-v1-agent>
  - summary: Reference stateful-agent architecture with core/archival/recall tiers.

- [LIDL: LLM Integration Defect Localization via Knowledge Graph-Enhanced Multi-Agent Analysis](https://arxiv.org/pdf/2601.05539v1)
  - `arxiv:2601.05539` · cited by 1: VA
  - summary: Localizes defects in LLM-integrated software by building an annotated knowledge graph across prompts, API calls, and outputs and reasoning over fused error traces, reaching 0.64 Top-3 accuracy (64.1% over the best baseline) at 92.5% lower cost.

- [LSTM-MAS: A Long Short-Term Memory Inspired Multi-Agent System for Long-Context Understanding](https://arxiv.org/pdf/2601.11913v1)
  - `arxiv:2601.11913` · cited by 1: VA
  - summary: Mirrors LSTM gates in a multi-agent chain, each node running comprehension, redundancy-pruning, error-detection, and flow-control agents, to pass long-context information forward while curbing error accumulation.

- [MAGE: Memory as Agent-Guided Exploration](https://arxiv.org/abs/2606.06090)
  - `arxiv:2606.06090` · cited by 1: HE
  - summary: Argues long-horizon agent memory should track execution state, not semantic similarity, storing interactions in a state tree with grow/compress/revise operations that isolate erroneous branches, for +7.8-20.4pp success and 55% fewer tokens on MemoryArena.

- [Making Theft Useless: Adulteration-Based Protection of Proprietary Knowledge Graphs in GraphRAG Systems](https://arxiv.org/pdf/2601.00274v1)
  - `arxiv:2601.00274` · cited by 1: VA
  - summary: Protects a proprietary GraphRAG knowledge graph by seeding it with plausible-false 'adulterants' that authorized users filter with a secret key, dropping a thief's accuracy to 5.3% while legitimate queries stay 100% correct.

- [mem0](https://github.com/mem0ai/mem0)
  - `gh:mem0ai/mem0` · cited by 1: HE
  - summary: Drop-in universal memory layer; lowest-integration path to cross-session retention.

- [Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://arxiv.org/pdf/2601.19935v1)
  - `arxiv:2601.19935` · cited by 1: VA
  - summary: Whether agents proactively *act* on long-term memory, not just retrieve.

- [MemArchitect: A Policy-Driven Memory Governance Layer](https://arxiv.org/abs/2603.18330)
  - `arxiv:2603.18330` · cited by 1: HE
  - summary: A governance layer over agent memory that enforces rule-based decay, conflict resolution, and privacy controls to keep stale 'zombie memories' out of the context window, treating memory lifecycle as policy rather than passive storage.

- [Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents](https://arxiv.org/pdf/2601.03785v2)
  - `arxiv:2601.03785` · cited by 1: VA
  - summary: Topic Loom groups same-topic turns into boxes linked by event timelines.

- [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/pdf/2601.20831v1)
  - `arxiv:2601.20831` · cited by 1: VA
  - summary: Trainable gate decides which observations to retain, update or discard.

- [MemoCue: Empowering LLM-Based Agents for Human Memory Recall via Strategy-Guided Querying](https://arxiv.org/abs/2507.23633)
  - `arxiv:2507.23633` · cited by 1: LJ
  - summary: Helps a person recall vague memories by rewriting their query into cue-rich prompts chosen from fifteen strategy patterns via tree search, improving recall inspiration 17.74% over plain LLM prompting.

- [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/pdf/2601.05504v2)
  - `arxiv:2601.05504` · cited by 1: VA
  - summary: Stress-tests memory-poisoning attacks on clinical-record agents and finds pre-existing legitimate memories blunt them, then proposes trust-scored moderation and decay-based memory sanitization as defenses.

- [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)
  - `arxiv:2508.19828` · cited by 1: LJ
  - summary: RL framework with two agents learning to manage external memory actively.

- [MemPalace](https://github.com/MemPalace/mempalace)
  - `gh:mempalace/mempalace` · cited by 1: HE
  - summary: A local-first memory that stores conversations verbatim and retrieves by semantic search with no summarization step, keeping 96.6% retrieval accuracy without cloud calls.

- [MemTrust: A Zero-Trust Architecture for Unified AI Memory System](https://arxiv.org/pdf/2601.07004v1)
  - `arxiv:2601.07004` · cited by 1: VA
  - summary: Puts a unified cross-agent memory behind a hardware zero-trust (TEE) architecture across five layers so users get local-equivalent security while still sharing memory across apps, targeting the trust gap in centralized memory services.

- [MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents](https://arxiv.org/pdf/2601.05215v2)
  - `arxiv:2601.05215` · cited by 1: VA
  - summary: Memory-aware Minecraft tasks with machine-checkable validators.

- [On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266)
  - `arxiv:2412.15266` · cited by 1: LJ
  - summary: Systematically compares memory representations (chunks, triples, atomic facts, summaries) and retrieval methods for agents, finding mixed structures most noise-resilient and iterative retrieval consistently best.

- [ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents](https://arxiv.org/pdf/2602.01869v1)
  - `arxiv:2602.01869` · cited by 1: VA
  - summary: Saves step-by-step procedural skills for reuse without retraining.

- [RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction](https://arxiv.org/pdf/2601.06966v1)
  - `arxiv:2601.06966` · cited by 1: VA
  - summary: 2,000+ cross-session dialogues tracking evolving goals.

- [Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents](https://arxiv.org/abs/2601.22352)
  - `arxiv:2601.22352` · cited by 1: HE
  - summary: Shows a tool-using agent's ability to recover from failed calls follows a measurable law, defining Expected Recovery Regret and validating its first-order link to an efficiency score across five benchmarks.

- [Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs](https://arxiv.org/pdf/2601.08773v1)
  - `arxiv:2601.08773` · cited by 1: VA
  - summary: Benchmarks deterministic against LLM graph construction for code.

- [Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://arxiv.org/pdf/2602.06052v3)
  - `arxiv:2602.06052` · cited by 1: VA
  - summary: Organizes memory by substrate, cognitive mechanism and subject. Best 2026 entry point.

- [ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory](https://arxiv.org/pdf/2601.21545v1)
  - `arxiv:2601.21545` · cited by 1: VA
  - summary: Probes only eligible memory shards under a fixed budget.

- [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/pdf/2601.02553v3)
  - `arxiv:2601.02553` · cited by 1: VA
  - summary: Semantic lossless compression, online synthesis, intent-aware retrieval planning.

- [StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management](https://arxiv.org/pdf/2601.05890v1)
  - `arxiv:2601.05890` · cited by 1: VA
  - summary: Decouples coordination from execution with RL-driven experience reuse.

- [Stash](https://github.com/alash3al/stash)
  - `gh:alash3al/stash` · cited by 1: HE
  - summary: Self-hosted memory with an 8-stage consolidation pipeline; single Docker Compose.

- [SwiftMem: Fast Agentic Memory via Query-aware Indexing](https://arxiv.org/pdf/2601.08160v1)
  - `arxiv:2601.08160` · cited by 1: VA
  - summary: Sub-linear retrieval via temporal/semantic DAG-Tag indexing.

- [TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory)
  - `gh:tencent/tencentdb-agent-memory` · cited by 1: HE
  - summary: Four-tier local pipeline; 61% token cut and 51% relative pass-rate gain on long-horizon tasks.

- [The AI Hippocampus: How Far are We From Human Memory?](https://arxiv.org/pdf/2601.09113v1)
  - `arxiv:2601.09113` · cited by 1: VA
  - summary: Surveys implicit, explicit and agentic memory paradigms including cross-modal.

- [Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/pdf/2601.14192v1)
  - `arxiv:2601.14192` · cited by 1: VA
  - summary: A survey of agent efficiency across memory, tool learning, and planning, cataloguing shared levers like context compression and reward shaping to cut tool calls, and how to measure cost against effectiveness.

- [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/abs/2309.03736)
  - `arxiv:2309.03736` · cited by 1: LJ
  - summary: A financial-trading multi-agent system whose agents organize history into three decaying memory layers and debate with distinct trading personalities, prioritizing recent high-relevance signals for decisions.

- [Warp-Cortex: An Asynchronous, Memory-Efficient Architecture for Million-Agent Cognitive Scaling on Consumer Hardware](https://arxiv.org/pdf/2601.01298v1)
  - `arxiv:2601.01298` · cited by 1: VA
  - summary: An asynchronous multi-agent architecture that shares one weight set and sparsifies the KV-cache to break linear memory scaling, demonstrating 100 concurrent agents in 2.2 GB on a single RTX 4090.

- [Zep](https://github.com/getzep/zep)
  - `gh:getzep/zep` · cited by 1: HE
  - summary: Agent memory store with automatic summarization, entity extraction and semantic session search.
