from __future__ import annotations

import json
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

from soane.thinking_engine.adapter_evaluation_workflow import (
    evaluate_from_files,
    render_text_report,
)


REPO_ROOT = Path(__file__).parents[1]
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "live_adapter_evaluation"
PROFILE_DIR = FIXTURE_ROOT / "profiles"
CONTEXT_JSON = FIXTURE_ROOT / "context_ready.json"
SOURCE_DATE = date(2026, 7, 23)


class ThinkingEngineAdapterEvaluationWorkflowTests(unittest.TestCase):
    def test_service_delegating_workflow_returns_stable_json_contract(self) -> None:
        payload = evaluate_from_files(
            profile_dir=PROFILE_DIR,
            context_json=CONTEXT_JSON,
            source_date=SOURCE_DATE,
        )

        self.assertTrue(payload["ok"])
        self.assertEqual("lcae-evaluation-v1", payload["schema_version"])
        self.assertEqual("lcae-score-v1", payload["scoring_version"])
        self.assertEqual("codex_cli", payload["recommendation"]["surface"])
        self.assertEqual(5, len(payload["surfaces"]))
        self.assertEqual("ready", payload["context"]["selection_state"])

    def test_text_report_explains_recommendation_blockers_and_no_side_effects(self) -> None:
        payload = evaluate_from_files(
            profile_dir=PROFILE_DIR,
            context_json=CONTEXT_JSON,
            source_date=SOURCE_DATE,
        )
        report = render_text_report(payload)

        self.assertIn("Recommendation: codex_cli (highest_eligible_score)", report)
        self.assertIn("cursor_cli: eligible=False", report)
        self.assertIn("source_contradiction", report)
        self.assertIn("measured=False", report)
        self.assertIn("Live use authorized: False", report)
        self.assertIn("Provider invocation performed: False", report)
        self.assertIn("Repository mutation performed: False", report)

    def test_cli_emits_json_and_text_for_explicit_inputs(self) -> None:
        json_result = self._run_cli("--json")
        text_result = self._run_cli()
        payload = json.loads(json_result.stdout)

        self.assertEqual("codex_cli", payload["recommendation"]["surface"])
        self.assertEqual("2026-07-23", payload["evidence_state"]["source_revalidation_date"])
        self.assertIn("Live Coding Adapter Evaluation", text_result.stdout)
        self.assertIn("Recommendation: codex_cli", text_result.stdout)

    def test_cli_fails_closed_when_source_date_is_not_revalidated(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.thinking_engine.adapter_evaluation_workflow",
                "--profile-dir",
                str(PROFILE_DIR),
                "--context-json",
                str(CONTEXT_JSON),
                "--source-date",
                "2026-07-20",
                "--json",
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode)
        payload = json.loads(result.stdout)
        self.assertIsNone(payload["recommendation"]["surface"])
        self.assertEqual("no_eligible_surface", payload["recommendation"]["reason"])
        self.assertTrue(
            all(
                "source_revalidation_required" in surface["blockers"]
                for surface in payload["surfaces"]
            )
        )

    def _run_cli(self, *extra: str) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.thinking_engine.adapter_evaluation_workflow",
                "--profile-dir",
                str(PROFILE_DIR),
                "--context-json",
                str(CONTEXT_JSON),
                "--source-date",
                "2026-07-23",
                *extra,
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        return result


if __name__ == "__main__":
    unittest.main()
