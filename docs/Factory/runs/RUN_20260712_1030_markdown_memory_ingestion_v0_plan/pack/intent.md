# Intent: MMI-V0-001 Markdown-To-Memory Candidate Ingestion

## Version

v2

## Change Log

- v1 (2026-07-12): Initial Stage A intent.
- v2 (2026-07-12): Hardened extraction, identity, authority-mode, comparison, and no-promotion rules after Stage B.

## Purpose

Plan the smallest local workflow that converts eligible Markdown prose into inspectable Claim candidates while preserving exact source lineage and the existing human review boundary. [SOURCE:RAW]

## Goal

Define a deterministic Claim candidate contract, bounded Markdown parser, change-comparison model, and thin CLI proof that agents can use before durable persistence or semantic retrieval. [SOURCE:RAW]

## Definitions

- `Claim candidate`: a proposed Project Memory Claim with epistemic status `asserted`, Project visibility, required provenance, and promotion flags. [SOURCE:REF:docs/CORE_CONCEPTS.md]
- `Markdown role`: retrieval/context classification such as constitutional, canonical, generated, evidence, working, or deprecated. It does not grant authority. [SOURCE:REF:docs/GOVERNANCE_MODEL.md]
- `authority mode`: authored authority, generated projection, or curated round trip. It controls ingestion and write-back expectations independently of role. [SOURCE:REF:docs/GOVERNANCE_MODEL.md]
- `source authority`: the named person, governance surface, or source system responsible for the source record; it is descriptive and does not mint Authority. [SOURCE:REF:docs/PROJECT_MEMORY_ARCHITECTURE.md]
- `Project Knowledge Scope`: the only allowed v0 scope; it does not authorize cross-project retrieval or promotion. [SOURCE:REF:docs/CORE_CONCEPTS.md]
- `source snapshot`: deterministic document and eligible-block metadata used for comparison without durable state mutation. [SOURCE:RAW]

## Requirements

- Add `CLAIM` to `MemoryObjectType` and validate Claim candidate metadata without changing the generic MemoryObject shape. [SOURCE:RAW]
- Claim candidates must use `PROPOSED`, `PROJECT`, E1 source-reference provenance, `candidate=true`, `promotion_required=true`, and epistemic status `asserted`. [SOURCE:RAW]
- Required candidate metadata must include proposition, source path, heading path, start/end lines, block fingerprint, document fingerprint, Markdown role, authority mode, source authority, knowledge scope, extraction method, and source snapshot version. [SOURCE:RAW]
- Candidate identity must be deterministic from normalized source path, heading path, occurrence identity, and exact block content; content changes create a new candidate identity and comparison lineage. [SOURCE:RAW]
- Ingestion accepts only repo-relative Markdown inside the requested repository root and must reject path escape, missing files, non-Markdown inputs, undecodable content, and symlink escape. [SOURCE:RAW]
- Markdown role may be inferred through the existing classifier, but authority mode and source authority must be supplied explicitly and validated. [SOURCE:RAW]
- Constitutional-role authored authority is excluded in v0 with an explicit reason. Deprecated, generated, evidence, and working roles are excluded from candidate creation in this slice. [SOURCE:RAW]
- Eligible v0 extraction is limited to non-empty prose paragraphs under ATX headings in canonical-role documents. Headings provide context but are not Claims. Fenced code, lists, tables, blockquotes, HTML blocks, and front matter must not become Claim candidates. [SOURCE:RAW]
- Paragraph text and line bounds must remain exact enough for direct-source review; normalization may stabilize line endings and surrounding blank space but must not paraphrase. [SOURCE:RAW]
- Repeated identical eligible blocks must retain distinct occurrence identities. Cross-snapshot matching that cannot distinguish duplicates must report `ambiguous_duplicate` rather than guess. [SOURCE:RAW]
- Comparison must report `unchanged`, `modified`, `moved`, `deleted`, `added`, `ambiguous_duplicate`, and `mode_changed` using deterministic rules and reasons. [SOURCE:RAW]
- Comparison is observational. It must not mutate candidate or accepted-memory lifecycle state. [SOURCE:RAW]
- Ingestion must not call `review_candidate`, create accepted objects, assign accepted or verified epistemic status, or add Authority. [SOURCE:RAW]
- Existing Candidate Review and Promotion remains the only promotion path; focused tests must prove accept/amend/reject/defer behavior still works for Claim candidates. [SOURCE:REF:soane/project_memory/review.py]
- Add thin `ingest-markdown` and `compare-markdown` CLI commands over service functions with deterministic JSON output; optional candidate export may write ordinary JSON artifacts but is not persistence. [SOURCE:RAW]
- Prove the workflow with synthetic fixtures and one copied, fixed excerpt from `docs/PROJECT_MEMORY_ARCHITECTURE.md`; tests must not depend on mutable live canonical text. [SOURCE:RAW]

## Non-Goals

- model-based extraction, sentence inference, summarization, or semantic deduplication
- automatic review, promotion, fact status, authority assignment, or accepted-memory mutation
- constitutional authored-authority ingestion
- list, table, code, blockquote, HTML, front-matter, or generated-artifact claim extraction
- generated or curated Markdown write-back
- runtime Decision Review, Delegation, or broad Knowledge Scope objects
- organisation, portfolio, public, or cross-project promotion
- persistence, schema migration, embeddings, external providers, product UI, or live adapters
- importing or depending on private helpers from `scripts/factory_context_index.py`
- changing the Factory context index schema or treating its `facts` table as Claims
- bulk repository ingestion

## Principles

- Candidate extraction is not truth creation.
- Exact provenance is more important than extraction coverage.
- Role, authority mode, source authority, evidence level, lifecycle, epistemic status, and Knowledge Scope remain distinct.
- Ambiguity fails closed and is reported.
- Product code must own its parser; Factory indexing remains an advisory retrieval input.
- The first proof optimizes for reviewability and determinism, not recall volume.

## Roles

- Project Memory contract: defines Claim candidate invariants.
- Markdown ingestion service: parses eligible blocks and creates proposed candidates and snapshots.
- Existing role classifier: supplies role only, never authority mode.
- Candidate Review and Promotion: remains the sole promotion path.
- Human reviewer: decides whether a Claim candidate may be accepted, amended, rejected, or deferred.
- Agent caller: requests ingestion or comparison and receives explanations; it gains no Authority.

## Acceptance Criteria

- Valid Claim candidate and every invalid metadata combination have focused contract coverage.
- Canonical prose creates stable proposed Claim candidates with exact anchors and fingerprints.
- Excluded roles and Markdown constructs produce explicit exclusions and zero candidates.
- Same input produces byte-stable semantic results and deterministic IDs.
- Every comparison state has a fixture, including duplicate ambiguity and authority-mode change.
- Claim candidates can traverse existing review semantics without any ingestion-side promotion.
- CLI JSON exposes source snapshot, candidates, exclusions, warnings, comparison states, and reasons.
- A fixed real canonical excerpt proves realistic paragraph extraction.
- Full repository tests pass and no forbidden dependency, persistence, index-schema, provider, UI, or external-product change appears.

## Open Questions

- NON-BLOCKING: Candidate export filenames may use candidate IDs or stable ordinal prefixes; outputs must be deterministic and collision-safe.
- NON-BLOCKING: The implementation may place shared role vocabulary in a small product-owned module if that removes a real import cycle without changing role semantics.

## Go Or No-Go Rule

Go only if the final pack proves exact provenance, fail-closed extraction and comparison, sole-path review promotion, compatibility with current agent context, and no scope expansion into persistence, semantic inference, write-back, or cross-project knowledge.
