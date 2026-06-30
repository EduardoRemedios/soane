# Intent Red Team

## Version

v1

## Change Log

- v1 (2026-06-30): Initial intent red-team review.

Iteration: 1 of max 2

## Findings

### High: Research Could Become Architecture By Accident

Why it matters: Adjacent systems such as Letta, LangGraph, Mem0, and Zep solve different problems. Copying their abstractions prematurely could distort the Workspace model.

Fix: Treat them as inputs and anti-pattern sources, not as implementation dependencies.

### High: Memory Could Collapse Into RAG

Why it matters: Project Memory must preserve decisions, assumptions, evidence, governance state, and execution lineage. A retrieval-only framing would lose authority and lifecycle semantics.

Fix: Require the synthesis to separate durable memory, execution state, governance records, and context assembly.

### Medium: Research Could Overreach Into Factory V3

Why it matters: Execution-state research is relevant, but Factory V3 owns mission governance.

Fix: Limit Soane conclusions to memory references, mission evidence links, and write-back expectations.

### Medium: Evidence Sources Are Mixed

Why it matters: The supplied research note includes papers, benchmarks, architecture papers, and product docs with different reliability levels.

Fix: Record source posture and avoid treating every source as equivalent.
