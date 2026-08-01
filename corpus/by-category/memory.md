# memory

95 entries.

## Timeline

93 dated entries, oldest first.

- [CoLT5: Faster Long-Range Transformers with Conditional Computation](https://arxiv.org/abs/2303.09752) · 2023-03
  - `arxiv:2303.09752` · cited by 1: ZJ
  - summary: CoLT5 spends feedforward and attention compute only on the tokens that matter instead of every token, beating LongT5 on speed and on the SCROLLS long-document benchmark while handling inputs up to 64k tokens.

- [ChatLog: Recording and Analyzing ChatGPT Across Time](https://arxiv.org/abs/2304.14106) · 2023-04
  - `arxiv:2304.14106` · cited by 1: ZJ
  - summary: ChatLog tracks ChatGPT's answers to the same 21 NLP benchmarks month over month since March 2023, showing capability isn't static and giving you a feature signature stable enough to fingerprint which ChatGPT version wrote a given output.

- [Emergent and Predictable Memorization in Large Language Models](https://arxiv.org/abs/2304.11158) · 2023-04
  - `arxiv:2304.11158` · cited by 1: ZJ
  - summary: Builds scaling laws on the Pythia model suite that predict, before training finishes, which training sequences an LLM will end up memorizing verbatim — useful if you care about leaking training data through agent outputs.

- [Unleashing Infinite-Length Input Capacity for Large-scale Language Models with Self-Controlled Memory System](https://arxiv.org/abs/2304.13343) · 2023-04
  - `arxiv:2304.13343` · cited by 1: ZJ
  - summary: The Self-Controlled Memory framework wraps an LLM with a memory stream plus a controller that decides what to keep, letting it handle effectively unlimited input (long dialogues, whole books, meeting transcripts) without retraining and outperforming alternatives on retrieval quality.

- [Zep](https://github.com/getzep/zep) · 2023-04
  - `gh:getzep/zep` · cited by 1: HE
  - summary: Agent memory store with automatic summarization, entity extraction and semantic session search.

- [Adapting Language Models to Compress Contexts](https://arxiv.org/abs/2305.14788) · 2023-05
  - `arxiv:2305.14788` · cited by 1: ZJ
  - summary: Fine-tunes OPT/Llama-2 to squeeze long context into compact summary vectors the model reads as soft prompts, cutting inference cost while extending effective context and improving retrieval and few-shot performance.

- [ChatGPT/GPT-4 for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities](https://arxiv.org/abs/2305.13168) · 2023-05
  - `arxiv:2305.13168` · cited by 1: ZJ
  - summary: Benchmarking GPT-4 on entity/relation/event extraction, link prediction and QA finds it's a mediocre few-shot extractor but a strong reasoner over knowledge graphs, which motivates AutoKG, a multi-agent pipeline combining LLMs with external sources for KG construction.

- [Landmark Attention: Random-Access Infinite Context Length for Transformers](https://arxiv.org/abs/2305.16300) · 2023-05
  - `arxiv:2305.16300` · cited by 1: ZJ
  - summary: Landmark Attention lets a transformer attend over its full context via retrievable block-level landmark tokens instead of a separate retrieval pipeline, and was used to stretch LLaMA-7B's context past 32k tokens at roughly GPT-4-era length with Transformer-XL-level quality.

- [Learning to Reason and Memorize with Self-Notes](https://arxiv.org/abs/2305.00833) · 2023-05
  - `arxiv:2305.00833` · cited by 1: ZJ
  - summary: Lets a model pause mid-generation to write free-form "Self-Notes" it can reread later, giving it working memory and on-the-fly reasoning that beats standard chain-of-thought on multi-step tasks.

- [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) · 2023-05
  - `arxiv:2305.10250` · cited by 1: ZJ
  - summary: Ebbinghaus-inspired forgetting curve over stored conversation memory.

- [Monotonic Location Attention for Length Generalization](https://arxiv.org/abs/2305.20019) · 2023-05
  - `arxiv:2305.20019` · cited by 1: ZJ
  - summary: Shows that interpolating a sequence's forward and reversed encodings with relative attention gets seq2seq models to near-perfect length generalization on lookup/copy tasks, and extends the idea with new location-attention variants for harder cases like SCAN and CFQ.

- [Randomized Positional Encodings Boost Length Generalization of Transformers](https://arxiv.org/abs/2305.16843) · 2023-05
  - `arxiv:2305.16843` · cited by 1: ZJ
  - summary: Randomizing positional encodings during training — so the model sees position patterns resembling longer sequences than it was trained on — lifts accuracy on unseen-length algorithmic tasks by 12% on average across 6,000 models and 15 tasks, a cheap fix for transformers that otherwise choke past their training length.

- [RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/abs/2305.13304) · 2023-05
  - `arxiv:2305.13304` · cited by 1: ZJ
  - summary: RecurrentGPT fakes an LSTM's long/short-term memory using natural-language state that gets written to and read from disk between paragraphs, letting an LLM generate arbitrarily long, coherent text (and let you inspect or edit its "memory" directly since it's just plain language).

- [RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322) · 2023-05
  - `arxiv:2305.14322` · cited by 1: ZJ
  - summary: RET-LLM gives an LLM an explicit write-read memory that stores facts as subject-predicate-object triplets, so it can extract, save, and later recall knowledge on demand — including handling temporal/date-sensitive questions well.

- [Revisiting Parallel Context Windows: A Frustratingly Simple Alternative and Chain-of-Thought Deterioration](https://arxiv.org/abs/2305.15262) · 2023-05
  - `arxiv:2305.15262` · cited by 1: ZJ
  - summary: Pokes holes in Parallel Context Windows: it's missing an obvious weighted-ensemble baseline for few-shot classification, and it degrades on multi-hop reasoning like HotpotQA through outright question misunderstanding — a caution against treating PCW as a solved way to extend context.

- [Small Models are Valuable Plug-ins for Large Language Models](https://arxiv.org/abs/2305.08848) · 2023-05
  - `arxiv:2305.08848` · cited by 1: ZJ
  - summary: SuperICL pairs a black-box LLM's in-context learning with a small, locally fine-tuned model plugged in as a tool, beating fine-tuned SOTA baselines on supervised tasks and, as a side effect, making the small model itself better at multilingual and interpretability tasks.

- [ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](https://arxiv.org/abs/2305.11554) · 2023-05
  - `arxiv:2305.11554` · cited by 1: ZJ
  - summary: Tools as learned embeddings ("toolkens") on a frozen model.

- [Unlimiformer: Long-Range Transformers with Unlimited Length Input](https://arxiv.org/abs/2305.01625) · 2023-05
  - `arxiv:2305.01625` · cited by 1: ZJ
  - summary: Unlimiformer swaps a transformer's cross-attention for a k-NN index lookup over the whole input, so a pretrained model like BART can process a 500,000-token document without truncation or any added parameters — just wrap it around what you already have.

- [ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory](https://arxiv.org/abs/2306.03901) · 2023-06
  - `arxiv:2306.03901` · cited by 1: ZJ
  - summary: SQL database as symbolic memory with explicit read/write chains.

- [mem0](https://github.com/mem0ai/mem0) · 2023-06
  - `gh:mem0ai/mem0` · cited by 1: HE
  - summary: Drop-in universal memory layer; lowest-integration path to cross-session retention.

- [cognee](https://github.com/topoteretes/cognee) · 2023-08
  - `gh:topoteretes/cognee` · cited by 1: HE
  - summary: An open-source memory layer that ingests an agent's data into a self-hosted knowledge graph, giving persistent cross-session recall instead of flat vector retrieval.

- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) · 2023-09
  - `arxiv:2309.02427` · cited by 2: LJ, ZJ
  - summary: Modular memory, action space and decision procedure. The most useful organizing framework in the pre-2026 literature.

- [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/abs/2309.03736) · 2023-09
  - `arxiv:2309.03736` · cited by 1: LJ
  - summary: A financial-trading multi-agent system whose agents organize history into three decaying memory layers and debate with distinct trading personalities, prioritizing recent high-relevance signals for decisions.

- [Letta (MemGPT)](https://github.com/letta-ai/letta) · 2023-10
  - `gh:letta-ai/letta` · cited by 1: HE
  - related: <https://www.letta.com/blog/letta-v1-agent>
  - summary: Reference stateful-agent architecture with core/archival/recall tiers.

- [JARVIS-1: Open-world Multi-task Agents with Memory-Augmented Multimodal Language Models](https://arxiv.org/abs/2311.05997) · 2023-11
  - `arxiv:2311.05997` · cited by 1: ZJ
  - summary: Multimodal memory-augmented open-world Minecraft agent.

- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) · 2024-04
  - `arxiv:2404.13501` · cited by 2: LJ, ZJ
  - summary: Design and evaluation of agent memory.

- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831) · 2024-05
  - `arxiv:2405.14831` · cited by 2: BK, ZJ
  - summary: Hippocampal-indexing analogy for single-step multi-hop retrieval.

- [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://arxiv.org/abs/2406.04271) · 2024-06
  - `arxiv:2406.04271` · cited by 1: ZJ
  - summary: Buffer of Thoughts caches reusable high-level "thought templates" distilled from prior problem-solving and retrieves/adapts them for new tasks, hitting big accuracy gains (20% on Geometric Shapes, 51% on Checkmate-in-One) at about 12% the cost of tree/graph-of-thought prompting.

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) · 2024-12
  - `url:https://anthropic.com/research/building-effective-agents` · cited by 1: HE
  - summary: Anthropic on composing simple primitives, and when a workflow beats an agent.

- [On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266) · 2024-12
  - `arxiv:2412.15266` · cited by 1: LJ
  - summary: Systematically compares memory representations (chunks, triples, atomic facts, summaries) and retrieval methods for agents, finding mixed structures most noise-resilient and iterative retrieval consistently best.

- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) · 2025-02
  - `arxiv:2502.12110` · cited by 1: LJ
  - summary: Organizes agent memory as a Zettelkasten-style network where each new note is auto-tagged and linked to related past memories, and adding a memory can revise existing ones, so the store keeps re-organizing itself instead of being fixed storage.

- [Cognitive AI Memory: A Framework for More Human-like Memory in LLMs](https://arxiv.org/abs/2505.13044) · 2025-05
  - `arxiv:2505.13044` · cited by 1: LJ
  - summary: A cognitively-inspired memory framework splitting long-term interaction into a controller, a retrieval filter, and a 'post-thinking' maintenance step, aimed at agents that must adapt to a user across many sessions.

- [MemoCue: Empowering LLM-Based Agents for Human Memory Recall via Strategy-Guided Querying](https://arxiv.org/abs/2507.23633) · 2025-07
  - `arxiv:2507.23633` · cited by 1: LJ
  - summary: Helps a person recall vague memories by rewriting their query into cue-rich prompts chosen from fifteen strategy patterns via tree search, improving recall inspiration 17.74% over plain LLM prompting.

- [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) · 2025-08
  - `arxiv:2508.19828` · cited by 1: LJ
  - summary: RL framework with two agents learning to manage external memory actively.

- [Hindsight](https://github.com/vectorize-io/hindsight) · 2025-10
  - `gh:vectorize-io/hindsight` · cited by 2: HE, KY
  - summary: Self-hostable long-term memory with LangChain/CrewAI/LlamaIndex/MCP integrations.

- [AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/pdf/2601.20352v2) · 2026-01
  - `arxiv:2601.20352` · cited by 1: VA
  - summary: Hierarchical granularity with adaptive routing and consistency verification.

- [AMER-RCL: Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices](https://arxiv.org/pdf/2601.02732v1) · 2026-01
  - `arxiv:2601.02732` · cited by 1: VA
  - summary: Localizes microservice failures with a multi-agent recursive-reasoning loop whose agentic memory reuses conclusions from prior alerts, cutting redundant analysis and latency versus schema-bound baselines.

- [Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning](https://arxiv.org/pdf/2601.06282v1) · 2026-01
  - `arxiv:2601.06282` · cited by 1: VA
  - summary: Builds episodic narratives from fragments and semanticizes peripheral facts offline.

- [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/pdf/2601.08323v2) · 2026-01
  - `arxiv:2601.08323` · cited by 1: VA
  - summary: Decomposes memory into CRUD ops and learns the policy via SFT+RL.

- [Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents](https://arxiv.org/pdf/2601.07468v1) · 2026-01
  - `arxiv:2601.07468` · cited by 1: VA
  - summary: Organizes by actual occurrence time rather than dialogue order.

- [Beyond Static Summarization: Proactive Memory Extraction for LLM Agents](https://arxiv.org/pdf/2601.04463v1) · 2026-01
  - `arxiv:2601.04463` · cited by 1: VA
  - summary: Self-questioning loops recover information one-off summarization drops.

- [Building an Agentic Memory System for GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) · 2026-01
  - `url:https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot` · cited by 1: HE
  - summary: GitHub Copilot's cross-agent memory stores learned facts with citations to code locations and re-verifies them just-in-time at recall, so shared memory does not drift as the codebase changes.

- [Connect the Dots: Knowledge Graph-Guided Crawler Attack on Retrieval-Augmented Generation Systems](https://arxiv.org/pdf/2601.15678v2) · 2026-01
  - `arxiv:2601.15678` · cited by 1: VA
  - summary: Frames stealing a RAG knowledge base as a coverage-maximization problem and builds RAGCrawler, which schedules non-redundant queries to extract 66.8% of a corpus within 1,000 queries, a concrete IP-theft threat against retrieval stores.

- [Continuum Memory Architectures for Long-Horizon LLM Agents](https://arxiv.org/pdf/2601.09913v1) · 2026-01
  - `arxiv:2601.09913` · cited by 1: VA
  - summary: Defines persistent temporally-chained state as a class distinct from stateless RAG.

- [Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction](https://arxiv.org/pdf/2601.05107v1) · 2026-01
  - `arxiv:2601.05107` · cited by 1: VA
  - summary: Models memory reliance as an explicit user-steerable dimension.

- [Dep-Search: Learning Dependency-Aware Reasoning Traces with Persistent Memory](https://arxiv.org/pdf/2601.18771v1) · 2026-01
  - `arxiv:2601.18771` · cited by 1: VA
  - summary: GRPO-trained dependency-aware decomposition with persistent intermediate results.

- [E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/pdf/2601.21714v1) · 2026-01
  - `arxiv:2601.21714` · cited by 1: VA
  - summary: Keeps uncompressed contexts in assistants, replacing destructive compression with reconstruction.

- [FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory](https://arxiv.org/pdf/2601.18642v2) · 2026-01
  - `arxiv:2601.18642` · cited by 1: VA
  - summary: Adaptive exponential decay with LLM-guided conflict resolution.

- [Grounding Agent Memory in Contextual Intent](https://arxiv.org/pdf/2601.10702v1) · 2026-01
  - `arxiv:2601.10702` · cited by 1: VA
  - summary: Indexes trajectory steps by intent cues to cut interference in long-horizon tasks.

- [HiMeS: Hippocampus-inspired Memory System for Personalized AI Assistants](https://arxiv.org/pdf/2601.06152v1) · 2026-01
  - `arxiv:2601.06152` · cited by 1: VA
  - summary: RL-trained short-term extraction fused with partitioned long-term memory.

- [Investigating Tool-Memory Conflicts in Tool-Augmented LLMs](https://arxiv.org/pdf/2601.09760v1) · 2026-01
  - `arxiv:2601.09760` · cited by 1: VA
  - summary: Names and measures 'tool-memory conflict', when an LLM's parametric knowledge contradicts what a tool returns, showing it is common on STEM tasks and that current prompting and RAG mitigations fail to resolve it.

- [Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory](https://arxiv.org/pdf/2601.07470v1) · 2026-01
  - `arxiv:2601.07470` · cited by 1: VA
  - summary: Trains a memory copilot via DPO to decide how memories get structured.

- [LIDL: LLM Integration Defect Localization via Knowledge Graph-Enhanced Multi-Agent Analysis](https://arxiv.org/pdf/2601.05539v1) · 2026-01
  - `arxiv:2601.05539` · cited by 1: VA
  - summary: Localizes defects in LLM-integrated software by building an annotated knowledge graph across prompts, API calls, and outputs and reasoning over fused error traces, reaching 0.64 Top-3 accuracy (64.1% over the best baseline) at 92.5% lower cost.

- [LSTM-MAS: A Long Short-Term Memory Inspired Multi-Agent System for Long-Context Understanding](https://arxiv.org/pdf/2601.11913v1) · 2026-01
  - `arxiv:2601.11913` · cited by 1: VA
  - summary: Mirrors LSTM gates in a multi-agent chain, each node running comprehension, redundancy-pruning, error-detection, and flow-control agents, to pass long-context information forward while curbing error accumulation.

- [MAGMA: A Multi-Graph based Agentic Memory Architecture](https://arxiv.org/abs/2601.03236) · 2026-01
  - `arxiv:2601.03236` · cited by 2: HE, VA
  - summary: Orthogonal semantic, temporal, causal and entity graphs with policy-guided traversal.

- [Making Theft Useless: Adulteration-Based Protection of Proprietary Knowledge Graphs in GraphRAG Systems](https://arxiv.org/pdf/2601.00274v1) · 2026-01
  - `arxiv:2601.00274` · cited by 1: VA
  - summary: Protects a proprietary GraphRAG knowledge graph by seeding it with plausible-false 'adulterants' that authorized users filter with a secret key, dropping a thief's accuracy to 5.3% while legitimate queries stay 100% correct.

- [Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://arxiv.org/pdf/2601.19935v1) · 2026-01
  - `arxiv:2601.19935` · cited by 1: VA
  - summary: Whether agents proactively *act* on long-term memory, not just retrieve.

- [Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents](https://arxiv.org/pdf/2601.03785v2) · 2026-01
  - `arxiv:2601.03785` · cited by 1: VA
  - summary: Topic Loom groups same-topic turns into boxes linked by event timelines.

- [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/pdf/2601.20831v1) · 2026-01
  - `arxiv:2601.20831` · cited by 1: VA
  - summary: Trainable gate decides which observations to retain, update or discard.

- [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/pdf/2601.05504v2) · 2026-01
  - `arxiv:2601.05504` · cited by 1: VA
  - summary: Stress-tests memory-poisoning attacks on clinical-record agents and finds pre-existing legitimate memories blunt them, then proposes trust-scored moderation and decay-based memory sanitization as defenses.

- [MemTrust: A Zero-Trust Architecture for Unified AI Memory System](https://arxiv.org/pdf/2601.07004v1) · 2026-01
  - `arxiv:2601.07004` · cited by 1: VA
  - summary: Puts a unified cross-agent memory behind a hardware zero-trust (TEE) architecture across five layers so users get local-equivalent security while still sharing memory across apps, targeting the trust gap in centralized memory services.

- [MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents](https://arxiv.org/pdf/2601.05215v2) · 2026-01
  - `arxiv:2601.05215` · cited by 1: VA
  - summary: Memory-aware Minecraft tasks with machine-checkable validators.

- [RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction](https://arxiv.org/pdf/2601.06966v1) · 2026-01
  - `arxiv:2601.06966` · cited by 1: VA
  - summary: 2,000+ cross-session dialogues tracking evolving goals.

- [Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents](https://arxiv.org/abs/2601.22352) · 2026-01
  - `arxiv:2601.22352` · cited by 1: HE
  - summary: Shows a tool-using agent's ability to recover from failed calls follows a measurable law, defining Expected Recovery Regret and validating its first-order link to an efficiency score across five benchmarks.

- [Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs](https://arxiv.org/pdf/2601.08773v1) · 2026-01
  - `arxiv:2601.08773` · cited by 1: VA
  - summary: Benchmarks deterministic against LLM graph construction for code.

- [ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory](https://arxiv.org/pdf/2601.21545v1) · 2026-01
  - `arxiv:2601.21545` · cited by 1: VA
  - summary: Probes only eligible memory shards under a fixed budget.

- [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/pdf/2601.02553v3) · 2026-01
  - `arxiv:2601.02553` · cited by 1: VA
  - summary: Semantic lossless compression, online synthesis, intent-aware retrieval planning.

- [StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management](https://arxiv.org/pdf/2601.05890v1) · 2026-01
  - `arxiv:2601.05890` · cited by 1: VA
  - summary: Decouples coordination from execution with RL-driven experience reuse.

- [SwiftMem: Fast Agentic Memory via Query-aware Indexing](https://arxiv.org/pdf/2601.08160v1) · 2026-01
  - `arxiv:2601.08160` · cited by 1: VA
  - summary: Sub-linear retrieval via temporal/semantic DAG-Tag indexing.

- [The AI Hippocampus: How Far are We From Human Memory?](https://arxiv.org/pdf/2601.09113v1) · 2026-01
  - `arxiv:2601.09113` · cited by 1: VA
  - summary: Surveys implicit, explicit and agentic memory paradigms including cross-modal.

- [Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/pdf/2601.14192v1) · 2026-01
  - `arxiv:2601.14192` · cited by 1: VA
  - summary: A survey of agent efficiency across memory, tool learning, and planning, cataloguing shared levers like context compression and reward shaping to cut tool calls, and how to measure cost against effectiveness.

- [Warp-Cortex: An Asynchronous, Memory-Efficient Architecture for Million-Agent Cognitive Scaling on Consumer Hardware](https://arxiv.org/pdf/2601.01298v1) · 2026-01
  - `arxiv:2601.01298` · cited by 1: VA
  - summary: An asynchronous multi-agent architecture that shares one weight set and sparsifies the KV-cache to break linear memory scaling, demonstrating 100 concurrent agents in 2.2 GB on a single RTX 4090.

- [agentmemory](https://github.com/rohitg00/agentmemory) · 2026-02
  - `gh:rohitg00/agentmemory` · cited by 1: HE
  - summary: Drop-in persistent memory for coding agents that captures each session and injects relevant hybrid-searched (BM25 + vector + graph) context into later ones across Claude Code, Copilot, and Cursor, cutting repeated re-explanation.

- [AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval](https://arxiv.org/pdf/2602.05524v1) · 2026-02
  - `arxiv:2602.05524` · cited by 1: VA
  - summary: Retrieves similar past decisions to adapt inventory ordering.

- [BudgetMem: Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory](https://arxiv.org/pdf/2602.06025v1) · 2026-02
  - `arxiv:2602.06025` · cited by 1: VA
  - summary: Routes memory queries to processing tiers by difficulty for runtime cost control.

- [Codified Context: Infrastructure for AI Agents in a Complex Codebase](https://arxiv.org/abs/2602.20478) · 2026-02
  - `arxiv:2602.20478` · cited by 1: HE
  - summary: Documents a three-tier 'codified context' setup (a hot-memory constitution of conventions, specialized domain agents, and a cold-memory spec base) built while shipping a 108k-line codebase to stop agents forgetting project conventions across sessions.

- [engram](https://github.com/Gentleman-Programming/engram) · 2026-02
  - `gh:gentleman-programming/engram` · cited by 1: HE
  - summary: Single Go binary, SQLite+FTS5, 18 MCP tools for save/search/session lifecycle.

- [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/pdf/2602.05665v1) · 2026-02
  - `arxiv:2602.05665` · cited by 1: VA
  - summary: Extraction, storage, retrieval and temporal evolution of graph memory.

- [How We Built Agent Builder's Memory System](https://blog.langchain.com/how-we-built-agent-builders-memory-system/) · 2026-02
  - `url:https://blog.langchain.com/how-we-built-agent-builders-memory-system` · cited by 1: HE
  - summary: Implements LangSmith Agent Builder's memory as plain files the agent reads and edits, betting that models handle filesystems well enough to skip specialized memory tooling.

- [Learning to Share: Selective Memory for Efficient Parallel Agentic Systems](https://arxiv.org/pdf/2602.05965v1) · 2026-02
  - `arxiv:2602.05965` · cited by 1: VA
  - summary: Learned controller decides what passes between parallel agent teams.

- [ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents](https://arxiv.org/pdf/2602.01869v1) · 2026-02
  - `arxiv:2602.01869` · cited by 1: VA
  - summary: Saves step-by-step procedural skills for reuse without retraining.

- [Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://arxiv.org/pdf/2602.06052v3) · 2026-02
  - `arxiv:2602.06052` · cited by 1: VA
  - summary: Organizes memory by substrate, cognitive mechanism and subject. Best 2026 entry point.

- [Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory](https://arxiv.org/abs/2603.17781) · 2026-03
  - `arxiv:2603.17781` · cited by 1: HE
  - summary: Benchmarks prompt-stored facts against hash-addressed 'Knowledge Objects' and shows in-context memory collapses in production (compaction destroys 60% of facts, drift erodes 54% of constraints) while KOs stay 100% accurate at 252x lower cost.

- [GAAMA: Graph Augmented Associative Memory for Agents](https://arxiv.org/abs/2603.27910) · 2026-03
  - `arxiv:2603.27910` · cited by 1: HE
  - summary: A graph memory that routes retrieval through concept nodes rather than entities to dodge the mega-hub problem of conversational knowledge graphs, plus a post-retrieval repair step, reaching 79.1% on LoCoMo-10.

- [Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures](https://arxiv.org/abs/2603.17244) · 2026-03
  - `arxiv:2603.17244` · cited by 1: HE
  - summary: Grounds agent memory in formal belief-revision (AGM) semantics as a versioned property graph of immutable revisions with typed dependency edges, hitting 93.3% on the implicit-constraint LoCoMo-Plus benchmark where the best baseline scores 45.7%.

- [MemArchitect: A Policy-Driven Memory Governance Layer](https://arxiv.org/abs/2603.18330) · 2026-03
  - `arxiv:2603.18330` · cited by 1: HE
  - summary: A governance layer over agent memory that enforces rule-based decay, conflict resolution, and privacy controls to keep stale 'zombie memories' out of the context window, treating memory lifecycle as policy rather than passive storage.

- [claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) · 2026-04
  - `gh:coleam00/claude-memory-compiler` · cited by 1: HE
  - summary: Uses Claude Code hooks to distill each conversation's decisions and lessons into compiled articles that feed back into later sessions, giving an agent evolving memory without a vector database.

- [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/abs/2604.10352) · 2026-04
  - `arxiv:2604.10352` · cited by 1: HE
  - summary: Treats the context window as OS-style virtual memory managed by the harness (typed pages with validated writeback at every lifecycle boundary), eliminating the state loss agents suffer after compaction or reset, at under 50 microseconds overhead per turn.

- [Continual learning for AI agents](https://blog.langchain.com/continual-learning-for-ai-agents/) · 2026-04
  - `url:https://blog.langchain.com/continual-learning-for-ai-agents` · cited by 1: HE
  - summary: Frames agent improvement as happening across three layers (model weights, the harness, and external context/memory) and argues most teams should target the latter two via trace-driven updates rather than retraining.

- [MemPalace](https://github.com/MemPalace/mempalace) · 2026-04
  - `gh:mempalace/mempalace` · cited by 1: HE
  - summary: A local-first memory that stores conversations verbatim and retrieves by semantic search with no summarization step, keeping 96.6% retrieval accuracy without cloud calls.

- [Stash](https://github.com/alash3al/stash) · 2026-04
  - `gh:alash3al/stash` · cited by 1: HE
  - summary: Self-hosted memory with an 8-stage consolidation pipeline; single Docker Compose.

- [TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) · 2026-04
  - `gh:tencent/tencentdb-agent-memory` · cited by 1: HE
  - summary: Four-tier local pipeline; 61% token cut and 51% relative pass-rate gain on long-horizon tasks.

- [MAGE: Memory as Agent-Guided Exploration](https://arxiv.org/abs/2606.06090) · 2026-06
  - `arxiv:2606.06090` · cited by 1: HE
  - summary: Argues long-horizon agent memory should track execution state, not semantic similarity, storing interactions in a state tree with grow/compress/revise operations that isolate erroneous branches, for +7.8-20.4pp success and 55% fewer tokens on MemoryArena.

## Tools & Undated

2 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Cortex Memory](https://github.com/sopaco/cortex-mem)
  - `gh:sopaco/cortex-mem` · cited by 1: KY
  - summary: Extraction, vector search and automated optimization with REST/MCP/CLI and dashboard.

- [Memgpt](https://github.com/cpacker/memgpt)
  - `gh:cpacker/memgpt` · cited by 1: KY
  - summary: Letta (formerly MemGPT) is an agent framework built around persistent, self-editing memory, so an agent can keep learning across sessions instead of forgetting everything once the context window fills up — usable via a local agent runtime or an SDK you embed in your own app.
