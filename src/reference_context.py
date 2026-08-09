"""SCOBY-D0 v0.4 evidence admission and context separation.

This module validates metadata discipline only. It does not establish physiological
normality, clinical safety, efficacy, or human formulation.
"""
from __future__ import annotations
from typing import Any

REQUIRED = (
    "source_type","source_lineage","study_design","cohort","sample_size","route","compartment",
    "physiological_state","sampling_times_or_window","analytical_method",
    "analyte","estimate","units","uncertainty","citation_locator","exclusions"
)

ROUTES = {
    "ORAL_FOOD","ORAL_BEVERAGE","ORAL_CAPSULE","COLON_DELIVERY_CAPSULE",
    "RECTAL_COLONIC_INFUSION","INTRAVENOUS_TRACER","OTHER_EXPLICIT"
}
COMPARTMENTS = {"PLASMA","SERUM","COLON_LUMEN","FECES","URINE","BREATH","OTHER_EXPLICIT"}
STATES = {"FASTED","POSTPRANDIAL","MIXED_PROTOCOL","OTHER_EXPLICIT"}

class ReferenceCollapseForbidden(RuntimeError):
    pass

def context_key(obs: dict[str, Any]) -> tuple[str, str, str, str]:
    return (obs["analyte"], obs["route"], obs["compartment"], obs["physiological_state"])

def _stable_source_id(lineage: dict[str, Any]) -> tuple[str, str]:
    pmid = str(lineage.get("pmid") or "").strip()
    doi = str(lineage.get("doi") or "").strip()
    if not pmid and not doi:
        raise ValueError("MISSING_STABLE_SOURCE_IDENTIFIER")
    return pmid, doi

def validate_observation(obs: dict[str, Any]) -> list[str]:
    errors = []
    for key in REQUIRED:
        if key not in obs or obs[key] is None or obs[key] == "":
            errors.append(f"MISSING_{key.upper()}")
    if obs.get("source_type") != "PRIMARY_HUMAN":
        errors.append("SOURCE_NOT_PRIMARY_HUMAN")
    if obs.get("route") not in ROUTES:
        errors.append("ROUTE_NOT_EXPLICIT")
    if obs.get("compartment") not in COMPARTMENTS:
        errors.append("COMPARTMENT_NOT_EXPLICIT")
    if obs.get("physiological_state") not in STATES:
        errors.append("PHYSIOLOGICAL_STATE_NOT_EXPLICIT")
    lineage = obs.get("source_lineage") or {}
    for key in ("title","year"):
        if not lineage.get(key):
            errors.append(f"MISSING_LINEAGE_{key.upper()}")
    if not str(lineage.get("pmid") or "").strip() and not str(lineage.get("doi") or "").strip():
        errors.append("MISSING_STABLE_SOURCE_IDENTIFIER")
    uncertainty = obs.get("uncertainty")
    if not isinstance(uncertainty, dict) or uncertainty.get("value") is None or not uncertainty.get("kind"):
        errors.append("MISSING_UNCERTAINTY")
    if not isinstance(obs.get("sample_size"), int) or obs.get("sample_size", 0) < 1:
        errors.append("INVALID_SAMPLE_SIZE")
    return sorted(set(errors))

def is_admissible(obs: dict[str, Any]) -> bool:
    return not validate_observation(obs)

_UNIT_FACTORS = {
    ("umol/L", "mmol/L"): 0.001,
    ("mmol/L", "umol/L"): 1000.0,
    ("percent", "fraction"): 0.01,
    ("fraction", "percent"): 100.0,
}

def convert_value(value: float, from_unit: str, to_unit: str) -> dict[str, Any]:
    if from_unit == to_unit:
        factor = 1.0
    else:
        try:
            factor = _UNIT_FACTORS[(from_unit, to_unit)]
        except KeyError as exc:
            raise ValueError("UNSUPPORTED_UNIT_CONVERSION") from exc
    return {
        "input_value": value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "factor": factor,
        "output_value": value * factor,
        "conversion_explicit": True,
    }

def comparable(obs_a: dict[str, Any], obs_b: dict[str, Any]) -> bool:
    return context_key(obs_a) == context_key(obs_b)

def independent_source_count(observations: list[dict[str, Any]]) -> int:
    return len({_stable_source_id(o["source_lineage"]) for o in observations})

def bucket_can_be_evidence_bound(observations: list[dict[str, Any]], minimum_sources: int = 2) -> bool:
    if not observations or any(not is_admissible(o) for o in observations):
        return False
    keys = {context_key(o) for o in observations}
    if len(keys) != 1:
        return False
    return independent_source_count(observations) >= minimum_sources

def preserve_conflicts(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [dict(o) for o in observations]

def collapse_reference_vector(_: list[dict[str, Any]]) -> None:
    raise ReferenceCollapseForbidden("BIOLOGICAL_REFERENCE_VECTOR_STILL_NOT_COLLAPSED_IN_V0_4")
