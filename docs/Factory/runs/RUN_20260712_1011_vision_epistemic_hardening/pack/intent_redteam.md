# Intent Red Team: VEH-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage B review.

Iteration: 1 of max 2

## Findings

### RT-001 - Critical - Project Memory could absorb external authority

Why it matters: Rewording source of truth without explicit source-system precedence could still imply that Workspace synthesis overrides evidence, proof, or external records.

Fix: Define Project Memory as the governed record of current understanding and require source authority on claims where applicable.

### RT-002 - High - Delegated judgement could become implied permission

Why it matters: Saying agents exercise judgement could weaken the existing Capability versus Authority boundary.

Fix: Require explicit, scoped, revocable external authority, conditions, duration, accountability, and escalation; doctrine must not mint authority.

### RT-003 - High - Cross-project retrieval could leak knowledge

Why it matters: Visibility alone is insufficient when provenance, privacy, contractual, or purpose restrictions must propagate.

Fix: Fail closed, require promotion, preserve restrictions and provenance, and never infer broader scope from relevance.

### RT-004 - High - Markdown round trips could overwrite human authority

Why it matters: A curated mode without conflict rules could silently replace authored constitutional meaning.

Fix: Separate authored authority, generated projection, and curated round trip; require reviewed promotion and conflict-safe regeneration.

### RT-005 - Medium - Claim could be mistaken for established fact

Why it matters: Extraction will produce assertions of varying quality.

Fix: Give Claim explicit epistemic states and make accepted fact status reviewable, sourced, scoped, and revisable.

### RT-006 - Medium - Outcome metrics could reward bureaucracy

Why it matters: Counts of memory objects or reviews would encourage artifact production rather than better decisions.

Fix: Use quality, latency, calibration, constraint, and human-attention measures; prohibit artifact volume as a success proxy.

### RT-007 - Medium - Doctrine could overpromise runtime support

Why it matters: New concepts do not yet exist in the v0 object registry.

Fix: Mark runtime representation as deferred and update project state truthfully.

## Verdict

Proceed after all fixes are incorporated. No scope expansion is required.
