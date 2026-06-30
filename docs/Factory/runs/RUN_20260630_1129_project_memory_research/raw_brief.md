# Raw Brief: Project Memory Research Spike

## Execution Mode

Execution Mode: PLANNING_ONLY

## Purpose

Run a bounded research spike before defining the Workspace Project Memory architecture.

## Goal

Produce `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as a reviewed synthesis of relevant memory, agent-state, tool-use, and governance research that should inform `docs/PROJECT_MEMORY_ARCHITECTURE.md`.

## Context

The Workspace treats Project Memory as its central architectural concept. Before defining its architecture, the repository should learn from adjacent research and systems without prematurely adopting any implementation.

The user supplied a scheduled research note covering agent memory, long-horizon execution, tool-use benchmarks, blind goal-directedness, reward hacking, and control-plane research.

## Scope

In scope:

- identify lessons relevant to Workspace Project Memory
- distinguish semantic memory, execution state, decisions, assumptions, evidence, and governance records
- inspect adjacent projects and research as architecture inputs
- produce a concise synthesis and recommendations
- record remaining uncertainties for the future architecture document

Out of scope:

- database selection
- schema finalization
- implementation
- UI design
- Factory V3 mission-governance design
- Aegis proof design
- replacing Project Memory with an external memory product

## Acceptance Criteria

- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` exists.
- The synthesis identifies architecture implications, anti-patterns, and open questions.
- The synthesis avoids committing to storage technology.
- The synthesis remains aligned with `docs/VISION.md`, `docs/CORE_CONCEPTS.md`, and `docs/GOVERNANCE_MODEL.md`.

