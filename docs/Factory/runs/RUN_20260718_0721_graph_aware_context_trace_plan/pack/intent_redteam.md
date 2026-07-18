# Intent Red Team: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage B adversarial review.

## Iteration

Iteration: 1 of max 2

## Findings

### RT-01 Critical: Direction Can Reverse Meaning

- Why it matters: `depends_on` outbound from a Decision identifies prerequisites, while inbound identifies dependents. Treating both as interchangeable would make `affected` results wrong.
- Fix: Require every path step to record direction and define command-specific direction policies.

### RT-02 Critical: Hidden Nodes Can Leak Through Explanations

- Why it matters: Recording a hidden object's title, type, or relationship metadata in exclusions reveals content that visibility rules deny.
- Fix: Use opaque exclusion records for inaccessible targets and never continue traversal through them.

### RT-03 Critical: Object Budget Alone Does Not Bound Work

- Why it matters: Dense cycles can enumerate many paths or neighbors before a small object result is emitted.
- Fix: Bound depth, selected objects, paths per object, total examined edges, exclusions, and serialized explanations.

### RT-04 High: Lifecycle Semantics Are Underspecified

- Why it matters: Proposed Claims and superseded Decisions could displace current accepted objects or disappear despite trace use cases.
- Fix: Make non-current inclusion explicit per request and rank current before non-current at equal depth.

### RT-05 High: Multiple Shortest Paths Can Be Nondeterministic

- Why it matters: Set/dict insertion order from fixture loading can alter explanations and snapshots.
- Fix: Define canonical neighbor and path ordering before budget application.

### RT-06 High: Seed Admission Can Bypass Policy

- Why it matters: A caller-provided hidden or unknown seed could surface through special-case handling.
- Fix: Apply the same visibility checks to seeds and record unknown versus inaccessible without content leakage.

### RT-07 High: `agent-context` May Retain Two Graph Implementations

- Why it matters: Keeping `_select_memory_ids` one-hop behavior alongside a new service creates inconsistent budgets and policies.
- Fix: Require removal or delegation of private relationship expansion to the shared traversal service.

### RT-08 High: `affected` Policy Could Overstate Impact

- Why it matters: Traversing every relationship type in both directions can label evidence, authorities, and unrelated references as impacted.
- Fix: Define a narrow allowlist and direction table for source-impact propagation and explain direct versus propagated matches.

### RT-09 Medium: Proposed Claim Proof May Not Exercise Review Boundaries

- Why it matters: A realistic Claim graph could accidentally imply proposed content is current truth.
- Fix: Include explicit proposed/non-current handling and assert no lifecycle mutation or promotion.

### RT-10 Medium: CLI Compatibility Could Break Existing Consumers

- Why it matters: Replacing outgoing/incoming arrays or current context reason strings would cause avoidable regressions.
- Fix: Preserve existing fields and add graph details additively where practical.

### RT-11 Medium: Missing Targets Need Stable Semantics

- Why it matters: External refs and malformed local refs can be confused with inaccessible objects.
- Fix: Classify external, missing-local, inaccessible, disallowed-relationship, depth, and budget exclusions separately.

### RT-12 Medium: Generalization Pressure

- Why it matters: A configurable traversal service can drift into a query language or graph persistence layer.
- Fix: Keep a frozen request/result dataclass API, two-hop maximum, existing relationship enum, and no predicate language.

## Agent Failure Modes

- Agent assumes inbound `depends_on` means the same as outbound.
- Agent includes every visible relationship because the user asked for context.
- Agent serializes all discovered paths after selection budget is reached.
- Agent traverses through a suppressed bridge to a visible destination.
- Agent treats a proposed Claim as accepted because it appears on a path.
- Agent presents source proximity as causal impact without relationship explanation.

## Verification Holes

- The initial intent does not name an examined-edge budget.
- External references versus unresolved local IDs need separate fixture cases.
- Backward-compatible JSON shape needs an explicit regression assertion.
- Equal-length alternate-path behavior needs a deterministic golden result.

## Required Synthesis

Harden the intent with an examined-edge budget, opaque policy exclusions, no traversal through hidden nodes, explicit impact-policy semantics, external-reference classification, additive CLI compatibility, and deterministic alternate-path rules.
