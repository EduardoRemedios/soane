# Sprint Envelope: MMI-V0-001

## Version
v2

## Change Log
- v1 (2026-07-12): Stage H envelope.
- v2 (2026-07-12): Added candidate budget, review-compatible export, and exact no-touch checks after Stage I.

## Objective

Implement a local deterministic path from one eligible canonical Markdown document to reviewable proposed Claim candidates and observational source-change events.

## Expected Files

- `soane/project_memory/contract.py`
- `soane/project_memory/markdown_roles.py` (new, only if needed to avoid process coupling/import cycles)
- `soane/project_memory/agent_context.py`
- `soane/project_memory/markdown_ingestion.py` (new)
- `soane/project_memory/cli.py`
- `tests/test_project_memory_contract.py`
- `tests/test_project_memory_agent_context.py`
- `tests/test_project_memory_markdown_ingestion.py` (new)
- `tests/test_project_memory_cli.py`
- `tests/test_project_memory_review.py` only if Claim review coverage cannot remain in the new ingestion test
- `tests/fixtures/project_memory/markdown_ingestion/` (new)
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- this run's `VALIDATION_CLOSEOUT_REPORT.md`

## File-Touch Budget

- MS-00: at most 4 code/test files plus fixture files.
- MS-01: at most 4 code/test files.
- MS-02: at most 3 code/test files plus fixture updates.
- MS-03: at most 2 code/test files plus fixture updates.
- MS-04: at most 2 code/test files.
- MS-05: tests/fixtures only unless a verified defect requires an in-envelope source fix.
- MS-06: exactly 3 state-hygiene files plus closeout when relevant.
- Total non-run budget: at most 15 code/test/state files plus bounded fixture files.

## Required API And Semantics

- `MemoryObjectType.CLAIM` and Claim candidate validation in the existing storage-neutral contract.
- Product-owned `MarkdownRole` compatibility and `MarkdownAuthorityMode` vocabulary.
- Immutable ingestion request/result, source snapshot, block, exclusion, warning, and comparison-event values.
- Exact prose paragraph extraction under ATX headings with fenced/structured construct exclusion and a positive candidate limit.
- Explicit request values for authority mode and source authority; inferred role only.
- Candidate metadata and deterministic identity exactly as locked in intent.
- Comparison precedence documented and tested for unchanged, mode change, moved, modified, deleted, added, and ambiguous duplicate.
- CLI commands delegate to service functions and emit stable JSON.
- Optional candidate export emits ordinary review-compatible JSON files and is labeled interchange output, not persistence.

## Comparison Rule Boundary

- Exact occurrence and fingerprint matches are `unchanged` unless authority mode changed.
- Exact block fingerprint at a new unambiguous anchor is `moved`.
- Same stable anchor with changed content is `modified`.
- Unmatched before/after blocks are `deleted`/`added`.
- Multiple plausible matches are `ambiguous_duplicate`; implementation must not guess.
- Rules are deterministic and ordered; no semantic similarity is allowed.

## No-Touch Constraints

- No database, migration, durable index, or repository-wide object corpus.
- No change to `scripts/factory_context_index.py` schema or its `facts` semantics.
- No dependency additions or imports of private Factory parser helpers.
- No review-service semantic change unless a focused Claim compatibility defect is proven; epistemic elevation remains out of scope.
- No canonical-document content changes, generated write-back, external providers, embeddings, UI, live adapters, or portfolio integrations.
- No Decision Review, Delegation, wider Knowledge Scope, or cross-project runtime implementation.

## Verification Before Merge

- Follow `verification_plan.md` and `traceability_matrix.md`.
- Run focused contract, ingestion, review, agent-context, and CLI tests.
- Run `python3 -m unittest discover -s tests`.
- Run knowledge lint, context-index refresh, pack lint, `git diff --check`, dependency/no-touch scans, and Factory execution-closeout.

## SIMPLE-CODE-GATE v2

- Prefer dataclasses, enums, and narrow functions over a generic ingestion framework.
- Do not introduce parser plugins, persistence repositories, event buses, strategy registries, or provider abstractions.
- Share Markdown role vocabulary only if it removes the existing process-coupled import path for ingestion without changing behavior.

## Stop Conditions

- Any candidate becomes accepted, verified, public, cross-project, or authority-bearing during ingestion.
- Any source read escapes the repository root.
- Duplicate lineage is guessed.
- Implementation requires persistence, dependency installation, semantic/model inference, write-back, or neighbouring-product work.
- Full regression or any Critical/High verification fails.

## Completion

Completion requires VC-001 through VC-014, no scope drift, and a READY execution closeout.
