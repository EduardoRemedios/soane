# Thinking Engine Architecture

## Status

This document defines the conceptual architecture for the Workspace Thinking Engine.

It is a canonical Soane architecture document. It is not an implementation plan, prompt specification, agent taxonomy, UI specification, API design, or model-routing configuration.

It consumes:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`

## Purpose

The Thinking Engine helps humans reduce uncertainty before planning, deciding, or delegating work.

It exists so the Workspace can help a Project answer:

- what are we trying to understand?
- what context is missing?
- what assumptions are being made?
- what hypotheses are worth testing?
- what evidence exists?
- what evidence is weak, stale, conflicting, or absent?
- what trade-offs matter?
- what decisions are ready?
- what work is not ready to delegate?

The Thinking Engine is not a replacement for human judgement.

It is a structured reasoning aid that makes uncertainty visible, challenges assumptions, guides discovery, assembles context, and writes durable learning back into Project Memory.

## Responsibilities

The Thinking Engine is responsible for:

- project intake and starting-context assessment
- discovery guidance
- selection and adaptation of Discovery Playbooks
- Socratic questioning
- hypothesis formation and testing paths
- assumption surfacing
- evidence gap identification
- option and trade-off comparison
- synthesis of candidate understanding
- readiness assessment before planning or delegation
- generation of proposed Decisions, Questions, Assumptions, Hypotheses, Constraints, Evidence links, and Mission Plan inputs
- writing reviewed thinking outputs into Project Memory

The Thinking Engine should improve decision quality before work moves into planning, execution, mission governance, coding agents, or external systems.

## Non-Goals

The Thinking Engine does not:

- own Project Memory
- replace Project Memory with chat history
- own Factory V2 process doctrine
- own Factory V3 mission governance
- own Temper agent-team runtime
- own Aegis authority, proof, receipts, or trust semantics
- own Harmony regulated conversation runtime
- own final model behavior
- own live Cursor, Codex, OpenAI, or other provider integrations
- decide that work may proceed without human or policy authority
- make generated synthesis authoritative by default
- define the final product shell
- choose a database or storage engine

## Architectural Principle

Thinking precedes planning.

Planning precedes delegation.

Delegation requires readiness, authority, constraints, context, capability, and verification expectations.

The Thinking Engine should never turn uncertainty into apparent certainty merely because a model produced a confident answer.

## Relationship To Project Memory

Project Memory is the substrate.

The Thinking Engine reads from Project Memory, external context sources, canonical documents, conversations, evidence, and source systems.

It writes back structured outputs such as:

- Questions
- Assumptions
- Hypotheses
- Constraints
- Research Findings
- Evidence Artifacts
- proposed Decisions
- readiness assessments
- Discovery Playbook outputs
- synthesis notes
- operational learning

Generated Markdown remains a projection. It may present Thinking Engine outputs, but it is not governed Project understanding unless the underlying Project Memory objects exist and have the required review state.

## Core Flow

The Thinking Engine follows a staged reasoning loop.

1. Intake
2. Context baseline
3. Discovery
4. Questioning
5. Hypothesis formation
6. Evidence and contradiction review
7. Synthesis
8. Readiness assessment
9. Decision or planning recommendation
10. Project Memory update

The loop may repeat. A Project may return from readiness assessment back to discovery when evidence is weak, context is missing, or assumptions are too consequential.

## Project Intake

Project intake establishes the starting point for a Project or work area.

The goal is not to gather every possible artifact. The goal is to know whether Soane has enough context to reason responsibly.

Intake should identify:

- project type
- project boundary
- human goal
- current state
- known stakeholders
- source systems
- canonical documents
- existing repositories or workspaces
- external artifacts
- known constraints
- known risks
- missing context
- authority expectations
- readiness for discovery, planning, or delegation

## Greenfield Intake

Greenfield projects start with limited existing structure.

The Thinking Engine should help create the initial context baseline before feature work or execution begins.

Greenfield intake should establish:

- project purpose
- initial scope
- non-goals
- assumptions
- constraints
- initial architecture or operating model
- expected evidence sources
- working agreements
- minimum canonical documents
- initial Project Memory objects
- first open Questions
- first candidate Hypotheses
- readiness state

Greenfield does not mean context-free. It means the starting context must be created rather than discovered from an existing system.

## Brownfield Intake

Brownfield projects start with existing reality.

For coding work, that reality may be one repository, multiple repositories, deployed systems, documentation, issue trackers, CI, production behavior, and historical decisions.

For non-coding work, that reality may include analytics dashboards, campaign assets, customer research, CRM data, ad accounts, spreadsheets, design files, briefs, documents, operational systems, and stakeholder knowledge.

Brownfield intake must happen before feature planning or delegated implementation.

Brownfield intake should establish:

- system boundary
- repository map where repositories exist
- non-repository context sources
- ownership map
- integration map
- build and test commands where applicable
- deployment or operational surfaces
- existing architecture documentation
- existing canonical documents
- missing documentation
- current decisions and decision gaps
- current evidence and evidence gaps
- assumptions inherited from the existing system
- constraints imposed by existing behavior
- known risks
- unresolved questions
- readiness state

Brownfield work is not ready merely because code or artifacts exist. Existing systems can contain undocumented assumptions, hidden dependencies, stale decisions, and missing evidence.

## Multi-Repository Systems

The Thinking Engine must not assume a Brownfield system is a monorepo.

Multi-repository intake should identify:

- repositories in scope
- repositories out of scope
- shared libraries or packages
- service boundaries
- deployment relationships
- API or event contracts
- ownership boundaries
- build/test responsibility by repository
- cross-repository documentation
- where decisions are recorded
- where evidence is produced

Before delegated coding work, Soane should know which repository or repositories are relevant and what context must cross repository boundaries.

## Non-Repository Context Sources

The Project is the unit of memory, not the repository.

Many Soane use cases will involve important context outside Git.

Examples include:

- Google Analytics dashboards
- advertising platform reports
- campaign briefs
- creative assets
- spreadsheets
- CRM records
- customer interviews
- research notes
- product analytics
- design files
- operations runbooks
- support tickets
- sales notes
- compliance documents
- screenshots
- data exports

The Thinking Engine should treat these as governed context sources with provenance, freshness, reliability, access constraints, and relevance to the Project.

When a source cannot be ingested directly, Soane should still be able to record a reference, summary, owner, access limitation, and evidence level.

## Context Baseline

A Context Baseline is the minimum agreed starting context for a Project or work area.

It is not permanent truth. It is the current basis for thinking.

A Context Baseline should identify:

- source documents and artifacts
- source repositories or systems
- known goals
- known non-goals
- important decisions
- active assumptions
- open questions
- known constraints
- evidence sources
- missing evidence
- responsible humans or teams
- readiness state

Soane should not delegate work from an empty or ambiguous context baseline unless the delegated work is explicitly a discovery task.

## Discovery Playbooks

A Discovery Playbook is a structured approach for reducing uncertainty within a domain.

The Thinking Engine should select, adapt, or compose Discovery Playbooks according to the Project and task.

Initial Discovery Playbook families should include:

- software engineering
- Brownfield repository and system audit
- Greenfield product definition
- research synthesis
- digital marketing campaign discovery
- operations review
- consulting engagement discovery
- product strategy

Each playbook should define:

- when it applies
- required context sources
- typical questions
- expected evidence
- common risks
- output objects
- readiness criteria
- escalation conditions

Playbooks should not become rigid rituals. They are guides for disciplined thinking.

## Socratic Dialogue

The Thinking Engine should use Socratic dialogue to reveal uncertainty, not to create friction.

Good questioning should:

- clarify goals
- expose hidden assumptions
- identify missing evidence
- test alternatives
- challenge weak causal claims
- separate preference from evidence
- separate capability from authority
- surface trade-offs
- ask what would change the answer

Questioning should be proportional to risk. Low-risk work should not be blocked by excessive interrogation. High-consequence work should not proceed on vague confidence.

## Hypothesis Management

The Thinking Engine should turn uncertainty into explicit Hypotheses when investigation is useful.

A Hypothesis should record:

- proposition
- question addressed
- supporting evidence
- conflicting evidence
- validation method
- expected implications if true
- expected implications if false
- current status

Hypotheses should not silently become Decisions.

Supported Hypotheses may inform Decisions, Mission Plans, or further discovery. Rejected Hypotheses should remain inspectable when they explain why a path was not taken.

## Evidence Review

The Thinking Engine should evaluate evidence for:

- relevance
- provenance
- freshness
- reliability
- completeness
- conflict with other sources
- privacy or access constraints
- producing system
- evidence level

Evidence review should preserve disagreement. Contradictions should remain visible until reviewed and resolved.

## Synthesis

Synthesis combines context, evidence, questions, assumptions, and hypotheses into a coherent current understanding.

Good synthesis should state:

- what is known
- what is likely
- what is assumed
- what is unknown
- what conflicts
- what matters
- what choices exist
- what the consequences are
- what should happen next

Synthesis is not a Decision. It may recommend a Decision, but the Decision must remain explicit.

## Decision Framing

For consequential choices, the Thinking Engine should create a structured Decision Frame before recommending commitment.

A Decision Frame should make visible:

- objective and decision deadline
- alternatives, including the status quo where meaningful
- decision criteria and their relative importance
- causal Claims and Assumptions
- predicted outcomes and confidence
- Evidence supporting and challenging each alternative
- trade-offs, sensitivity, and uncertainty
- dissent, counterarguments, and what would change the recommendation
- reversibility, information value, and review trigger

Decision framing should be proportional to consequence. It should not turn low-risk choices into ceremony, and it should not allow high-consequence choices to proceed without explicit alternatives and uncertainty.

After an important Decision reaches its review trigger, the Thinking Engine should help produce a Decision Review comparing expected and observed outcomes. It should preserve causal uncertainty and feed resulting Operational Learning into future Assumptions, readiness assessments, and Decision Frames.

## Inference Strategy

The Thinking Engine owns Inference Strategy selection for reasoning tasks.

An Inference Strategy may use:

- one model
- multiple models
- local models
- cloud models
- specialist models
- verifier models
- sequential reasoning steps
- Mixture of Agents
- human review

Selection should consider:

- task type
- domain
- privacy
- policy
- available capabilities
- confidence required
- latency
- cost
- evidence requirements
- need for verification

The Workspace owns the strategy. It does not own the models.

Inference Strategy outputs should be recorded as Provider Invocation or reasoning metadata where they materially affect conclusions.

## Readiness Assessment

Readiness is the assessed state of whether a Project, Decision, or Mission has enough understanding, evidence, authority, and constraint clarity to proceed.

The Thinking Engine should make readiness visible before planning or delegation.

Initial readiness dimensions should include:

- goal clarity
- boundary clarity
- context baseline completeness
- evidence sufficiency
- assumption risk
- open question severity
- contradiction status
- constraint clarity
- capability availability
- authority status
- verification path
- rollback or recovery path where applicable

Readiness should be expressed as a structured assessment, not a magical score.

A future readiness score may become useful, but the architecture should not define one before implementation teaches what deserves scoring.

## Readiness States

Initial readiness states should include:

- `not_ready`
- `ready_for_discovery`
- `ready_for_planning`
- `ready_for_decision`
- `ready_for_delegation`
- `blocked`

These states should be explainable. Each state should identify the evidence, assumptions, missing context, or authority condition behind it.

## Outputs

Thinking Engine outputs should be durable Project Memory candidates.

Expected outputs include:

- intake report
- context baseline
- Discovery Playbook result
- Questions
- Assumptions
- Hypotheses
- Constraints
- Evidence references
- synthesis
- Decision Frames
- proposed Decisions
- Decision Review candidates
- readiness assessment
- planning recommendation
- delegation blockers

Outputs should be reviewable before promotion when they materially affect future work.

## Coding Proof Path

Coding remains a useful first proof path because it exposes context, evidence, delegation, verification, and review needs clearly.

For a Greenfield coding project, Soane should help establish the initial project context before creating or modifying code.

For a Brownfield coding project, Soane should first run or request discovery sufficient to understand the existing repository, multi-repository system, documentation, build/test commands, architecture, and risks.

Only after readiness is established should Soane prepare a work package for a coding adapter such as Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, or OpenAI Agents SDK.

The coding agent performs work. Soane governs context, memory, readiness, evidence, and review.

## Non-Coding Proof Paths

The Thinking Engine should be domain-general.

For a digital marketing campaign, the important context may include campaign goals, audience, analytics, channel performance, creative assets, budget constraints, prior experiments, brand rules, and stakeholder approvals.

For operations work, context may include runbooks, incidents, metrics, SLAs, ownership, risk controls, and historical recovery actions.

For research, context may include research questions, source reliability, prior synthesis, competing interpretations, and evidence gaps.

In each case, Soane should identify the context sources, reduce uncertainty, and preserve outputs in Project Memory before delegated work proceeds.

## Human Role

Humans remain responsible for judgement, priorities, approvals, and accepting risk.

The Thinking Engine may recommend, challenge, summarize, compare, or ask. It should not obscure when a human decision or authority is required.

## Failure Modes

The Thinking Engine should be designed against these failure modes:

- treating chat history as durable memory
- treating synthesis as a Decision
- treating confidence as evidence
- treating capability as authority
- treating a repository as the whole Project
- assuming Brownfield systems are monorepos
- ignoring non-repository context sources
- delegating work before context baseline exists
- flattening contradictions into a false summary
- over-questioning low-risk work
- under-questioning high-risk work
- using live adapters before contract semantics are stable
- allowing model output to silently rewrite Project Memory

## Implementation Reconciliation

The first bounded workflow has been implemented without building the full product shell. It includes:

- intake classification
- context baseline assessment
- Discovery Playbook selection
- readiness assessment
- Project Memory write-back

Candidate Review and Promotion, Socratic Discovery, the Coding Proof Harness, its CLI workflow, and Brownfield multi-repository behavior have also been implemented as local deterministic slices.

## Remaining Questions

- How should external non-repository artifacts be referenced before connector integrations exist?
- Which non-coding domain should provide the second end-to-end proof?
- How should agent-context relevance, freshness, and bounded graph expansion affect readiness?

These questions should be resolved through bounded Factory V2 runs before product-shell or persistence commitments.
