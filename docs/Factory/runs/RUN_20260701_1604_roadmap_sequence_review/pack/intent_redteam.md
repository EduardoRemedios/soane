# Intent Red Team: Roadmap Sequencing Review

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red team.

## Iteration

Iteration: 1 of max 2

## Findings

### High: Workspace Shell could be pulled forward too early

- Why it matters: The product shell will be better designed after the coding proof is navigable as a workflow.
- Fix recommendation: Put a thin workflow wrapper before Workspace Shell architecture.

### High: Live adapters could be started before boundaries are inspectable

- Why it matters: Live provider calls add nondeterminism and authority risk.
- Fix recommendation: Keep live adapter evaluation after deterministic workflow wrapper and explicit adapter evaluation planning.

### Medium: Persistence could be chosen too early

- Why it matters: Storage choices are expensive to unwind if object lifecycle and workflow usage are still moving.
- Fix recommendation: Place persistence architecture after workflow wrapper and memory-provider evaluation.

### Medium: Brownfield complexity could be underrepresented

- Why it matters: Brownfield multi-repo systems are likely, and single-repo proof may hide system-boundary gaps.
- Fix recommendation: Add Brownfield multi-repo coding proof before first product surface.

## Critical Findings

- None after proposed sequencing.
