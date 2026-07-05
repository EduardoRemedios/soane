"""CLI-first workflow wrapper for Coding Proof Harness v0.

This module is deliberately thin. It loads fixtures, delegates execution to
``soane.thinking_engine.coding_harness``, and renders inspectable summaries.
It does not call live providers, mutate repositories, persist state, or create
Workspace Shell behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from soane.project_memory.review import ReviewDecision, ReviewOutcome, is_candidate_object
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory
from soane.thinking_engine.coding_harness import (
    CodingHarnessFixture,
    CodingHarnessResult,
    load_coding_harness_fixtures,
    review_provider_output,
    run_coding_proof,
)


DEFAULT_CODING_FIXTURE_DIR = Path("tests/fixtures/coding_proof_harness")


class CodingWorkflowError(ValueError):
    """Raised for user-facing coding workflow errors."""


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        result = args.func(args)
    except Exception as exc:
        if getattr(args, "json", False):
            print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 1
    if isinstance(result, str):
        print(result, end="" if result.endswith("\n") else "\n")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def list_fixture_summaries(fixture_dir: Path | str = DEFAULT_CODING_FIXTURE_DIR) -> tuple[dict[str, Any], ...]:
    """Return deterministic summaries for available coding harness fixtures."""

    return tuple(_fixture_summary(fixture) for fixture in load_coding_harness_fixtures(fixture_dir))


def run_workflow_summary(
    fixture_id: str,
    fixture_dir: Path | str = DEFAULT_CODING_FIXTURE_DIR,
    review_decision: ReviewDecision | None = None,
) -> dict[str, Any]:
    """Run one coding fixture through the harness and return a workflow summary."""

    fixture = _fixture_by_id(fixture_id, fixture_dir)
    result = run_coding_proof(fixture)
    reviewed = review_provider_output(result, review_decision) if review_decision is not None else None
    memory_objects = result.memory_objects
    if reviewed is not None:
        memory_objects = (*memory_objects, reviewed.reviewed_object)
    memory = ProjectMemory(memory_objects)
    current_ids = {memory_object.id for memory_object in memory.current_objects(PROJECT_READER)}

    return {
        "ok": True,
        "command": "run",
        "fixture": _fixture_summary(fixture),
        "intake": {
            "category": result.intake.baseline.category.value,
            "readiness_state": result.intake.readiness.state.value,
            "blockers": list(result.intake.readiness.blockers),
            "missing_context": list(result.intake.readiness.missing_context),
            "canonical_docs": list(result.intake.baseline.canonical_docs),
        },
        "discovery": {
            "stop_condition": result.discovery.stop_condition.value,
            "question_count": len(result.discovery.questions),
            "candidate_count": len(result.discovery.memory_candidates),
        },
        "context_package": {
            "purpose": result.context_package.purpose,
            "boundary": result.context_package.boundary,
            "current_count": len(result.context_package.current),
            "surfaced_count": len(result.context_package.surfaced),
            "contradiction_count": len(result.context_package.contradictions),
            "exclusion_count": len(result.context_package.exclusions),
        },
        "system_boundary": _system_boundary_summary(result),
        "provider": _provider_summary(result),
        "output_candidate": _candidate_summary(result, current_ids),
        "review": _review_summary(reviewed, current_ids),
        "side_effects": {
            "live_call_performed": result.live_call_performed,
            "repository_mutation_performed": result.repository_mutation_performed,
        },
    }


def render_text_summary(summary: dict[str, Any]) -> str:
    """Render a compact terminal summary for one workflow run."""

    fixture = summary["fixture"]
    intake = summary["intake"]
    discovery = summary["discovery"]
    context = summary["context_package"]
    system_boundary = summary["system_boundary"]
    provider = summary["provider"]
    candidate = summary["output_candidate"]
    review = summary["review"]
    side_effects = summary["side_effects"]

    lines = [
        f"Coding Harness Workflow: {fixture['fixture_id']}",
        f"Title: {fixture['title']}",
        f"Category: {intake['category']}",
        f"Readiness: {intake['readiness_state']}",
        f"Discovery stop: {discovery['stop_condition']}",
        f"Context: current={context['current_count']} surfaced={context['surfaced_count']} "
        f"excluded={context['exclusion_count']}",
        f"System boundary: multi_repo={system_boundary['multi_repo']} "
        f"ready={system_boundary['ready_for_provider']} "
        f"relevant_repos={system_boundary['relevant_repository_count']} "
        f"out_of_scope_repos={system_boundary['out_of_scope_repository_count']}",
        f"Provider: {provider['surface']} ready={provider['ready_for_provider']} "
        f"invocation_available={provider['invocation_available']} mocked={provider['mocked']}",
        f"Output candidate: available={candidate['available']} status={candidate['status']} "
        f"current_truth={candidate['current_truth']}",
        f"Review: state={review['state']} outcome={review['outcome']} "
        f"current_truth={review['current_truth']}",
        f"Live call performed: {side_effects['live_call_performed']}",
        f"Repository mutation performed: {side_effects['repository_mutation_performed']}",
    ]
    if intake["blockers"]:
        lines.append("Blockers:")
        lines.extend(f"- {blocker}" for blocker in intake["blockers"])
    return "\n".join(lines) + "\n"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m soane.thinking_engine.coding_workflow")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = _add_fixture_args(subparsers.add_parser("list", help="list coding harness fixtures"))
    list_parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    list_parser.set_defaults(func=_cmd_list)

    run_parser = _add_fixture_args(subparsers.add_parser("run", help="run one coding harness fixture"))
    run_parser.add_argument("fixture_id", help="coding harness fixture id")
    run_parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    run_parser.add_argument(
        "--review-outcome",
        choices=[outcome.value for outcome in ReviewOutcome],
        help="explicitly review the output candidate after harness execution",
    )
    run_parser.add_argument("--reviewer", help="reviewer identifier")
    run_parser.add_argument("--rationale", help="review rationale")
    run_parser.add_argument("--amended-title", help="amended title for amend outcome")
    run_parser.add_argument("--authority-ref", help="authority reference for authority-gated promotion")
    run_parser.set_defaults(func=_cmd_run)

    return parser


def _add_fixture_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--fixture-dir", type=Path, default=DEFAULT_CODING_FIXTURE_DIR, help="fixture directory")
    return parser


def _cmd_list(args: argparse.Namespace) -> str | dict[str, Any]:
    fixtures = list_fixture_summaries(args.fixture_dir)
    if args.json:
        return {"ok": True, "command": "list", "fixture_count": len(fixtures), "fixtures": list(fixtures)}
    lines = ["Coding Harness Fixtures"]
    lines.extend(
        f"- {fixture['fixture_id']}: {fixture['title']} "
        f"({fixture['category']}, ready_for_provider={fixture['expected_ready_for_provider']})"
        for fixture in fixtures
    )
    return "\n".join(lines) + "\n"


def _cmd_run(args: argparse.Namespace) -> str | dict[str, Any]:
    summary = run_workflow_summary(
        args.fixture_id,
        args.fixture_dir,
        review_decision=_review_decision_from_args(args),
    )
    if args.json:
        return summary
    return render_text_summary(summary)


def _review_decision_from_args(args: argparse.Namespace) -> ReviewDecision | None:
    if args.review_outcome is None:
        if args.reviewer or args.rationale or args.amended_title or args.authority_ref:
            raise CodingWorkflowError("review fields require --review-outcome")
        return None
    if not args.reviewer:
        raise CodingWorkflowError("--reviewer is required with --review-outcome")
    if not args.rationale and args.review_outcome != ReviewOutcome.KEEP_OPEN.value:
        raise CodingWorkflowError("--rationale is required with this review outcome")
    return ReviewDecision(
        outcome=ReviewOutcome(args.review_outcome),
        reviewer=args.reviewer,
        rationale=args.rationale or "",
        amended_title=args.amended_title,
        authority_ref=args.authority_ref,
    )


def _fixture_by_id(fixture_id: str, fixture_dir: Path | str) -> CodingHarnessFixture:
    for fixture in load_coding_harness_fixtures(fixture_dir):
        if fixture.fixture_id == fixture_id:
            return fixture
    raise CodingWorkflowError(f"unknown coding harness fixture: {fixture_id}")


def _fixture_summary(fixture: CodingHarnessFixture) -> dict[str, Any]:
    return {
        "fixture_id": fixture.fixture_id,
        "title": fixture.title,
        "category": fixture.intake_fixture.expected_category.value,
        "expected_readiness": fixture.intake_fixture.expected_readiness.value,
        "expected_ready_for_provider": fixture.expected_ready_for_provider,
        "provider_surface": fixture.provider_surface.value,
        "path": str(fixture.path),
        "multi_repo": fixture.multi_repo_system is not None,
    }


def _system_boundary_summary(result: CodingHarnessResult) -> dict[str, Any]:
    system = result.multi_repo_system
    if system is None:
        return {
            "multi_repo": False,
            "ready_for_provider": True,
            "repository_map": [],
            "relevant_repositories": [],
            "out_of_scope_repositories": [],
            "relevant_repository_count": 0,
            "out_of_scope_repository_count": 0,
            "service_boundaries": [],
            "integration_contracts": [],
            "ownership": [],
            "build_test_responsibility": [],
            "documentation_gaps": [],
            "authority_path": [],
        }
    metadata = system.as_metadata()
    return {
        **metadata,
        "multi_repo": True,
        "relevant_repository_count": len(system.relevant_repositories),
        "out_of_scope_repository_count": len(system.out_of_scope_repositories),
    }


def _provider_summary(result: CodingHarnessResult) -> dict[str, Any]:
    provider_invocation = result.provider_invocation
    metadata = dict(provider_invocation.metadata) if provider_invocation is not None else {}
    return {
        "surface": result.provider_surface.value,
        "ready_for_provider": result.ready_for_provider,
        "invocation_available": provider_invocation is not None,
        "invocation_id": provider_invocation.id if provider_invocation is not None else None,
        "mocked": bool(metadata.get("mock", False)),
        "adapter_twin": bool(metadata.get("adapter_twin", False)),
        "live_call_performed": result.live_call_performed,
    }


def _candidate_summary(result: CodingHarnessResult, current_ids: set[str]) -> dict[str, Any]:
    candidate = result.output_candidate
    if candidate is None:
        return {
            "available": False,
            "id": None,
            "status": None,
            "promotion_required": False,
            "current_truth": False,
        }
    return {
        "available": True,
        "id": candidate.id,
        "status": candidate.status.value,
        "promotion_required": is_candidate_object(candidate),
        "current_truth": candidate.id in current_ids,
    }


def _review_summary(reviewed: Any, current_ids: set[str]) -> dict[str, Any]:
    if reviewed is None:
        return {
            "state": "candidate_only",
            "outcome": None,
            "reviewed_object_id": None,
            "reviewed_status": None,
            "current_truth": False,
        }
    reviewed_object = reviewed.reviewed_object
    return {
        "state": "reviewed",
        "outcome": reviewed.decision.outcome.value,
        "reviewed_object_id": reviewed_object.id,
        "reviewed_status": reviewed_object.status.value,
        "current_truth": reviewed_object.id in current_ids,
    }


if __name__ == "__main__":
    raise SystemExit(main())
