# Intent: GCT-V0-001 Graph-Aware Context And Trace

## Version

v2

## Change Log

- v1 (2026-07-18): Initial Stage A intent.
- v2 (2026-07-18): Hardened policy, work budgets, impact semantics, and compatibility after Stage B.

## Purpose

Plan the smallest reusable graph traversal capability that lets agents assemble and explain relevant Project Memory without rereading broad repository context. [SOURCE:RAW]

## Goal

Define deterministic, policy-preserving, typed traversal and integrate it into the existing agent context, trace, and affected-by commands using one realistic Markdown Claim graph. [SOURCE:RAW]

## Definitions

- `seed`: a visible Project Memory object from which traversal begins. [SOURCE:RAW]
- `outbound`: following a relationship stored on the current object to its target. [SOURCE:REF:soane/project_memory/contract.py]
- `inbound`: following a relationship stored on another object whose target is the current object. [SOURCE:RAW]
- `path`: an ordered sequence of seed, typed directional steps, and destination object. [SOURCE:RAW]
- `selected object`: a visible object admitted within traversal policy and object budget, with at least one proof path. [SOURCE:RAW]
- `affected object`: a directly source-linked object or a visible dependent reached through an allowed inbound or outbound path. [SOURCE:RAW]
- `current object`: an object not in the existing non-current lifecycle set. [SOURCE:REF:soane/project_memory/semantics.py]

## Requirements

- Add one product-owned, storage-neutral traversal module over `ProjectMemory`, `MemoryObject`, and existing `RelationshipType`; commands must not implement independent graph engines. [SOURCE:RAW]
- A request must explicitly contain seed IDs, allowed directions, relationship allowlist, maximum depth, object limit, path limit per object, and access context. [SOURCE:RAW]
- Defaults used by agent commands must be command-specific and declared at their CLI boundaries; the core service must not silently broaden an empty allowlist or missing seed set. [SOURCE:RAW]
- Depth zero returns only visible seeds. Depth counts relationship steps, and the bounded v0 maximum accepted depth is two. [SOURCE:RAW]
- Traversal must enforce visibility and suppression rules at seed admission and every hop, recording inaccessible or missing objects as structured exclusions without exposing hidden titles or metadata. [SOURCE:REF:soane/project_memory/semantics.py]
- Traversal must not use an inaccessible object as an intermediate bridge to a visible destination. Inaccessible exclusions may identify only the requesting source object, relationship type, direction, and opaque target ID. [SOURCE:RAW]
- Current objects must rank before non-current objects at equal depth, while non-current objects remain eligible only when the caller explicitly allows them. [SOURCE:REF:docs/PROJECT_MEMORY_ARCHITECTURE.md]
- Neighbor ordering must be deterministic by depth, lifecycle rank, relationship type, direction, object type, title, and object ID. [SOURCE:RAW]
- A visited object may be selected once but may retain multiple distinct proof paths up to the path budget; cycles and repeated edges must terminate without duplicate selection. [SOURCE:RAW]
- Every selected non-seed object must include at least one path whose steps record source ID, relationship type, direction, and target ID. [SOURCE:RAW]
- Object, path, and explanation budget exhaustion must produce explicit structured truncations; traversal must never continue unbounded after output truncation. [SOURCE:RAW]
- The request must also include a positive examined-edge limit. Exclusion and serialized explanation collections must have fixed service-owned caps with aggregate omitted counts. [SOURCE:RAW]
- `agent-context` must replace its private one-hop expansion with the traversal service while preserving document recall, explicit-seed fail-closed behavior, separate document/memory budgets, selection states, and existing public output fields. [SOURCE:REF:soane/project_memory/agent_context.py]
- `agent-trace` must accept bounded direction, relationship, depth, and object-limit controls and return paths, exclusions, and truncations in addition to the focal object. [SOURCE:RAW]
- `agent-trace` must preserve existing focal-object, outgoing, and incoming fields while adding traversal details unless a separately approved breaking contract is recorded. [SOURCE:RAW]
- `agent-affected` must find direct source matches first, then traverse a command-owned dependent relationship policy and explain each direct or propagated result; the policy must distinguish relationship direction rather than using all types bidirectionally, and an unmatched path must return an empty successful result. [SOURCE:RAW]
- Source matching must continue using normalized exact provenance and derivation refs; v0 must not infer semantic source links. [SOURCE:REF:soane/project_memory/cli.py]
- The realistic proof graph must include a proposed/asserted MMI-style Claim with exact source metadata plus visible current and non-current dependents, a cycle, an inaccessible object, and at least one unrelated object. [SOURCE:RAW]
- The implementation must preserve the existing relationship vocabulary and validation contract unless intent is explicitly unlocked. [SOURCE:REF:soane/project_memory/contract.py]
- External refs, unresolved local targets, inaccessible targets, disallowed relationships, depth boundaries, and work-budget truncation must remain distinguishable without leaking inaccessible content. [SOURCE:RAW]

## Non-Goals

- persistence, graph database, schema migration, or graph materialization
- general graph query language, arbitrary predicates, aggregation, or path algebra
- semantic edge inference, embeddings, fuzzy matching, or model-based ranking
- code symbols, imports, architectural dependency extraction, or repository-wide code graph
- new Project Memory object or relationship types
- automatic review, promotion, lifecycle mutation, epistemic elevation, or Authority assignment
- external providers, product UI, live adapters, or cross-project knowledge
- traversal deeper than two hops in v0

## Principles

- One traversal primitive, several bounded agent workflows.
- Paths are explanations, not merely implementation detail.
- Access policy applies before relevance or convenience.
- Empty seeds and empty allowlists fail closed.
- Bounded useful context is the product outcome; graph completeness is not.
- Existing Project Memory relationships remain the graph authority.

## Roles

- Project Memory contract: owns objects, relationship vocabulary, lifecycle, and provenance.
- Traversal service: owns direction-aware neighbor discovery, policy checks, ordering, paths, exclusions, and budgets.
- Agent context assembler: owns document recall and task-specific seed selection.
- Agent trace command: owns trace defaults and presentation.
- Agent affected command: owns source matching and dependent-propagation policy.
- Human reviewer: authorizes execution and any future relationship-vocabulary expansion.

## Acceptance Criteria

- Zero-seed and empty-allowlist requests return no expanded objects and explain why.
- Depth-zero, one-hop, and two-hop traversal have deterministic focused tests.
- Inbound and outbound traversal produce distinct expected results.
- Cycles terminate; repeated runs produce identical semantic output.
- Hidden and suppressed objects never leak descriptive content through paths or exclusions.
- Current-first ranking and explicit non-current inclusion are proven.
- Every selected non-seed object has a typed directional proof path.
- Object and path budgets produce deterministic truncation records.
- Examined-edge, exclusion, and explanation caps prevent dense graphs from doing or serializing unbounded work.
- Existing `agent-context` tests continue to pass after private graph expansion is removed.
- Trace and affected CLI tests prove new controls and explanations.
- A fixed MMI-style Claim graph proves source-to-Claim-to-dependent Decision or Constraint propagation.
- Full repository tests and no-touch scans pass.

## Open Questions

- NON-BLOCKING: The traversal result may expose either one canonical shortest path or multiple equal-length shortest paths by default, provided alternate paths are ordered canonically before the path budget is applied.
- NON-BLOCKING: Direct source matches in `agent-affected` may use a synthetic zero-step path marker or a separate `matched_by` field; direct versus propagated provenance must remain unambiguous.

## Go Or No-Go Rule

Go only if the final pack proves bounded typed paths, per-hop policy enforcement, deterministic cycle and budget behavior, shared consumption by all three agent workflows, realistic Claim propagation, and no expansion into persistence, semantic inference, code graphs, or automatic truth mutation.
