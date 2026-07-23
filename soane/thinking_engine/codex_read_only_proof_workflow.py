"""Offline candidate-report workflow for the bounded Codex CLI proof."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Sequence

from soane.thinking_engine.codex_read_only_proof import (
    ProofContractError,
    build_offline_candidate,
    candidate_payload,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a candidate-only Codex read-only proof report."
    )
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--fixture-root", required=True, type=Path)
    parser.add_argument("--source-date", required=True)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        source_date = date.fromisoformat(args.source_date)
        config = json.loads(args.config.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            raise ProofContractError("config must contain a JSON object")
        candidate = build_offline_candidate(
            config,
            fixture_root=args.fixture_root,
            required_source_date=source_date,
        )
        payload = candidate_payload(candidate)
    except (OSError, ValueError, json.JSONDecodeError, ProofContractError) as exc:
        raise SystemExit(f"candidate generation failed: {exc}") from exc

    if args.as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(f"Status: {payload['status']}")
        print("Review state: candidate_only")
        blockers = payload["blockers"]
        print(f"Blockers: {', '.join(blockers) if blockers else 'none'}")
        print("MS-04 authorized: false")
        print("Provider invocation performed: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
