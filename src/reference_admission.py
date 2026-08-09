"""SCOBY-D0 v0.6 authoritative dataset-observation admission.

Authority here means evidence-ingestion authority inside SCOBY-D0 only.
It does not mean a universal human reference standard, biological truth,
clinical validation, safety, efficacy, or independent biological replication.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

from extraction_lineage import normalized_matches_replay, stable_source_id, validate_extraction_record


def _missing(v: Any) -> bool:
    return v is None or v == "" or v == [] or v == {}


def validate_representation_provenance(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    provenance = record.get("extraction_provenance") or {}
    for key in ("representation_id", "representation_role", "provider", "format",
                "stable_locator", "process_family", "process_id"):
        if _missing(provenance.get(key)):
            errors.append(f"MISSING_EXTRACTION_PROVENANCE_{key.upper()}")
    return sorted(set(errors))


def semantic_observation_payload(record: dict[str, Any]) -> dict[str, Any]:
    """Representation-independent semantics used for A/B comparison."""
    return {
        "stable_source_id": stable_source_id(record["source_identity"]),
        "observation_id": record["observation_id"],
        "reported_observation": deepcopy(record["reported_observation"]),
        "context": deepcopy(record["context"]),
        "normalized_observation": deepcopy(record["normalized_observation"]),
    }


def compare_cross_representation_extractions(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    if validate_extraction_record(a) or validate_extraction_record(b):
        return {"status": "INVALID_EXTRACTION_RECORD", "authoritative_admission": "BLOCKED"}
    if validate_representation_provenance(a) or validate_representation_provenance(b):
        return {"status": "INVALID_REPRESENTATION_PROVENANCE", "authoritative_admission": "BLOCKED"}
    if not normalized_matches_replay(a) or not normalized_matches_replay(b):
        return {"status": "NORMALIZATION_REPLAY_FAIL", "authoritative_admission": "BLOCKED"}
    if a.get("extractor_id") == b.get("extractor_id"):
        return {"status": "NOT_SEPARATE_EXTRACTOR_IDS", "authoritative_admission": "BLOCKED"}

    pa, pb = a["extraction_provenance"], b["extraction_provenance"]
    if pa["representation_id"] == pb["representation_id"]:
        return {"status": "NOT_DISTINCT_SOURCE_REPRESENTATIONS", "authoritative_admission": "BLOCKED"}
    if pa["process_family"] == pb["process_family"]:
        return {"status": "NOT_DISTINCT_PROCESS_FAMILIES", "authoritative_admission": "BLOCKED"}
    if stable_source_id(a["source_identity"]) != stable_source_id(b["source_identity"]):
        return {"status": "PRIMARY_SOURCE_IDENTITY_MISMATCH", "authoritative_admission": "BLOCKED"}

    left = semantic_observation_payload(a)
    right = semantic_observation_payload(b)
    if left != right:
        return {
            "status": "EXTRACTION_CONFLICT_PRESERVED",
            "authoritative_admission": "BLOCKED",
            "left": left,
            "right": right,
        }

    return {
        "status": "CROSS_REPRESENTATION_EXTRACTION_MATCH",
        "authoritative_admission": "ELIGIBLE_FOR_V0_6_INGESTION_AUTHORITY",
        "representation_A": pa["representation_id"],
        "representation_B": pb["representation_id"],
        "process_family_A": pa["process_family"],
        "process_family_B": pb["process_family"],
        "semantic_observation": left,
    }


def admit_dataset_observation(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    comparison = compare_cross_representation_extractions(a, b)
    if comparison["status"] != "CROSS_REPRESENTATION_EXTRACTION_MATCH":
        return {
            "status": "ADMISSION_BLOCKED",
            "reason": comparison["status"],
            "authoritative_observation": False,
            "biological_reference_standard": "NOT_ESTABLISHED",
            "biological_reference_vector": "UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW",
        }
    return {
        "status": "AUTHORITATIVE_DATASET_OBSERVATION_ADMITTED",
        "authority_scope": "SCOBY_D0_EVIDENCE_INGESTION_ONLY",
        "authoritative_observation": True,
        "observation": comparison["semantic_observation"],
        "cross_representation_receipt": {
            "representation_A": comparison["representation_A"],
            "representation_B": comparison["representation_B"],
            "process_family_A": comparison["process_family_A"],
            "process_family_B": comparison["process_family_B"],
        },
        "biological_reference_standard": "NOT_ESTABLISHED",
        "external_review": "NOT_YET_ESTABLISHED",
        "biological_reference_vector": "UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW",
        "pareto_search": "BLOCKED_UNTIL_V0_7_AND_MULTIPLE_CONTEXT_OBSERVATIONS",
    }
