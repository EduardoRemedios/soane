# Project Memory Research Synthesis

## Status

This is a bounded research synthesis for the Workspace Project Memory architecture.

It is not the architecture itself. It exists to constrain and improve the next canonical document: `docs/PROJECT_MEMORY_ARCHITECTURE.md`.

Factory run: `docs/Factory/runs/RUN_20260630_1129_project_memory_research/`

## Executive Conclusion

The research supports the Workspace's existing direction: Project Memory should be treated as infrastructure, not as chat history plus retrieval.

The most important architectural implication is that Project Memory should separate at least four concerns:

- durable semantic/project knowledge
- execution and mission state
- governance records such as Decisions, Authority references, Evidence, and Proof references
- retrieval/context assembly for current reasoning tasks

The Workspace should not begin by choosing a database. It should begin by defining memory object types, lifecycle states, provenance rules, contradiction handling, and promotion rules from conversation or research into durable memory.

## Sources Reviewed

User-supplied scheduled research note:

- `pasted-text.txt` attached to this task, covering MARS, MemoryAgentBench, MemoryArena, MAGE, OSWorld-MCP, BLIND-ACT, SCUBA, FeatureBench, reward hacking benchmarks, and control-plane research.

External research and implementation references:

- MemoryAgentBench: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions" ([OpenReview](https://openreview.net/forum?id=DT7JyQC3MR))
- MemoryArena: "Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks" ([arXiv](https://arxiv.org/abs/2602.16313))
- MAGE: "Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents" ([arXiv](https://arxiv.org/abs/2606.06090))
- BLIND-ACT: "Computer-Use Agents Exhibit Blind Goal-Directedness" ([OpenReview](https://openreview.net/forum?id=9W4bPRsEIT))
- Letta memory blocks and archival memory ([Letta docs](https://docs.letta.com/guides/core-concepts/memory/memory-blocks))
- LangGraph long-term memory ([LangChain docs](https://docs.langchain.com/oss/python/langchain/long-term-memory))
- Mem0 memory layer ([Mem0 GitHub](https://github.com/mem0ai/mem0))
- Zep temporal knowledge graph memory ([arXiv](https://arxiv.org/abs/2501.13956))

## Relevant Signals

### Memory Is Not Just Retrieval

MemoryAgentBench frames memory quality around retrieval, test-time learning, long-range understanding, and selective forgetting.

Implication for the Workspace:

- Project Memory needs explicit lifecycle operations, not only vector search.
- "Remember this" should not mean "append this to a RAG store."
- Memory should be testable against retrieval, update, contradiction, and forgetting behavior.

### Memory Must Influence Later Action

MemoryArena is important because it evaluates whether memory helps later multi-session tasks.

Implication for the Workspace:

- Project Memory should be judged by whether it improves future Thinking, decisions, planning, mission readiness, and review.
- A memory that is retrievable but does not affect downstream reasoning is not enough.
- Operational learning should feed back into future readiness assessments and mission planning.

### Execution State Is Different From Semantic Memory

MAGE argues that semantic similarity retrieval can mix valid and invalid trajectories. Its state-tree framing is relevant even if the Workspace does not adopt the implementation.

Implication for the Workspace:

- Project Memory should distinguish durable knowledge from execution branches.
- Failed attempts, superseded paths, and invalidated branches should remain inspectable without polluting active context.
- Mission history and operational learning need lineage, not just summaries.

### Agents Need Act-Or-Ask Boundaries

BLIND-ACT reinforces that agents pursue goals under ambiguity, infeasibility, or missing context.

Implication for the Workspace:

- Project Memory should store unresolved questions and blocking assumptions as first-class objects.
- Context assembly should surface uncertainty, not hide it.
- Readiness should include "should this proceed?" checks before "how should this proceed?" planning.

### Tool Availability Is Not Tool Competence

OSWorld-MCP shows that tool availability does not imply effective tool invocation.

Implication for the Workspace:

- Capabilities should be represented separately from verified competence and authority.
- Provider/tool invocation records should include rationale, success/failure, and evidence.
- Project Memory should be able to store capability evidence and not just connector availability.

### Research And Experimentation Need Branch-Level Evidence

MARS suggests long-horizon research work benefits from branch-level evidence, reflective memory, and budget-aware search.

Implication for the Workspace:

- Hypotheses and research branches should be represented without forcing premature convergence.
- Lessons extracted from failed or partial branches should be quarantined until reviewed.
- Inference Strategy should include budget, confidence, and evidence considerations.

## Adjacent Implementation Patterns

### Letta

Letta's memory-block distinction is useful because it treats memory as structured state that can be edited and inspected.

Workspace lesson:

- Project Memory should support named, inspectable memory objects rather than opaque embeddings only.
- Human-editable memory surfaces matter.

Do not copy:

- agent-persona memory as the core abstraction for Workspace Project Memory.

### LangGraph

LangGraph's long-term memory model is useful because it separates thread state from long-term memory and supports namespace/key organization.

Workspace lesson:

- The Workspace should distinguish current working context from durable memory.
- Namespaces will likely matter for Project, person, organisation, mission, and cross-project memory.

Do not copy:

- treating generic key-value memory as sufficient for Project Memory semantics.

### Mem0

Mem0 is useful as an example of extraction, consolidation, and retrieval as an explicit memory layer.

Workspace lesson:

- Memory writes should involve extraction and consolidation, not raw transcript dumping.
- Memory update policies are a product concern.

Do not copy:

- assuming a third-party memory service can own Workspace Project Memory.

### Zep

Zep's temporal knowledge graph framing is relevant because Workspace Project Memory needs time, relationship, and provenance.

Workspace lesson:

- Project Memory likely needs graph-shaped relationships and temporal facts.
- Provenance and supersession should be built into the model early.

Do not copy:

- committing to a graph database before object lifecycles and governance semantics are clear.

## Architectural Requirements For Project Memory

The architecture document should define first-class objects for at least:

- Project
- Project Memory
- Conversation
- Question
- Assumption
- Hypothesis
- Constraint
- Decision
- Evidence Artifact
- Verification
- Mission Reference
- Authority Reference
- Capability Reference
- Research Finding
- Operational Learning
- Canonical Knowledge Artifact

Each object should have:

- stable identifier
- status
- provenance
- created time
- updated time
- source references
- confidence or evidence posture where relevant
- relationships to other objects
- supersession or invalidation behavior where relevant

## Required Distinctions

The architecture should keep these distinctions explicit:

- Conversation is not Memory.
- Memory is not Context.
- Evidence is not Proof.
- Capability is not Authority.
- Hypothesis is not Decision.
- Semantic retrieval is not execution state.
- Mission history is not Project Memory by itself, but should write back into it.
- Generated Markdown is a view over memory, not the memory substrate.

## Recommended Initial Memory Layers

### 1. Canonical Knowledge Layer

Stores durable project facts, concepts, boundaries, architecture, roadmap, and stable summaries.

### 2. Governance Record Layer

Stores Decisions, Assumptions, Constraints, Evidence, Verification, Authority references, and Proof references.

### 3. Inquiry Layer

Stores Questions, Hypotheses, Research Findings, Discovery Playbooks, and unresolved uncertainty.

### 4. Execution State Layer

Stores Mission references, checkpoints, operational learning, failed branches, stale states, and replay/evidence links.

### 5. Context Assembly Layer

Selects relevant memory for a task without becoming the source of truth.

## Anti-Patterns

Avoid:

- raw transcript as primary memory
- vector database as architecture
- silent memory writes
- unreviewed agent-generated facts
- flattening assumptions into facts
- losing failed branches
- retrieving stale decisions without supersession state
- mixing active execution state with historical evidence
- treating human preference as authority
- treating tool availability as verified capability
- treating generated Markdown as the only source of truth

## Open Questions For Architecture

The Project Memory architecture should answer:

- What is the minimum object model for v1?
- What is the lifecycle for memory creation, review, promotion, amendment, supersession, and deletion?
- Which objects can be created by agents, and which require human review?
- How are contradictory claims represented?
- How are stale assumptions surfaced?
- How does Project Memory decide what becomes canonical Markdown?
- How does Project Memory store external references without mirroring external systems?
- How do mission records from Factory V3 write back into Workspace memory?
- How do evidence packets or proof bundles from Aegis relate to local Evidence Artifacts?
- What must be forgettable, redactable, or revocable?

## Recommendation

Proceed to `docs/PROJECT_MEMORY_ARCHITECTURE.md`, but constrain it to conceptual architecture.

Do define:

- memory object types
- lifecycle states
- provenance model
- relationship model
- context assembly principles
- canonical Markdown generation rules
- integration boundaries
- v1 non-goals

Do not define yet:

- database choice
- indexing implementation
- API endpoints
- UI flows
- synchronization architecture
- migration tooling

The first implementation slice should be a local Project Memory object-model prototype only after the conceptual architecture is accepted.

