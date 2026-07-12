# Pre-Mortem: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage E pre-mortem.

## Failure Scenarios

### PM-001 - Canonical text becomes accepted truth
The ingester uses document status as promotion. Mitigation: fixed proposed/asserted candidate state and negative review-call tests.

### PM-002 - Agent reads outside the repository
Path traversal or a symlink escapes the root. Mitigation: resolved containment checks before every read and adversarial path fixtures.

### PM-003 - Candidate volume overwhelms review
Lists, tables, headings, and code become noisy Claims. Mitigation: prose paragraphs only, hard candidate budget, exclusions, and a real-document reviewability fixture.

### PM-004 - Document edits create false lineage
Anchor movement, repeated paragraphs, or line changes are guessed incorrectly. Mitigation: separate hashes and occurrence identity; ambiguous duplicates fail closed.

### PM-005 - Comparison mutates memory
Deleted or changed source blocks directly stale accepted objects. Mitigation: immutable snapshots and observational events only.

### PM-006 - Role refactor breaks agent context
Moving MarkdownRole creates import cycles or changes precedence. Mitigation: one small product-owned vocabulary module and full agent-context regression.

### PM-007 - Export becomes persistence
Agents treat exported candidate JSON as canonical storage. Mitigation: label interchange output, no index/mutation API, and retain persistence non-goals.

### PM-008 - Real-source proof becomes flaky
The live architecture document changes. Mitigation: fixed copied excerpt with origin metadata and a separate optional manual smoke against the live file.

## Highest-Risk Execution Moment

Candidate construction is the highest-risk point because role, authority mode, evidence level, epistemic status, lifecycle, and source authority converge there. Contract validation must reject every invalid combination before a candidate reaches review.
