from __future__ import annotations

import unittest

from soane.project_memory.adapters import (
    AdapterInvocationStatus,
    AdapterSurface,
    AdapterSurfaceKind,
    AdapterTwin,
    AdapterTwinError,
    default_adapter_twins,
)
from soane.project_memory.contract import (
    LifecycleStatus,
    MemoryObjectType,
    RelationshipType,
    validate_memory_object,
)


class ProjectMemoryAdapterTwinTests(unittest.TestCase):
    def test_default_twins_cover_cursor_codex_and_openai_surfaces(self) -> None:
        twins = default_adapter_twins()
        self.assertEqual(
            {
                AdapterSurface.CURSOR_CLI,
                AdapterSurface.CODEX_CLI,
                AdapterSurface.CURSOR_SDK,
                AdapterSurface.OPENAI_SDK,
                AdapterSurface.OPENAI_AGENTS_SDK,
            },
            set(twins),
        )

    def test_each_twin_records_a_provider_invocation_without_live_calls(self) -> None:
        for surface, twin in default_adapter_twins().items():
            with self.subTest(surface=surface.value):
                result = twin.invoke(
                    purpose="MS-04 adapter contract proof",
                    input_refs=("docs/ROADMAP.md",),
                    output_refs=(f"adapter-output://{surface.value}/proof",),
                    policy_context="mock_first_contract",
                    privacy_classification="project",
                    evidence_refs=("docs/INTEGRATION_ARCHITECTURE.md",),
                    confidence=0.82,
                    cost_estimate={"unit": "mock", "amount": 0},
                    latency_ms=0,
                )
                memory_object = result.to_memory_object(created_by="adapter-twin-test")

                validate_memory_object(memory_object)
                self.assertEqual(AdapterInvocationStatus.ALLOWED, result.status)
                self.assertFalse(result.live_call_performed)
                self.assertEqual(MemoryObjectType.PROVIDER_INVOCATION, memory_object.type)
                self.assertEqual(LifecycleStatus.ACCEPTED, memory_object.status)
                self.assertEqual(surface.value, memory_object.metadata["adapter_surface"])
                self.assertEqual(twin.surface_kind.value, memory_object.metadata["surface_kind"])
                self.assertTrue(memory_object.metadata["adapter_twin"])
                self.assertTrue(memory_object.metadata["mock"])
                self.assertFalse(memory_object.metadata["live_call_performed"])
                self.assertIsNone(memory_object.authority_ref)
                self.assertIn(
                    twin.capability_ref,
                    [
                        relationship.target_id
                        for relationship in memory_object.relationships
                        if relationship.type == RelationshipType.HAS_CAPABILITY
                    ],
                )

    def test_cli_and_sdk_surface_kinds_are_explicit(self) -> None:
        twins = default_adapter_twins()
        self.assertEqual(AdapterSurfaceKind.CLI, twins[AdapterSurface.CURSOR_CLI].surface_kind)
        self.assertEqual(AdapterSurfaceKind.CLI, twins[AdapterSurface.CODEX_CLI].surface_kind)
        self.assertEqual(AdapterSurfaceKind.SDK, twins[AdapterSurface.CURSOR_SDK].surface_kind)
        self.assertEqual(AdapterSurfaceKind.SDK, twins[AdapterSurface.OPENAI_SDK].surface_kind)
        self.assertEqual(AdapterSurfaceKind.SDK, twins[AdapterSurface.OPENAI_AGENTS_SDK].surface_kind)

    def test_missing_authority_denies_authority_required_invocation(self) -> None:
        twin = AdapterTwin(
            surface=AdapterSurface.CODEX_CLI,
            surface_kind=AdapterSurfaceKind.CLI,
            capability_ref="capability://codex-cli/edit-files",
            requires_authority=True,
        )
        result = twin.invoke(
            purpose="edit repository files",
            input_refs=("docs/ROADMAP.md",),
        )
        memory_object = result.to_memory_object()

        self.assertEqual(AdapterInvocationStatus.DENIED, result.status)
        self.assertEqual("missing_authority", result.error_code)
        self.assertEqual(LifecycleStatus.REJECTED, memory_object.status)
        self.assertIsNone(memory_object.authority_ref)
        self.assertEqual("missing_authority", memory_object.metadata["error_code"])
        self.assertEqual("capability://codex-cli/edit-files", memory_object.metadata["capability_ref"])

    def test_present_authority_is_recorded_separately_from_capability(self) -> None:
        twin = AdapterTwin(
            surface=AdapterSurface.CURSOR_CLI,
            surface_kind=AdapterSurfaceKind.CLI,
            capability_ref="capability://cursor-cli/edit-files",
            requires_authority=True,
        )
        result = twin.invoke(
            purpose="edit repository files",
            input_refs=("docs/ROADMAP.md",),
            authority_ref="authority://human-go/MS-04",
        )
        memory_object = result.to_memory_object()

        self.assertEqual(AdapterInvocationStatus.ALLOWED, result.status)
        self.assertEqual(LifecycleStatus.ACCEPTED, memory_object.status)
        self.assertEqual("authority://human-go/MS-04", memory_object.authority_ref)
        self.assertEqual("capability://cursor-cli/edit-files", memory_object.metadata["capability_ref"])
        self.assertEqual("authority://human-go/MS-04", memory_object.metadata["authority_ref"])
        self.assertIn(
            "authority://human-go/MS-04",
            [
                relationship.target_id
                for relationship in memory_object.relationships
                if relationship.type == RelationshipType.HAS_AUTHORITY
            ],
        )

    def test_unavailable_twin_records_unavailable_result_without_live_call(self) -> None:
        twin = AdapterTwin(
            surface=AdapterSurface.OPENAI_SDK,
            surface_kind=AdapterSurfaceKind.SDK,
            capability_ref="capability://openai-sdk/model-tool-invocation",
            available=False,
        )
        result = twin.invoke(
            purpose="model tool invocation",
            input_refs=("docs/INTEGRATION_ARCHITECTURE.md",),
        )
        memory_object = result.to_memory_object()

        self.assertEqual(AdapterInvocationStatus.UNAVAILABLE, result.status)
        self.assertEqual("adapter_surface_unavailable", result.error_code)
        self.assertEqual(LifecycleStatus.REJECTED, memory_object.status)
        self.assertFalse(memory_object.metadata["live_call_performed"])

    def test_blank_purpose_is_rejected_before_memory_object_creation(self) -> None:
        twin = default_adapter_twins()[AdapterSurface.OPENAI_AGENTS_SDK]
        with self.assertRaises(AdapterTwinError):
            twin.invoke(purpose=" ")


if __name__ == "__main__":
    unittest.main()
