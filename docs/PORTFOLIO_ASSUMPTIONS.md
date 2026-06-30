# Portfolio Assumptions

## Status

This document records the Workspace's current assumptions about neighbouring portfolio products.

These are assumptions, not final facts. The neighbouring products evolve independently. The Workspace should depend on stable contracts rather than implementation details.

Source posture: based on `docs/VISION.md`, `docs/CORE_CONCEPTS.md`, and `/Users/eduardodosremedios/Eduardo_Product_Stack`.

## Factory V2

### Current Assumption

Factory V2 is the current stable planning-first process substrate and fallback discipline for AI-assisted software delivery across the portfolio.

### Expected Responsibilities

- planning-first delivery process
- stage contracts
- Product Owner lane
- templates and validators
- execution-mode controls
- human Go/No-go checkpoints
- verification design before implementation
- stage lint, pack lint, knowledge lint, context recall, and merge handoff discipline
- Mission Mode as an additive multi-sprint wrapper

### Expected Integration

The Workspace may use Factory V2 to structure plans, readiness reviews, implementation briefs, verification plans, and migration paths.

Factory V2 concepts may appear in Project Memory as source material, but Factory V2 remains the owner of its process doctrine and artifact schemas.

### Assumptions The Workspace Relies Upon

- Factory V2 remains the default fallback while Factory V3 matures.
- Factory V2 templates can be referenced without embedding Factory V2 as Workspace logic.
- Factory V2 artifacts can be linked from Project Memory.

### Uncertainties

- Which Factory V2 artifacts should become first-class Project Memory objects.
- Which V2 helpers should be required versus optional in Workspace-generated planning.
- How project-specific Factory V2 usage should be detected, normalized, or migrated.

### Questions For Portfolio Brain

- What Factory V2 artifacts should the Workspace support first?
- What evidence would justify migration from V2 to V3 for a specific project?
- Should the Workspace expose Factory V2 terminology directly or translate it into Workspace-native concepts?

## Factory V3

### Current Assumption

Factory V3 is the supervised mission-governance engine for AI workers.

It is not the Workspace, not Temper, not Harmony, and not Aegis. It governs how AI work is formed, authorized, executed, interrupted, verified, closed out, and replayed.

### Expected Responsibilities

- mission envelopes
- mission records
- checkpoints
- human decision interrupts
- halt, recovery, fallback, and safe-hold rules
- mission telemetry and replay
- operational profiles
- advisory validators for mission readiness, records, telemetry replay, and loop contracts
- promotion criteria for broader autonomous work
- evidence ladders for mission class approval

### Expected Integration

The Workspace drafts, validates, launches, pauses, resumes, monitors, and reviews missions through Factory V3.

Factory V3 owns mission validity, executable mission contracts, mission state, checkpoint semantics, replay, evidence, and promotion state.

### Assumptions The Workspace Relies Upon

- Factory V3 will expose stable mission references.
- Factory V3 will validate draft mission envelopes before execution.
- Factory V3 can expose mission state, checkpoints, human interrupts, telemetry, records, replay, and evidence.
- Factory V3 will preserve explicit approval status for operational profiles.
- The Workspace must respect the current narrow approval posture: optional bounded code-change missions only, with broader long-running work gated.

### Uncertainties

- The final mission envelope contract.
- The exact boundary between Workspace readiness assessment and Factory V3 mission admission.
- Whether all mission-governed execution flows pass through Factory V3 before Temper, or whether some Temper work is initiated directly.
- How V3 mission evidence maps into Project Memory and Aegis-grade proof.

### Questions For Portfolio Brain

- What is the canonical mission reference and mission envelope contract?
- What are the minimum fields the Workspace must provide for mission validation?
- Which Factory V3 states must be visible in the Workspace?
- How should V3 operational-profile approval be represented so the Workspace cannot imply broader promotion than exists?

## Temper

### Current Assumption

Temper is the governed agent-team orchestration product and likely commercial beachhead for operational AI teams.

### Expected Responsibilities

- agent-team orchestration
- Agent Pack runtime
- capability mesh
- work ledger
- governed action ingress
- policy-owned action routing
- evidence export
- pack installation, activation, and composition
- adapter trust tiers and execution contracts
- operational packaging for business workflows

### Expected Integration

The Workspace helps users discover, configure, initiate, monitor, approve, deny, and review Temper work.

Temper remains the runtime for operational agent teams and packs.

### Assumptions The Workspace Relies Upon

- Temper can expose available agent packs and capabilities.
- Temper can accept bounded goals or work items connected to Workspace Project Memory.
- Temper can expose work-ledger state in a human-reviewable form.
- Temper can export evidence that the Workspace can link into Project Memory.
- Temper's core boundary remains: cognition may propose work, but runtime policy authorizes consequential action.

### Uncertainties

- The exact relationship between Factory V3 missions and Temper goal runs.
- Whether Temper work initiated by the Workspace must always be mission-governed.
- How approvals, denials, and escalations should flow among Workspace, Temper, Factory V3, and Aegis.
- Which Agent Pack configuration details should be exposed in the Workspace.

### Questions For Portfolio Brain

- What is the canonical Temper work or goal reference?
- What is the intended contract between V3 mission envelopes and Temper goal runs?
- What evidence export shape should the Workspace expect?
- Which Temper approvals require Aegis authority references?

## Aegis

### Current Assumption

Aegis is the constitutional authority and proof substrate for consequential autonomous systems.

### Expected Responsibilities

- constitutional autonomy kernel
- authority leasing
- mediation decisions
- receipts
- evidence packets
- proof bundles
- offline verification
- temporal and finality semantics
- fail-closed policy and invariant enforcement
- tool-use mediation
- trust, verification, simulation, and evidence primitives

### Expected Integration

The Workspace requests and displays Aegis-backed authority, receipts, proof bundles, and evidence packets.

The Workspace may reason over Aegis outputs, but it must not create authority, leases, receipts, or proof by itself.

### Assumptions The Workspace Relies Upon

- Aegis can provide authority references that the Workspace can store in Project Memory.
- Aegis can verify receipts and proof bundles.
- Aegis can represent denial, expiry, revocation, and fail-closed states.
- Aegis can provide evidence packets linked to decisions, missions, approvals, and consequential actions.
- Aegis remains the upgrade path when local evidence needs stronger proof.

### Uncertainties

- The minimum Aegis contract the Workspace must integrate with first.
- The boundary between Workspace Evidence Artifacts and Aegis evidence packets.
- Which Workspace actions require Aegis mediation.
- How Aegis constitutional governance should be surfaced without turning the Workspace into the proof kernel.

### Questions For Portfolio Brain

- What is the canonical authority lease or authority reference format?
- What fail-closed Aegis states must block Workspace actions?
- How should the Workspace distinguish local evidence, product receipts, mission evidence, and Aegis proof?
- What proof-bundle verification flow should be supported first?

## Sentinel

### Current Assumption

Sentinel is the passive boundary discovery and governance-readiness subsystem within the Aegis orbit.

It is currently best treated as architecturally important research/pre-implementation design rather than a broadly available runtime service.

### Expected Responsibilities

- passive boundary discovery
- effect-boundary detection and classification
- topology and consequence mapping
- bypass and orphan metrics
- governance-readiness reports
- first-boundary recommendations
- data-minimized, no-write, removable observation

### Expected Integration

The Workspace consumes Sentinel findings during discovery, Project Memory creation, readiness assessment, and mission planning.

Sentinel should discover and classify boundaries. The Workspace should use those findings to help humans understand risk, readiness, constraints, and delegation boundaries.

### Assumptions The Workspace Relies Upon

- Sentinel can eventually return topology maps, boundary reports, readiness blockers, and first-boundary recommendations.
- Sentinel findings can become Project Memory evidence, constraints, questions, hypotheses, or recommendations.
- Sentinel observation is no-write and removable by default.
- Sentinel recommendations are not the same as Aegis enforcement.

### Uncertainties

- The stable Sentinel report contract.
- The confidence model for candidate, probable, and confirmed boundaries.
- How Sentinel readiness findings should gate Factory V3 mission launch.
- How often Sentinel observations should be refreshed.

### Questions For Portfolio Brain

- What is the canonical Sentinel boundary report shape?
- What does "first-boundary recommendation" mean operationally?
- Which Sentinel findings should block mission readiness?
- How should conflicts between Sentinel findings and human assumptions be resolved?

## Harmony

### Current Assumption

Harmony is the governed conversational runtime for regulated user/operator interactions.

It is not the general Workspace chat layer.

### Expected Responsibilities

- conversational ingress and intent normalization
- deterministic policy-pack evaluation
- confirmation and disclosure lifecycles
- typed response blocks
- channel and surface contracts
- adapter dispatch under fail-closed rules
- runtime-authored evidence and receipts
- operator-specific integration surfaces
- regulated interaction workflows

### Expected Integration

The Workspace owns general project conversation and voice. Harmony owns regulated conversation, regulated workflow voice, policy-pack execution, confirmations, disclosures, typed blocks, receipts, and channel contracts.

When Workspace conversation becomes a regulated workflow, the Workspace should route or hand off to Harmony.

### Assumptions The Workspace Relies Upon

- Harmony can evaluate policy packs for regulated conversation contexts.
- Harmony can accept handoff context from the Workspace.
- Harmony can return conversation evidence or references where appropriate.
- Harmony can distinguish policy-governed workflows from general project dialogue.
- Harmony evidence remains subject to regulatory, privacy, and operator constraints.

### Uncertainties

- The exact handoff trigger from Workspace conversation to Harmony.
- The minimum handoff context Harmony requires.
- How Harmony conversation evidence should be represented in Project Memory.
- Which Harmony policy decisions are advisory versus blocking.

### Questions For Portfolio Brain

- What triggers mandatory handoff to Harmony?
- What is the canonical regulated-conversation handoff contract?
- What Harmony policy states must the Workspace surface?
- What conversation evidence can be stored or referenced in Project Memory?

## Cross-Portfolio Assumptions

The Workspace currently assumes:

- shared contracts matter more than shared internal code
- neighbouring systems should expose stable references rather than requiring the Workspace to mirror implementation state
- Project Memory can store references to missions, work items, evidence, authority, receipts, proof, topology, and regulated conversations
- evidence levels need to be explicit across the portfolio
- provider/model invocation needs a shared contract even if each product has local adapters
- human approval needs a consistent representation across Workspace, Factory V3, Temper, Aegis, and Harmony
- the Workspace should be the portfolio/project improvement view, while source systems own native telemetry

## Cross-Portfolio Uncertainties

The largest unresolved uncertainties are:

- the canonical cross-portfolio identity model
- the governed work event schema
- evidence levels and escalation rules
- the relationship between local evidence, mission evidence, product receipts, and Aegis proof
- whether Workspace-to-Temper work is always mediated by Factory V3
- which integrations must exist before the Workspace can launch its first governed mission

