# Integration Architecture

## Status

This document describes how the Workspace expects to integrate with the wider portfolio.

It does not design final APIs. It defines conceptual interfaces, architectural contracts, and ownership boundaries from the Workspace's perspective.

Source posture: based on `docs/VISION.md`, `docs/CORE_CONCEPTS.md`, and `/Users/eduardodosremedios/Eduardo_Product_Stack/docs/portfolio/portfolio-architecture-briefing-new-ai-workspace.md`.

## Integration Principles

The Workspace should integrate by contract, not by absorbing neighbouring responsibilities.

Integration should preserve these rules:

- Project Memory stores Workspace understanding and references to external records
- neighbouring products remain authoritative for their own responsibilities
- stable references are preferred over copied implementation state
- evidence, proof, receipt, authority, approval, mission, work item, and capability remain distinct
- human-facing workflows expose ownership and state clearly
- authority, proof, policy, and boundary failures should fail closed
- provider/model invocation should carry policy, privacy, confidence, cost, latency, and evidence metadata

## Shared Cross-Portfolio Contracts

The following contracts are expected to be needed before durable implementation.

### Project Identity

Identifies a Workspace Project across portfolio interactions.

Expected responsibilities:

- stable project identifier
- human-readable project name
- Project Memory reference
- owning organisation or workspace
- policy context
- related repositories, documents, systems, and external surfaces

The Workspace owns Project Identity. Other products may store references to it.

### Work Item Contract

Represents a bounded unit of work that may be planned, routed, executed, governed, or reviewed.

Expected responsibilities:

- work item identifier
- related Project Identity
- objective
- scope
- owner or responsible system
- status
- constraints
- evidence requirements
- related mission, goal run, approval, or authority reference

The owner depends on the layer. Factory V3 owns mission work. Temper owns agent-team work. The Workspace owns planning and Project Memory views.

### Mission Reference

Identifies a Factory V3-governed Mission.

Expected responsibilities:

- mission identifier
- related Project Identity
- mission envelope reference
- mission status
- checkpoint references
- human interrupt references
- evidence references
- mission record and replay references
- operational profile approval state

Factory V3 owns Mission Reference semantics. The Workspace stores and presents them.

### Governed Work Event

Records an important event in governed AI work.

Expected responsibilities:

- event identifier
- event type
- producing system
- timestamp
- actor or system
- affected Project, Mission, work item, conversation, or authority reference
- evidence references
- policy or authority context where applicable

This contract should allow the Workspace to build cross-project improvement views without taking ownership of source-system telemetry.

### Human Approval

Records a human approval, denial, or decision interrupt response.

Expected responsibilities:

- approving human or responsible authority
- action being approved or denied
- scope
- conditions
- evidence reviewed
- decision timestamp
- related authority reference where required
- related Mission, work item, Decision, or policy request

The Workspace may collect human intent. The governed interpretation belongs to the relevant owner: Aegis, Factory V3, Temper, or Harmony.

### Evidence Artifact

Represents information used to support or challenge a claim, assumption, hypothesis, decision, verification, mission result, or governance action.

Expected responsibilities:

- evidence identifier
- evidence level
- evidence type
- provenance
- producing system
- creation time
- freshness
- integrity or verification metadata where available
- related Project Memory objects

The producing system owns the artifact. The Workspace indexes, links, and presents it.

### Policy Decision

Represents an evaluated policy outcome.

Expected responsibilities:

- policy decision identifier
- policy or policy pack reference
- input context reference
- decision result
- reason code
- blocking or advisory status
- evidence references
- expiry or reevaluation condition

Harmony owns regulated conversation policy decisions. Temper owns agent-team runtime policy decisions. Aegis owns high-assurance authority/proof decisions.

### Receipt And Proof Reference

Identifies a receipt, evidence packet, proof bundle, or verification result.

Expected responsibilities:

- reference identifier
- issuing system
- type
- related action or event
- verification method
- validity state
- expiry, revocation, or fail-closed state
- related Project, Mission, Decision, or Evidence Artifact

Aegis owns high-assurance receipt and proof semantics. Other products may emit local receipts or evidence exports.

### Provider Invocation

Represents the invocation of a model, tool, agent, provider, or execution system.

Expected responsibilities:

- provider or system invoked
- task purpose
- Inference Strategy or execution strategy reference where applicable
- policy context
- privacy classification
- input references
- output references
- cost, latency, and confidence metadata where available
- evidence or trace references where required

Each product may have local adapters. The contract should preserve cross-portfolio governance and evidence continuity.

### Canonical Knowledge Artifact

Represents a durable generated or curated view over Project Memory.

Expected responsibilities:

- artifact identifier
- source Project Memory references
- generation or curation method
- version
- review status
- related decisions, assumptions, hypotheses, constraints, and evidence

The Workspace owns canonical knowledge artifacts derived from Project Memory.

## Workspace To Factory V3

Factory V3 governs supervised missions.

The Workspace should integrate with Factory V3 for mission formation, validation, lifecycle visibility, checkpoint review, replay, and mission evidence.

### Conceptual Interfaces

#### Create Mission

Equivalent conceptual shape: `createMission(envelopeDraft)`.

The Workspace assembles a candidate mission envelope from Project Memory.

Expected inputs:

- Project Identity
- objective
- scope
- constraints
- relevant Project Memory references
- assumptions and unresolved questions
- verification requirements
- budget or time limits
- approval and authority context
- operational profile target

Expected output:

- draft or created Mission Reference
- validation readiness state

#### Validate Mission

Equivalent conceptual shape: `validateMission(envelope)`.

Factory V3 evaluates whether a mission is valid and admissible.

Expected output:

- validation result
- missing fields
- blocked conditions
- required human decisions
- required authority
- required evidence
- operational profile limitations

#### Start Mission

Equivalent conceptual shape: `startMission(missionId)`.

The Workspace requests launch after readiness and authority conditions are satisfied.

Expected output:

- Mission Reference
- initial state
- checkpoint plan
- telemetry availability

#### Pause Mission

Equivalent conceptual shape: `pauseMission(missionId, reason)`.

Expected output:

- updated mission status
- pause reason
- safe-hold or checkpoint reference

#### Resume Mission

Equivalent conceptual shape: `resumeMission(missionId)`.

Expected output:

- updated mission status
- re-entry state
- active checkpoint or next action

#### Record Or Inspect Checkpoint

Equivalent conceptual shape: `recordCheckpoint(missionId, decision)`.

The Workspace should support human review of checkpoints and decision interrupts.

Expected output:

- checkpoint reference
- decision state
- evidence available
- required human response
- risks or blockers

#### Get Mission Record

Equivalent conceptual shape: `getMissionRecord(missionId)`.

Expected output:

- lifecycle events
- checkpoint outcomes
- decision interrupts
- halt, recovery, fallback, and safe-hold events
- closeout state

#### Replay Mission

Equivalent conceptual shape: `replayMission(missionId)`.

Expected output:

- replay reference
- replayable event sequence
- evidence references
- limitations

#### Get Mission Evidence

Equivalent conceptual shape: `getMissionEvidence(missionId)`.

Expected output:

- Evidence Artifacts
- evidence metadata
- relation to objective, checkpoints, and completion criteria

### Boundary

The Workspace drafts, monitors, and reviews missions.

Factory V3 validates and governs executable missions.

## Workspace To Temper

Temper executes governed agent-team work.

The Workspace should integrate with Temper for pack discovery, team activation, goal submission, work-ledger visibility, approval handling, and evidence export.

### Conceptual Interfaces

#### List Agent Packs

Equivalent conceptual shape: `listAgentPacks()`.

Expected output:

- pack identifiers
- capabilities
- domain profiles
- policy requirements
- activation constraints

#### Install Pack

Equivalent conceptual shape: `installPack(projectId, packId)`.

Expected output:

- installed pack reference
- compatibility state
- unresolved policy or configuration requirements

#### Activate Team

Equivalent conceptual shape: `activateTeam(projectId, teamSpec)`.

Expected output:

- team reference
- selected capabilities
- policy constraints
- unresolved configuration questions

#### Submit Goal

Equivalent conceptual shape: `submitGoal(teamId, goal)`.

Expected inputs:

- Project Identity
- goal statement
- relevant Project Memory references
- constraints
- authority references where required
- success criteria

Expected output:

- goal run or work reference
- initial work-ledger entry
- status

#### Get Work Ledger

Equivalent conceptual shape: `getWorkLedger(teamId)`.

Expected output:

- work items
- owners or agents
- status
- dependencies
- decisions requested
- evidence generated

#### Approve Action

Equivalent conceptual shape: `approveAction(actionRequestId)`.

Expected output:

- approval reference
- updated work state
- related authority or receipt reference where applicable

#### Deny Action

Equivalent conceptual shape: `denyAction(actionRequestId)`.

Expected output:

- denial reference
- updated work state
- rationale or retry conditions

#### Export Evidence

Equivalent conceptual shape: `exportEvidence(goalRunId)`.

Expected output:

- Evidence Artifacts
- work-ledger references
- provenance
- integrity metadata where available

### Boundary

The Workspace coordinates and supervises.

Temper owns operational agent teams, packs, work ledger, and governed execution.

## Workspace To Aegis

Aegis owns authority, receipts, proof bundles, evidence packets, temporal/finality semantics, and fail-closed mediation.

The Workspace should integrate with Aegis when actions require high-assurance authority or proof.

### Conceptual Interfaces

#### Request Authority Lease

Equivalent conceptual shape: `requestAuthorityLease(actionContext)`.

Expected output:

- Authority Reference
- approval, denial, or conditional state
- scope
- expiry or revocation conditions
- required evidence or proof

#### Mediate Action

Equivalent conceptual shape: `mediateAction(actionRequest)`.

Expected output:

- mediation decision
- allowed, denied, conditional, or fail-closed state
- receipt or evidence reference
- reason code

#### Verify Receipt

Equivalent conceptual shape: `verifyReceipt(receipt)`.

Expected output:

- verified, invalid, expired, revoked, or unknown state
- related event metadata
- trust implications

#### Verify Evidence Packet

Equivalent conceptual shape: `verifyEvidencePacket(packet)`.

Expected output:

- validation result
- failed checks
- missing evidence
- authority implications

#### Get Proof Bundle

Equivalent conceptual shape: `getProofBundle(correlationId)`.

Expected output:

- proof bundle reference
- verification method
- included evidence packets
- limitations

#### Record Finality

Equivalent conceptual shape: `recordFinality(event)`.

Expected output:

- finality reference
- receipt or proof reference
- temporal state

### Boundary

The Workspace requests, displays, and reasons over authority and proof.

Aegis owns authority, leases, receipts, proof, and fail-closed mediation.

## Workspace To Sentinel

Sentinel discovers boundaries and governance readiness.

The Workspace should integrate with Sentinel during discovery, readiness assessment, and mission planning.

### Conceptual Interfaces

#### Start Observation

Equivalent conceptual shape: `startObservation(scope, mode)`.

Expected input:

- Project Identity
- target references
- observation scope
- mode
- known assumptions
- data-minimization constraints

Expected output:

- observation reference
- accepted scope
- expected findings

#### Get Boundary Report

Equivalent conceptual shape: `getBoundaryReport(observationId)`.

Expected output:

- boundary report reference
- candidate, probable, or confirmed boundaries
- affected systems
- risk notes
- confidence levels
- evidence references

#### Get Topology Map

Equivalent conceptual shape: `getTopologyMap(observationId)`.

Expected output:

- components
- dependencies
- topology
- consequence paths
- confidence levels

#### Get Bypass Metrics

Equivalent conceptual shape: `getBypassMetrics(observationId)`.

Expected output:

- bypass paths
- orphan effects
- gap indicators
- supporting evidence

#### Get Governance Readiness

Equivalent conceptual shape: `getGovernanceReadiness(boundaryId)`.

Expected output:

- readiness state
- blockers
- missing evidence
- governance gaps
- recommended next discovery steps

#### Recommend First Boundary

Equivalent conceptual shape: `recommendFirstBoundary(observationId)`.

Expected output:

- first-boundary recommendation
- rationale
- affected systems
- confidence
- related evidence

### Boundary

The Workspace consumes and presents Sentinel findings.

Sentinel owns passive discovery and boundary reporting. Sentinel does not enforce by default.

## Workspace To Harmony

Harmony owns regulated conversational runtime and channel-mediated workflow execution.

The Workspace should integrate with Harmony when general project conversation crosses into regulated workflow.

### Conceptual Interfaces

#### Start Conversation

Equivalent conceptual shape: `startConversation(sessionContext)`.

Expected output:

- Harmony session reference
- accepted scope
- policy context
- evidence expectations

#### Evaluate Policy Pack

Equivalent conceptual shape: `evaluatePolicyPack(messageContext)`.

Expected output:

- policy decision
- reason code
- blocking or advisory state
- required confirmation
- required evidence
- allowed or disallowed actions

#### Render Typed Block

Equivalent conceptual shape: `renderTypedBlock(block)`.

Expected output:

- rendered response block
- supported surface metadata
- policy and evidence references

#### Request Confirmation

Equivalent conceptual shape: `requestConfirmation(confirmationContext)`.

Expected output:

- confirmation reference
- status
- evidence reference
- policy context

#### Dispatch Channel Action

Equivalent conceptual shape: `dispatchChannelAction(action)`.

Expected output:

- dispatch result
- adapter state
- receipt or evidence reference
- fail-closed state where applicable

#### Get Conversation Evidence

Equivalent conceptual shape: `getConversationEvidence(sessionId)`.

Expected output:

- conversation evidence reference
- transcript or structured evidence where permitted
- policy metadata
- privacy constraints

#### Handoff To Operator

Equivalent conceptual shape: `handoffToOperator(sessionId)`.

Expected output:

- operator handoff reference
- status
- reason
- evidence reference

### Boundary

The Workspace owns general project conversation and voice.

Harmony owns regulated conversation, policy-pack workflows, confirmations, typed blocks, channel runtime, receipts, and regulated workflow evidence.

## Integration State In Project Memory

Project Memory should store:

- external references
- human-readable summaries of external state
- mission, work, authority, receipt, proof, topology, and conversation references
- evidence links
- local Workspace decisions
- assumptions and uncertainties about integrations
- cross-project improvement signals

Project Memory should not become a full mirror of neighbouring products.

## Failure And Blocking States

The Workspace should treat these states as blocking unless governed authority explicitly permits continuation:

- missing authority for an action that requires authority
- failed proof verification
- invalid, expired, or revoked receipt
- mission validation failure
- operational profile not approved for the requested mission class
- unresolved human decision interrupt
- denied or blocked Temper action
- Sentinel boundary finding that affects mission safety
- Harmony policy evaluation that blocks regulated conversation
- stale or missing evidence for a critical decision

Blocking states should be visible to humans and recorded in Project Memory.

## Open Architectural Questions

The Workspace should clarify these questions before committing to final implementation contracts:

- What is the canonical cross-portfolio identity model?
- What is the governed work event schema?
- What evidence levels should be used across local logs, product receipts, mission evidence, and Aegis proof?
- How should human approvals flow between Workspace, Aegis, Factory V3, Temper, and Harmony?
- Does the Workspace call Factory V3, Temper, Aegis, Sentinel, and Harmony directly, or are some flows mediated?
- Which integration contracts must exist before the Workspace can launch its first governed mission?
- What are the minimum fail-closed states the Workspace must enforce in v1?

