# Intent Red Team: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage B red-team review.

Iteration: 1 of max 2

## Findings

### RT-001 - Critical - Extraction can silently create truth
Why it matters: Markdown authority or canonical status could be mistaken for accepted memory.
Fix: All outputs remain proposed/asserted candidates; ingestion cannot invoke review or set accepted/verified state.

### RT-002 - Critical - Source paths can escape the repository
Why it matters: Agent-facing ingestion could read arbitrary files or follow symlinks outside the approved root.
Fix: Resolve and enforce repo containment, `.md` type, regular-file status, and symlink containment before reading.

### RT-003 - High - Role and authority mode can collapse
Why it matters: Existing role classification is retrieval precedence, not document write authority.
Fix: Infer role only; require explicit validated authority mode and source authority in the request and output.

### RT-004 - High - Rule-based sentence extraction produces garbage
Why it matters: Lists, tables, code, and fragmented sentences are not reliable standalone Claims.
Fix: Limit v0 to exact prose paragraphs under ATX headings and report excluded constructs.

### RT-005 - High - Fingerprints do not solve moved or duplicate blocks
Why it matters: Content-only identity collides; anchor-only identity treats every move as a rewrite.
Fix: Separate candidate identity, block fingerprint, occurrence identity, and comparison matching; report duplicate ambiguity.

### RT-006 - High - Staleness logic can mutate accepted memory
Why it matters: Persistence and lifecycle propagation are not designed.
Fix: Return observational comparison states only; lifecycle mutation is deferred.

### RT-007 - High - Importing Factory parser creates product/process coupling
Why it matters: `scripts/factory_context_index.py` is advisory Factory machinery, not the product architecture.
Fix: Implement a small product-owned parser with matching deterministic conventions and independent tests.

### RT-008 - Medium - Live canonical tests become brittle
Why it matters: Normal documentation edits would unexpectedly break fixture counts and hashes.
Fix: Check in a fixed excerpt copied from one canonical architecture document and record its origin.

### RT-009 - Medium - Export can become accidental persistence
Why it matters: Writing candidate JSON may be interpreted as the durable store.
Fix: Label export as optional interchange artifacts, use no lookup index or mutation semantics, and keep service return values primary.

### RT-010 - Medium - Scope expands to every accepted doctrine concept
Why it matters: Decision Review, Delegation, and organisation-level Knowledge Scope would turn ingestion into a platform rewrite.
Fix: Implement Claim only and represent v0 Project scope/source authority as validated candidate metadata.

## Verdict

Proceed after incorporating RT-001 through RT-010. No scope expansion is required.
