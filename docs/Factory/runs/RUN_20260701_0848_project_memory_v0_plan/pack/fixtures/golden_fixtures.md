# Golden Fixture Definitions

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F golden fixture definitions.

## GF-001 Decision Linked To Evidence

- Given: a Decision object and an Evidence Artifact object.
- When: the Decision is accepted.
- Then: the Decision records the Evidence Artifact relationship and evidence level.

## GF-002 Assumption Superseded By Evidence

- Given: an active Assumption and later stronger Evidence.
- When: the Evidence invalidates or replaces the Assumption.
- Then: the Assumption remains inspectable but is marked superseded or invalidated.

## GF-003 Contradiction Between Sources

- Given: two source references with incompatible claims.
- When: both are ingested or reviewed.
- Then: Project Memory records a contradiction and does not flatten the claims into false synthesis.

## GF-004 Stale Evidence

- Given: accepted Evidence with freshness metadata.
- When: the evidence becomes stale.
- Then: context assembly does not use it as current support without surfacing staleness.

## GF-005 Markdown Source Mapping

- Given: generated or curated Markdown.
- When: a claim appears in Markdown.
- Then: the claim maps back to source memory object identifiers.

## GF-006 Mocked Provider Invocation

- Given: a mocked Cursor, Codex, or OpenAI adapter invocation.
- When: the invocation record is stored.
- Then: it records provider, task purpose, inputs, outputs, policy context, evidence or trace reference, and confidence/cost/latency metadata where available.

## GF-007 Capability Without Authority

- Given: an adapter or model has a declared Capability.
- When: no Authority Reference exists for a consequential action.
- Then: Project Memory represents capability separately and does not imply permission.

## GF-008 Redaction Or Retrieval Suppression

- Given: a memory object requiring redaction, access restriction, or retrieval suppression.
- When: context assembly runs.
- Then: restricted content is not exposed while audit-safe metadata remains where allowed.

## GF-009 Unauthorized Retrieval Blocked

- Given: a caller outside object visibility scope.
- When: direct lookup, search, or context assembly requests the object.
- Then: all retrieval paths enforce the same denial.

## GF-010 Superseded Record Excluded As Current Truth

- Given: a superseded Decision or Assumption.
- When: current context is assembled.
- Then: the superseded object can be inspected but is not presented as current truth.

## GF-011 Provenance Lineage

- Given: a promoted claim derived from a source and review step.
- When: provenance is inspected.
- Then: source, writer, time, evidence level, and derivation lineage are reconstructable.

## GF-012 Controlled Propagation

- Given: memory with project, actor, task, and adapter visibility constraints.
- When: a task context package is built.
- Then: context assembly includes only allowed memory and records exclusions.
