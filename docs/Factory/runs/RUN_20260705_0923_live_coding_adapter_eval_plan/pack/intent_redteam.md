# Intent Red Team: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage B red-team.

## Iteration: 1 of max 2

## Findings

| Severity | Finding | Why It Matters | Fix Recommendation |
| --- | --- | --- | --- |
| Critical | "Live evaluation" could be misread as permission to call live providers. | This would bypass the roadmap gate and could expose credentials, mutate repos, or create unreviewed output. | State that this slice evaluates surfaces from source-backed profiles and deterministic fixtures only. |
| High | Cursor CLI non-interactive mode may have broad write capability. | A CLI proof can mutate workspaces if invoked without strict containment. | Require blocked fixture and safety gate for any surface whose dry-run or read-only behavior is not proven. |
| High | SDK surfaces may pull Soane toward orchestration before the adapter contract is stable. | SDK integration could blur Provider Invocation, Inference Strategy, and mission/execution ownership. | Keep SDK evaluation as profile/scoring only until CLI-backed proof contracts are verified. |
| Medium | Auth requirements may be treated as availability. | Having an API key or login does not grant authority to use a provider for a project. | Model auth, capability, and authority as separate criteria. |
| Medium | Output capture may skip Candidate Review and Promotion. | Model output could enter Project Memory as truth. | Require candidate-only fixtures and review-gated promotion as verification checks. |

## Agent Failure Modes

- Agent invokes a CLI while "checking availability."
- Agent stores or prints credential material while assessing auth.
- Agent treats provider trace output as accepted evidence without review.
- Agent recommends the most powerful SDK instead of the safest first proof.
- Agent ignores Brownfield multi-repo boundary requirements.

## Verification Holes

- Need explicit no-live-call tests.
- Need fixture coverage for missing auth, missing authority, unsafe mutation permissions, and missing structured output.
- Need source provenance for each adapter profile.
