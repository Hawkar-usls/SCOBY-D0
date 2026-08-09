"""SCOBY-D0 v0.6.1 multicontext evidence-ingestion replay.

Builds two representation-specific extraction records for each compact ledger
observation and reuses the v0.6 admission kernel. Authority remains limited to
SCOBY-D0 evidence ingestion; no biological reference vector is produced.
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from reference_admission import admit_dataset_observation, compare_cross_representation_extractions

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "evidence/reference_context/MULTICONTEXT_EXTRACTION_LEDGER_V0_1.json"


def load_ledger(path: Path = DEFAULT_LEDGER) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_record(ledger: dict[str, Any], obs: dict[str, Any], side: str) -> dict[str, Any]:
    study = ledger["study_bindings"][obs["study"]]
    rep = study[side]
    context = {
        "route": study["context"]["route"],
        "compartment": obs["compartment"],
        "physiological_state": study["context"]["physiological_state"],
        "time_window": study["context"]["time_window"],
        "study_arm": obs.get("arm", "SINGLE_TEST_CONTEXT"),
        "analyte": obs["analyte"],
        "metric": obs["metric"],
    }
    return {
        "observation_id": obs["id"],
        "extractor_id": f"{side}_{rep['process_id']}_{obs['id']}",
        "source_identity": deepcopy(study["source_identity"]),
        "citation_locator": {
            "type": "DIRECT_REPORTED_SOURCE_VALUE",
            "locator": obs["locator"],
        },
        "reported_observation": {
            "estimate": obs["estimate"],
            "uncertainty": deepcopy(obs["uncertainty"]),
            "units": obs["units"],
            "n": obs["n"],
        },
        "context": context,
        "extraction": {
            "method": "DIRECT_REPORTED_VALUE",
            "derived": False,
            "digitized_from_figure": False,
            "unit_conversion": {"applied": False},
        },
        "normalized_observation": {
            "estimate": obs["estimate"],
            "uncertainty": deepcopy(obs["uncertainty"]),
            "units": obs["units"],
        },
        "extraction_provenance": deepcopy(rep),
    }


def replay_observation_pair(ledger: dict[str, Any], obs: dict[str, Any]) -> dict[str, Any]:
    a = build_record(ledger, obs, "A")
    b = build_record(ledger, obs, "B")
    comparison = compare_cross_representation_extractions(a, b)
    admission = admit_dataset_observation(a, b)
    return {"A": a, "B": b, "comparison": comparison, "admission": admission}


def replay_all(ledger: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    ledger = ledger or load_ledger()
    return [replay_observation_pair(ledger, obs) for obs in ledger["observations"]]


if __name__ == "__main__":
    rows = replay_all()
    for row in rows:
        print(row["A"]["observation_id"], row["comparison"]["status"], row["admission"]["status"])
