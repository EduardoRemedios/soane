"""Thin terminal navigation for Project Memory v0."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Sequence

from soane.project_memory.cli import DEFAULT_FIXTURE_DIR
from soane.project_memory.context import ContextRequest, build_context_package
from soane.project_memory.contract import LifecycleStatus, MemoryObject, MemoryObjectType, validate_memory_object
from soane.project_memory.fixtures import GoldenFixture, load_fixtures
from soane.project_memory.semantics import AccessContext, ProjectMemory


class TuiScreen(StrEnum):
    OVERVIEW = "overview"
    MEMORY = "memory"
    EVIDENCE = "evidence"
    DECISIONS = "decisions"
    HYPOTHESES = "hypotheses"
    ADAPTERS = "adapters"
    QUESTIONS = "questions"


@dataclass(frozen=True)
class TuiRow:
    label: str
    value: str
    object_id: str | None = None


@dataclass(frozen=True)
class TuiModel:
    screen: TuiScreen
    title: str
    rows: tuple[TuiRow, ...]
    navigation: tuple[TuiScreen, ...]


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.list_screens:
        print("\n".join(screen.value for screen in TuiScreen))
        return 0

    try:
        fixtures = _load_required_fixtures(args.fixture_dir)
        access = _access_context(args)
        if args.interactive:
            return _run_interactive(fixtures, access, args.width)
        model = build_tui_model(fixtures, TuiScreen(args.screen), access)
        print(render_tui_model(model, width=args.width))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


def build_tui_model(
    fixtures: Sequence[GoldenFixture],
    screen: TuiScreen,
    access: AccessContext,
) -> TuiModel:
    """Build a navigational TUI model from shared Project Memory primitives."""

    memory = ProjectMemory.from_fixtures(fixtures)
    if screen == TuiScreen.OVERVIEW:
        return _overview_model(fixtures, memory, access)
    if screen == TuiScreen.MEMORY:
        return _object_list_model("Memory Browser", screen, memory.current_objects(access))
    if screen == TuiScreen.EVIDENCE:
        return _object_list_model(
            "Evidence",
            screen,
            _objects_by_type(
                memory,
                access,
                {
                    MemoryObjectType.EVIDENCE_ARTIFACT,
                    MemoryObjectType.RESEARCH_FINDING,
                    MemoryObjectType.VERIFICATION,
                },
            ),
        )
    if screen == TuiScreen.DECISIONS:
        return _object_list_model(
            "Decisions",
            screen,
            _objects_by_type(memory, access, {MemoryObjectType.DECISION}),
        )
    if screen == TuiScreen.HYPOTHESES:
        return _object_list_model(
            "Hypotheses And Assumptions",
            screen,
            _objects_by_type(memory, access, {MemoryObjectType.HYPOTHESIS, MemoryObjectType.ASSUMPTION}),
        )
    if screen == TuiScreen.ADAPTERS:
        return _object_list_model(
            "Adapter Invocations And Capabilities",
            screen,
            _objects_by_type(
                memory,
                access,
                {
                    MemoryObjectType.PROVIDER_INVOCATION,
                    MemoryObjectType.CAPABILITY_REFERENCE,
                    MemoryObjectType.AUTHORITY_REFERENCE,
                },
            ),
        )
    if screen == TuiScreen.QUESTIONS:
        return _object_list_model(
            "Unresolved Questions",
            screen,
            tuple(
                obj
                for obj in _objects_by_type(memory, access, {MemoryObjectType.QUESTION})
                if obj.status
                in {
                    LifecycleStatus.OPEN,
                    LifecycleStatus.UNDER_INVESTIGATION,
                    LifecycleStatus.DEFERRED,
                    LifecycleStatus.BLOCKED,
                }
            ),
        )
    raise ValueError(f"unknown TUI screen: {screen}")


def render_tui_model(model: TuiModel, *, width: int = 100) -> str:
    """Render a deterministic terminal screen."""

    bounded_width = max(60, min(width, 140))
    rule = "=" * bounded_width
    nav = " | ".join(f"{index}:{screen.value}" for index, screen in enumerate(model.navigation, start=1))
    lines = [
        rule,
        "Soane Project Memory",
        rule,
        f"Screen: {model.title}",
        _truncate(f"Navigation: {nav}", bounded_width),
        _truncate(
            "Actions: q quit | number/name switch | inspect with `python -m soane.project_memory.cli inspect --id <id>`",
            bounded_width,
        ),
        "-" * bounded_width,
    ]
    if model.rows:
        lines.extend(_render_row(row, bounded_width) for row in model.rows)
    else:
        lines.append("No visible records.")
    lines.append(rule)
    return "\n".join(lines) + "\n"


def _overview_model(fixtures: Sequence[GoldenFixture], memory: ProjectMemory, access: AccessContext) -> TuiModel:
    for fixture in fixtures:
        for memory_object in fixture.objects.values():
            validate_memory_object(memory_object)

    package = build_context_package(
        memory,
        ContextRequest(purpose="TUI overview", access=access),
    )
    rows = (
        TuiRow("Validation", f"{len(fixtures)} fixtures loaded"),
        TuiRow("Current Memory", str(len(package.current))),
        TuiRow("Surfaced Non-Current", str(len(package.surfaced))),
        TuiRow("Contradictions", str(len(package.contradictions))),
        TuiRow("Exclusions", str(len(package.exclusions))),
        TuiRow("Next Screen", TuiScreen.MEMORY.value),
    )
    return TuiModel(
        screen=TuiScreen.OVERVIEW,
        title="Project Navigation",
        rows=rows,
        navigation=tuple(TuiScreen),
    )


def _object_list_model(title: str, screen: TuiScreen, objects: Sequence[MemoryObject]) -> TuiModel:
    rows = tuple(
        TuiRow(
            label=f"{obj.type.value}/{obj.status.value}",
            value=obj.title,
            object_id=obj.id,
        )
        for obj in sorted(objects, key=lambda item: (item.type.value, item.title, item.id))
    )
    return TuiModel(
        screen=screen,
        title=title,
        rows=rows,
        navigation=tuple(TuiScreen),
    )


def _objects_by_type(
    memory: ProjectMemory,
    access: AccessContext,
    object_types: set[MemoryObjectType],
) -> tuple[MemoryObject, ...]:
    return tuple(obj for obj in memory.visible_objects(access) if obj.type in object_types)


def _render_row(row: TuiRow, width: int) -> str:
    id_fragment = f" [{row.object_id}]" if row.object_id else ""
    label_width = 30
    label = _truncate(row.label, label_width)
    value = _truncate(row.value, width - label_width - 1 - len(id_fragment))
    return f"{label:<{label_width}} {value}{id_fragment}"


def _truncate(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    if limit <= 3:
        return value[:limit]
    return value[: limit - 3] + "..."


def _run_interactive(fixtures: Sequence[GoldenFixture], access: AccessContext, width: int) -> int:
    screen = TuiScreen.OVERVIEW
    screens = tuple(TuiScreen)
    while True:
        print(render_tui_model(build_tui_model(fixtures, screen, access), width=width))
        response = input("screen number, name, or q: ").strip().lower()
        if response in {"q", "quit", "exit"}:
            return 0
        if response.isdigit() and 1 <= int(response) <= len(screens):
            screen = screens[int(response) - 1]
            continue
        try:
            screen = TuiScreen(response)
        except ValueError:
            print(f"unknown screen: {response}", file=sys.stderr)


def _load_required_fixtures(fixture_dir: Path) -> tuple[GoldenFixture, ...]:
    fixtures = load_fixtures(fixture_dir)
    if not fixtures:
        raise ValueError(f"no fixtures found in {fixture_dir}")
    return fixtures


def _access_context(args: argparse.Namespace) -> AccessContext:
    scopes = tuple(scope for scope in (args.scope or ["project"]) if scope)
    return AccessContext(scopes=scopes, include_suppressed=args.include_suppressed)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m soane.project_memory.tui")
    parser.add_argument("--fixture-dir", type=Path, default=DEFAULT_FIXTURE_DIR, help="golden fixture directory")
    parser.add_argument("--screen", choices=[screen.value for screen in TuiScreen], default=TuiScreen.OVERVIEW.value)
    parser.add_argument("--scope", action="append", default=None, help="access scope; repeatable")
    parser.add_argument("--include-suppressed", action="store_true", help="allow suppressed audit visibility")
    parser.add_argument("--width", type=int, default=100, help="render width")
    parser.add_argument("--interactive", action="store_true", help="run simple terminal navigation loop")
    parser.add_argument("--list-screens", action="store_true", help="list available screens")
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
