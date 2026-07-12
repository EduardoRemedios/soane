# Envelope Red Team: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage I envelope review.

Iteration: 1 of max 2

## Findings

### ER-001 - High - Relationship allowlist is not named

Why it matters: Leaving the allowlist entirely to implementation permits accidental fan-out or inconsistent fixtures.

Fix: Name the default semantic edge types and explicitly exclude generic structural/provenance fan-out types unless directly seeded.

### ER-002 - High - Output states need closed vocabularies

Why it matters: Free-form selection and refresh labels make CLI tests and downstream agent behavior ambiguous.

Fix: Define bounded values for selection state/mode and refresh state.

### ER-003 - Medium - Non-current related objects need presentation rules

Why it matters: A stale, superseded, proposed, or open object could appear indistinguishable from current accepted memory.

Fix: Preserve existing current versus surfaced separation and require relationship reason plus lifecycle status.

### ER-004 - Medium - Locking must not leave stale lock artifacts

Why it matters: A crashed process could permanently block refresh.

Fix: Use operating-system file locking or another ownership-aware local mechanism; do not rely only on an unowned sentinel file.

### ER-005 - Low - Closeout should record residual lexical limitations

Why it matters: Passing bounded lexical fixtures does not prove semantic retrieval quality.

Fix: Require the validation closeout to retain this residual risk.

## Scope Expansion Check

- No scope expansion is required.
- Findings harden the existing refresh, traversal, output, and closeout contracts.

## Verdict

Incorporate ER-001 through ER-005 in envelope v2, then proceed to Stage J.
