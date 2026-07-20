# Pre-Mortem: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage E pre-mortem in the upstream planning run.
- v2 (2026-07-20): Reworked failure scenarios for source contradiction and current context reuse.

## Failure Scenarios

| Scenario | Consequence | Mitigation |
| --- | --- | --- |
| Implementation probes a provider binary, environment, config, auth state, or session while building a profile. | Credentials or user state are exposed; unreviewed code runs; local files may change. | Fixture-only inputs, explicit paths, no subprocess/provider imports/environment credential reads, and no-touch tests. |
| Cursor's contradictory write claims are normalized into one favorable interpretation. | A later "read-only" proof can mutate a workspace. | Treat contradiction and unproven hard read-only as non-compensable blockers with exact source refs. |
| Codex CLI is hard-coded as the winner. | Evaluation becomes confirmation rather than evidence. | Freeze criteria, weights, hard gates, and tie rules before evaluating any surface. |
| Aggregate scoring allows a dangerous surface to win. | Strong output or trace support hides a missing sandbox or authority control. | Run hard gates before scoring; blocked surfaces are ineligible regardless of total score. |
| Evaluator scans the repository or traverses memory independently. | Soane gets a parallel context brain with different visibility, lifecycle, and budgets. | Accept only existing agent-context bundle payloads and preserve their explanations verbatim. |
| Documentation evidence is presented as measured behavior. | Human reviewers overestimate readiness for a live proof. | Label evidence kind, access date, contradiction state, and V4 deferral in every profile and report. |
| Agents SDK traces capture sensitive context by default. | Project material leaks through observability even without repository mutation. | Make trace sensitivity and export control a hard safety dimension. |
| Recommendation is written into accepted Project Memory. | A planning artifact gains authority without review. | Produce local text/JSON only; no memory mutation or review invocation in this slice. |
| Codex SDK is added opportunistically. | The bounded five-surface contract and verification matrix drift. | Keep it in a deferral note and fail unknown-surface validation. |

## Stop Conditions

- Any provider invocation, provider import, credential/config/session inspection, network access, dependency install, or external repository operation.
- Any new repository scan, graph traversal, retrieval ranker, persistence layer, or automatic memory write.
- Any unresolved Critical finding, unapproved scope expansion, or hard blocker made score-compensable.
