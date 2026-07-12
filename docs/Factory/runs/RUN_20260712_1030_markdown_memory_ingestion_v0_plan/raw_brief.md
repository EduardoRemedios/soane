# Raw Brief: MMI-V0-001 Markdown-To-Memory Candidate Ingestion

## Request

Plan the next bounded Soane slice: deterministic Markdown-to-memory ingestion that creates reviewable Claim candidates with precise provenance, source authority, Markdown mode, Project Knowledge Scope, fingerprints, and freshness behavior.

## Approved Direction

The human agreed on 2026-07-12 to proceed with the recommended `MMI-V0-001` planning-only Factory run.

The pack should define:

1. the smallest runtime Claim candidate contract required for ingestion
2. explicit Markdown role versus authority-mode semantics
3. deterministic heading-bounded parsing and source anchors
4. candidate creation through existing Candidate Review and Promotion semantics
5. unchanged, modified, moved, deleted, duplicate, and mode-change behavior
6. agent-facing ingest and inspection commands
7. one end-to-end proof using a real canonical architecture document

## Execution Contract

Execution Mode: EXECUTION_ENABLED

Execution Authorization: Human Go in the current Codex conversation on 2026-07-12

Downstream Fan-Out: NOT_APPROVED

## Execution Authorization Addendum

- Human decision: Go
- Recorded: 2026-07-12
- Authorized envelope: `pack/MMI-V0-001_ENVELOPE.md`
- Scope change: none

## Scope

- Project Memory contract extension for Claim only
- local deterministic Markdown ingestion service
- bounded authority-mode and source-authority classification
- candidate metadata validation
- source-change comparison without durable mutation
- thin headless CLI commands wrapping service behavior
- focused fixtures and tests
- state, roadmap, changelog, and validation closeout during later authorized implementation

## Non-Goals

- automatic candidate acceptance or fact promotion
- constitutional authored-authority ingestion in v0
- generated or curated Markdown write-back
- Decision Review, Delegation, or broad Knowledge Scope runtime objects
- organisation, portfolio, public, or cross-project promotion
- persistence, migrations, embeddings, semantic retrieval, external providers, UI, or live adapters
- bulk ingestion of the repository
- changing Factory context-index schema or treating its `facts` table as Project Memory Claims

## Acceptance

- Claim candidates are valid Project Memory objects with `proposed` lifecycle and Project visibility
- every candidate preserves exact path, heading, line bounds, block and document fingerprints, Markdown role, authority mode, source authority, Project Knowledge Scope, and derivation method
- role, authority mode, source authority, evidence level, lifecycle, and epistemic status remain distinct
- constitutional authored authority fails closed with an explicit exclusion in v0
- ingestion never invokes review or creates accepted memory
- source comparison is deterministic and reports unchanged, modified, moved, deleted, ambiguous duplicate, and mode-change states without silently mutating accepted memory
- the existing review service is the only promotion path
- one real canonical architecture document proves the workflow alongside synthetic negative fixtures
- no persistence, external dependency, provider, UI, or neighbouring-product scope is introduced
