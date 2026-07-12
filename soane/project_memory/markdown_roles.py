"""Shared Markdown role and authority-mode vocabulary."""

from __future__ import annotations

from enum import StrEnum
from pathlib import Path


class MarkdownRole(StrEnum):
    CONSTITUTIONAL = "constitutional"
    CANONICAL = "canonical"
    WORKING = "working"
    GENERATED = "generated"
    EVIDENCE = "evidence"
    DEPRECATED = "deprecated"


class MarkdownAuthorityMode(StrEnum):
    AUTHORED_AUTHORITY = "authored_authority"
    GENERATED_PROJECTION = "generated_projection"
    CURATED_ROUND_TRIP = "curated_round_trip"


CONSTITUTIONAL_DOCS = frozenset(
    {
        "docs/VISION.md",
        "docs/CORE_CONCEPTS.md",
        "docs/GOVERNANCE_MODEL.md",
    }
)

CANONICAL_DOCS = frozenset(
    {
        "AGENTS.md",
        "docs/PORTFOLIO_CONTEXT.md",
        "docs/PORTFOLIO_ASSUMPTIONS.md",
        "docs/INTEGRATION_ARCHITECTURE.md",
        "docs/PROJECT_MEMORY_ARCHITECTURE.md",
        "docs/THINKING_ENGINE_ARCHITECTURE.md",
        "docs/PROJECT_STATE.md",
        "docs/ROADMAP.md",
        "docs/CHANGELOG.md",
    }
)

GENERATED_NAME_MARKERS = frozenset(
    {
        "CONTEXT_RECALL_REPORT.md",
        "VALIDATION_CLOSEOUT_REPORT.md",
        "PACK_AUDIT_REPORT.md",
        "PACK_CHECKLIST.md",
        "INTENT_LOCK_REPORT.md",
        "EXECUTION_PROMPT.md",
        "MISSION_CHECKPOINT.md",
        "MISSION_COMPLETION_REPORT.md",
    }
)

EVIDENCE_NAME_MARKERS = frozenset(
    {
        "verification_plan.md",
        "traceability_matrix.md",
        "risk_register.md",
        "premortem.md",
        "external_source_review.md",
    }
)


def markdown_role_for_source(source_path: str, artifact_type: str = "") -> MarkdownRole:
    """Classify repository Markdown without implying document authority."""

    normalized = source_path.strip().lstrip("./")
    name = Path(normalized).name
    lowered_parts = tuple(part.lower() for part in Path(normalized).parts)
    if "deprecated" in lowered_parts or "archive" in lowered_parts or "archives" in lowered_parts:
        return MarkdownRole.DEPRECATED
    if normalized in CONSTITUTIONAL_DOCS:
        return MarkdownRole.CONSTITUTIONAL
    if normalized in CANONICAL_DOCS:
        return MarkdownRole.CANONICAL
    if name in GENERATED_NAME_MARKERS or artifact_type in {
        "factory_run_root_artifact",
        "mission_artifact",
        "po_phase_artifact",
    }:
        return MarkdownRole.GENERATED
    if name in EVIDENCE_NAME_MARKERS:
        return MarkdownRole.EVIDENCE
    if normalized.startswith("docs/Factory/runs/") or normalized.startswith("docs/Factory/templates/"):
        return MarkdownRole.WORKING
    if normalized.startswith("docs/research/"):
        return MarkdownRole.EVIDENCE
    return MarkdownRole.WORKING
