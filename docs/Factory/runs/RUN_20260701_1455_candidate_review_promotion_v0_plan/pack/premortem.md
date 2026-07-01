# Pre-Mortem

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E pre-mortem.

## Failure Scenarios

### PM-001 Silent Promotion

Candidate objects become accepted Project Memory without explicit review action.

Mitigation: Require review decision objects or transition functions with reviewer provenance and rationale.

### PM-002 Authority Drift

Accepted memory is misread as authority to execute work or call an adapter.

Mitigation: Test that accepted objects do not grant authority without explicit Authority Reference linkage.

### PM-003 Lost Lineage

Amended candidates overwrite original claims and lose evidence of what changed.

Mitigation: Preserve derivation references and original candidate inspectability.

### PM-004 Current Truth Pollution

Rejected, deferred, stale, superseded, or candidate-only records appear in current-truth retrieval.

Mitigation: Add fixtures and service tests that separate current objects from non-current review states.

### PM-005 CLI Scope Creep

A CLI command grows into a product workflow or duplicates service logic.

Mitigation: Keep CLI optional and thin; require shared service delegation if implemented.

### PM-006 Persistence Prematureness

Database concerns force migration or storage decisions before local semantics are stable.

Mitigation: Keep the slice in-memory and fixture-backed.

## Top Mitigation Summary

The future implementation should start with service semantics and negative fixtures before any CLI wrapper.
