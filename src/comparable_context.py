"""SCOBY-D0 v0.6.2 comparable-context qualification gate.

This module qualifies whether observations from independent primary studies
have exactly compatible context keys. It never pools or averages values.
"""
from __future__ import annotations
from collections import defaultdict
from typing import Any

KEY_FIELDS = (
    "population_health_class",
    "specimen",
    "route_or_exposure",
    "fasting_duration",
    "tracer_state",
    "analyte",
    "metric",
    "units",
    "uncertainty_semantics",
)

UNRESOLVED_PREFIXES = ("UNRESOLVED", "UNKNOWN", "NOT_ESTABLISHED")


def stable_study_id(candidate: dict[str, Any]) -> tuple[str, str]:
    source = candidate.get("source") or {}
    if source.get("pmid"):
        return ("PMID", str(source["pmid"]))
    if source.get("doi"):
        return ("DOI", str(source["doi"]))
    raise ValueError("MISSING_STABLE_PRIMARY_SOURCE_ID")


def exact_comparability_key(candidate: dict[str, Any]) -> tuple[str, ...]:
    key = candidate.get("comparability_key") or {}
    values = []
    for field in KEY_FIELDS:
        value = key.get(field)
        if not isinstance(value, str) or not value:
            raise ValueError(f"MISSING_COMPARABILITY_FIELD:{field}")
        values.append(value)
    return tuple(values)


def unresolved_key_fields(candidate: dict[str, Any]) -> list[str]:
    key = candidate.get("comparability_key") or {}
    unresolved = []
    for field in KEY_FIELDS:
        value = key.get(field)
        if not isinstance(value, str) or not value or value.startswith(UNRESOLVED_PREFIXES):
            unresolved.append(field)
    return unresolved


def candidate_is_qualifiable(candidate: dict[str, Any]) -> bool:
    if candidate.get("ingestion_status") == "CANDIDATE_BLOCKED":
        return False
    if candidate.get("blockers"):
        return False
    if unresolved_key_fields(candidate):
        return False
    stable_study_id(candidate)
    exact_comparability_key(candidate)
    return True


def qualify_comparable_buckets(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    buckets: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    blocked = []
    for candidate in candidates:
        if not candidate_is_qualifiable(candidate):
            blocked.append(candidate["candidate_id"])
            continue
        buckets[exact_comparability_key(candidate)].append(candidate)

    ready = []
    for key, members in buckets.items():
        studies = {stable_study_id(x) for x in members}
        if len(studies) >= 2:
            ready.append({
                "comparability_key": dict(zip(KEY_FIELDS, key)),
                "independent_primary_study_count": len(studies),
                "candidate_ids": [x["candidate_id"] for x in members],
                "status": "COMPARABLE_READY_NOT_POOLED",
            })

    return {
        "comparable_ready_bucket_count": len(ready),
        "ready_buckets": ready,
        "blocked_candidate_ids": blocked,
        "pooled_reference_created": False,
        "averaging_performed": False,
        "biological_reference_vector": "UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW",
        "pareto_search": "BLOCKED",
    }


def assert_no_pooling(result: dict[str, Any]) -> None:
    if result.get("pooled_reference_created") is not False:
        raise AssertionError("V0_6_2_MUST_NOT_CREATE_POOLED_REFERENCE")
    if result.get("averaging_performed") is not False:
        raise AssertionError("V0_6_2_MUST_NOT_AVERAGE")
    if not str(result.get("biological_reference_vector", "")).startswith("UNSET"):
        raise AssertionError("BIOLOGICAL_REFERENCE_VECTOR_MUST_STAY_UNSET")
    if result.get("pareto_search") != "BLOCKED":
        raise AssertionError("PARETO_MUST_STAY_BLOCKED")
