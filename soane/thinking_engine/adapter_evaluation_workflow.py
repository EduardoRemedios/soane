"""Thin CLI for deterministic coding adapter evaluation."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Sequence

from soane.thinking_engine.adapter_evaluation import (
    AdapterEvaluationError,
    evaluate_adapter_profiles,
    evaluation_result_payload,
    load_adapter_profiles,
)


def evaluate_from_files(
    *,
    profile_dir: Path,
    context_json: Path,
    source_date: date,
) -> dict[str, Any]:
    profiles = load_adapter_profiles(profile_dir, required_access_date=source_date)
    try:
        context_payload = json.loads(context_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdapterEvaluationError(f"invalid context JSON: {context_json}") from exc
    if not isinstance(context_payload, dict):
        raise AdapterEvaluationError(f"context JSON must contain an object: {context_json}")
    result = evaluate_adapter_profiles(
        profiles,
        context_payload,
        required_access_date=source_date,
    )
    return evaluation_result_payload(result)


def render_text_report(payload: dict[str, Any]) -> str:
    recommendation = payload["recommendation"]
    lines = [
        "Live Coding Adapter Evaluation",
        f"Recommendation: {recommendation['surface'] or 'none'} ({recommendation['reason']})",
        (
            "Evidence: official_documentation "
            f"revalidated={payload['evidence_state']['source_revalidation_date']} "
            "measured=False"
        ),
        (
            f"Context: selection={payload['context']['selection_state']} "
            f"refresh={payload['context']['refresh_state']}"
        ),
        "Surfaces:",
    ]
    for surface in payload["surfaces"]:
        blockers = ",".join(surface["blockers"]) or "none"
        lines.append(
            f"- {surface['surface']}: eligible={surface['eligible']} "
            f"score={surface['score']} blockers={blockers}"
        )
    lines.extend(
        [
            "Live use authorized: False",
            "Provider invocation performed: False",
            "Repository mutation performed: False",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate committed coding-adapter evidence without invoking providers."
    )
    parser.add_argument("--profile-dir", type=Path, required=True)
    parser.add_argument("--context-json", type=Path, required=True)
    parser.add_argument("--source-date", type=date.fromisoformat, required=True)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        payload = evaluate_from_files(
            profile_dir=args.profile_dir,
            context_json=args.context_json,
            source_date=args.source_date,
        )
    except AdapterEvaluationError as exc:
        parser.error(str(exc))
    if args.as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_text_report(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
