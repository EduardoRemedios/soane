# Risk Register: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage E risk register.
- v2 (2026-07-23): Hardened credential isolation after second-cycle review.

| ID | Risk | Severity | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Model commands can read host files outside the fixture. | Critical | Require an attested disposable runner with a deny-by-absence mount topology and no host state. | VC-001, VC-002, VC-021 |
| R-002 | Provider credential reaches model-generated subprocesses through inheritance or parent-process inspection, or enters persisted/provider-visible output. | Critical | Prefer an external single-run credential proxy; block direct keys without parent-path denial proof; retain shell filtering and protected-form stream rejection as secondary controls. | VC-003, VC-004, VC-005, VC-022 |
| R-003 | User, project, managed, plugin, MCP, hook, skill, app, proxy, or session state changes behavior. | High | Use a fresh controlled home, explicit overrides, an instruction-free fixture, and fail on unknown state/events. | VC-006, VC-007, VC-008 |
| R-004 | Codex or the fixture mutates despite read-only claims. | Critical | Use a non-writable fixture, no writable Codex mount, pre/post manifests, Git status, and file-change event rejection. | VC-009, VC-010, VC-023 |
| R-005 | Wrapper evidence writes are confused with Codex writes or exposed to Codex. | High | Capture through supervisor pipes to an invisible evidence root and record write attribution. | VC-011, VC-012 |
| R-006 | Retry, resume, fallback, auth recovery, or rerun exceeds the one-call ceiling. | High | Use a terminal one-shot state machine; any attempt consumes authority and ambiguity fails. | VC-013, VC-024 |
| R-007 | CLI/source drift invalidates required flags or config semantics. | High | Pin runner/CLI evidence, revalidate official sources, and run no-provider compatibility checks. | VC-014, VC-015 |
| R-008 | Unknown events or external tools are interpreted permissively. | High | Use an explicit event allowlist and fail on unknown, approval, web, MCP, app, remote, or mutation events. | VC-016, VC-025 |
| R-009 | Timeout, output overflow, malformed schema, non-zero exit, or wrong facts still yields a favorable result. | High | Use independent terminal reason codes and evaluate correctness only after containment passes. | VC-017, VC-018 |
| R-010 | Live execution occurs before offline controls pass or without complete authority inputs. | Critical | Put every offline gate, authority reference, model, runner identity, permission, and spend ceiling before the invocation transition. | VC-019, VC-026 |
| R-011 | Receipt is promoted or treated as broad operational authorization. | High | Mark it generated, candidate-only, narrowly scoped, and subject to Candidate Review and a new Go. | VC-020 |
| R-012 | Disposable runner or raw evidence is not destroyed as claimed. | High | Record teardown and retention outcomes; incomplete destruction fails closeout. | VC-012, VC-021 |
