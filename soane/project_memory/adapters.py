"""Deterministic adapter twins for Project Memory provider invocations.

Adapter twins are contract fixtures, not live integrations. They model the
metadata Soane must preserve when a future Cursor, Codex, or OpenAI adapter is
invoked, while keeping Project Memory tests deterministic and offline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from hashlib import sha256
from typing import Mapping

from soane.project_memory.contract import (
    CONTRACT_VERSION,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    utc_now,
    validate_memory_object,
)


class AdapterTwinError(ValueError):
    """Raised when an adapter twin invocation violates the local contract."""


class AdapterSurface(StrEnum):
    CURSOR_CLI = "cursor_cli"
    CODEX_CLI = "codex_cli"
    CURSOR_SDK = "cursor_sdk"
    OPENAI_SDK = "openai_sdk"
    OPENAI_AGENTS_SDK = "openai_agents_sdk"


class AdapterSurfaceKind(StrEnum):
    CLI = "cli"
    SDK = "sdk"


class AdapterInvocationStatus(StrEnum):
    ALLOWED = "allowed"
    DENIED = "denied"
    UNAVAILABLE = "unavailable"
    FAILED = "failed"


@dataclass(frozen=True)
class AdapterTwinInvocation:
    """Resolved invocation metadata for a deterministic adapter twin."""

    surface: AdapterSurface
    surface_kind: AdapterSurfaceKind
    purpose: str
    input_refs: tuple[str, ...]
    output_refs: tuple[str, ...]
    policy_context: str
    privacy_classification: str
    capability_ref: str
    authority_ref: str | None = None
    evidence_refs: tuple[str, ...] = ()
    confidence: float | None = None
    cost_estimate: Mapping[str, object] = field(default_factory=dict)
    latency_ms: int = 0


@dataclass(frozen=True)
class AdapterTwinResult:
    """Deterministic result emitted by an adapter twin."""

    invocation: AdapterTwinInvocation
    status: AdapterInvocationStatus
    error_code: str | None = None
    live_call_performed: bool = False

    def to_memory_object(self, *, created_by: str = "adapter-twin") -> MemoryObject:
        """Return a provider invocation Project Memory object."""

        _require(created_by.strip(), "created_by is required")
        memory_status = LifecycleStatus.ACCEPTED
        if self.status != AdapterInvocationStatus.ALLOWED:
            memory_status = LifecycleStatus.REJECTED

        relationships = [
            Relationship(
                type=RelationshipType.HAS_CAPABILITY,
                target_id=self.invocation.capability_ref,
            )
        ]
        if self.invocation.authority_ref:
            relationships.append(
                Relationship(
                    type=RelationshipType.HAS_AUTHORITY,
                    target_id=self.invocation.authority_ref,
                )
            )
        relationships.extend(
            Relationship(type=RelationshipType.EVIDENCES, target_id=evidence_ref)
            for evidence_ref in self.invocation.evidence_refs
        )

        title = f"{self.invocation.surface.value} adapter twin invocation: {self.invocation.purpose}"
        memory_object = MemoryObject(
            id=_deterministic_invocation_id(self),
            type=MemoryObjectType.PROVIDER_INVOCATION,
            title=title,
            status=memory_status,
            visibility=Visibility.PROJECT,
            provenance=Provenance(
                source_refs=(f"adapter-twin://{self.invocation.surface.value}",),
                created_by=created_by,
                created_at=utc_now(),
                evidence_level=EvidenceLevel.E3_MECHANICAL_VERIFICATION,
                derivation_refs=self.invocation.input_refs,
            ),
            relationships=tuple(relationships),
            authority_ref=self.invocation.authority_ref,
            confidence=self.invocation.confidence,
            metadata={
                "adapter_surface": self.invocation.surface.value,
                "surface_kind": self.invocation.surface_kind.value,
                "purpose": self.invocation.purpose,
                "input_refs": list(self.invocation.input_refs),
                "output_refs": list(self.invocation.output_refs),
                "policy_context": self.invocation.policy_context,
                "privacy_classification": self.invocation.privacy_classification,
                "capability_ref": self.invocation.capability_ref,
                "authority_ref": self.invocation.authority_ref,
                "evidence_refs": list(self.invocation.evidence_refs),
                "cost_estimate": dict(self.invocation.cost_estimate),
                "latency_ms": self.invocation.latency_ms,
                "adapter_status": self.status.value,
                "error_code": self.error_code,
                "mock": True,
                "adapter_twin": True,
                "live_call_performed": self.live_call_performed,
            },
        )
        validate_memory_object(memory_object)
        return memory_object


@dataclass(frozen=True)
class AdapterTwin:
    """A local deterministic stand-in for a future live adapter surface."""

    surface: AdapterSurface
    surface_kind: AdapterSurfaceKind
    capability_ref: str
    available: bool = True
    requires_authority: bool = False

    def invoke(
        self,
        *,
        purpose: str,
        input_refs: tuple[str, ...] = (),
        output_refs: tuple[str, ...] = (),
        policy_context: str = "project_default",
        privacy_classification: str = "project",
        authority_ref: str | None = None,
        evidence_refs: tuple[str, ...] = (),
        confidence: float | None = None,
        cost_estimate: Mapping[str, object] | None = None,
        latency_ms: int = 0,
    ) -> AdapterTwinResult:
        """Record an invocation outcome without calling the live surface."""

        invocation = AdapterTwinInvocation(
            surface=self.surface,
            surface_kind=self.surface_kind,
            purpose=purpose,
            input_refs=tuple(input_refs),
            output_refs=tuple(output_refs),
            policy_context=policy_context,
            privacy_classification=privacy_classification,
            capability_ref=self.capability_ref,
            authority_ref=authority_ref,
            evidence_refs=tuple(evidence_refs),
            confidence=confidence,
            cost_estimate=cost_estimate or {},
            latency_ms=latency_ms,
        )
        _validate_invocation(invocation)

        if not self.available:
            return AdapterTwinResult(
                invocation=invocation,
                status=AdapterInvocationStatus.UNAVAILABLE,
                error_code="adapter_surface_unavailable",
            )
        if self.requires_authority and not authority_ref:
            return AdapterTwinResult(
                invocation=invocation,
                status=AdapterInvocationStatus.DENIED,
                error_code="missing_authority",
            )
        return AdapterTwinResult(invocation=invocation, status=AdapterInvocationStatus.ALLOWED)


def default_adapter_twins() -> Mapping[AdapterSurface, AdapterTwin]:
    """Return the canonical MS-04 local adapter twin set."""

    return {
        AdapterSurface.CURSOR_CLI: AdapterTwin(
            surface=AdapterSurface.CURSOR_CLI,
            surface_kind=AdapterSurfaceKind.CLI,
            capability_ref="capability://cursor-cli/coding-harness",
        ),
        AdapterSurface.CODEX_CLI: AdapterTwin(
            surface=AdapterSurface.CODEX_CLI,
            surface_kind=AdapterSurfaceKind.CLI,
            capability_ref="capability://codex-cli/coding-harness",
        ),
        AdapterSurface.CURSOR_SDK: AdapterTwin(
            surface=AdapterSurface.CURSOR_SDK,
            surface_kind=AdapterSurfaceKind.SDK,
            capability_ref="capability://cursor-sdk/coding-harness",
        ),
        AdapterSurface.OPENAI_SDK: AdapterTwin(
            surface=AdapterSurface.OPENAI_SDK,
            surface_kind=AdapterSurfaceKind.SDK,
            capability_ref="capability://openai-sdk/model-tool-invocation",
        ),
        AdapterSurface.OPENAI_AGENTS_SDK: AdapterTwin(
            surface=AdapterSurface.OPENAI_AGENTS_SDK,
            surface_kind=AdapterSurfaceKind.SDK,
            capability_ref="capability://openai-agents-sdk/agent-orchestration",
        ),
    }


def _validate_invocation(invocation: AdapterTwinInvocation) -> None:
    _require(invocation.purpose.strip(), "purpose is required")
    _require(invocation.policy_context.strip(), "policy_context is required")
    _require(invocation.privacy_classification.strip(), "privacy_classification is required")
    _require(invocation.capability_ref.strip(), "capability_ref is required")
    _require(invocation.latency_ms >= 0, "latency_ms must not be negative")
    if invocation.confidence is not None:
        _require(0.0 <= invocation.confidence <= 1.0, "confidence must be between 0 and 1")
    for ref in (*invocation.input_refs, *invocation.output_refs, *invocation.evidence_refs):
        _require(ref.strip(), "references must not be blank")
    if invocation.authority_ref is not None:
        _require(invocation.authority_ref.strip(), "authority_ref must not be blank")


def _deterministic_invocation_id(result: AdapterTwinResult) -> str:
    invocation = result.invocation
    seed_parts = (
        CONTRACT_VERSION,
        "adapter-twin",
        invocation.surface.value,
        invocation.surface_kind.value,
        invocation.purpose,
        "|".join(invocation.input_refs),
        "|".join(invocation.output_refs),
        invocation.policy_context,
        invocation.privacy_classification,
        invocation.capability_ref,
        invocation.authority_ref or "",
        "|".join(invocation.evidence_refs),
        result.status.value,
        result.error_code or "",
    )
    seed = ":".join(seed_parts).strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"pmem_{MemoryObjectType.PROVIDER_INVOCATION.value}_{digest}"


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AdapterTwinError(message)
