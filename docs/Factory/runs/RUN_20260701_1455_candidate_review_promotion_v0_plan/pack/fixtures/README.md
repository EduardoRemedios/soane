# Fixture Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F fixture plan.

## Required Future Fixtures

The future `CRP-V0-001` implementation should add deterministic fixtures for:

- `CRP-GF-001`: accept a candidate with reviewer rationale and retained provenance
- `CRP-GF-002`: reject a candidate while keeping it inspectable and out of current truth
- `CRP-GF-003`: defer a candidate with non-empty reason and open follow-up
- `CRP-GF-004`: amend a candidate while preserving lineage to the original candidate
- `CRP-GF-005`: block unauthorized promotion where authority is absent
- `CRP-GF-006`: preserve conflicting candidates without flattening contradiction

## Fixture Constraints

- Fixtures must be local JSON or Python fixture data.
- Fixtures must not call live adapters, external connectors, or databases.
- Fixtures must be deterministic across repeated test runs.
- Accepted objects must not imply execution authority.
