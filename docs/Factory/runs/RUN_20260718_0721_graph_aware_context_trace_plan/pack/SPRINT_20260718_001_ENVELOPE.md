# Sprint Envelope: GCT-V0-001 Graph-Aware Context And Trace

## Version

v2

## Change Log

- v1 (2026-07-18): Stage H execution envelope.
- v2 (2026-07-18): Added hard service ceilings, path identity, and command defaults after Stage I.

## Sprint Identity

- Factory Sprint ID: `SPRINT_20260718_001`
- Product slice: `GCT-V0-001`
- Execution Mode: `PLANNING_ONLY`
- Authorization: Explicit human Go required before implementation.

## Objective

Implement one deterministic, storage-neutral, two-hop Project Memory traversal service and make existing agent context, trace, and affected-by workflows consume its typed paths, policy enforcement, and bounded explanations.

## Required API Shape

The implementation should use frozen dataclasses and existing enums. Exact names may follow repository conventions, but the semantic fields are locked.

### Traversal Request

- `seed_object_ids`
- `access`
- `directions`: explicit inbound/outbound set
- `relationship_types`: explicit existing-type allowlist
- `max_depth`: integer from 0 through 2
- `object_limit`: positive integer
- `path_limit_per_object`: positive integer
- `examined_edge_limit`: positive integer
- `include_non_current`: boolean

### Traversal Result

- admitted seeds
- selected objects with depth and lifecycle state
- typed directional proof paths
- opaque structured exclusions
- work and output truncations with aggregate omitted counts
- examined-edge count

Every non-seed selected object must have a path. Missing, external, inaccessible, disallowed, depth-bound, and budget outcomes remain distinct. Inaccessible nodes never bridge traversal.

### Hard Service Ceilings

- maximum depth: `2`
- maximum selected objects: `64`
- maximum paths per object: `4`
- maximum examined edges: `512`
- maximum serialized exclusions: `64`
- maximum serialized truncation/explanation records: `32`

Requests above a ceiling fail validation; they are not silently clamped. A path is identified by its complete ordered step tuple, and duplicate authored edges do not create duplicate paths.

## Command Policies

- `agent-context`: task/document selection remains in `agent_context.py`; memory relationship expansion delegates to the traversal service and retains existing selection states, fail-closed behavior, document budget, memory budget, reasons, and output fields.
- `agent-context`: default graph depth `2`, paths per object `1`, examined edges `128`; selected objects remain capped by the existing memory budget.
- `agent-trace`: keeps focal object, outgoing, and incoming output; adds controls with defaults depth `1`, objects `32`, paths per object `2`, examined edges `256`.
- `agent-affected`: exact normalized provenance/derivation matching supplies direct seeds; a narrow direction-aware relationship policy supplies propagated dependents; defaults depth `2`, objects `32`, paths per object `2`, examined edges `256`; direct and propagated results are distinguishable.

Command defaults must be explicit and bounded. Empty service seeds or allowlists never broaden automatically.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Add one graph module only unless a second file removes demonstrable complexity.
- Use no new dependency, database, cache, registry, plugin layer, query DSL, semantic ranker, or persistence abstraction.
- Preserve all existing object and relationship types.
- Do not call Candidate Review or mutate memory lifecycle.
- Do not import Factory context-index private helpers into graph code.
- Keep maximum traversal depth at two.
- Sort before every budget decision.
- Build the inbound index once per traversal from visible-safe edge records; do not repeatedly scan the full memory collection for each frontier object.
- Never expose hidden titles, types, metadata, or onward topology.

## Expected File Surface

- Create: `soane/project_memory/graph.py`
- Create: `tests/test_project_memory_graph_traversal.py`
- Modify: `soane/project_memory/__init__.py`
- Modify: `soane/project_memory/agent_context.py`
- Modify: `soane/project_memory/cli.py`
- Modify: `tests/test_project_memory_agent_context.py`
- Modify only if fixture reuse is materially clearer: Project Memory fixture helpers or fixed JSON fixture.
- Closeout modifications: `docs/PROJECT_MEMORY_ARCHITECTURE.md`, `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, `docs/CHANGELOG.md`, run closeout artifacts.

## File-Touch Budgets

| Micro-Sprint | Max Modified | Max Created | Max Deleted |
| --- | ---: | ---: | ---: |
| MS-00 | 2 | 2 | 0 |
| MS-01 | 2 | 1 | 0 |
| MS-02 | 2 | 0 | 0 |
| MS-03 | 2 | 0 | 0 |
| MS-04 | 2 | 1 | 0 |
| MS-05 | 1 | 0 | 0 |
| MS-06 | 6 | 1 | 0 |
| Sprint Total | 12 | 4 | 0 |

Overlapping files across micro-sprints count once in the sprint total. The total permits canonical-doc closeout and one optional fixed fixture without licensing unrelated edits.

## Verification

- Follow `verification_plan.md` and `traceability_matrix.md`.
- VC-01 through VC-07 must pass before command integration.
- VC-08 through VC-12 and VC-14 must pass before full regression.
- VC-13 and VC-15 close the implementation.
- Run focused tests, full tests, knowledge lint, pack lint, and `git diff --check`.
- Record actual graph sizes, selected counts, examined edges, exclusions, and truncations for the realistic proof.

## No-Touch Boundaries

- requirements and dependency manifests
- Factory Core scripts/specification
- Project Memory object and relationship enum values
- review/promotion semantics
- Factory context-index schema
- Thinking Engine, adapters, TUI, product UI, and neighbouring repositories

## Stop Conditions

- Any hidden content or hidden bridge is observable.
- Work continues after a declared traversal budget is exhausted.
- `agent-context` retains an independent relationship walker.
- Existing trace fields must be removed.
- Affected-by needs fuzzy source matching or inferred edges.
- A Claim is promoted, mutated, or presented as accepted truth.
- New persistence, relationship type, dependency, query language, semantic inference, code graph, external provider, UI, or depth greater than two is required.

## Completion Rule

Implementation is complete only when VC-01 through VC-15 pass, Factory execution closeout finds no scope drift, canonical status documents are reconciled, and the realistic Claim graph demonstrates a small explained bundle without broad repository rereading.
