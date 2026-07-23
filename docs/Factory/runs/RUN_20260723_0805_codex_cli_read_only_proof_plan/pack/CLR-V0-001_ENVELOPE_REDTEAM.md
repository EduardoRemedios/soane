# Envelope Red Team: CLR-V0-001

## Version

v1

## Change Log

- v1 (2026-07-23): Initial Stage I envelope and verification red-team.

## Iteration: 1 of max 2

## Findings

| Severity | Finding | Resolution |
| --- | --- | --- |
| Critical | Child environment filtering does not prevent a model command from recovering a direct key from the parent Codex process through procfs, process listings, files, sockets, or diagnostics. | Reopened the allowed intent cycle. Intent v3 prefers a single-run credential-isolating provider proxy outside Codex/model visibility and blocks direct-key auth without mechanical denial proof for all parent paths. VC-003/VC-004 and credential-route fixtures now enforce it. |
| Critical | A disposable fixture inside a workstation process still leaves unrelated host reads possible. | The locked runner topology excludes Soane, host home, unrelated repos, credential stores, agent sockets, and control sockets; VC-001/VC-002/VC-021 require offline and live evidence. |
| High | A "compatibility check" could accidentally execute a prompted `codex exec` and consume provider authority before MS-04. | Envelope v3 permits only credential-free/network-denied `codex --version` and `codex exec --help` inside the isolated runner. All other runtime discovery commands are forbidden. |
| High | A process-start race or operator rerun could turn one human Go into multiple attempts. | VC-013 and envelope v3 require a unique live-authorization ID atomically consumed before process launch; ambiguity is terminal and cannot restore the ID. |
| High | A general credential proxy could become a new platform or be reachable by model shell commands. | The allowed route is one provider, one destination allowlist, one attempt, outside Codex visibility, and unreachable from model commands. General proxy work is out of scope. |
| High | Raw evidence could be written into Soane while Codex is still active or before secret checks. | The supervisor captures through bounded pipes to an invisible quarantine outside Codex roots; only redacted post-teardown artifacts may enter normal generated paths. |
| Medium | A BLOCKED receipt might be treated as failure to implement and trigger an improvised fallback. | MS-03/MS-04 define BLOCKED as a valid terminal outcome. No alternate auth, runner, model, or retry may be improvised. |
| Medium | A successful proof could silently broaden to another repository or model. | Receipt scope and Candidate Review gates remain exact; MS-05 may recommend at most one separately planned proof. |

## Verification Asset Changes

- Hardened VC-003, VC-004, VC-005, VC-013, VC-015, and VC-022.
- Added `pack/fixtures/credential_route_cases.json`.
- Extended shell fixtures with parent-process inspection paths.
- Updated MS-02 through MS-04 and envelope v3.

## Scope Expansion Check

PASS. Credential isolation is necessary to safely perform the already scoped live
proof. It is constrained to one exact route and cannot become a reusable proxy or
runner platform.

## Verdict

PASS. No unresolved Critical finding or unapproved `[SCOPE EXPANSION]` remains.

