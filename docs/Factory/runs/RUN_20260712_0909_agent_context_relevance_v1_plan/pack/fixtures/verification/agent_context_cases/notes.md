# Agent Context Case Sketches

## Version

v1

## Change Log

- v1 (2026-07-12): Initial fixture sketches.

## Cases

- `natural_task_fallback`: long task text selects `docs/PROJECT_MEMORY_ARCHITECTURE.md` and `docs/ROADMAP.md` within budget.
- `zero_match`: unknown task selects no documents and no memory, with `selection_state=degraded` and `reason=no_relevant_context`.
- `explicit_broad`: lower-level explicit broad selection returns visible memory but never suppressed or inaccessible objects.
- `one_hop_budget`: allowlisted edges expand once, dedupe a cycle, and record budget truncation.
- `refresh_contention`: competing rebuilds never expose a partially built database.
- `refresh_failure`: failed isolated rebuild preserves prior index and returns `refresh_state=failed`.

Exact fixture JSON belongs to implementation MS-00 so it matches the selected public data shape.
