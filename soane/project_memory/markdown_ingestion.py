"""Deterministic Markdown-to-Claim candidate ingestion."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, Mapping, Sequence

from soane.project_memory.contract import (
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Visibility,
    deterministic_fixture_id,
    validate_memory_object,
)
from soane.project_memory.markdown_roles import MarkdownAuthorityMode, MarkdownRole, markdown_role_for_source


SOURCE_SNAPSHOT_VERSION = "markdown-ingestion-v0"
EXTRACTION_METHOD = "deterministic_atx_prose_v0"
OUTPUT_EXCLUSION_LIMIT = 20
_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
_FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
_LIST_RE = re.compile(r"^[ \t]*(?:[-+*]|\d+[.)])[ \t]+")
_TABLE_SEPARATOR_RE = re.compile(r"^[ \t]*\|?[ \t]*:?-{3,}")


class MarkdownIngestionError(ValueError):
    """Raised when a Markdown ingestion request is unsafe or invalid."""


class ExclusionReason(StrEnum):
    CONSTITUTIONAL_AUTHORITY = "constitutional_authority_excluded"
    INELIGIBLE_ROLE = "markdown_role_ineligible"
    OUTSIDE_HEADING = "outside_atx_heading"
    FRONT_MATTER = "front_matter"
    FENCED_CODE = "fenced_code"
    LIST = "list"
    TABLE = "table"
    BLOCKQUOTE = "blockquote"
    HTML = "html"
    INDENTED_CODE = "indented_code"
    STRUCTURED_INTRO = "structured_intro"
    CANDIDATE_BUDGET = "candidate_budget"


class MarkdownChangeState(StrEnum):
    UNCHANGED = "unchanged"
    MODE_CHANGED = "mode_changed"
    MOVED = "moved"
    MODIFIED = "modified"
    DELETED = "deleted"
    ADDED = "added"
    AMBIGUOUS_DUPLICATE = "ambiguous_duplicate"


@dataclass(frozen=True)
class MarkdownIngestionRequest:
    root: Path
    source_path: str
    authority_mode: MarkdownAuthorityMode
    source_authority: str
    candidate_limit: int = 20
    created_by: str = "markdown-ingestion-v0"


@dataclass(frozen=True)
class MarkdownBlock:
    proposition: str
    heading_path: str
    start_line: int
    end_line: int
    anchor_key: str
    occurrence_id: str
    block_fingerprint: str
    candidate_id: str


@dataclass(frozen=True)
class MarkdownExclusion:
    reason: ExclusionReason
    start_line: int
    end_line: int
    excerpt: str


@dataclass(frozen=True)
class MarkdownSourceSnapshot:
    source_path: str
    markdown_role: MarkdownRole
    authority_mode: MarkdownAuthorityMode
    source_authority: str
    document_fingerprint: str
    source_snapshot_version: str
    blocks: tuple[MarkdownBlock, ...]


@dataclass(frozen=True)
class MarkdownIngestionResult:
    snapshot: MarkdownSourceSnapshot
    candidates: tuple[MemoryObject, ...]
    exclusions: tuple[MarkdownExclusion, ...]
    warnings: tuple[str, ...]
    truncated: bool


@dataclass(frozen=True)
class MarkdownComparisonEvent:
    state: MarkdownChangeState
    before_occurrence_ids: tuple[str, ...]
    after_occurrence_ids: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class MarkdownComparison:
    before: MarkdownSourceSnapshot
    after: MarkdownSourceSnapshot
    events: tuple[MarkdownComparisonEvent, ...]


@dataclass(frozen=True)
class _RawBlock:
    proposition: str
    heading_path: str
    start_line: int
    end_line: int


def ingest_markdown(request: MarkdownIngestionRequest) -> MarkdownIngestionResult:
    """Create proposed Claim candidates from one eligible Markdown source."""

    root, path, source_path = _resolve_source(request)
    del root
    raw_bytes = path.read_bytes()
    try:
        text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise MarkdownIngestionError(f"Markdown source is not valid UTF-8: {source_path}") from exc
    normalized_text = text.replace("\r\n", "\n").replace("\r", "\n")
    role = markdown_role_for_source(source_path)
    authority_mode = MarkdownAuthorityMode(request.authority_mode)
    source_authority = request.source_authority.strip()
    if not source_authority:
        raise MarkdownIngestionError("source_authority is required")
    if request.candidate_limit <= 0:
        raise MarkdownIngestionError("candidate_limit must be positive")

    document_fingerprint = _sha256(normalized_text)
    if role != MarkdownRole.CANONICAL:
        reason = (
            ExclusionReason.CONSTITUTIONAL_AUTHORITY
            if role == MarkdownRole.CONSTITUTIONAL and authority_mode == MarkdownAuthorityMode.AUTHORED_AUTHORITY
            else ExclusionReason.INELIGIBLE_ROLE
        )
        snapshot = MarkdownSourceSnapshot(
            source_path=source_path,
            markdown_role=role,
            authority_mode=authority_mode,
            source_authority=source_authority,
            document_fingerprint=document_fingerprint,
            source_snapshot_version=SOURCE_SNAPSHOT_VERSION,
            blocks=(),
        )
        return MarkdownIngestionResult(
            snapshot=snapshot,
            candidates=(),
            exclusions=(MarkdownExclusion(reason, 1, max(1, len(normalized_text.splitlines())), source_path),),
            warnings=(f"source excluded because Markdown role is {role.value}",),
            truncated=False,
        )

    raw_blocks, exclusions = _parse_markdown(normalized_text)
    blocks = _materialize_blocks(source_path, raw_blocks)
    selected_blocks = blocks[: request.candidate_limit]
    truncated = len(blocks) > request.candidate_limit
    if truncated:
        omitted = blocks[request.candidate_limit :]
        exclusions.append(
            MarkdownExclusion(
                ExclusionReason.CANDIDATE_BUDGET,
                omitted[0].start_line,
                omitted[-1].end_line,
                f"{len(omitted)} eligible block(s) omitted by candidate budget",
            )
        )
    observed_at = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    candidates = tuple(
        _claim_candidate(
            block,
            source_path=source_path,
            document_fingerprint=document_fingerprint,
            role=role,
            authority_mode=authority_mode,
            source_authority=source_authority,
            created_by=request.created_by,
            observed_at=observed_at,
        )
        for block in selected_blocks
    )
    snapshot = MarkdownSourceSnapshot(
        source_path=source_path,
        markdown_role=role,
        authority_mode=authority_mode,
        source_authority=source_authority,
        document_fingerprint=document_fingerprint,
        source_snapshot_version=SOURCE_SNAPSHOT_VERSION,
        blocks=blocks,
    )
    warnings = (f"candidate limit {request.candidate_limit} truncated {len(blocks) - len(selected_blocks)} block(s)",) if truncated else ()
    return MarkdownIngestionResult(snapshot, candidates, tuple(exclusions), warnings, truncated)


def compare_markdown_snapshots(
    before: MarkdownSourceSnapshot,
    after: MarkdownSourceSnapshot,
) -> MarkdownComparison:
    """Compare immutable source snapshots without mutating Project Memory."""

    before_remaining = {block.occurrence_id: block for block in before.blocks}
    after_remaining = {block.occurrence_id: block for block in after.blocks}
    events: list[MarkdownComparisonEvent] = []

    exact_matches = [
        block.occurrence_id
        for block in sorted(before_remaining.values(), key=_block_sort_key)
        if block.occurrence_id in after_remaining
    ]
    for occurrence_id in exact_matches:
        state = (
            MarkdownChangeState.MODE_CHANGED
            if before.authority_mode != after.authority_mode
            else MarkdownChangeState.UNCHANGED
        )
        events.append(
            MarkdownComparisonEvent(
                state,
                (occurrence_id,),
                (occurrence_id,),
                "same occurrence and content; authority mode changed" if state == MarkdownChangeState.MODE_CHANGED else "same occurrence and content",
            )
        )
        del before_remaining[occurrence_id]
        del after_remaining[occurrence_id]

    _match_unique_anchor_modifications(before_remaining, after_remaining, events)
    _match_fingerprint_moves(before_remaining, after_remaining, events)

    for block in sorted(before_remaining.values(), key=_block_sort_key):
        events.append(
            MarkdownComparisonEvent(MarkdownChangeState.DELETED, (block.occurrence_id,), (), "source block no longer exists")
        )
    for block in sorted(after_remaining.values(), key=_block_sort_key):
        events.append(
            MarkdownComparisonEvent(MarkdownChangeState.ADDED, (), (block.occurrence_id,), "new source block")
        )
    return MarkdownComparison(before=before, after=after, events=tuple(events))


def memory_object_payload(memory_object: MemoryObject) -> dict[str, Any]:
    """Return review-compatible JSON for a MemoryObject."""

    return {
        "id": memory_object.id,
        "type": memory_object.type.value,
        "title": memory_object.title,
        "status": memory_object.status.value,
        "visibility": memory_object.visibility.value,
        "provenance": {
            "source_refs": list(memory_object.provenance.source_refs),
            "created_by": memory_object.provenance.created_by,
            "created_at": memory_object.provenance.created_at.isoformat(),
            "evidence_level": memory_object.provenance.evidence_level.value,
            "derivation_refs": list(memory_object.provenance.derivation_refs),
        },
        "relationships": [
            {
                "type": relationship.type.value,
                "target_id": relationship.target_id,
                "evidence_ids": list(relationship.evidence_ids),
            }
            for relationship in memory_object.relationships
        ],
        "updated_at": memory_object.updated_at.isoformat() if memory_object.updated_at else None,
        "supersedes": list(memory_object.supersedes),
        "superseded_by": list(memory_object.superseded_by),
        "authority_ref": memory_object.authority_ref,
        "confidence": memory_object.confidence,
        "metadata": dict(memory_object.metadata),
    }


def ingestion_result_payload(result: MarkdownIngestionResult) -> dict[str, Any]:
    selected_exclusions = result.exclusions[:OUTPUT_EXCLUSION_LIMIT]
    reason_counts: dict[str, int] = {}
    for exclusion in result.exclusions:
        reason_counts[exclusion.reason.value] = reason_counts.get(exclusion.reason.value, 0) + 1
    return {
        "snapshot": snapshot_payload(result.snapshot, block_limit=len(result.candidates)),
        "candidates": [memory_object_payload(candidate) for candidate in result.candidates],
        "exclusions": [
            {
                "reason": exclusion.reason.value,
                "start_line": exclusion.start_line,
                "end_line": exclusion.end_line,
                "excerpt": exclusion.excerpt,
            }
            for exclusion in selected_exclusions
        ],
        "exclusion_count": len(result.exclusions),
        "exclusion_reason_counts": dict(sorted(reason_counts.items())),
        "exclusions_truncated": len(selected_exclusions) < len(result.exclusions),
        "warnings": list(result.warnings),
        "truncated": result.truncated,
    }


def snapshot_payload(snapshot: MarkdownSourceSnapshot, *, block_limit: int | None = None) -> dict[str, Any]:
    selected_blocks = snapshot.blocks if block_limit is None else snapshot.blocks[:block_limit]
    return {
        "source_path": snapshot.source_path,
        "markdown_role": snapshot.markdown_role.value,
        "authority_mode": snapshot.authority_mode.value,
        "source_authority": snapshot.source_authority,
        "document_fingerprint": snapshot.document_fingerprint,
        "source_snapshot_version": snapshot.source_snapshot_version,
        "block_count": len(snapshot.blocks),
        "blocks_included": len(selected_blocks),
        "blocks_truncated": len(selected_blocks) < len(snapshot.blocks),
        "blocks": [
            {
                "proposition": block.proposition,
                "heading_path": block.heading_path,
                "start_line": block.start_line,
                "end_line": block.end_line,
                "anchor_key": block.anchor_key,
                "occurrence_id": block.occurrence_id,
                "block_fingerprint": block.block_fingerprint,
                "candidate_id": block.candidate_id,
            }
            for block in selected_blocks
        ],
    }


def comparison_payload(comparison: MarkdownComparison, *, event_limit: int | None = None) -> dict[str, Any]:
    selected_events = comparison.events if event_limit is None else comparison.events[:event_limit]
    state_counts: dict[str, int] = {}
    for event in comparison.events:
        state_counts[event.state.value] = state_counts.get(event.state.value, 0) + 1
    return {
        "before": snapshot_payload(comparison.before, block_limit=0),
        "after": snapshot_payload(comparison.after, block_limit=0),
        "events": [
            {
                "state": event.state.value,
                "before_occurrence_ids": list(event.before_occurrence_ids),
                "after_occurrence_ids": list(event.after_occurrence_ids),
                "reason": event.reason,
            }
            for event in selected_events
        ],
        "event_count": len(comparison.events),
        "event_state_counts": dict(sorted(state_counts.items())),
        "events_truncated": len(selected_events) < len(comparison.events),
    }


def _resolve_source(request: MarkdownIngestionRequest) -> tuple[Path, Path, str]:
    root = request.root.resolve()
    source = Path(request.source_path)
    if source.is_absolute():
        raise MarkdownIngestionError("source_path must be repository-relative")
    try:
        path = (root / source).resolve(strict=True)
    except FileNotFoundError as exc:
        raise MarkdownIngestionError(f"Markdown source does not exist: {request.source_path}") from exc
    try:
        source_path = path.relative_to(root).as_posix()
    except ValueError as exc:
        raise MarkdownIngestionError("Markdown source escapes repository root") from exc
    if not path.is_file():
        raise MarkdownIngestionError(f"Markdown source is not a file: {request.source_path}")
    if path.suffix.lower() != ".md":
        raise MarkdownIngestionError(f"Markdown source must use .md: {request.source_path}")
    return root, path, source_path


def _parse_markdown(text: str) -> tuple[list[_RawBlock], list[MarkdownExclusion]]:
    lines = text.splitlines()
    blocks: list[_RawBlock] = []
    exclusions: list[MarkdownExclusion] = []
    heading_stack: list[tuple[int, str]] = []
    paragraph_lines: list[str] = []
    paragraph_start = 0
    in_fence = False
    fence_marker = ""
    fence_lines: list[str] = []
    fence_start = 0
    index = 0

    if lines and lines[0].strip() == "---":
        closing = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if closing is not None:
            exclusions.append(MarkdownExclusion(ExclusionReason.FRONT_MATTER, 1, closing + 1, _excerpt("\n".join(lines[: closing + 1]))))
            index = closing + 1

    def flush_paragraph(end_line: int) -> None:
        nonlocal paragraph_lines, paragraph_start
        if not paragraph_lines:
            return
        proposition = "\n".join(paragraph_lines).strip()
        heading_path = " > ".join(title for _, title in heading_stack)
        reason = _structured_reason(paragraph_lines)
        if not heading_path:
            reason = ExclusionReason.OUTSIDE_HEADING
        if reason is not None:
            exclusions.append(MarkdownExclusion(reason, paragraph_start, end_line, _excerpt(proposition)))
        else:
            blocks.append(_RawBlock(proposition, heading_path, paragraph_start, end_line))
        paragraph_lines = []
        paragraph_start = 0

    while index < len(lines):
        line_number = index + 1
        line = lines[index]
        fence_match = _FENCE_RE.match(line)
        if in_fence:
            fence_lines.append(line)
            if fence_match and fence_match.group(1)[0] == fence_marker[0] and len(fence_match.group(1)) >= len(fence_marker):
                exclusions.append(MarkdownExclusion(ExclusionReason.FENCED_CODE, fence_start, line_number, _excerpt("\n".join(fence_lines))))
                in_fence = False
                fence_marker = ""
                fence_lines = []
            index += 1
            continue
        if fence_match:
            flush_paragraph(line_number - 1)
            in_fence = True
            fence_marker = fence_match.group(1)
            fence_start = line_number
            fence_lines = [line]
            index += 1
            continue
        heading_match = _HEADING_RE.match(line)
        if heading_match:
            flush_paragraph(line_number - 1)
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            heading_stack = [(old_level, old_title) for old_level, old_title in heading_stack if old_level < level]
            heading_stack.append((level, title))
            index += 1
            continue
        if not line.strip():
            flush_paragraph(line_number - 1)
            index += 1
            continue
        if not paragraph_lines:
            paragraph_start = line_number
        paragraph_lines.append(line)
        index += 1

    flush_paragraph(len(lines))
    if in_fence:
        exclusions.append(MarkdownExclusion(ExclusionReason.FENCED_CODE, fence_start, len(lines), _excerpt("\n".join(fence_lines))))
    return blocks, exclusions


def _structured_reason(lines: Sequence[str]) -> ExclusionReason | None:
    stripped = [line.lstrip() for line in lines]
    if len(lines) == 1 and lines[0].rstrip().endswith(":"):
        return ExclusionReason.STRUCTURED_INTRO
    if any(_LIST_RE.match(line) for line in lines):
        return ExclusionReason.LIST
    if any(line.startswith(">") for line in stripped):
        return ExclusionReason.BLOCKQUOTE
    if any(line.startswith("    ") or line.startswith("\t") for line in lines):
        return ExclusionReason.INDENTED_CODE
    if any(line.startswith("<") for line in stripped):
        return ExclusionReason.HTML
    if any(_TABLE_SEPARATOR_RE.match(line) or line.count("|") >= 2 for line in lines):
        return ExclusionReason.TABLE
    return None


def _materialize_blocks(source_path: str, raw_blocks: Sequence[_RawBlock]) -> tuple[MarkdownBlock, ...]:
    heading_ordinals: dict[str, int] = {}
    fingerprint_ordinals: dict[str, int] = {}
    blocks: list[MarkdownBlock] = []
    for raw in raw_blocks:
        block_fingerprint = _sha256(raw.proposition)
        heading_ordinals[raw.heading_path] = heading_ordinals.get(raw.heading_path, 0) + 1
        fingerprint_ordinals[block_fingerprint] = fingerprint_ordinals.get(block_fingerprint, 0) + 1
        anchor_key = f"{raw.heading_path}::paragraph-{heading_ordinals[raw.heading_path]:03d}"
        occurrence_id = _short_hash(
            f"{source_path}:{anchor_key}:{block_fingerprint}:{fingerprint_ordinals[block_fingerprint]}"
        )
        candidate_id = deterministic_fixture_id(
            f"markdown:{source_path}:{occurrence_id}",
            MemoryObjectType.CLAIM,
            raw.proposition,
        )
        blocks.append(
            MarkdownBlock(
                proposition=raw.proposition,
                heading_path=raw.heading_path,
                start_line=raw.start_line,
                end_line=raw.end_line,
                anchor_key=anchor_key,
                occurrence_id=occurrence_id,
                block_fingerprint=block_fingerprint,
                candidate_id=candidate_id,
            )
        )
    return tuple(blocks)


def _claim_candidate(
    block: MarkdownBlock,
    *,
    source_path: str,
    document_fingerprint: str,
    role: MarkdownRole,
    authority_mode: MarkdownAuthorityMode,
    source_authority: str,
    created_by: str,
    observed_at: datetime,
) -> MemoryObject:
    candidate = MemoryObject(
        id=block.candidate_id,
        type=MemoryObjectType.CLAIM,
        title=block.proposition,
        status=LifecycleStatus.PROPOSED,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=(source_path, f"{source_path}#L{block.start_line}-L{block.end_line}"),
            created_by=created_by,
            created_at=observed_at,
            evidence_level=EvidenceLevel.E1_SOURCE_REFERENCE,
        ),
        metadata={
            "candidate": True,
            "promotion_required": True,
            "proposition": block.proposition,
            "source_path": source_path,
            "heading_path": block.heading_path,
            "start_line": block.start_line,
            "end_line": block.end_line,
            "anchor_key": block.anchor_key,
            "occurrence_id": block.occurrence_id,
            "block_fingerprint": block.block_fingerprint,
            "document_fingerprint": document_fingerprint,
            "markdown_role": role.value,
            "authority_mode": authority_mode.value,
            "source_authority": source_authority,
            "knowledge_scope": "project",
            "epistemic_status": "asserted",
            "extraction_method": EXTRACTION_METHOD,
            "source_snapshot_version": SOURCE_SNAPSHOT_VERSION,
        },
    )
    validate_memory_object(candidate)
    return candidate


def _match_unique_anchor_modifications(
    before: dict[str, MarkdownBlock],
    after: dict[str, MarkdownBlock],
    events: list[MarkdownComparisonEvent],
) -> None:
    before_by_anchor = _group_blocks(before.values(), "anchor_key")
    after_by_anchor = _group_blocks(after.values(), "anchor_key")
    for anchor in sorted(set(before_by_anchor) & set(after_by_anchor)):
        old_group = before_by_anchor[anchor]
        new_group = after_by_anchor[anchor]
        if len(old_group) != 1 or len(new_group) != 1:
            continue
        old = old_group[0]
        new = new_group[0]
        if old.block_fingerprint == new.block_fingerprint:
            continue
        events.append(
            MarkdownComparisonEvent(
                MarkdownChangeState.MODIFIED,
                (old.occurrence_id,),
                (new.occurrence_id,),
                "same stable anchor with changed content",
            )
        )
        before.pop(old.occurrence_id, None)
        after.pop(new.occurrence_id, None)


def _match_fingerprint_moves(
    before: dict[str, MarkdownBlock],
    after: dict[str, MarkdownBlock],
    events: list[MarkdownComparisonEvent],
) -> None:
    before_by_hash = _group_blocks(before.values(), "block_fingerprint")
    after_by_hash = _group_blocks(after.values(), "block_fingerprint")
    for fingerprint in sorted(set(before_by_hash) & set(after_by_hash)):
        old_group = before_by_hash[fingerprint]
        new_group = after_by_hash[fingerprint]
        if len(old_group) == 1 and len(new_group) == 1:
            old = old_group[0]
            new = new_group[0]
            events.append(
                MarkdownComparisonEvent(
                    MarkdownChangeState.MOVED,
                    (old.occurrence_id,),
                    (new.occurrence_id,),
                    "same block content at a new anchor",
                )
            )
        else:
            events.append(
                MarkdownComparisonEvent(
                    MarkdownChangeState.AMBIGUOUS_DUPLICATE,
                    tuple(block.occurrence_id for block in old_group),
                    tuple(block.occurrence_id for block in new_group),
                    "multiple identical blocks prevent one-to-one lineage",
                )
            )
        for block in old_group:
            before.pop(block.occurrence_id, None)
        for block in new_group:
            after.pop(block.occurrence_id, None)


def _group_blocks(blocks: Sequence[MarkdownBlock] | Any, attribute: str) -> dict[str, list[MarkdownBlock]]:
    grouped: dict[str, list[MarkdownBlock]] = {}
    for block in blocks:
        grouped.setdefault(str(getattr(block, attribute)), []).append(block)
    for group in grouped.values():
        group.sort(key=_block_sort_key)
    return grouped


def _block_sort_key(block: MarkdownBlock) -> tuple[int, int, str]:
    return (block.start_line, block.end_line, block.occurrence_id)


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _short_hash(value: str) -> str:
    return _sha256(value)[:16]


def _excerpt(value: str, limit: int = 160) -> str:
    compact = " ".join(value.split())
    return compact if len(compact) <= limit else compact[: limit - 3] + "..."
