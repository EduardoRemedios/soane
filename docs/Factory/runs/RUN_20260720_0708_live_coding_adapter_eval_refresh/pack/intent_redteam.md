# Intent Red Team: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage B red-team in the upstream planning run.
- v2 (2026-07-20): Re-ran Stage B against current sources and context implementation.

## Iteration: 1 of max 2

## Findings

| Severity | Finding | Why It Matters | Fix Recommendation |
| --- | --- | --- | --- |
| Critical | "Evaluate live adapters" can still be misread as permission to probe an installed CLI, auth status, or environment. | Even `--version`, `status`, config, or help probes can inspect user state, execute unreviewed binaries, or create files. | Limit implementation inputs to committed fixtures and explicit function arguments; forbid subprocess, provider imports, environment credential lookup, and provider config discovery. |
| Critical | Current Cursor official pages conflict on whether headless mode can write without `--force`. | A favorable score would rest on ambiguous mutation containment. | Add `source_contradiction` and `hard_read_only_unproven` blockers that scoring cannot override. |
| High | The old pack expected Codex CLI to win. | Predetermined outcomes undermine a deterministic comparison. | Remove expected winner language; apply fixed gates and tie-breaks before loading profiles. |
| High | A new evaluator could build its own repository scanner or context summary. | This would create a second brain beside `agent-context` and bypass visibility, lifecycle, graph, and budget semantics. | Require existing agent-context output as the only repo-context input and test that no scan/traversal implementation is introduced. |
| High | Source recency can be mistaken for behavioral proof. | Current documentation can change and may omit operational constraints. | Record source access date, evidence kind, contradiction state, and implementation-time revalidation; keep live behavior as deferred V4 proof. |
| High | Agents SDK tracing and state may carry sensitive inputs. | A later integration could leak project context even when tool mutation is gated. | Score trace privacy and state/credential handling separately; block when sensitive capture controls are unclear. |
| Medium | Codex SDK is now an adjacent credible surface. | Silently adding it would expand the five-surface contract and file budget. | Record it as a bounded deferral only. |
| Medium | Recommendation output could be treated as accepted Project Memory. | Evaluation is evidence for review, not authority. | Keep output as deterministic local report and require explicit later review/write path. |

## Agent Failure Modes

- Executes a local provider command while gathering "static" metadata.
- Reads `OPENAI_API_KEY`, `CURSOR_API_KEY`, `CODEX_HOME`, config files, login state, or session history.
- Resolves contradictory source claims by choosing the more favorable page.
- gives a high aggregate score to a surface with one hard safety blocker.
- Reimplements file discovery, symbol search, context ranking, or graph traversal inside the evaluator.
- Adds Codex SDK or another surface because it now looks stronger than an in-scope candidate.
- Treats a deterministic recommendation as authority for a live run.

## Verification Holes Closed By Synthesis

- Add no-touch dependency-injection tests that fail on subprocess, network, environment credential access, and writes outside approved report destinations.
- Add contradictory-source, stale-source, missing-read-only, and no-safe-surface fixtures.
- Add order-independence, tie, blocked-winner, and reason-code tests.
- Add context-bundle contract tests using existing agent-context output.
- Add static import and scope scans for provider SDKs, alternate graph/context modules, and persistence.
