"""SCOBY-D0 v0.6.3 cross-study independence and pre-analytic hardening.

The module can mark a set of studies COMPARABLE_READY_NOT_POOLED only when
both biological/measurement context and cohort-independence requirements pass.
It never computes a pooled reference or biological optimum.
"""
from __future__ import annotations
from collections import defaultdict
from typing import Any

BASE_FIELDS = (
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
HARDENING_FIELDS = (
    "preanalytic_handling",
    "analytical_method_family",
)
ALL_FIELDS = BASE_FIELDS + HARDENING_FIELDS

COHORT_DISTINCT = "DISTINCT_COHORT_ESTABLISHED"
COHORT_OVERLAP = "PARTICIPANT_OVERLAP_CONFIRMED"
COHORT_UNRESOLVED = "PARTICIPANT_OVERLAP_UNRESOLVED"
VALID_COHORT_STATES = {COHORT_DISTINCT, COHORT_OVERLAP, COHORT_UNRESOLVED}
UNRESOLVED_PREFIXES = ("UNRESOLVED", "UNKNOWN", "NOT_ESTABLISHED")


def _source_id(record: dict[str, Any]) -> tuple[str, str]:
    src = record.get("source") or {}
    if src.get("pmid"):
        return ("PMID", str(src["pmid"]))
    if src.get("doi"):
        return ("DOI", str(src["doi"]))
    raise ValueError("MISSING_STABLE_PRIMARY_SOURCE_ID")


def hardening_key(record: dict[str, Any]) -> tuple[str, ...]:
    context = record.get("comparability_key") or {}
    values = []
    for field in ALL_FIELDS:
        value = context.get(field)
        if not isinstance(value, str) or not value:
            raise ValueError(f"MISSING_HARDENED_COMPARABILITY_FIELD:{field}")
        values.append(value)
    return tuple(values)


def unresolved_hardened_fields(record: dict[str, Any]) -> list[str]:
    context = record.get("comparability_key") or {}
    out = []
    for field in ALL_FIELDS:
        value = context.get(field)
        if not isinstance(value, str) or not value or value.startswith(UNRESOLVED_PREFIXES):
            out.append(field)
    return out


def cohort_status(record: dict[str, Any]) -> str:
    independence = record.get("cohort_independence") or {}
    status = independence.get("status")
    if status not in VALID_COHORT_STATES:
        raise ValueError("COHORT_INDEPENDENCE_STATUS_REQUIRED")
    return status


def record_can_count_as_distinct_cohort(record: dict[str, Any]) -> bool:
    try:
        _source_id(record)
        hardening_key(record)
        status = cohort_status(record)
    except ValueError:
        return False
    if unresolved_hardened_fields(record):
        return False
    if record.get("blockers"):
        return False
    return status == COHORT_DISTINCT


def qualify_hardened_buckets(records: list[dict[str, Any]]) -> dict[str, Any]:
    buckets: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    blocked: list[dict[str, Any]] = []

    for record in records:
        if not record_can_count_as_distinct_cohort(record):
            blocked.append({
                "record_id": record.get("record_id"),
                "cohort_status": (record.get("cohort_independence") or {}).get("status", "MISSING"),
                "unresolved_fields": unresolved_hardened_fields(record),
                "blockers": list(record.get("blockers") or []),
            })
            continue
        buckets[hardening_key(record)].append(record)

    ready = []
    for key, members in buckets.items():
        distinct_sources = {_source_id(m) for m in members}
        distinct_cohort_ids = {
            (m.get("cohort_independence") or {}).get("cohort_id") for m in members
        }
        distinct_cohort_ids.discard(None)
        if len(distinct_sources) >= 2 and len(distinct_cohort_ids) >= 2:
            ready.append({
                "comparability_key": dict(zip(ALL_FIELDS, key)),
                "independent_primary_study_count": len(distinct_sources),
                "distinct_cohort_count": len(distinct_cohort_ids),
                "record_ids": [m["record_id"] for m in members],
                "status": "COMPARABLE_READY_NOT_POOLED",
            })

    return {
        "hardened_ready_bucket_count": len(ready),
        "ready_buckets": ready,
        "blocked_records": blocked,
        "pooled_reference_created": False,
        "averaging_performed": False,
        "biological_reference_vector": "UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW",
        "pareto_search": "BLOCKED",
    }


def assert_v063_ceiling(result: dict[str, Any]) -> None:
    if result.get("pooled_reference_created") is not False:
        raise AssertionError("V0_6_3_MUST_NOT_POOL")
    if result.get("averaging_performed") is not False:
        raise AssertionError("V0_6_3_MUST_NOT_AVERAGE")
    if not str(result.get("biological_reference_vector", "")).startswith("UNSET"):
        raise AssertionError("BIOLOGICAL_REFERENCE_VECTOR_MUST_STAY_UNSET")
    if result.get("pareto_search") != "BLOCKED":
        raise AssertionError("PARETO_MUST_STAY_BLOCKED")
