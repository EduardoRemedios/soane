# Live Coding Adapter Evaluation Fixture Contract

## Version

v2

## Change Log

- v1 (2026-07-05): Initial fixture sketch in the upstream planning run.
- v2 (2026-07-20): Replaced boolean suitability with evidence state, hard blockers, and separate governance dimensions.

## Profile Shape

```json
{
  "schema_version": "lcae-profile-v1",
  "surface": "codex_cli",
  "surface_kind": "cli",
  "sources": [
    {
      "url": "https://developers.openai.com/codex/cli/reference/",
      "accessed_on": "2026-07-20",
      "evidence_kind": "official_documentation",
      "claims": ["read_only_sandbox", "jsonl_events", "resume_identity"]
    }
  ],
  "source_state": "current_consistent",
  "invocation_modes": ["interactive", "non_interactive"],
  "authentication_modes": ["chatgpt", "api_key"],
  "capabilities": ["coding_harness"],
  "requires_authority": true,
  "requires_project_permission": true,
  "repository_scope_controls": ["working_directory"],
  "mutation_controls": ["read_only_sandbox"],
  "structured_output": ["jsonl_events", "output_schema"],
  "traceability": ["event_stream", "provider_invocation_record"],
  "session_identity": ["resume_session_id"],
  "cost_metadata": "provider_reported_or_deferred",
  "latency_metadata": "locally_measured_in_future_live_proof",
  "trace_privacy": "requires_explicit_policy",
  "candidate_review_required": true,
  "hard_blockers": [],
  "limitations": ["documentation_not_measured_behavior"]
}
```

## Hard Blocker Rules

- `source_contradiction`
- `hard_read_only_unproven`
- `repository_scope_unbounded`
- `authority_or_permission_missing`
- `trace_privacy_unclear`
- `candidate_review_bypass`
- `live_only_evaluation_required`

Hard blockers make a surface ineligible before scoring.

## Context Payload Rule

The evaluator accepts the existing `agent-context --json` contract or an equivalent payload produced by `build_agent_context_bundle`. It may select evidence refs from that payload but must not perform its own repository scan, document ranking, memory traversal, visibility check, lifecycle filtering, or freshness mutation.
