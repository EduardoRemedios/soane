# Intent Red Team: Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red team.

## Iteration

Iteration: 1 of max 2

## Findings

### High: Harness could become a product workflow too early

- Why it matters: A broad workflow layer could pull in Workspace Shell, UI, persistence, or live adapter concerns before the service contract is proven.
- Fix recommendation: Keep the slice service-first. Make any CLI wrapper optional and require it to delegate to shared service functions.

### High: Provider output could bypass review

- Why it matters: The whole Soane memory model depends on generated material staying candidate-only until reviewed.
- Fix recommendation: Require tests proving provider outputs are non-current Project Memory candidates and only become current after Candidate Review and Promotion.

### Medium: Greenfield/Brownfield behavior may flatten into one generic coding path

- Why it matters: Brownfield work requires repository audit and starting-context checks that Greenfield work does not.
- Fix recommendation: Require separate fixtures for Greenfield and Brownfield coding contexts, with Brownfield readiness gates.

### Medium: Adapter selection could imply authority

- Why it matters: A provider may be technically available but not authorized for a task.
- Fix recommendation: Preserve Capability Reference and Authority Reference separation in Provider Invocation records.

### Medium: Verification could accidentally require live tools

- Why it matters: Live provider calls would make v0 nondeterministic and would exceed the intended proof.
- Fix recommendation: Keep all checks V1 to V3 and explicitly forbid V4 live verification in this slice.

## Verification Holes

- Need a fixture proving proposed code output is not accepted truth.
- Need a fixture proving Brownfield blocked/audit state prevents ready-for-planning.
- Need a check proving no live CLI, SDK, database, or repository mutation is invoked.

## Critical Findings

- None after proposed hardening.
