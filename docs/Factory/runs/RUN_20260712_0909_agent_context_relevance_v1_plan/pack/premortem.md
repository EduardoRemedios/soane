# Pre-Mortem: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage E pre-mortem.

## Failure Scenarios

### PM-001 - Recall appears smarter but remains brittle

The implementation adds ad hoc token fallbacks that work for one example but produce unstable or excessive results for other natural tasks.

Mitigation: deterministic normalization, bounded attempts, stable scoring, deduplication, golden task fixtures, and hard document budgets.

### PM-002 - Zero matches still leak broad memory

An empty document result reaches lower-level context assembly and silently returns every visible memory object.

Mitigation: explicit agent selection mode, fail-closed empty/degraded result, and negative tests proving no implicit broad fallback.

### PM-003 - Graph expansion overwhelms relevance

One-hop traversal follows too many relationship types or ignores lifecycle state, consuming the memory budget with historical or weakly related objects.

Mitigation: allowlisted types, deterministic ordering, lifecycle policy, cycle deduplication, and truncation explanations.

### PM-004 - Refresh contention corrupts or lies

Two agent processes rebuild the shared SQLite index concurrently, one fails after partially replacing state, or output reports success despite reuse/failure.

Mitigation: isolated build, serialized or atomic publication, prior-index preservation, explicit refresh state, contention and failure-injection tests.

### PM-005 - Role weighting becomes authority

Constitutional or canonical Markdown is treated as automatically true, overriding Project Memory lifecycle, evidence, or contradictions.

Mitigation: role only influences document selection; output preserves role/status distinction and governance tests.

### PM-006 - Freshness expands into persistence

The slice starts mutating object staleness, creating schema or migration commitments without an ingestion contract.

Mitigation: freshness remains observational metadata; lifecycle mutation is explicitly excluded.

### PM-007 - Compatibility fix breaks audit workflows

Changing empty-seed behavior globally removes intentional lower-level broad inspection used by fixtures or auditors.

Mitigation: keep broad inspection explicit and access-controlled, test both agent fail-closed and lower-level broad paths, run full regression.

## Highest-Risk Execution Moment

The selection boundary between agent context and lower-level context assembly is the highest-risk point. Implementation must make caller intent explicit rather than infer broad selection from an empty seed list.
