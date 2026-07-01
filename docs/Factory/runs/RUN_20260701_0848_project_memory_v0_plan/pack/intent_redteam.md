# Intent Red Team: Project Memory v0 Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red-team review.

## Iteration

Iteration: 1 of max 2

## Findings

### R1: The prototype could collapse into generic CRUD

- Severity: High
- Why it matters: A simple object store would not prove Project Memory semantics such as lifecycle, provenance, evidence attachment, contradiction handling, scope enforcement, or context assembly.
- Fix recommendation: Require contract-level invariants and golden fixtures before implementation.

### R2: The adapter proof could couple v0 to live CLI or SDK behavior too early

- Severity: High
- Why it matters: Live Cursor, Codex, or OpenAI behavior may be nondeterministic, version-sensitive, or unavailable in CI. That would make Project Memory tests brittle.
- Fix recommendation: Require a mock adapter contract first. Treat live CLI or SDK adapters as later implementations behind the same contract.

### R3: Coding proof could narrow the Workspace concept

- Severity: Medium
- Why it matters: The Workspace is not primarily a coding tool. Coding is useful because it provides a demanding proof path, but the object model must support other domains.
- Fix recommendation: Require domain-neutral object names and fixtures that do not depend on repository-specific semantics except in the adapter proof fixture.

### R4: Authority and capability could be blurred

- Severity: High
- Why it matters: A provider or tool being available does not mean it is permitted to act. This would violate core concepts and governance posture.
- Fix recommendation: Include `Capability without Authority` and denied/retrieval-suppressed fixtures.

### R5: Context assembly could become plain retrieval

- Severity: High
- Why it matters: Project Memory context must surface stale, superseded, contradictory, and low-evidence records correctly. Top-k retrieval is not sufficient.
- Fix recommendation: Require context assembly v0 with explicit rules for scope, freshness, lifecycle status, evidence level, and unresolved questions.

### R6: The plan may not define reversibility

- Severity: Medium
- Why it matters: Early memory formats often become sticky. Without deterministic IDs, portable storage, and migration guardrails, early data may become untrustworthy or disposable.
- Fix recommendation: Require local portable storage, deterministic IDs for fixtures, and explicit migration/rewrite rules.

## Verification Holes

- No current runnable tests exist because no product code exists.
- Golden fixtures must be specified at planning time before implementation starts.
- Stage F should map each high-risk requirement to fixture or mechanical verification tier.

## Recommendation

Proceed to Stage C only if the synthesis keeps all red-team concerns inside the locked intent and avoids expanding into implementation.

