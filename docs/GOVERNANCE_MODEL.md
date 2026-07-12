# Governance Model

## Status

This document defines how the Soane repository governs its own architectural knowledge, decisions, assumptions, evidence, and implementation readiness.

It is a Soane document. It does not define the authority model of Aegis, the mission governance model of Factory V3, the process doctrine of Factory V2, the runtime policy model of Harmony, or the execution model of Temper.

It builds on:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/PORTFOLIO_CONTEXT.md`
- `docs/PORTFOLIO_ASSUMPTIONS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`

Amendment record:

- 2026-07-12: Aligned the explicit canonical-document registry and current governance-work summary with the implemented architecture, repository context, and Project Memory slices. Human authority: repository owner approval in the canonical-doc freshness review.

## Purpose

The Workspace exists to improve human judgement before autonomous execution.

This repository therefore needs a governance model before it needs application code. The model should make it clear:

- which documents are authoritative
- how constitutional documents change
- how decisions are recorded
- how assumptions are handled
- what evidence is sufficient for different claims
- what blocks implementation
- how Factory V2 process relates to Soane governance
- where Soane authority stops and neighbouring products begin

The goal is discipline, not bureaucracy.

## Document Status Levels

Soane documents should have one of four status levels.

### Constitutional

Constitutional documents define durable product identity, core vocabulary, product boundaries, and governance rules.

Current constitutional documents:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`

Constitutional documents should change rarely. They may be amended, but not casually rewritten.

### Canonical

Canonical documents are stable architectural or product records that guide future work but sit below constitutional documents.

Current canonical documents:

- `AGENTS.md`
- `docs/PORTFOLIO_CONTEXT.md`
- `docs/PORTFOLIO_ASSUMPTIONS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`

Canonical documents should remain aligned with constitutional documents and Project Memory once Project Memory exists.

### Working

Working documents support active planning, research, Factory V2 runs, design exploration, or implementation preparation.

Examples include:

- Factory V2 run artifacts
- planning briefs
- research notes
- architecture sketches
- readiness reports
- implementation plans

Working documents may contain open questions, unresolved assumptions, and draft recommendations. They should not be treated as settled truth until promoted.

### Generated

Generated documents are produced from tools, Project Memory, Factory V2 process, or other systems.

Generated documents are useful evidence and review surfaces. They are not automatically authoritative unless a human or governance process promotes them.

## Markdown Role Vocabulary

Markdown files should be classified by their role before agents use them as context.

The current role vocabulary is:

- `constitutional`: durable product identity, core vocabulary, and governance rules. Current examples: `docs/VISION.md`, `docs/CORE_CONCEPTS.md`, and `docs/GOVERNANCE_MODEL.md`.
- `canonical`: stable architectural, project-state, roadmap, changelog, integration, or repository-context records that guide future work.
- `working`: active planning, templates, run artifacts, sketches, and other non-final work surfaces.
- `generated`: tool-produced or process-produced reports, prompts, closeouts, checklists, and recall artifacts.
- `evidence`: verification plans, traceability matrices, risk registers, pre-mortems, research synthesis, and reviewed source-analysis artifacts.
- `deprecated`: archived, superseded, or intentionally retired Markdown that must not be treated as current truth unless surfaced for history.

Markdown role is not the same thing as Project Memory status. A canonical Markdown file can still contain claims that need Project Memory objects, and a generated Markdown file can become evidence without becoming authoritative truth.

## Amendment Rules

### Constitutional Amendments

Changing a constitutional document requires an explicit amendment.

An amendment should record:

- document being amended
- reason for change
- current problem or ambiguity
- proposed change
- expected consequences
- affected documents
- evidence or reasoning
- approval by the responsible human authority

An amendment should not be hidden inside unrelated edits.

### Canonical Updates

Canonical documents may be updated when:

- new architectural understanding exists
- a boundary has been clarified
- an assumption has changed
- implementation has taught something durable
- a portfolio source has superseded prior understanding

Canonical updates should preserve traceability. If a change alters meaning, the commit or document should explain why.

### Working Changes

Working documents may evolve freely during active work.

They should still distinguish:

- facts
- assumptions
- hypotheses
- decisions
- evidence
- recommendations

## Decisions

A Decision is an explicit commitment to a course of action, interpretation, boundary, priority, design, policy, or plan.

Important Decisions should be recorded when they affect:

- product scope
- core terminology
- architecture
- portfolio boundaries
- implementation readiness
- integration contracts
- authority or evidence expectations
- document status
- long-term Project Memory shape

A Decision should record:

- decision statement
- decision owner or responsible authority
- date
- context
- options considered
- rationale
- evidence used
- assumptions accepted
- constraints applied
- expected consequences
- reversal conditions
- affected documents or systems

Until Project Memory exists, important Decisions should be recorded in canonical Markdown documents or Factory V2 run artifacts and reflected in `docs/PROJECT_STATE.md` when they change repository posture.

## Assumptions

An Assumption is a statement treated as true for reasoning or planning without enough evidence to treat it as established fact.

Assumptions should be visible when they affect architecture or implementation.

An Assumption may be:

- accepted for planning
- under investigation
- converted to a Hypothesis
- converted to a Decision
- invalidated
- superseded

Assumptions should not silently become facts.

Portfolio assumptions belong in `docs/PORTFOLIO_ASSUMPTIONS.md` unless they become stable Workspace decisions or integration contracts.

## Evidence Levels

Soane should distinguish evidence strength before Aegis integration exists.

### E0: Stated Intent

Human-stated intent, notes, conversation, or planning text.

Use for early direction. Do not treat as proof.

### E1: Source Reference

Evidence from an existing canonical document, repository file, or portfolio source.

Use for architectural grounding.

### E2: Reviewed Synthesis

Evidence from a reviewed document that compares sources, records assumptions, and names uncertainty.

Use for canonical planning and architecture decisions.

### E3: Mechanical Verification

Evidence from deterministic checks, tests, lints, scripts, or reproducible commands.

Use for implementation readiness and process confidence.

### E4: Runtime Or Mission Evidence

Evidence produced during execution, mission runs, operational workflows, telemetry, or supervised delegation.

Use only when the producing system owns that evidence.

### E5: Authority Or Proof

Authority references, receipts, proof bundles, or evidence packets from Aegis or another explicitly authorized governance system.

Use for consequential action, high-assurance claims, and proof-grade trust.

The Workspace may store and present E5 references. It does not create E5 proof by itself.

## Authority

Soane does not own the portfolio authority substrate.

In this repository:

- human approval can authorize repository changes
- Factory V2 can structure planning and evidence
- deterministic checks can support confidence
- Aegis remains the expected owner of authority, receipts, proof, and trust semantics

Factory V2 process does not create authority by itself.

A passing Factory V2 pack means the planning artifact satisfied the local process gate. It does not mean execution is authorized, proof exists, or a neighbouring product boundary may be crossed.

## Implementation Readiness

Implementation should be considered ready only when the relevant work has:

- clear objective
- bounded scope
- known non-goals
- identified assumptions
- known constraints
- evidence appropriate to risk
- verification plan
- affected documents or systems identified
- ownership boundary checked
- human authorization where execution is consequential

For small, clear documentation updates, a full Factory V2 run is not required.

For larger architecture, implementation, integration, or product-surface work, use Factory V2 planning before execution.

## Blocking Conditions

Work should halt or return to planning when any of these conditions apply:

- product boundary is unclear
- authority is required but absent
- evidence is missing for a consequential claim
- assumption is being treated as fact
- decision owner is unclear
- Factory V2 or Factory V3 responsibilities are confused
- Workspace is duplicating Temper, Aegis, Sentinel, Harmony, or Factory V3 responsibilities
- external portfolio context conflicts with Soane documents
- implementation scope exceeds the approved intent
- verification path is absent for risky changes

When blocked, record the blocker as a Question, Assumption, Constraint, or Decision need.

## Factory V2 Relationship

Soane includes a local Factory V2 scaffold under `docs/Factory/`.

Factory V2 is used for:

- planning discipline
- raw brief hardening
- bounded execution contracts
- verification planning
- evidence-backed handoffs
- review readiness

Factory V2 does not own:

- Soane product vision
- Workspace architecture
- authority
- proof
- mission governance
- agent runtime
- regulated conversation

In `docs/Factory/`, the unqualified term "Factory" means the Factory V2 starter-kit process. It does not mean Factory V3.

## Factory V3 Relationship

Factory V3 remains separate in `/Users/eduardodosremedios/Factory_V3`.

Soane may eventually integrate with Factory V3 for mission governance. Soane should not import Factory V3 mission governance into this repository.

The Workspace may plan, launch, monitor, pause, resume, inspect, and review missions through Factory V3. Factory V3 governs executable missions.

## Project Memory Relationship

Project Memory is the intended governed system of record for the Workspace's current Project understanding. It does not supersede source-system authority for external records.

Until richer Project Memory representation exists, canonical Markdown documents act as the repository's durable knowledge surface according to their declared document status and authority mode.

Once Project Memory exists:

- canonical Markdown should declare authored-authority, generated-projection, or curated-round-trip mode
- Claims should preserve provenance, source authority, epistemic status, and review state
- Decisions should be first-class Project Memory objects
- Decision Reviews should compare expected and observed outcomes
- Assumptions should remain visible and linked
- Evidence should be traceable to source artifacts
- constitutional documents should remain human-readable governance surfaces

Markdown is important. Project Memory is fundamental.

## Review Discipline

Review should prioritize:

- boundary correctness
- terminology consistency
- evidence quality
- authority clarity
- implementation readiness
- reversibility
- alignment with constitutional documents

Review should not continuously polish stable documents merely for style. Constitutional and canonical documents should evolve because understanding changed, not because phrasing could be improved.

## Current Governance Work

The repository now has a Project Memory object model, evidence and decision objects, candidate review and promotion semantics, and reviewed repo-local memory inputs.

The next governance work should be driven by observed agent-context behavior. Immediate needs are fail-closed context selection, explicit relevance and traversal explanations, source freshness, and reviewed Markdown-to-memory candidate ingestion. Durable record formats and persistence remain deferred until these access and mutation patterns are proven.
