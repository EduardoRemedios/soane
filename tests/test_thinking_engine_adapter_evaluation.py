from __future__ import annotations

import ast
import json
import tempfile
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path

from soane.project_memory.adapters import AdapterSurface
from soane.thinking_engine.adapter_evaluation import (
    AdapterEvaluationError,
    FirstProofMode,
    HardBlocker,
    SourceState,
    evaluate_adapter_profiles,
    evaluation_result_payload,
    load_adapter_profile,
    load_adapter_profiles,
)


REPO_ROOT = Path(__file__).parents[1]
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "live_adapter_evaluation"
PROFILE_DIR = FIXTURE_ROOT / "profiles"
SOURCE_DATE = date(2026, 7, 23)


class ThinkingEngineAdapterEvaluationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profiles = load_adapter_profiles(PROFILE_DIR, required_access_date=SOURCE_DATE)
        self.context = json.loads((FIXTURE_ROOT / "context_ready.json").read_text(encoding="utf-8"))

    def test_loads_exact_five_typed_source_profiles(self) -> None:
        self.assertEqual(
            {
                "codex_cli",
                "cursor_cli",
                "cursor_sdk",
                "openai_sdk",
                "openai_agents_sdk",
            },
            {profile.surface.value for profile in self.profiles},
        )
        for profile in self.profiles:
            self.assertTrue(profile.sources)
            self.assertTrue(profile.authentication_modes)
            self.assertTrue(profile.authentication_state)
            self.assertTrue(profile.capabilities)
            self.assertTrue(profile.capability_state)
            self.assertTrue(profile.requires_authority)
            self.assertTrue(profile.requires_project_permission)
            self.assertTrue(profile.authority_control)
            self.assertTrue(profile.project_permission_control)
            self.assertTrue(profile.sandbox_state)
            self.assertTrue(profile.limitations)
            self.assertTrue(profile.candidate_review_required)
            self.assertTrue(
                all(source.accessed_on == SOURCE_DATE for source in profile.sources)
            )

    def test_unknown_duplicate_malformed_and_incomplete_profiles_fail_closed(self) -> None:
        cases = (
            ("unknown", lambda payload: payload.update(surface="codex_sdk")),
            ("duplicate", lambda payload: payload.update(surface="codex_cli")),
            ("wrong_kind", lambda payload: payload.update(surface_kind="cli")),
            (
                "unofficial_source",
                lambda payload: payload["sources"][0].update(url="https://example.com/evidence"),
            ),
            ("incomplete", lambda payload: payload.pop("authority_control")),
        )
        for name, mutate in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self._copy_profiles(root)
                target = root / "openai_sdk.json"
                payload = json.loads(target.read_text(encoding="utf-8"))
                mutate(payload)
                target.write_text(json.dumps(payload), encoding="utf-8")
                with self.assertRaises(AdapterEvaluationError):
                    load_adapter_profiles(root, required_access_date=SOURCE_DATE)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._copy_profiles(root)
            (root / "openai_sdk.json").write_text("{not-json", encoding="utf-8")
            with self.assertRaises(AdapterEvaluationError):
                load_adapter_profiles(root, required_access_date=SOURCE_DATE)

    def test_profile_path_escape_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            contained = root / "profiles"
            contained.mkdir()
            escaped = root / "escaped.json"
            escaped.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(AdapterEvaluationError, "escapes"):
                load_adapter_profile(escaped, profile_root=contained)

    def test_current_documentation_blockers_are_non_compensable(self) -> None:
        result = evaluate_adapter_profiles(
            self.profiles,
            self.context,
            required_access_date=SOURCE_DATE,
        )
        by_surface = {item.profile.surface: item for item in result.surfaces}

        self.assertTrue(by_surface[AdapterSurface.CODEX_CLI].eligible)
        self.assertIsNotNone(by_surface[AdapterSurface.CODEX_CLI].score)
        cursor_cli = by_surface[AdapterSurface.CURSOR_CLI]
        self.assertFalse(cursor_cli.eligible)
        self.assertIsNone(cursor_cli.score)
        self.assertIn(HardBlocker.SOURCE_CONTRADICTION, cursor_cli.blockers)
        self.assertIn(HardBlocker.HARD_READ_ONLY_UNPROVEN, cursor_cli.blockers)
        self.assertIn(
            HardBlocker.REPOSITORY_SCOPE_UNBOUNDED,
            by_surface[AdapterSurface.OPENAI_SDK].blockers,
        )
        self.assertIn(
            HardBlocker.TRACE_PRIVACY_UNCLEAR,
            by_surface[AdapterSurface.OPENAI_AGENTS_SDK].blockers,
        )

    def test_stale_source_mutation_cloud_and_governance_gates_are_independent(self) -> None:
        codex = self._profile(AdapterSurface.CODEX_CLI)
        stale_source = replace(codex.sources[0], accessed_on=date(2026, 7, 20))
        variants = (
            (
                replace(codex, sources=(stale_source,)),
                HardBlocker.SOURCE_REVALIDATION_REQUIRED,
            ),
            (
                replace(codex, first_proof_mode=FirstProofMode.MUTATION_CAPABLE),
                HardBlocker.HARD_READ_ONLY_UNPROVEN,
            ),
            (
                replace(codex, first_proof_mode=FirstProofMode.EXTERNALLY_HOSTED),
                HardBlocker.LIVE_ONLY_EVALUATION_REQUIRED,
            ),
            (
                replace(codex, authority_control="missing"),
                HardBlocker.AUTHORITY_OR_PERMISSION_MISSING,
            ),
            (
                replace(codex, project_permission_control="missing"),
                HardBlocker.AUTHORITY_OR_PERMISSION_MISSING,
            ),
            (
                replace(codex, trace_privacy="unclear"),
                HardBlocker.TRACE_PRIVACY_UNCLEAR,
            ),
            (
                replace(codex, candidate_review_required=False),
                HardBlocker.CANDIDATE_REVIEW_BYPASS,
            ),
        )
        for replacement, expected in variants:
            with self.subTest(blocker=expected.value):
                profiles = self._replace_profile(replacement)
                result = evaluate_adapter_profiles(
                    profiles,
                    self.context,
                    required_access_date=SOURCE_DATE,
                )
                evaluated = next(
                    item for item in result.surfaces if item.profile.surface == AdapterSurface.CODEX_CLI
                )
                self.assertFalse(evaluated.eligible)
                self.assertIsNone(evaluated.score)
                self.assertIn(expected, evaluated.blockers)

    def test_recommendation_tie_alternatives_and_input_order_are_deterministic(self) -> None:
        baseline = evaluate_adapter_profiles(
            self.profiles,
            self.context,
            required_access_date=SOURCE_DATE,
        )
        reversed_result = evaluate_adapter_profiles(
            tuple(reversed(self.profiles)),
            self.context,
            required_access_date=SOURCE_DATE,
        )
        self.assertEqual(
            evaluation_result_payload(baseline),
            evaluation_result_payload(reversed_result),
        )
        self.assertEqual(AdapterSurface.CODEX_CLI, baseline.recommended_surface)

        cursor = replace(
            self._profile(AdapterSurface.CURSOR_CLI),
            source_state=SourceState.CURRENT_CONSISTENT,
            first_proof_mode=FirstProofMode.LOCAL_READ_ONLY,
            mutation_controls=("read_only_sandbox",),
            sandbox_state="documented_read_only",
            cost_metadata="provider_reported_or_deferred",
            declared_hard_blockers=(),
        )
        tied = evaluate_adapter_profiles(
            self._replace_profile(cursor),
            self.context,
            required_access_date=SOURCE_DATE,
        )
        self.assertIsNone(tied.recommended_surface)
        self.assertEqual("top_score_tie", tied.recommendation_reason)

        lower_cursor = replace(cursor, cost_metadata="unavailable")
        ranked = evaluate_adapter_profiles(
            self._replace_profile(lower_cursor),
            self.context,
            required_access_date=SOURCE_DATE,
        )
        self.assertEqual(AdapterSurface.CODEX_CLI, ranked.recommended_surface)
        cursor_result = next(
            item for item in ranked.surfaces if item.profile.surface == AdapterSurface.CURSOR_CLI
        )
        self.assertTrue(cursor_result.eligible)
        self.assertLess(cursor_result.score or 0, 100)

    def test_blocked_high_feature_profile_is_never_scored(self) -> None:
        agents = self._profile(AdapterSurface.OPENAI_AGENTS_SDK)
        self.assertTrue(agents.structured_output)
        self.assertTrue(agents.traceability)
        self.assertTrue(agents.session_identity)

        result = evaluate_adapter_profiles(
            self.profiles,
            self.context,
            required_access_date=SOURCE_DATE,
        )
        evaluated = next(
            item
            for item in result.surfaces
            if item.profile.surface == AdapterSurface.OPENAI_AGENTS_SDK
        )
        self.assertFalse(evaluated.eligible)
        self.assertIsNone(evaluated.score)
        self.assertEqual({}, evaluated.score_components)

    def test_agent_context_payload_is_preserved_without_broadening(self) -> None:
        result = evaluate_adapter_profiles(
            self.profiles,
            self.context,
            required_access_date=SOURCE_DATE,
        )
        payload = evaluation_result_payload(result)

        self.assertEqual(self.context, payload["context"])
        self.assertEqual("refreshed", payload["context"]["refresh_state"])
        self.assertEqual(
            "not_visible_to_access_context",
            payload["context"]["graph"]["exclusions"][0]["reason"],
        )
        self.assertEqual(
            {"documents": 3, "memory": 4},
            payload["context"]["budgets"],
        )

    def test_blocked_context_prevents_recommendation(self) -> None:
        blocked = json.loads((FIXTURE_ROOT / "context_blocked.json").read_text(encoding="utf-8"))
        result = evaluate_adapter_profiles(
            self.profiles,
            blocked,
            required_access_date=SOURCE_DATE,
        )
        self.assertIsNone(result.recommended_surface)
        self.assertEqual("context_not_ready", result.recommendation_reason)

    def test_output_is_documentation_only_local_and_non_authorizing(self) -> None:
        payload = evaluation_result_payload(
            evaluate_adapter_profiles(
                self.profiles,
                self.context,
                required_access_date=SOURCE_DATE,
            )
        )
        self.assertEqual("official_documentation", payload["evidence_state"]["kind"])
        self.assertFalse(payload["evidence_state"]["measured_behavior"])
        self.assertFalse(payload["recommendation"]["authorizes_live_use"])
        self.assertFalse(payload["governance"]["project_memory_write_performed"])
        self.assertFalse(payload["governance"]["provider_invocation_record_created"])
        self.assertEqual(
            {
                "provider_invocation_performed": False,
                "credential_or_user_state_read": False,
                "network_call_performed": False,
                "repository_mutation_performed": False,
            },
            payload["side_effects"],
        )
        self.assertNotIn("codex_sdk", {item["surface"] for item in payload["surfaces"]})

    def test_implementation_has_no_provider_network_or_process_import(self) -> None:
        paths = (
            REPO_ROOT / "soane" / "thinking_engine" / "adapter_evaluation.py",
            REPO_ROOT / "soane" / "thinking_engine" / "adapter_evaluation_workflow.py",
        )
        forbidden_roots = {"openai", "cursor", "requests", "httpx", "urllib", "socket", "subprocess"}
        imported_roots: set[str] = set()
        for path in paths:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported_roots.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported_roots.add(node.module.split(".")[0])
        self.assertFalse(imported_roots & forbidden_roots)

    def _profile(self, surface: AdapterSurface):
        return next(item for item in self.profiles if item.surface == surface)

    def _replace_profile(self, replacement):
        return tuple(
            replacement if item.surface == replacement.surface else item
            for item in self.profiles
        )

    @staticmethod
    def _copy_profiles(root: Path) -> None:
        for source in PROFILE_DIR.glob("*.json"):
            (root / source.name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
