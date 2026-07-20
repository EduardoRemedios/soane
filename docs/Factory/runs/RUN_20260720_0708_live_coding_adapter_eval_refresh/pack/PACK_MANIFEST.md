# Pack Manifest

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage J manifest in the upstream planning run.
- v2 (2026-07-20): Consolidated refreshed run before Stage I2.

## Run Metadata

- RUN_ID: RUN_20260720_0708_live_coding_adapter_eval_refresh
- Sprint ID: LCAE-V0-001
- Created: 2026-07-20 07:08 local
- Owner: Soane project owner
- Execution Mode: PLANNING_ONLY
- Spec Versions: STAGE_CONTRACTS v4.14, PURPLE_GATE_CHECKLIST v3.3
- Upstream Pack: RUN_20260705_0923_live_coding_adapter_eval_plan

## Required Run Root Files

- raw_brief.md: present and non-empty
- KNOWLEDGE_LINT.txt: present and PASS
- CONTEXT_RECALL_REPORT.md: present and repaired
- EXECUTION_MODE.txt: present and PLANNING_ONLY
- SPRINT_ID.txt: present and matches manifest
- RETRO.md: present and non-empty

## Required Pack Files

- intent.md: present and non-empty
- intent_redteam.md: present and non-empty
- intent_synthesis.md: present and non-empty
- intent_lock_report.md: present and PASS
- premortem.md: present and non-empty
- risk_register.md: present and non-empty
- verification_plan.md: present and non-empty
- traceability_matrix.md: present and non-empty
- micro_sprints.md: present and non-empty
- LCAE-V0-001_ENVELOPE.md: present and non-empty
- LCAE-V0-001_ENVELOPE_REDTEAM.md: present and PASS
- external_source_review.md: present and non-empty
- fixtures/: present with two non-empty contract files
- PACK_CHECKLIST.md: present and non-empty
- PACK_MANIFEST.md: present and non-empty
- PACK_AUDIT_REPORT.md: present, non-empty, and PASS

## Handoffs

- HANDOFF_STAGE_A.md: present
- HANDOFF_STAGE_B.md: present
- HANDOFF_STAGE_C.md: present
- HANDOFF_STAGE_D.md: present
- HANDOFF_STAGE_E.md: present
- HANDOFF_STAGE_F.md: present
- HANDOFF_STAGE_G.md: present
- HANDOFF_STAGE_H.md: present
- HANDOFF_STAGE_I.md: present
- HANDOFF_STAGE_J.md: present
- HANDOFF_STAGE_I2.md: present

## Verification Manifest

- verification_manifest.yaml present: no
- Reason: this is a planning-only pack; runnable checks are specified in `verification_plan.md`.
