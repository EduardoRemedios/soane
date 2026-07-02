# Risk Register: Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage E risk register.

| Risk ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | High | CLI duplicates harness semantics. | Require delegation to existing service functions. | VC-001, VC-004 |
| R-002 | High | Mocked invocation appears live. | Show mock/live status in summaries. | VC-005, VC-008 |
| R-003 | High | Candidate output appears accepted. | Include candidate/review status and review path guard. | VC-006 |
| R-004 | Medium | JSON output is incomplete. | Require machine-readable summary assertions. | VC-003 |
| R-005 | Medium | Optional TUI becomes product shell. | Keep TUI optional and skippable. | VC-009, VC-010 |
| R-006 | Medium | Tests depend on external state. | Use deterministic fixtures only. | VC-008 |
