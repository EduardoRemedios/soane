# Intent Red Team: Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage B red team.

## Iteration

Iteration: 1 of max 2

## Findings

### High: CLI wrapper could duplicate harness logic

- Why it matters: Duplicated workflow semantics would create drift from the tested coding harness service.
- Fix recommendation: Require the CLI to delegate to `load_coding_harness_fixtures`, `run_coding_proof`, and review helpers.

### High: Workflow could imply live execution

- Why it matters: A command named like a coding workflow may be mistaken for a live coding agent.
- Fix recommendation: Require command output and metadata to show mock provider invocation and `live_call_performed=false`.

### High: Review status could be unclear

- Why it matters: Users must see that proposed output is candidate-only unless reviewed.
- Fix recommendation: Include candidate/review state in text and JSON summaries.

### Medium: Optional TUI could become product shell

- Why it matters: TUI work can drift into product UX.
- Fix recommendation: Make TUI optional and skippable; require service delegation if included.

## Verification Holes

- Need CLI tests for fixture listing.
- Need CLI tests for text and JSON run summaries.
- Need tests proving no live provider or repository mutation is invoked.

## Critical Findings

- None after proposed hardening.
