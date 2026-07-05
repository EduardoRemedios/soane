from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from soane.thinking_engine.coding_workflow import (
    list_fixture_summaries,
    render_text_summary,
    run_workflow_summary,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "coding_proof_harness"


class ThinkingEngineCodingWorkflowTests(unittest.TestCase):
    def test_list_fixtures_delegates_to_coding_harness_fixture_loader(self) -> None:
        fixtures = list_fixture_summaries(FIXTURE_DIR)

        self.assertEqual(
            ["CPH-GF-001", "CPH-GF-002", "CPH-GF-003", "CPH-MR-001", "CPH-MR-002"],
            [item["fixture_id"] for item in fixtures],
        )
        self.assertEqual("codex_cli", fixtures[0]["provider_surface"])
        self.assertEqual("cursor_cli", fixtures[1]["provider_surface"])
        self.assertFalse(fixtures[2]["expected_ready_for_provider"])
        self.assertTrue(fixtures[3]["multi_repo"])
        self.assertTrue(fixtures[3]["expected_ready_for_provider"])
        self.assertTrue(fixtures[4]["multi_repo"])
        self.assertFalse(fixtures[4]["expected_ready_for_provider"])

    def test_run_workflow_summary_exposes_required_harness_sections(self) -> None:
        summary = run_workflow_summary("CPH-GF-001", FIXTURE_DIR)

        self.assertTrue(summary["ok"])
        self.assertEqual("greenfield", summary["intake"]["category"])
        self.assertEqual("ready_for_planning", summary["intake"]["readiness_state"])
        self.assertEqual("ready_for_planning", summary["discovery"]["stop_condition"])
        self.assertGreater(summary["context_package"]["surfaced_count"], 0)
        self.assertTrue(summary["provider"]["ready_for_provider"])
        self.assertTrue(summary["provider"]["invocation_available"])
        self.assertTrue(summary["provider"]["mocked"])
        self.assertTrue(summary["provider"]["adapter_twin"])
        self.assertFalse(summary["provider"]["live_call_performed"])
        self.assertTrue(summary["output_candidate"]["available"])
        self.assertTrue(summary["output_candidate"]["promotion_required"])
        self.assertFalse(summary["output_candidate"]["current_truth"])
        self.assertEqual("candidate_only", summary["review"]["state"])
        self.assertFalse(summary["side_effects"]["live_call_performed"])
        self.assertFalse(summary["side_effects"]["repository_mutation_performed"])

    def test_multi_repo_workflow_summary_exposes_system_boundary(self) -> None:
        summary = run_workflow_summary("CPH-MR-001", FIXTURE_DIR)

        self.assertEqual("brownfield_multi_repo", summary["intake"]["category"])
        self.assertEqual("ready_for_planning", summary["intake"]["readiness_state"])
        self.assertTrue(summary["system_boundary"]["multi_repo"])
        self.assertTrue(summary["system_boundary"]["ready_for_provider"])
        self.assertEqual(3, summary["system_boundary"]["relevant_repository_count"])
        self.assertEqual(1, summary["system_boundary"]["out_of_scope_repository_count"])
        self.assertEqual(
            ["repo-checkout-web", "repo-order-api", "repo-payments-adapter"],
            summary["system_boundary"]["relevant_repositories"],
        )
        self.assertEqual(["repo-analytics-export"], summary["system_boundary"]["out_of_scope_repositories"])
        self.assertTrue(summary["provider"]["invocation_available"])
        self.assertTrue(summary["output_candidate"]["available"])
        self.assertFalse(summary["output_candidate"]["current_truth"])

    def test_reviewed_workflow_summary_requires_explicit_review(self) -> None:
        candidate_only = run_workflow_summary("CPH-GF-002", FIXTURE_DIR)
        reviewed = self._run_json(
            "run",
            "CPH-GF-002",
            "--review-outcome",
            "accept",
            "--reviewer",
            "workflow-reviewer",
            "--rationale",
            "Accepted through explicit workflow review.",
        )

        self.assertEqual("candidate_only", candidate_only["review"]["state"])
        self.assertFalse(candidate_only["output_candidate"]["current_truth"])
        self.assertEqual("reviewed", reviewed["review"]["state"])
        self.assertEqual("accept", reviewed["review"]["outcome"])
        self.assertEqual("accepted", reviewed["review"]["reviewed_status"])
        self.assertTrue(reviewed["review"]["current_truth"])
        self.assertFalse(reviewed["output_candidate"]["current_truth"])

    def test_brownfield_blocked_summary_has_no_provider_invocation_or_output(self) -> None:
        summary = run_workflow_summary("CPH-GF-003", FIXTURE_DIR)

        self.assertEqual("brownfield_single_repo", summary["intake"]["category"])
        self.assertEqual("blocked", summary["intake"]["readiness_state"])
        self.assertEqual("blocked", summary["discovery"]["stop_condition"])
        self.assertFalse(summary["provider"]["ready_for_provider"])
        self.assertFalse(summary["provider"]["invocation_available"])
        self.assertFalse(summary["provider"]["mocked"])
        self.assertFalse(summary["output_candidate"]["available"])
        self.assertEqual("candidate_only", summary["review"]["state"])

    def test_brownfield_multi_repo_blocked_summary_has_no_provider_invocation_or_output(self) -> None:
        summary = run_workflow_summary("CPH-MR-002", FIXTURE_DIR)

        self.assertEqual("brownfield_multi_repo", summary["intake"]["category"])
        self.assertEqual("blocked", summary["intake"]["readiness_state"])
        self.assertEqual("blocked", summary["discovery"]["stop_condition"])
        self.assertTrue(summary["system_boundary"]["multi_repo"])
        self.assertFalse(summary["system_boundary"]["ready_for_provider"])
        self.assertIn("integration contract", summary["intake"]["missing_context"])
        self.assertIn("missing approval path", summary["system_boundary"]["documentation_gaps"])
        self.assertFalse(summary["provider"]["ready_for_provider"])
        self.assertFalse(summary["provider"]["invocation_available"])
        self.assertFalse(summary["output_candidate"]["available"])

    def test_text_summary_is_terminal_readable(self) -> None:
        summary = run_workflow_summary("CPH-GF-001", FIXTURE_DIR)
        text = render_text_summary(summary)

        self.assertIn("Coding Harness Workflow: CPH-GF-001", text)
        self.assertIn("Readiness: ready_for_planning", text)
        self.assertIn("System boundary: multi_repo=False", text)
        self.assertIn("Provider: codex_cli ready=True", text)
        self.assertIn("Output candidate: available=True", text)
        self.assertIn("Live call performed: False", text)
        self.assertIn("Repository mutation performed: False", text)

    def test_cli_list_and_run_emit_json(self) -> None:
        listed = self._run_json("list")
        ran = self._run_json("run", "CPH-GF-001")

        self.assertEqual("list", listed["command"])
        self.assertEqual(5, listed["fixture_count"])
        self.assertEqual("run", ran["command"])
        self.assertEqual("CPH-GF-001", ran["fixture"]["fixture_id"])

    def test_cli_runs_multi_repo_fixture_and_emits_json(self) -> None:
        ran = self._run_json("run", "CPH-MR-001")

        self.assertEqual("run", ran["command"])
        self.assertEqual("CPH-MR-001", ran["fixture"]["fixture_id"])
        self.assertTrue(ran["fixture"]["multi_repo"])
        self.assertEqual(3, ran["system_boundary"]["relevant_repository_count"])
        self.assertEqual(1, ran["system_boundary"]["out_of_scope_repository_count"])

    def test_cli_default_run_emits_text(self) -> None:
        result = self._run_cli("run", "CPH-GF-003")

        self.assertIn("Coding Harness Workflow: CPH-GF-003", result.stdout)
        self.assertIn("Readiness: blocked", result.stdout)
        self.assertIn("invocation_available=False", result.stdout)

    def test_cli_rejects_review_without_provider_output(self) -> None:
        result = self._run_cli(
            "run",
            "CPH-GF-003",
            "--review-outcome",
            "accept",
            "--reviewer",
            "workflow-reviewer",
            "--rationale",
            "Cannot review absent output.",
            "--json",
            expect_success=False,
        )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("provider output is unavailable", result.stderr)

    def _run_json(self, command: str, *args: str) -> dict[str, object]:
        result = self._run_cli(command, *args, "--json")
        return json.loads(result.stdout)

    def _run_cli(self, command: str, *args: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.thinking_engine.coding_workflow",
                command,
                "--fixture-dir",
                str(FIXTURE_DIR),
                *args,
            ],
            check=False,
            cwd=Path(__file__).parents[1],
            text=True,
            capture_output=True,
        )
        if expect_success and result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        return result


if __name__ == "__main__":
    unittest.main()
