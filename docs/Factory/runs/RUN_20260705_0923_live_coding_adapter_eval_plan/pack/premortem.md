# Pre-Mortem: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage E pre-mortem.

## Failure Scenarios

| Scenario | Consequence | Mitigation |
| --- | --- | --- |
| The implementation calls a live provider while evaluating it. | Credential exposure, cost, mutation, or unreviewed output. | Require no-live-call tests and fixtures; no SDK/CLI execution beyond optional local help probes unless separately authorized. |
| Cursor CLI is treated as safe because it has command approval. | Non-interactive full-write behavior could mutate workspaces. | Score mutation control explicitly and fail closed when read-only behavior cannot be proven. |
| OpenAI SDK is treated as a coding-agent harness. | Soane may lose repository/context semantics that coding agents provide. | Classify OpenAI SDK as model/tool invocation unless wrapped by Soane-owned orchestration. |
| Agents SDK is adopted too early. | Soane duplicates orchestration before Project Memory and authority contracts mature. | Gate Agents SDK behind trace, approval, state, and orchestration ownership requirements. |
| Evaluation matrix becomes subjective prose. | Future Go decision lacks testable evidence. | Add typed fixtures and deterministic scoring tests. |
| Provider output enters Project Memory as truth. | Candidate/review boundary breaks. | Require candidate-only output and explicit review-gated promotion in verification. |
