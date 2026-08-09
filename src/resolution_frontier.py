"""Fail-closed helpers for the v0.6.5 cohort/method resolution frontier.

This module ranks or validates follow-up work only. It is intentionally not an
admission channel and cannot create authoritative observations.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict


REQUIRED_STATE = {
    "real_hardened_ready_pairs": 0,
    "cohort_independence_resolved_pairs": 0,
    "method_identity_resolved_pairs": 0,
    "admission_mutations": 0,
    "new_authoritative_observations": 0,
    "pooled_reference_created": False,
    "averaging_performed": False,
    "pareto_search": "BLOCKED",
}


def canonical_payload_sha256(obj: Dict[str, Any]) -> str:
    payload = dict(obj)
    payload.pop("content_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def load_frontier(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_frontier(frontier: Dict[str, Any]) -> None:
    if frontier.get("status") != "RESOLUTION_FRONTIER_NOT_ADMISSION":
        raise ValueError("v0.6.5 must remain a resolution frontier, not admission")
    pairs = frontier.get("near_pairs", [])
    state = frontier.get("frontier_state", {})
    if state.get("near_pair_count") != len(pairs):
        raise ValueError("near_pair_count mismatch")
    for key, expected in REQUIRED_STATE.items():
        if state.get(key) != expected:
            raise ValueError(f"forbidden state mutation: {key}")
    if not str(state.get("biological_reference_vector", "")).startswith("UNSET"):
        raise ValueError("biological reference vector must remain UNSET")
    for pair in pairs:
        if not pair.get("pair_id"):
            raise ValueError("pair_id required")
        if not pair.get("blockers"):
            raise ValueError(f"blockers required for unresolved pair {pair.get('pair_id')}")
    expected_hash = frontier.get("content_sha256")
    if expected_hash and canonical_payload_sha256(frontier) != expected_hash:
        raise ValueError("content hash mismatch")


def pair_can_admit_from_resolution_frontier(_: Dict[str, Any]) -> bool:
    """Resolution metadata never grants evidence admission."""
    return False


def distinct_trial_ids_establish_independent_cohorts(_: Dict[str, Any]) -> bool:
    """A pair of trial identifiers is provenance, not participant-independence proof."""
    return False


def same_lab_establishes_same_method(_: Dict[str, Any]) -> bool:
    """A shared laboratory is provenance, not analytical-method identity."""
    return False


def resolution_summary(pair: Dict[str, Any]) -> Dict[str, Any]:
    blockers = list(pair.get("blockers", []))
    return {
        "pair_id": pair.get("pair_id"),
        "positive_evidence_count": len(pair.get("positive_resolution_evidence", [])),
        "blocker_count": len(blockers),
        "blockers": blockers,
        "admissible_from_frontier": False,
    }
