"""Headless CLI for Project Memory v0."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from soane.project_memory.context import (
    ContextRequest,
    ContextSelectionMode,
    build_context_package,
    render_markdown_view,
)
from soane.project_memory.agent_context import (
    agent_context_summary,
    build_agent_context_bundle,
    format_agent_context_markdown,
    markdown_role_for_source,
)
from soane.project_memory.contract import (
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    validate_memory_object,
)
from soane.project_memory.fixtures import GoldenFixture, load_fixtures
from soane.project_memory.review import ReviewDecision, ReviewOutcome, review_candidate
from soane.project_memory.semantics import AccessContext, ProjectMemory


DEFAULT_FIXTURE_DIR = Path("tests/fixtures/project_memory/golden")
DEFAULT_MEMORY_DIR = Path("docs/project_memory/objects")


class CliError(ValueError):
    """Raised for user-facing CLI errors."""


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        result = args.func(args)
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 1
    if isinstance(result, str):
        print(result, end="" if result.endswith("\n") else "\n")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m soane.project_memory.cli")
    parser.set_defaults(json=True)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = _add_memory_source_args(subparsers.add_parser("validate", help="validate Project Memory inputs"))
    validate_parser.set_defaults(func=_cmd_validate)

    fixture_parser = _add_memory_source_args(
        subparsers.add_parser("fixture-test", help="load fixtures into local Project Memory")
    )
    fixture_parser.set_defaults(func=_cmd_fixture_test)

    context_parser = _add_context_args(
        _add_memory_source_args(subparsers.add_parser("context-build", help="build a context package"))
    )
    context_parser.set_defaults(func=_cmd_context_build)

    markdown_parser = _add_context_args(
        _add_memory_source_args(subparsers.add_parser("export-markdown", help="render a context package as Markdown"))
    )
    markdown_parser.add_argument("--output", type=Path, help="optional output Markdown path")
    markdown_parser.add_argument("--source-map-json", type=Path, help="optional output source-map JSON path")
    markdown_parser.add_argument("--json", action="store_true", help="return JSON metadata instead of Markdown body")
    markdown_parser.set_defaults(func=_cmd_export_markdown, json=False)

    inspect_parser = _add_access_args(
        _add_memory_source_args(subparsers.add_parser("inspect", help="inspect one memory object"))
    )
    inspect_selector = inspect_parser.add_mutually_exclusive_group(required=True)
    inspect_selector.add_argument("--id", dest="object_id", help="memory object ID")
    inspect_selector.add_argument("--fixture-key", nargs=2, metavar=("FIXTURE_ID", "KEY"), help="fixture object selector")
    inspect_parser.add_argument("--audit", action="store_true", help="inspect without visibility filtering")
    inspect_parser.set_defaults(func=_cmd_inspect)

    agent_context_parser = _add_access_args(
        _add_memory_source_args(
            subparsers.add_parser("agent-context", help="build an agent-facing context bundle"),
            fixture_default=None,
            memory_dir_default=(DEFAULT_MEMORY_DIR,),
        )
    )
    agent_context_parser.add_argument("--task", required=True, help="agent task to assemble context for")
    agent_context_parser.add_argument("--query", action="append", default=[], help="additional recall query; repeatable")
    agent_context_parser.add_argument("--context-scope", default=None, help="optional context-index scope filter")
    agent_context_parser.add_argument("--seed", action="append", default=[], help="seed memory object ID; repeatable")
    agent_context_parser.add_argument(
        "--fixture-key",
        action="append",
        nargs=2,
        metavar=("FIXTURE_ID", "KEY"),
        default=[],
        help="seed memory object by fixture ID and key; repeatable",
    )
    agent_context_parser.add_argument("--limit", type=int, default=5, help="maximum document slices")
    agent_context_parser.add_argument("--memory-limit", type=int, default=8, help="maximum memory objects")
    agent_context_parser.add_argument("--repo-root", type=Path, default=Path("."), help="repository root")
    agent_context_parser.add_argument("--db-path", type=Path, default=None, help="optional context-index SQLite path")
    agent_context_parser.add_argument("--no-refresh-index", action="store_true", help="use the existing context index")
    agent_context_parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="output format",
    )
    agent_context_parser.set_defaults(func=_cmd_agent_context)

    agent_trace_parser = _add_access_args(
        _add_memory_source_args(
            subparsers.add_parser("agent-trace", help="trace one memory object for agent context"),
            fixture_default=None,
            memory_dir_default=(DEFAULT_MEMORY_DIR,),
        )
    )
    agent_trace_selector = agent_trace_parser.add_mutually_exclusive_group(required=True)
    agent_trace_selector.add_argument("--id", dest="object_id", help="memory object ID")
    agent_trace_selector.add_argument("--fixture-key", nargs=2, metavar=("FIXTURE_ID", "KEY"), help="fixture object selector")
    agent_trace_parser.add_argument("--audit", action="store_true", help="inspect without visibility filtering")
    agent_trace_parser.set_defaults(func=_cmd_agent_trace)

    agent_affected_parser = _add_access_args(
        _add_memory_source_args(
            subparsers.add_parser("agent-affected", help="list memory objects affected by a source path"),
            fixture_default=None,
            memory_dir_default=(DEFAULT_MEMORY_DIR,),
        )
    )
    agent_affected_parser.add_argument("--path", required=True, help="source path to match against provenance refs")
    agent_affected_parser.set_defaults(func=_cmd_agent_affected)

    review_parser = _add_fixture_args(subparsers.add_parser("review-candidate", help="review one candidate object"))
    review_parser.add_argument("--candidate-json", type=Path, required=True, help="candidate MemoryObject JSON path")
    review_parser.add_argument(
        "--outcome",
        choices=[outcome.value for outcome in ReviewOutcome],
        required=True,
        help="review outcome",
    )
    review_parser.add_argument("--reviewer", required=True, help="reviewer identifier")
    review_parser.add_argument("--rationale", default="", help="review rationale")
    review_parser.add_argument("--amended-title", help="amended title for amend outcome")
    review_parser.add_argument("--authority-ref", help="authority reference for authority-gated promotion")
    review_parser.set_defaults(func=_cmd_review_candidate)

    return parser


def _add_fixture_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--fixture-dir", type=Path, default=DEFAULT_FIXTURE_DIR, help="golden fixture directory")
    return parser


def _add_memory_source_args(
    parser: argparse.ArgumentParser,
    *,
    fixture_default: Path | None = DEFAULT_FIXTURE_DIR,
    memory_dir_default: Sequence[Path] = (),
) -> argparse.ArgumentParser:
    parser.add_argument("--fixture-dir", type=Path, default=fixture_default, help="golden fixture directory")
    parser.add_argument("--memory-file", type=Path, action="append", default=[], help="MemoryObject JSON file; repeatable")
    parser.add_argument(
        "--memory-dir",
        type=Path,
        action="append",
        default=list(memory_dir_default),
        help="directory of MemoryObject JSON files; repeatable",
    )
    parser.add_argument("--no-fixtures", action="store_true", help="do not load fixture objects")
    return parser


def _add_access_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--scope", action="append", default=None, help="access scope; repeatable")
    parser.add_argument("--include-suppressed", action="store_true", help="allow suppressed audit visibility")
    return parser


def _add_context_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    _add_access_args(parser)
    parser.add_argument("--purpose", required=True, help="context package purpose")
    parser.add_argument("--boundary", default="project_context", help="context propagation boundary")
    parser.add_argument("--seed", action="append", default=[], help="seed object ID; repeatable")
    parser.add_argument(
        "--fixture-key",
        action="append",
        nargs=2,
        metavar=("FIXTURE_ID", "KEY"),
        default=[],
        help="seed object by fixture ID and key; repeatable",
    )
    return parser


def _cmd_validate(args: argparse.Namespace) -> dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    return {
        "ok": True,
        "command": "validate",
        "fixture_count": len(fixtures),
        "object_count": len(memory.objects()),
    }


def _cmd_fixture_test(args: argparse.Namespace) -> dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    expectation_count = sum(len(fixture.expectations) for fixture in fixtures)
    return {
        "ok": True,
        "command": "fixture-test",
        "fixture_count": len(fixtures),
        "visible_object_count": len(memory.visible_objects(AccessContext(scopes=("project", "project_reviewer")))),
        "expectation_count": expectation_count,
    }


def _cmd_context_build(args: argparse.Namespace) -> dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    package = build_context_package(memory, _context_request(args, fixtures))
    return _context_package_summary(package)


def _cmd_export_markdown(args: argparse.Namespace) -> str | dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    package = build_context_package(memory, _context_request(args, fixtures))
    view = render_markdown_view(package)
    if args.output:
        args.output.write_text(view.body, encoding="utf-8")
    if args.source_map_json:
        args.source_map_json.write_text(
            json.dumps(_source_map_summary(view.source_map), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.json:
        return {
            "ok": True,
            "command": "export-markdown",
            "body_chars": len(view.body),
            "source_count": len(view.source_map),
            "output": str(args.output) if args.output else None,
            "source_map_json": str(args.source_map_json) if args.source_map_json else None,
        }
    return view.body


def _cmd_inspect(args: argparse.Namespace) -> dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    object_id = args.object_id
    if args.fixture_key:
        object_id = _object_id_for_fixture_key(fixtures, args.fixture_key[0], args.fixture_key[1])

    memory_object = memory.inspect(object_id) if args.audit else memory.get(object_id, _access_context(args))
    if memory_object is None:
        raise CliError(f"memory object is not visible or does not exist: {object_id}")
    return {
        "ok": True,
        "command": "inspect",
        "object": _memory_object_summary(memory_object),
    }


def _cmd_agent_context(args: argparse.Namespace) -> dict[str, Any] | str:
    fixtures, memory = _load_project_memory(args)
    seed_ids = list(args.seed)
    for fixture_id, key in args.fixture_key:
        seed_ids.append(_object_id_for_fixture_key(fixtures, fixture_id, key))
    bundle = build_agent_context_bundle(
        root=args.repo_root,
        task=args.task,
        memory=memory,
        access=_access_context(args),
        scope=args.context_scope,
        queries=tuple(args.query),
        seed_object_ids=tuple(seed_ids),
        limit=args.limit,
        memory_limit=args.memory_limit,
        db_path=args.db_path,
        refresh_index=not args.no_refresh_index,
    )
    if args.format == "markdown":
        return format_agent_context_markdown(bundle)
    return agent_context_summary(bundle)


def _cmd_agent_trace(args: argparse.Namespace) -> dict[str, Any]:
    fixtures, memory = _load_project_memory(args)
    object_id = args.object_id
    if args.fixture_key:
        object_id = _object_id_for_fixture_key(fixtures, args.fixture_key[0], args.fixture_key[1])
    memory_object = memory.inspect(object_id) if args.audit else memory.get(object_id, _access_context(args))
    if memory_object is None:
        raise CliError(f"memory object is not visible or does not exist: {object_id}")
    return {
        "ok": True,
        "command": "agent-trace",
        "object": _memory_object_summary(memory_object),
        "outgoing": _outgoing_relationship_summary(memory, memory_object, _access_context(args), audit=args.audit),
        "incoming": _incoming_relationship_summary(memory, memory_object.id, _access_context(args), audit=args.audit),
    }


def _cmd_agent_affected(args: argparse.Namespace) -> dict[str, Any]:
    _, memory = _load_project_memory(args)
    access = _access_context(args)
    source_path = _normalize_source_ref(args.path)
    affected = []
    for memory_object in memory.visible_objects(access):
        refs = {
            _normalize_source_ref(ref)
            for ref in (*memory_object.provenance.source_refs, *memory_object.provenance.derivation_refs)
        }
        if source_path in refs:
            affected.append(_memory_object_summary(memory_object))
    return {
        "ok": True,
        "command": "agent-affected",
        "path": source_path,
        "markdown_role": markdown_role_for_source(source_path).value,
        "affected_count": len(affected),
        "objects": affected,
    }


def _load_project_memory(args: argparse.Namespace) -> tuple[tuple[GoldenFixture, ...], ProjectMemory]:
    fixtures = _load_fixture_inputs(args)
    objects = [memory_object for fixture in fixtures for memory_object in fixture.objects.values()]
    objects.extend(_load_memory_object_inputs(args))
    return fixtures, ProjectMemory(objects)


def _load_fixture_inputs(args: argparse.Namespace) -> tuple[GoldenFixture, ...]:
    fixture_dir = getattr(args, "fixture_dir", None)
    if getattr(args, "no_fixtures", False) or fixture_dir is None:
        return ()
    return load_fixtures(fixture_dir)


def _load_memory_object_inputs(args: argparse.Namespace) -> list[MemoryObject]:
    objects: list[MemoryObject] = []
    for path in getattr(args, "memory_file", []) or []:
        objects.append(_memory_object_from_json(path))
    for directory in getattr(args, "memory_dir", []) or []:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.json")):
            objects.append(_memory_object_from_json(path))
    return objects


def _cmd_review_candidate(args: argparse.Namespace) -> dict[str, Any]:
    candidate = _memory_object_from_json(args.candidate_json)
    decision = ReviewDecision(
        outcome=ReviewOutcome(args.outcome),
        reviewer=args.reviewer,
        rationale=args.rationale,
        amended_title=args.amended_title,
        authority_ref=args.authority_ref,
    )
    result = review_candidate(candidate, decision)
    return {
        "ok": True,
        "command": "review-candidate",
        "candidate": _memory_object_summary(result.candidate),
        "reviewed_object": _memory_object_summary(result.reviewed_object),
        "decision": {
            "outcome": result.decision.outcome.value,
            "reviewer": result.decision.reviewer,
            "rationale": result.decision.rationale,
            "reviewed_at": result.decision.reviewed_at.isoformat(),
            "amended_title": result.decision.amended_title,
            "authority_ref": result.decision.authority_ref,
        },
    }


def _context_request(args: argparse.Namespace, fixtures: Sequence[GoldenFixture]) -> ContextRequest:
    seed_ids = list(args.seed)
    for fixture_id, key in args.fixture_key:
        seed_ids.append(_object_id_for_fixture_key(fixtures, fixture_id, key))
    return ContextRequest(
        purpose=args.purpose,
        access=_access_context(args),
        boundary=args.boundary,
        seed_object_ids=tuple(seed_ids),
        selection_mode=(
            ContextSelectionMode.EXPLICIT_SEED if seed_ids else ContextSelectionMode.EXPLICIT_BROAD
        ),
    )


def _access_context(args: argparse.Namespace) -> AccessContext:
    scopes = tuple(scope for scope in (args.scope or ["project"]) if scope)
    return AccessContext(scopes=scopes, include_suppressed=args.include_suppressed)


def _object_id_for_fixture_key(fixtures: Sequence[GoldenFixture], fixture_id: str, key: str) -> str:
    for fixture in fixtures:
        if fixture.fixture_id != fixture_id:
            continue
        memory_object = fixture.objects.get(key)
        if memory_object is None:
            raise CliError(f"unknown fixture key: {fixture_id} {key}")
        return memory_object.id
    raise CliError(f"unknown fixture id: {fixture_id}")


def _context_package_summary(package: Any) -> dict[str, Any]:
    return {
        "ok": True,
        "command": "context-build",
        "purpose": package.purpose,
        "boundary": package.boundary,
        "selection_mode": package.selection_mode.value,
        "current": [_context_item_summary(item) for item in package.current],
        "surfaced": [_context_item_summary(item) for item in package.surfaced],
        "contradictions": [
            {"left": _memory_object_summary(left), "right": _memory_object_summary(right)}
            for left, right in package.contradictions
        ],
        "exclusions": [
            {"object_id": exclusion.object_id, "title": exclusion.title, "reason": exclusion.reason}
            for exclusion in package.exclusions
        ],
    }


def _context_item_summary(item: Any) -> dict[str, Any]:
    summary = _memory_object_summary(item.object)
    summary["reason"] = item.reason
    return summary


def _memory_object_summary(memory_object: MemoryObject) -> dict[str, Any]:
    return {
        "id": memory_object.id,
        "type": memory_object.type.value,
        "title": memory_object.title,
        "status": memory_object.status.value,
        "visibility": memory_object.visibility.value,
        "authority_ref": memory_object.authority_ref,
        "confidence": memory_object.confidence,
        "source_refs": list(memory_object.provenance.source_refs),
        "derivation_refs": list(memory_object.provenance.derivation_refs),
        "created_by": memory_object.provenance.created_by,
        "created_at": memory_object.provenance.created_at.isoformat(),
        "evidence_level": memory_object.provenance.evidence_level.value,
        "relationships": [
            {
                "type": relationship.type.value,
                "target_id": relationship.target_id,
                "evidence_ids": list(relationship.evidence_ids),
            }
            for relationship in memory_object.relationships
        ],
        "metadata": dict(memory_object.metadata),
    }


def _memory_object_from_json(path: Path) -> MemoryObject:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise CliError(f"{path} must contain a JSON object")
    provenance_payload = payload.get("provenance")
    if not isinstance(provenance_payload, dict):
        raise CliError(f"{path} requires provenance object")
    memory_object = MemoryObject(
        id=_required_payload_str(payload, "id", path),
        type=MemoryObjectType(_required_payload_str(payload, "type", path)),
        title=_required_payload_str(payload, "title", path),
        status=LifecycleStatus(_required_payload_str(payload, "status", path)),
        visibility=Visibility(_required_payload_str(payload, "visibility", path)),
        provenance=Provenance(
            source_refs=tuple(_required_payload_str_list(provenance_payload, "source_refs", path)),
            created_by=_required_payload_str(provenance_payload, "created_by", path),
            created_at=_parse_datetime(_required_payload_str(provenance_payload, "created_at", path), path),
            evidence_level=EvidenceLevel(_required_payload_str(provenance_payload, "evidence_level", path)),
            derivation_refs=tuple(_optional_payload_str_list(provenance_payload, "derivation_refs")),
        ),
        relationships=tuple(_relationship_from_payload(item, path) for item in payload.get("relationships", [])),
        updated_at=_parse_optional_datetime(payload.get("updated_at"), path),
        supersedes=tuple(_optional_payload_str_list(payload, "supersedes")),
        superseded_by=tuple(_optional_payload_str_list(payload, "superseded_by")),
        authority_ref=payload.get("authority_ref") if isinstance(payload.get("authority_ref"), str) else None,
        confidence=payload.get("confidence") if isinstance(payload.get("confidence"), float | int) else None,
        metadata=payload.get("metadata", {}) if isinstance(payload.get("metadata", {}), dict) else {},
    )
    validate_memory_object(memory_object)
    return memory_object


def _relationship_from_payload(payload: Any, path: Path) -> Relationship:
    if not isinstance(payload, dict):
        raise CliError(f"{path} relationship entries must be objects")
    return Relationship(
        type=RelationshipType(_required_payload_str(payload, "type", path)),
        target_id=_required_payload_str(payload, "target_id", path),
        evidence_ids=tuple(_optional_payload_str_list(payload, "evidence_ids")),
    )


def _parse_datetime(raw_value: str, path: Path) -> datetime:
    try:
        value = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CliError(f"{path} invalid datetime: {raw_value}") from exc
    if value.tzinfo is None:
        raise CliError(f"{path} datetime must be timezone-aware: {raw_value}")
    return value


def _parse_optional_datetime(raw_value: Any, path: Path) -> datetime | None:
    if raw_value is None:
        return None
    if not isinstance(raw_value, str):
        raise CliError(f"{path} optional datetime must be a string")
    return _parse_datetime(raw_value, path)


def _required_payload_str(payload: Mapping[str, Any], key: str, path: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CliError(f"{path} requires non-empty string field: {key}")
    return value


def _required_payload_str_list(payload: Mapping[str, Any], key: str, path: Path) -> tuple[str, ...]:
    value = payload.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
        raise CliError(f"{path} requires non-empty string list field: {key}")
    return tuple(value)


def _optional_payload_str_list(payload: Mapping[str, Any], key: str) -> tuple[str, ...]:
    value = payload.get(key, [])
    if not isinstance(value, list):
        return ()
    return tuple(item for item in value if isinstance(item, str) and item)


def _source_map_summary(source_map: Mapping[str, Any]) -> dict[str, Any]:
    return {
        anchor: {
            "object_id": source.object_id,
            "title": source.title,
            "source_refs": list(source.source_refs),
            "evidence_level": source.evidence_level,
            "related_object_ids": list(source.related_object_ids),
        }
        for anchor, source in source_map.items()
    }


def _outgoing_relationship_summary(
    memory: ProjectMemory,
    memory_object: MemoryObject,
    access: AccessContext,
    *,
    audit: bool,
) -> list[dict[str, Any]]:
    items = []
    for relationship in memory_object.relationships:
        target = memory.inspect(relationship.target_id) if audit else memory.get(relationship.target_id, access)
        items.append(
            {
                "type": relationship.type.value,
                "target_id": relationship.target_id,
                "target": _memory_object_summary(target) if target else None,
                "evidence_ids": list(relationship.evidence_ids),
            }
        )
    return items


def _incoming_relationship_summary(
    memory: ProjectMemory,
    object_id: str,
    access: AccessContext,
    *,
    audit: bool,
) -> list[dict[str, Any]]:
    source_objects = memory.objects() if audit else memory.visible_objects(access)
    items = []
    for source in source_objects:
        for relationship in source.relationships:
            if relationship.target_id != object_id:
                continue
            items.append(
                {
                    "type": relationship.type.value,
                    "source": _memory_object_summary(source),
                    "evidence_ids": list(relationship.evidence_ids),
                }
            )
    return items


def _normalize_source_ref(ref: str) -> str:
    return ref.strip().lstrip("./").split("#", 1)[0]


if __name__ == "__main__":
    raise SystemExit(main())
