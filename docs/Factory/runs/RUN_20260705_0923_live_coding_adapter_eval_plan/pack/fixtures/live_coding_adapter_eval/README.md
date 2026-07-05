# Live Coding Adapter Evaluation Fixtures

## Version

v1

## Change Log

- v1 (2026-07-05): Initial fixture contract sketch.

## Suggested Fixture Shape

```json
{
  "surface": "codex_cli",
  "surface_kind": "cli",
  "source_refs": ["https://developers.openai.com/codex/cli"],
  "invocation_modes": ["interactive", "non_interactive"],
  "auth_modes": ["chatgpt", "api_key"],
  "mutation_controls": ["sandbox", "approval_policy"],
  "structured_output": true,
  "event_stream": true,
  "traceability": ["jsonl_events", "provider_invocation_record"],
  "requires_authority_for_live_use": true,
  "recommended_first_live_proof": true,
  "blocked_reasons": []
}
```

## Required Negative Cases

- Missing authority.
- Missing credential boundary.
- No proven read-only or dry-run mode.
- No structured output or parseable event stream.
- No trace/evidence reference path.
- Surface requires repository mutation to evaluate.
