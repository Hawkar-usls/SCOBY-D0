"""SCOBY-D0 v0.6.6 hardened candidate discovery ledger.

This module is deliberately non-authoritative. It uses the exact v0.6.3
comparison surface to rank literature candidates, but it cannot admit a
candidate, create an authoritative observation, pool studies, or create a
biological reference vector.
"""
from __future__ import annotations

import hashlib
import json
from itertools import combinations
from typing import Any

from cross_study_hardening import ALL_FIELDS, COHORT_UNRESOLVED, qualify_hardened_buckets

UNRESOLVED_PREFIXES = ("UNRESOLVED", "UNKNOWN", "NOT_ESTABLISHED")


def canonical_payload_sha256(obj: dict[str, Any]) -> str:
    payload = dict(obj)
    payload.pop("content_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def measurement_key(candidate: dict[str, Any]) -> dict[str, str]:
    key = candidate.get("measurement_key") or {}
    return {field: key.get(field) for field in ALL_FIELDS}


def unresolved_measurement_fields(candidate: dict[str, Any]) -> list[str]:
    key = measurement_key(candidate)
    out: list[str] = []
    for field in ALL_FIELDS:
        value = key.get(field)
        if not isinstance(value, str) or not value or value.startswith(UNRESOLVED_PREFIXES):
            out.append(field)
    return out


def measurement_key_is_fully_bound(candidate: dict[str, Any]) -> bool:
    return not unresolved_measurement_fields(candidate)


def key_differences(a: dict[str, Any], b: dict[str, Any]) -> list[str]:
    ka, kb = measurement_key(a), measurement_key(b)
    return [field for field in ALL_FIELDS if ka.get(field) != kb.get(field)]


def candidate_can_admit_from_ledger(candidate: dict[str, Any]) -> bool:
    """Discovery ledger has no admission authority by construction."""
    return False


def _kernel_record(candidate: dict[str, Any]) -> dict[str, Any]:
    """Replay a candidate through v0.6.3 in fail-closed cohort state."""
    source = candidate.get("source") or {}
    return {
        "record_id": candidate.get("candidate_id"),
        "source": {"pmid": source.get("pmid"), "doi": source.get("doi")},
        "comparability_key": measurement_key(candidate),
        "cohort_independence": {
            "status": COHORT_UNRESOLVED,
            "cohort_id": source.get("cohort_label") or candidate.get("candidate_id"),
        },
        "blockers": list(candidate.get("blockers") or []),
    }


def replay_candidates_through_v063(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    result = qualify_hardened_buckets([_kernel_record(c) for c in candidates])
    result["candidate_ledger_admission_authority"] = False
    return result


def rank_candidate_pairs(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Rank discovery proximity only. Lower distance never changes authority."""
    ranked = []
    for a, b in combinations(candidates, 2):
        diffs = key_differences(a, b)
        ranked.append({
            "candidate_a": a.get("candidate_id"),
            "candidate_b": b.get("candidate_id"),
            "differing_fields": diffs,
            "distance": len(diffs),
            "admission_effect": "NONE",
        })
    return sorted(ranked, key=lambda x: (x["distance"], x["candidate_a"], x["candidate_b"]))


def assert_candidate_ledger_ceiling(ledger: dict[str, Any]) -> None:
    state = ledger.get("dry_run_state") or {}
    if state.get("real_hardened_ready_pairs") != 0:
        raise AssertionError("LEDGER_MUST_NOT_DECLARE_READY_PAIR")
    if state.get("new_authoritative_observations") != 0:
        raise AssertionError("LEDGER_MUST_NOT_CREATE_AUTHORITY")
    if state.get("admission_mutations") != 0:
        raise AssertionError("LEDGER_MUST_NOT_MUTATE_ADMISSION")
    if state.get("pooled_reference_created") is not False:
        raise AssertionError("LEDGER_MUST_NOT_POOL")
    if state.get("averaging_performed") is not False:
        raise AssertionError("LEDGER_MUST_NOT_AVERAGE")
    if not str(state.get("biological_reference_vector", "")).startswith("UNSET"):
        raise AssertionError("BIOLOGICAL_REFERENCE_VECTOR_MUST_STAY_UNSET")
    if state.get("pareto_search") != "BLOCKED":
        raise AssertionError("PARETO_MUST_STAY_BLOCKED")
