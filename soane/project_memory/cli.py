"""Headless CLI for Project Memory v0."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from soane.project_memory.context import ContextRequest, build_context_package, render_markdown_view
from soane.project_memory.contract import MemoryObject, validate_memory_object
from soane.project_memory.fixtures import GoldenFixture, load_fixtures
from soane.project_memory.semantics import AccessContext, ProjectMemory


DEFAULT_FIXTURE_DIR = Path("tests/fixtures/project_memory/golden")


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

    validate_parser = _add_fixture_args(subparsers.add_parser("validate", help="validate Project Memory fixtures"))
    validate_parser.set_defaults(func=_cmd_validate)

    fixture_parser = _add_fixture_args(
        subparsers.add_parser("fixture-test", help="load fixtures into local Project Memory")
    )
    fixture_parser.set_defaults(func=_cmd_fixture_test)

    context_parser = _add_context_args(
        _add_fixture_args(subparsers.add_parser("context-build", help="build a context package"))
    )
    context_parser.set_defaults(func=_cmd_context_build)

    markdown_parser = _add_context_args(
        _add_fixture_args(subparsers.add_parser("export-markdown", help="render a context package as Markdown"))
    )
    markdown_parser.add_argument("--output", type=Path, help="optional output Markdown path")
    markdown_parser.add_argument("--source-map-json", type=Path, help="optional output source-map JSON path")
    markdown_parser.add_argument("--json", action="store_true", help="return JSON metadata instead of Markdown body")
    markdown_parser.set_defaults(func=_cmd_export_markdown, json=False)

    inspect_parser = _add_access_args(
        _add_fixture_args(subparsers.add_parser("inspect", help="inspect one memory object"))
    )
    inspect_selector = inspect_parser.add_mutually_exclusive_group(required=True)
    inspect_selector.add_argument("--id", dest="object_id", help="memory object ID")
    inspect_selector.add_argument("--fixture-key", nargs=2, metavar=("FIXTURE_ID", "KEY"), help="fixture object selector")
    inspect_parser.add_argument("--audit", action="store_true", help="inspect without visibility filtering")
    inspect_parser.set_defaults(func=_cmd_inspect)

    return parser


def _add_fixture_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--fixture-dir", type=Path, default=DEFAULT_FIXTURE_DIR, help="golden fixture directory")
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
    fixtures = load_fixtures(args.fixture_dir)
    object_count = 0
    for fixture in fixtures:
        for memory_object in fixture.objects.values():
            validate_memory_object(memory_object)
            object_count += 1
    return {
        "ok": True,
        "command": "validate",
        "fixture_count": len(fixtures),
        "object_count": object_count,
    }


def _cmd_fixture_test(args: argparse.Namespace) -> dict[str, Any]:
    fixtures = load_fixtures(args.fixture_dir)
    memory = ProjectMemory.from_fixtures(fixtures)
    expectation_count = sum(len(fixture.expectations) for fixture in fixtures)
    return {
        "ok": True,
        "command": "fixture-test",
        "fixture_count": len(fixtures),
        "visible_object_count": len(memory.visible_objects(AccessContext(scopes=("project", "project_reviewer")))),
        "expectation_count": expectation_count,
    }


def _cmd_context_build(args: argparse.Namespace) -> dict[str, Any]:
    fixtures = load_fixtures(args.fixture_dir)
    memory = ProjectMemory.from_fixtures(fixtures)
    package = build_context_package(memory, _context_request(args, fixtures))
    return _context_package_summary(package)


def _cmd_export_markdown(args: argparse.Namespace) -> str | dict[str, Any]:
    fixtures = load_fixtures(args.fixture_dir)
    memory = ProjectMemory.from_fixtures(fixtures)
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
    fixtures = load_fixtures(args.fixture_dir)
    memory = ProjectMemory.from_fixtures(fixtures)
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


def _context_request(args: argparse.Namespace, fixtures: Sequence[GoldenFixture]) -> ContextRequest:
    seed_ids = list(args.seed)
    for fixture_id, key in args.fixture_key:
        seed_ids.append(_object_id_for_fixture_key(fixtures, fixture_id, key))
    return ContextRequest(
        purpose=args.purpose,
        access=_access_context(args),
        boundary=args.boundary,
        seed_object_ids=tuple(seed_ids),
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


if __name__ == "__main__":
    raise SystemExit(main())
