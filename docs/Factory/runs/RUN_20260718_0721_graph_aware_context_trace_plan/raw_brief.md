# Raw Brief: GCT-V0-001 Graph-Aware Context And Trace

## Request

Plan the next bounded Soane slice: relationship-typed Project Memory traversal that improves agent context, trace, and affected-by workflows using realistic Claim density from Markdown ingestion.

## Approved Direction

The human asked on 2026-07-18 to proceed with the next bounded slice identified in the canonical roadmap.

The pack should define:

1. one reusable, local, deterministic graph traversal service over existing Project Memory objects and relationships
2. explicit inbound and outbound direction, relationship allowlists, bounded depth, object budgets, cycle handling, visibility enforcement, and lifecycle-aware ordering
3. explained paths for `agent-trace`
4. source-to-memory-to-dependent-object propagation for `agent-affected`
5. graph expansion inside `agent-context` without creating a competing selection system
6. one realistic proof graph containing a Markdown-ingested Claim and dependent Decision, Constraint, Evidence, or Assumption objects

## Execution Contract

Execution Mode: EXECUTION_ENABLED

Execution Authorization: Human Go in the current Codex conversation on 2026-07-18.

Downstream Fan-Out: NOT_APPROVED

## Execution Authorization Addendum

- Human decision: Go
- Recorded: 2026-07-18
- Authorized envelope: `pack/SPRINT_20260718_001_ENVELOPE.md`
- Scope change: none

## Scope

- storage-neutral graph traversal over the existing in-memory Project Memory contract
- existing relationship vocabulary only
- direction-aware, allowlisted, depth-bounded traversal
- deterministic path explanations, exclusions, and truncation reasons
- integration with existing `agent-context`, `agent-trace`, and `agent-affected` commands
- focused synthetic and realistic Claim-graph fixtures and tests
- state, roadmap, changelog, and validation closeout during later authorized implementation

## Non-Goals

- durable persistence, database schema, migrations, or graph database
- a general graph query language
- embeddings, semantic inference, fuzzy edge discovery, or external providers
- full code-symbol or import graph
- automatic Claim review, promotion, fact elevation, or lifecycle mutation
- new relationship types unless execution discovers a contract-critical omission and intent is explicitly unlocked
- product UI, live adapters, portfolio knowledge, or neighbouring-product scope
- unbounded traversal or repository-wide graph materialization

## Acceptance

- traversal is deterministic and storage-neutral
- every returned object has at least one explicit typed path from a seed
- inbound and outbound traversal semantics are distinct and testable
- access visibility, suppression, and lifecycle rules apply at every hop
- cycles terminate deterministically and do not duplicate selected objects
- depth, object, path, and explanation budgets fail closed with explicit truncation reasons
- `agent-context` uses the traversal service instead of retaining separate one-hop graph logic
- `agent-trace` and `agent-affected` expose explained, bounded propagation
- a realistic MMI-style Claim graph proves source-to-Claim-to-dependent-object behavior
- no persistence, semantic graph, code graph, provider, UI, or automatic truth promotion is introduced
