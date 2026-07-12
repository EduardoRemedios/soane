# Sprint Envelope: ACR-V1-001

## Version

v2

## Change Log

- v1 (2026-07-12): Initial Stage H sprint envelope.
- v2 (2026-07-12): Named traversal and output vocabularies and hardened refresh locking and closeout after Stage I.

## Sprint Objective

Make the existing agent-context front door select bounded relevant documents and memory, fail closed on zero matches, explain one-hop expansion, and refresh the local index truthfully under contention.

## Locked Scope

- deterministic bounded query planning over the existing Factory recall API
- separate document and memory budgets
- explicit selection and refresh states in service and CLI output
- fail-closed agent zero-match behavior with preserved explicit broad inspection
- one-hop allowlisted relationship expansion with lifecycle/access enforcement
- isolated and serialized or atomic context-index publication
- focused, contention, failure-injection, CLI-output, and full regression tests
- validation closeout and state-doc updates

## Non-Goals

- persistence, migration, embeddings, external retrieval, ingestion, automatic promotion, deeper graph APIs, product UI, live adapters, or portfolio-boundary changes

## Expected File Boundary

Primary modifications:

- `scripts/factory_context_index.py`
- `soane/project_memory/agent_context.py`
- `soane/project_memory/context.py` only if explicit selection semantics cannot remain at the agent boundary
- `soane/project_memory/cli.py`
- `tests/test_project_memory_agent_context.py`
- `tests/test_project_memory_context.py`
- focused Factory context-index tests in an existing or new test file

Closeout modifications:

- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- run-local validation closeout artifact

Any change outside this boundary requires documented justification; persistence, provider, UI, or neighbouring-product changes require intent unlock.

## File-Touch Budgets

| Micro-Sprint | Max Modified | Max Created | Max Deleted |
| --- | ---: | ---: | ---: |
| MS-00 | 3 | 2 | 0 |
| MS-01 | 3 | 1 | 0 |
| MS-02 | 4 | 1 | 0 |
| MS-03 | 3 | 1 | 0 |
| MS-04 | 3 | 1 | 0 |
| MS-05 | 4 | 0 | 0 |
| MS-06 | 4 | 1 | 0 |

Sprint total unique-file budget:

- Max files modified: 12
- Max files created: 4
- Max files deleted: 0

The per-step totals intentionally overlap because the same service and test files may be refined across steps.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2: prefer direct helpers in existing owner modules; add no framework, registry, strategy layer, plugin seam, or dependency without a demonstrated need.
- Do not catch and relabel refresh failure as success.
- Do not make document role an authority or lifecycle signal.
- Do not weaken `AccessContext`, visibility, suppression, propagation, contradiction, or current-truth semantics.
- Do not infer broad selection from an empty seed collection.
- Do not issue unbounded recall queries derived from every task token.
- Preserve the previous valid index until a replacement is fully built and valid.
- Keep output deterministic for the same repository state and request.
- Default one-hop expansion allowlist: `supports`, `challenges`, `depends_on`, `supersedes`, `invalidates`, `derived_from`, `evidences`, `has_capability`, `has_authority`, `blocks`, `answers`, `contradicts`, and `maps_to`.
- Exclude generic `contains`, `references`, and `produced_by` fan-out from automatic expansion; direct seeds remain inspectable under existing access rules.
- Preserve current versus surfaced non-current separation; every expanded object records relationship reason and lifecycle status.
- Selection mode vocabulary: `relevance`, `explicit_seed`, or `explicit_broad`. Selection state vocabulary: `ready`, `degraded`, or `blocked`.
- Refresh state vocabulary: `refreshed`, `reused`, or `failed`; failure details must remain inspectable without fabricating success.
- Refresh coordination must use ownership-aware operating-system locking or equivalent local coordination, not a stale unowned sentinel file.

## Micro-Sprint Gates

### MS-00

- Entry: explicit human Go and execution enablement.
- Exit: focused tests encode VC-001 through VC-009 and VC-013.
- Stop: external or timing-dependent test requirement.

### MS-01

- Entry: MS-00 tests exist.
- Exit: bounded query and document-budget tests pass.
- Stop: embeddings, dependency, or unbounded term fan-out.

### MS-02

- Entry: MS-01 passes.
- Exit: zero-match, explicit broad, budgets, and output-state checks pass.
- Stop: any access-control or lifecycle bypass.

### MS-03

- Entry: MS-02 passes.
- Exit: one-hop traversal, cycles, exclusions, and role distinction pass.
- Stop: traversal exceeds one hop or becomes general graph infrastructure.

### MS-04

- Entry: MS-03 passes.
- Exit: contention and failure-publication checks pass.
- Stop: solution requires daemon, service, dependency, or schema redesign.

### MS-05

- Entry: MS-04 passes.
- Exit: VC-010 through VC-013, knowledge lint, and diff hygiene pass.
- Stop: Critical failure or scope drift.

### MS-06

- Entry: implementation verification is complete.
- Exit: execution closeout and state docs truthfully record outcome and residual risk.
- Exit: closeout retains the residual limitation that bounded lexical relevance is not semantic retrieval proof.
- Stop: evidence is incomplete or intent unlock is required.

## Required Verification Before Merge

- focused agent-context and context-index tests
- `python3 -m unittest discover -s tests`
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl pack-lint --run RUN_20260712_0909_agent_context_relevance_v1_plan`
- `git diff --check`
- scoped diff review against `verification_plan.md` and `traceability_matrix.md`

## Go Or No-Go

No implementation begins from this planning-only pack. After Stage I2 PASS and pack-lint PASS, human Go must explicitly authorize execution and execution-mode evidence must be updated through the Factory contract.
