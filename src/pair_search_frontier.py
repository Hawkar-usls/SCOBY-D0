"""SCOBY-D0 v0.6.4 hardened-pair literature search frontier.

Discovery/ranking metadata is non-authoritative. The frontier can preserve
blockers and prioritize follow-up, but cannot mutate evidence admission,
create pooled references, or open Pareto search.
"""
from __future__ import annotations
from typing import Any

ALLOWED_VERDICTS = {
    "NOT_HARDENED_COMPARABLE",
    "PROTOCOL_MATCH_BUT_INDEPENDENCE_FAIL",
}


def validate_frontier(frontier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    state = frontier.get("frontier_state") or {}
    pairs = frontier.get("pairs") or []

    if state.get("pair_count") != len(pairs):
        errors.append("PAIR_COUNT_MISMATCH")
    if state.get("real_hardened_ready_pairs") != 0:
        errors.append("REAL_READY_PAIR_COUNT_MUST_STAY_ZERO")
    if state.get("admission_mutations") != 0:
        errors.append("FRONTIER_MUST_NOT_MUTATE_ADMISSION")
    if state.get("new_authoritative_observations") != 0:
        errors.append("FRONTIER_MUST_NOT_CREATE_AUTHORITATIVE_OBSERVATIONS")
    if state.get("pooled_reference_created") is not False:
        errors.append("FRONTIER_MUST_NOT_CREATE_POOLED_REFERENCE")
    if state.get("averaging_performed") is not False:
        errors.append("FRONTIER_MUST_NOT_AVERAGE")
    if not str(state.get("biological_reference_vector", "")).startswith("UNSET"):
        errors.append("BIOLOGICAL_REFERENCE_VECTOR_MUST_STAY_UNSET")
    if state.get("pareto_search") != "BLOCKED":
        errors.append("PARETO_MUST_STAY_BLOCKED")

    seen = set()
    for pair in pairs:
        pair_id = pair.get("pair_id")
        if not pair_id:
            errors.append("MISSING_PAIR_ID")
            continue
        if pair_id in seen:
            errors.append("DUPLICATE_PAIR_ID")
        seen.add(pair_id)
        if pair.get("verdict") not in ALLOWED_VERDICTS:
            errors.append(f"UNSUPPORTED_FRONTIER_VERDICT:{pair_id}")
        if not pair.get("blockers"):
            errors.append(f"BLOCKERS_REQUIRED:{pair_id}")
        for side in ("source_A", "source_B"):
            src = pair.get(side) or {}
            if not src.get("title") or not src.get("year"):
                errors.append(f"MISSING_SOURCE_IDENTITY:{pair_id}:{side}")
            if not (src.get("pmid") or src.get("doi")):
                errors.append(f"MISSING_STABLE_SOURCE_IDENTIFIER:{pair_id}:{side}")
    return sorted(set(errors))


def pair_is_admissible_from_frontier(pair: dict[str, Any]) -> bool:
    """Always false: frontier metadata is never an admission channel."""
    return False


def priority_signature(pair: dict[str, Any]) -> tuple[int, int, str]:
    """Discovery-only ordering: fewer blockers and more shared surface features rank first.

    This cannot affect pair_is_admissible_from_frontier().
    """
    blockers = len(pair.get("blockers") or [])
    shared = len(pair.get("shared_surface_features") or [])
    return (blockers, -shared, str(pair.get("pair_id", "")))


def ranked_frontier(frontier: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted(list(frontier.get("pairs") or []), key=priority_signature)


def assert_frontier_ceiling(frontier: dict[str, Any]) -> None:
    errors = validate_frontier(frontier)
    if errors:
        raise AssertionError("INVALID_FRONTIER:" + ",".join(errors))
    if any(pair_is_admissible_from_frontier(p) for p in frontier.get("pairs") or []):
        raise AssertionError("FRONTIER_MUST_NOT_BE_ADMISSION_CHANNEL")
