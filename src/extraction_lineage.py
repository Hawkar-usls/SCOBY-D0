"""SCOBY-D0 v0.5 evidence extraction lineage.

Validates extraction provenance and replayability only.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

METHODS = {"DIRECT_REPORTED_VALUE", "DERIVED_VALUE", "FIGURE_DIGITIZATION"}
UNCERTAINTY_TYPES = {"SD", "SE", "CI95", "IQR", "RANGE", "RAW_DISTRIBUTION", "OTHER_EXPLICIT"}

def _missing(v: Any) -> bool:
    return v is None or v == "" or v == [] or v == {}

def stable_source_id(lineage: dict[str, Any]) -> tuple[str, str]:
    if lineage.get("pmid"):
        return ("PMID", str(lineage["pmid"]))
    if lineage.get("doi"):
        return ("DOI", str(lineage["doi"]))
    raise ValueError("MISSING_STABLE_SOURCE_IDENTIFIER")

def validate_extraction_record(record: dict[str, Any]) -> list[str]:
    errors = []
    for key in ("observation_id","extractor_id","source_identity","citation_locator",
                "reported_observation","context","extraction","normalized_observation"):
        if key not in record or _missing(record.get(key)):
            errors.append(f"MISSING_{key.upper()}")

    source = record.get("source_identity") or {}
    try:
        stable_source_id(source)
    except ValueError:
        errors.append("MISSING_STABLE_SOURCE_IDENTIFIER")

    locator = record.get("citation_locator") or {}
    if not locator.get("type") or not locator.get("locator"):
        errors.append("MISSING_EXACT_CITATION_LOCATOR")

    reported = record.get("reported_observation") or {}
    if _missing(reported.get("estimate")): errors.append("MISSING_REPORTED_ESTIMATE")
    if _missing(reported.get("units")): errors.append("MISSING_SOURCE_UNIT")
    if not isinstance(reported.get("n"), int) or reported.get("n", 0) < 1:
        errors.append("INVALID_SAMPLE_SIZE")
    uncertainty = reported.get("uncertainty") or {}
    if not uncertainty.get("type"):
        errors.append("UNCERTAINTY_TYPE_REQUIRED")
    elif uncertainty.get("type") not in UNCERTAINTY_TYPES:
        errors.append("UNCERTAINTY_TYPE_UNSUPPORTED")
    if _missing(uncertainty.get("value")):
        errors.append("MISSING_UNCERTAINTY")

    context = record.get("context") or {}
    for key in ("route","compartment","physiological_state","time_window"):
        if _missing(context.get(key)):
            errors.append(f"MISSING_CONTEXT_{key.upper()}")

    extraction = record.get("extraction") or {}
    method = extraction.get("method")
    if method not in METHODS:
        errors.append("EXTRACTION_METHOD_REQUIRED")
    if method == "DIRECT_REPORTED_VALUE":
        if extraction.get("derived") is not False:
            errors.append("DIRECT_VALUE_MUST_NOT_BE_DERIVED")
        if extraction.get("digitized_from_figure") is not False:
            errors.append("DIRECT_VALUE_MUST_NOT_BE_DIGITIZED")
    if method == "DERIVED_VALUE":
        if extraction.get("derived") is not True:
            errors.append("DERIVED_FLAG_REQUIRED")
        deriv = extraction.get("derivation") or {}
        for key in ("operation","inputs","rounding_rule","derivation_replayable"):
            if _missing(deriv.get(key)):
                errors.append(f"MISSING_DERIVATION_{key.upper()}")
        if deriv.get("derivation_replayable") is not True:
            errors.append("DERIVATION_MUST_BE_REPLAYABLE")
    if method == "FIGURE_DIGITIZATION":
        if extraction.get("digitized_from_figure") is not True:
            errors.append("DIGITIZED_FLAG_REQUIRED")
        if _missing(extraction.get("digitization_method")):
            errors.append("DIGITIZATION_METHOD_REQUIRED")
        err = extraction.get("extraction_error") or {}
        if _missing(err.get("type")) or _missing(err.get("value")):
            errors.append("EXTRACTION_ERROR_REQUIRED")

    conversion = extraction.get("unit_conversion") or {"applied": False}
    if conversion.get("applied"):
        for key in ("source_unit","target_unit","exact_transform"):
            if _missing(conversion.get(key)):
                errors.append(f"MISSING_CONVERSION_{key.upper()}")
        if conversion.get("source_unit") != reported.get("units"):
            errors.append("SOURCE_UNIT_MISMATCH")

    normalized = record.get("normalized_observation") or {}
    if _missing(normalized.get("estimate")): errors.append("MISSING_NORMALIZED_ESTIMATE")
    if _missing(normalized.get("units")): errors.append("MISSING_TARGET_UNIT")
    nu = normalized.get("uncertainty") or {}
    if not nu.get("type"): errors.append("NORMALIZED_UNCERTAINTY_TYPE_REQUIRED")
    if _missing(nu.get("value")): errors.append("MISSING_NORMALIZED_UNCERTAINTY")
    return sorted(set(errors))

def _apply_transform(value: float, transform: dict[str, Any]) -> float:
    kind = transform.get("kind")
    if kind == "IDENTITY": return value
    if kind == "MULTIPLY_EXACT":
        factor = transform.get("factor")
        if not isinstance(factor, (int,float)): raise ValueError("INVALID_EXACT_TRANSFORM")
        return value * factor
    raise ValueError("UNSUPPORTED_EXACT_TRANSFORM")

def replay_normalization(record: dict[str, Any]) -> dict[str, Any]:
    errors = validate_extraction_record(record)
    if errors:
        raise ValueError("INVALID_EXTRACTION_RECORD:" + ",".join(errors))
    reported = record["reported_observation"]
    extraction = record["extraction"]
    method = extraction["method"]
    if method == "DIRECT_REPORTED_VALUE":
        estimate = reported["estimate"]
    elif method == "DERIVED_VALUE":
        deriv = extraction["derivation"]
        vals = [x["value"] for x in deriv["inputs"]]
        if deriv["operation"] == "RATIO":
            if len(vals) != 2 or vals[1] == 0: raise ValueError("INVALID_RATIO_DERIVATION")
            estimate = vals[0] / vals[1]
        elif deriv["operation"] == "DIFFERENCE":
            if len(vals) != 2: raise ValueError("INVALID_DIFFERENCE_DERIVATION")
            estimate = vals[0] - vals[1]
        else:
            raise ValueError("UNSUPPORTED_DERIVATION_OPERATION")
    else:
        estimate = reported["estimate"]

    uncertainty = deepcopy(reported["uncertainty"])
    out_unit = reported["units"]
    conversion = extraction.get("unit_conversion") or {"applied":False}
    if conversion.get("applied"):
        estimate = _apply_transform(estimate, conversion["exact_transform"])
        uncertainty["value"] = _apply_transform(uncertainty["value"], conversion["exact_transform"])
        out_unit = conversion["target_unit"]
    return {"estimate":estimate, "uncertainty":uncertainty, "units":out_unit}

def normalized_matches_replay(record: dict[str, Any], tolerance: float = 1e-12) -> bool:
    replayed = replay_normalization(record)
    target = record["normalized_observation"]
    if replayed["units"] != target["units"]: return False
    if replayed["uncertainty"]["type"] != target["uncertainty"]["type"]: return False
    for a,b in ((replayed["estimate"],target["estimate"]),
                (replayed["uncertainty"]["value"],target["uncertainty"]["value"])):
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            if abs(a-b) > tolerance: return False
        elif a != b:
            return False
    return True

def canonical_extraction_payload(record: dict[str, Any]) -> dict[str, Any]:
    return {k: deepcopy(record[k]) for k in (
        "source_identity","citation_locator","reported_observation",
        "context","extraction","normalized_observation"
    )}

def compare_independent_extractions(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    if a.get("extractor_id") == b.get("extractor_id"):
        return {"status":"NOT_INDEPENDENT","authoritative_admission":"BLOCKED"}
    if validate_extraction_record(a) or validate_extraction_record(b):
        return {"status":"INVALID_EXTRACTION_RECORD","authoritative_admission":"BLOCKED"}
    if canonical_extraction_payload(a) == canonical_extraction_payload(b):
        return {"status":"EXTRACTION_MATCH","authoritative_admission":"STILL_BLOCKED_UNTIL_V0_6"}
    return {
        "status":"EXTRACTION_CONFLICT_PRESERVED",
        "authoritative_admission":"BLOCKED",
        "left":canonical_extraction_payload(a),
        "right":canonical_extraction_payload(b),
    }
