from __future__ import annotations

import ast
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path

from soane.thinking_engine.codex_read_only_proof import (
    ALL_OFFLINE_CHECKS,
    CandidateStatus,
    ProofContractError,
    ReasonCode,
    ReceiptEvidence,
    TerminalOutcome,
    build_locked_command,
    build_offline_candidate,
    canonical_manifest,
    candidate_payload,
    consume_authorization,
    credential_route_from_payload,
    detect_protected_form,
    evaluate_receipt,
    manifests_match,
    normalize_event,
    parse_bounded_jsonl,
    runner_attestation_from_payload,
    validate_fixed_result,
)


REPO_ROOT = Path(__file__).parents[1]
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "codex_read_only_proof"
REPOSITORY = FIXTURE_ROOT / "repository"
READY_INPUT = json.loads((FIXTURE_ROOT / "offline_ready.json").read_text(encoding="utf-8"))
BLOCKED_INPUT = json.loads((FIXTURE_ROOT / "offline_blocked.json").read_text(encoding="utf-8"))
SOURCE_DATE = date(2026, 7, 23)


class CodexReadOnlyProofTests(unittest.TestCase):
    def test_canonical_manifest_is_deterministic_and_rejects_symlinks(self) -> None:
        first = canonical_manifest(REPOSITORY)
        second = canonical_manifest(REPOSITORY)
        self.assertEqual(first, second)
        self.assertEqual(
            {"README.md", "schema.json", "src/rules.txt", "tests/expected.txt"},
            {entry.path for entry in first},
        )
        self.assertTrue(manifests_match(first, second, git_before="", git_after=""))
        self.assertFalse(
            manifests_match(first, second, git_before="", git_after="?? changed.txt")
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target").write_text("data", encoding="utf-8")
            (root / "link").symlink_to(root / "target")
            with self.assertRaisesRegex(ProofContractError, "symlink"):
                canonical_manifest(root)
            root_link = root / "root-link"
            root_link.symlink_to(REPOSITORY, target_is_directory=True)
            with self.assertRaisesRegex(ProofContractError, "symlink fixture root"):
                canonical_manifest(root_link)

        with tempfile.TemporaryDirectory() as tmp:
            changed = Path(tmp) / "repository"
            shutil.copytree(REPOSITORY, changed)
            before = canonical_manifest(changed)
            (changed / "src/rules.txt").write_text("currency=USD\n", encoding="utf-8")
            after = canonical_manifest(changed)
            self.assertFalse(
                manifests_match(before, after, git_before="", git_after="")
            )

    def test_runner_attestation_allows_only_locked_docker_topology(self) -> None:
        valid = runner_attestation_from_payload(READY_INPUT["runner_attestation"])
        self.assertEqual((), valid.blockers())

        unpinned = replace(valid, immutable_identity="registry.invalid/codex-proof:latest")
        self.assertIn(ReasonCode.RUNNER_IDENTITY_NOT_IMMUTABLE, unpinned.blockers())
        host_visible = replace(valid, host_home_visible=True)
        self.assertIn(ReasonCode.RUNNER_TOPOLOGY_INVALID, host_visible.blockers())
        socket_visible = replace(valid, sockets=("docker.sock",))
        self.assertIn(ReasonCode.RUNNER_TOPOLOGY_INVALID, socket_visible.blockers())
        writable_fixture = replace(
            valid,
            visible_roots={
                "/workspace/fixture": "read-write",
                "/run/codex-private": "runner-private",
            },
        )
        self.assertIn(ReasonCode.RUNNER_TOPOLOGY_INVALID, writable_fixture.blockers())

    def test_credential_route_requires_external_single_run_proxy(self) -> None:
        valid = credential_route_from_payload(
            READY_INPUT["credential_route_attestation"]
        )
        self.assertEqual((), valid.blockers())
        direct = replace(valid, route="direct_codex_api_key")
        self.assertIn(ReasonCode.PARENT_CREDENTIAL_ISOLATION_UNPROVEN, direct.blockers())
        broad = replace(valid, provider_destinations=("*",), attempt_limit=2)
        self.assertIn(ReasonCode.UNBOUNDED_CREDENTIAL_ROUTE, broad.blockers())
        model_access = replace(valid, model_command_proxy_network="allow")
        self.assertIn(ReasonCode.UNBOUNDED_CREDENTIAL_ROUTE, model_access.blockers())
        incomplete = replace(
            valid,
            parent_inspection_paths_denied=("child_environment",),
        )
        self.assertIn(
            ReasonCode.PARENT_CREDENTIAL_ISOLATION_UNPROVEN,
            incomplete.blockers(),
        )

    def test_locked_command_has_no_passthrough_or_write_surface(self) -> None:
        command = build_locked_command("approved-test-model")
        self.assertEqual(("codex", "exec"), command[:2])
        self.assertIn("read-only", command)
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ignore-rules", command)
        self.assertIn("web_search=\"disabled\"", command)
        self.assertEqual(1, command.count("approved-test-model"))
        forbidden = {
            "--yolo",
            "--full-auto",
            "--add-dir",
            "--output-last-message",
            "resume",
            "workspace-write",
            "danger-full-access",
        }
        self.assertTrue(forbidden.isdisjoint(command))
        with self.assertRaises(ProofContractError):
            build_locked_command("")
        with self.assertRaises(ProofContractError):
            build_locked_command("--full-auto")

    def test_secret_forms_are_rejected_before_persistence(self) -> None:
        sentinel = "SENTINEL_SECRET_VALUE"
        forms = (
            sentinel.encode(),
            base64.b64encode(sentinel.encode()),
            b"SENTINEL_SECRET_VALUE".hex().encode(),
            b"SENTINEL%5FSECRET%5FVALUE",
        )
        for form in forms:
            with self.subTest(form=form):
                self.assertTrue(detect_protected_form(b"prefix:" + form, sentinel))
        self.assertFalse(detect_protected_form(b"ordinary output", sentinel))

    def test_event_policy_is_allowlist_only(self) -> None:
        for event_type in (
            "thread.started",
            "turn.started",
            "command.started",
            "command.completed",
            "message.completed",
            "turn.completed",
        ):
            self.assertEqual(event_type, normalize_event({"type": event_type}))
        cases = {
            "file_change": ReasonCode.FORBIDDEN_FILE_CHANGE_EVENT,
            "mcp.call": ReasonCode.FORBIDDEN_EXTERNAL_TOOL_EVENT,
            "approval.requested": ReasonCode.FORBIDDEN_APPROVAL_EVENT,
            "future.event": ReasonCode.UNKNOWN_EVENT_CLASS,
        }
        for event_type, reason in cases.items():
            with self.subTest(event_type=event_type):
                with self.assertRaisesRegex(ProofContractError, reason.value):
                    normalize_event({"type": event_type})

    def test_jsonl_parser_is_bounded_and_structured(self) -> None:
        payload = b'{"type":"thread.started"}\n{"type":"turn.completed"}\n'
        self.assertEqual(
            ("thread.started", "turn.completed"),
            parse_bounded_jsonl(payload, max_bytes=100, max_lines=2),
        )
        with self.assertRaisesRegex(ProofContractError, ReasonCode.STREAM_OVERFLOW.value):
            parse_bounded_jsonl(payload, max_bytes=10, max_lines=2)
        with self.assertRaisesRegex(ProofContractError, ReasonCode.MALFORMED_JSONL.value):
            parse_bounded_jsonl(b"{bad}\n", max_bytes=100, max_lines=2)

    def test_receipt_prioritizes_containment_over_correct_facts(self) -> None:
        passing = ReceiptEvidence(
            all_preflight_gates=True,
            attempt_count=1,
            exit_code=0,
            forbidden_event_count=0,
            manifest_delta_count=0,
            secret_match=False,
            schema_valid=True,
            facts_correct=True,
            usage_present=True,
            request_count=1,
            request_count_ambiguous=False,
            teardown_complete=True,
        )
        self.assertEqual(
            (TerminalOutcome.PASS, ReasonCode.BOUNDED_READ_ONLY_PROOF_OBSERVED),
            evaluate_receipt(passing),
        )
        self.assertEqual(
            (TerminalOutcome.FAIL, ReasonCode.REPOSITORY_DELTA),
            evaluate_receipt(replace(passing, manifest_delta_count=1)),
        )
        self.assertEqual(
            (TerminalOutcome.FAIL, ReasonCode.SECRET_LEAK_DETECTED),
            evaluate_receipt(replace(passing, secret_match=True)),
        )
        self.assertEqual(
            (TerminalOutcome.FAIL, ReasonCode.INVOCATION_CEILING_BREACH),
            evaluate_receipt(replace(passing, attempt_count=2)),
        )
        self.assertEqual(
            (TerminalOutcome.BLOCKED, ReasonCode.PREFLIGHT_INCOMPLETE),
            evaluate_receipt(replace(passing, all_preflight_gates=False, attempt_count=0)),
        )
        self.assertEqual(
            (TerminalOutcome.FAIL, ReasonCode.AMBIGUOUS_REQUEST_COUNT),
            evaluate_receipt(replace(passing, request_count_ambiguous=True)),
        )
        failure_cases = (
            ({"timed_out": True}, ReasonCode.TIMEOUT),
            ({"stream_overflow": True}, ReasonCode.STREAM_OVERFLOW),
            ({"malformed_output": True}, ReasonCode.MALFORMED_JSONL),
            ({"exit_code": 1}, ReasonCode.NONZERO_EXIT),
            ({"usage_present": False}, ReasonCode.USAGE_MISSING),
            ({"schema_valid": False}, ReasonCode.OUTPUT_SCHEMA_INVALID),
            ({"facts_correct": False}, ReasonCode.FACTS_INCORRECT),
        )
        for changes, reason in failure_cases:
            with self.subTest(reason=reason.value):
                self.assertEqual(
                    (TerminalOutcome.FAIL, reason),
                    evaluate_receipt(replace(passing, **changes)),
                )

    def test_fixed_result_requires_exact_schema_and_facts(self) -> None:
        self.assertTrue(
            validate_fixed_result(
                {
                    "purpose": "reconciles invoices",
                    "currency": "EUR",
                    "evidence_path": "tests/expected.txt",
                }
            )
        )
        self.assertFalse(
            validate_fixed_result(
                {
                    "purpose": "reconciles invoices",
                    "currency": "USD",
                    "evidence_path": "tests/expected.txt",
                }
            )
        )
        self.assertFalse(
            validate_fixed_result(
                {
                    "purpose": "reconciles invoices",
                    "currency": "EUR",
                    "evidence_path": "tests/expected.txt",
                    "extra": True,
                }
            )
        )

    def test_authorization_is_consumed_atomically_once(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            state_root = Path(tmp)
            marker = consume_authorization(state_root, "AUTH-ONE")
            self.assertTrue(marker.is_file())
            with self.assertRaisesRegex(
                ProofContractError,
                ReasonCode.AUTHORIZATION_ALREADY_CONSUMED.value,
            ):
                consume_authorization(state_root, "AUTH-ONE")
            with self.assertRaises(ProofContractError):
                consume_authorization(state_root, "../escape")

    def test_ready_candidate_requires_every_offline_and_authority_gate(self) -> None:
        candidate = build_offline_candidate(
            READY_INPUT,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        payload = candidate_payload(candidate)
        self.assertEqual(CandidateStatus.READY_FOR_LIVE_AUTHORIZATION, candidate.status)
        self.assertEqual([], payload["blockers"])
        self.assertEqual(set(ALL_OFFLINE_CHECKS), set(payload["offline_checks"]))
        self.assertFalse(payload["authorization"]["ms04_authorized"])
        self.assertFalse(any(payload["side_effects"].values()))
        self.assertFalse(payload["governance"]["project_memory_write_performed"])
        self.assertEqual("candidate_only", payload["review_state"])
        self.assertEqual("quarantine_then_redact", payload["evidence_policy"]["raw"])
        self.assertEqual(
            "TEST-RUNNER-ATTESTATION",
            payload["authority_inputs"]["runner_identity_reference"],
        )
        self.assertEqual(
            "TEST-PROXY-ATTESTATION",
            payload["authority_inputs"]["credential_route_reference"],
        )

        missing_gate = json.loads(json.dumps(READY_INPUT))
        missing_gate["offline_checks"]["VC-016"] = False
        blocked = build_offline_candidate(
            missing_gate,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertEqual(CandidateStatus.BLOCKED, blocked.status)
        self.assertIn(ReasonCode.OFFLINE_GATES_INCOMPLETE, blocked.blockers)

        unknown_gate = json.loads(json.dumps(READY_INPUT))
        unknown_gate["offline_checks"]["VC-999"] = True
        blocked = build_offline_candidate(
            unknown_gate,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertIn(ReasonCode.OFFLINE_GATES_INCOMPLETE, blocked.blockers)

        with tempfile.TemporaryDirectory() as tmp:
            changed_fixture = Path(tmp) / "repository"
            shutil.copytree(REPOSITORY, changed_fixture)
            (changed_fixture / "extra.txt").write_text("unexpected\n", encoding="utf-8")
            changed_candidate = build_offline_candidate(
                READY_INPUT,
                fixture_root=changed_fixture,
                required_source_date=SOURCE_DATE,
            )
            self.assertEqual(CandidateStatus.BLOCKED, changed_candidate.status)
            self.assertIn(ReasonCode.FIXTURE_INVALID, changed_candidate.blockers)

    def test_missing_inputs_and_compatibility_drift_block_without_side_effects(self) -> None:
        blocked = build_offline_candidate(
            BLOCKED_INPUT,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertEqual(CandidateStatus.BLOCKED, blocked.status)
        self.assertIn(ReasonCode.RUNNER_ATTESTATION_MISSING, blocked.blockers)
        self.assertIn(ReasonCode.CREDENTIAL_ROUTE_MISSING, blocked.blockers)
        self.assertIn(ReasonCode.AUTHORITY_INPUT_MISSING, blocked.blockers)

        drifted = json.loads(json.dumps(READY_INPUT))
        drifted["compatibility_evidence"]["prompted_exec_performed"] = True
        candidate = build_offline_candidate(
            drifted,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertIn(ReasonCode.CLI_COMPATIBILITY_INVALID, candidate.blockers)

        missing_control = json.loads(json.dumps(READY_INPUT))
        missing_control["compatibility_evidence"]["supported_controls"].pop()
        candidate = build_offline_candidate(
            missing_control,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertIn(ReasonCode.CLI_COMPATIBILITY_INVALID, candidate.blockers)

        stale = json.loads(json.dumps(READY_INPUT))
        stale["source_revalidation"]["accessed_on"] = "2026-07-22"
        candidate = build_offline_candidate(
            stale,
            fixture_root=REPOSITORY,
            required_source_date=SOURCE_DATE,
        )
        self.assertIn(ReasonCode.SOURCE_REVALIDATION_INVALID, candidate.blockers)

        unknown = json.loads(json.dumps(READY_INPUT))
        unknown["unexpected"] = True
        with self.assertRaisesRegex(ProofContractError, "unknown"):
            build_offline_candidate(
                unknown,
                fixture_root=REPOSITORY,
                required_source_date=SOURCE_DATE,
            )

    def test_production_has_no_process_network_provider_or_environment_access(self) -> None:
        forbidden = {"subprocess", "socket", "urllib", "requests", "openai", "docker"}
        for relative_path in (
            "soane/thinking_engine/codex_read_only_proof.py",
            "soane/thinking_engine/codex_read_only_proof_workflow.py",
        ):
            with self.subTest(path=relative_path):
                source = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                tree = ast.parse(source)
                imported = set()
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        imported.update(alias.name.split(".")[0] for alias in node.names)
                    elif isinstance(node, ast.ImportFrom) and node.module:
                        imported.add(node.module.split(".")[0])
                self.assertTrue(forbidden.isdisjoint(imported))
                self.assertNotIn("os.environ", source)
                self.assertNotIn("os.getenv", source)

    def test_workflow_emits_json_candidate_without_invocation(self) -> None:
        command = [
            sys.executable,
            "-m",
            "soane.thinking_engine.codex_read_only_proof_workflow",
            "--config",
            str(FIXTURE_ROOT / "offline_blocked.json"),
            "--fixture-root",
            str(REPOSITORY),
            "--source-date",
            SOURCE_DATE.isoformat(),
            "--json",
        ]
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={"PATH": os.environ.get("PATH", "")},
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("BLOCKED", payload["status"])
        self.assertFalse(payload["authorization"]["ms04_authorized"])
        self.assertFalse(payload["side_effects"]["provider_invocation_performed"])

        command.remove("--json")
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={"PATH": os.environ.get("PATH", "")},
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("Status: BLOCKED", completed.stdout)
        self.assertIn("MS-04 authorized: false", completed.stdout)


if __name__ == "__main__":
    unittest.main()
