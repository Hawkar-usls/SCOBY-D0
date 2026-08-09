import copy
import hashlib
import json
import unittest
from pathlib import Path

from cross_study_hardening import (
    COHORT_DISTINCT,
    COHORT_OVERLAP,
    COHORT_UNRESOLVED,
    assert_v063_ceiling,
    hardening_key,
    qualify_hardened_buckets,
    record_can_count_as_distinct_cohort,
)

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json"
MANIFEST = ROOT / "evidence/reference_context/REFERENCE_DATASET_V0_5.json"


def record(record_id="R1", pmid="1", cohort_id="C1"):
    return {
        "record_id": record_id,
        "source": {"pmid": pmid, "doi": f"10.example/{pmid}"},
        "comparability_key": {
            "population_health_class": "HEALTHY",
            "specimen": "VENOUS_PLASMA",
            "route_or_exposure": "FASTING_BASELINE_NO_EXOGENOUS_ACETATE",
            "fasting_duration": "12_HOURS",
            "tracer_state": "NO_TRACER",
            "analyte": "ACETATE",
            "metric": "CONCENTRATION",
            "units": "umol/L",
            "uncertainty_semantics": "SD",
            "preanalytic_handling": "FRESH_PLASMA_ANALYZED_WITHOUT_FREEZE_STORAGE",
            "analytical_method_family": "GAS_CHROMATOGRAPHY",
        },
        "cohort_independence": {
            "status": COHORT_DISTINCT,
            "cohort_id": cohort_id,
        },
        "blockers": [],
    }


class TestCrossStudyHardeningV063(unittest.TestCase):
    def test_experiment_hash_recomputes(self):
        obj = json.loads(EXPERIMENT.read_text(encoding="utf-8"))
        expected = obj.pop("content_sha256")
        payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), expected)

    def test_manifest_keeps_reference_vector_unset(self):
        m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(m["authoritative_observation_count"], 10)
        self.assertEqual(m["v0_6_3_hardened_ready_buckets"], 0)
        self.assertFalse(m["pooled_reference_created"])
        self.assertFalse(m["averaging_performed"])
        self.assertTrue(m["biological_reference_vector"].startswith("UNSET"))
        self.assertTrue(m["pareto_search"].startswith("BLOCKED"))

    def test_two_distinct_publications_with_confirmed_overlap_do_not_qualify(self):
        a = record("A", "100", "SHARED_COHORT")
        b = record("B", "200", "SHARED_COHORT")
        b["cohort_independence"]["status"] = COHORT_OVERLAP
        out = qualify_hardened_buckets([a, b])
        self.assertEqual(out["hardened_ready_bucket_count"], 0)
        assert_v063_ceiling(out)

    def test_unresolved_participant_overlap_does_not_count_as_distinct(self):
        a = record("A", "100", "C1")
        b = record("B", "200", "C2")
        b["cohort_independence"]["status"] = COHORT_UNRESOLVED
        self.assertFalse(record_can_count_as_distinct_cohort(b))
        out = qualify_hardened_buckets([a, b])
        self.assertEqual(out["hardened_ready_bucket_count"], 0)

    def test_two_exact_matching_distinct_cohorts_can_be_ready_not_pooled(self):
        a = record("A", "100", "C1")
        b = record("B", "200", "C2")
        out = qualify_hardened_buckets([a, b])
        self.assertEqual(out["hardened_ready_bucket_count"], 1)
        self.assertEqual(out["ready_buckets"][0]["status"], "COMPARABLE_READY_NOT_POOLED")
        self.assertEqual(out["ready_buckets"][0]["distinct_cohort_count"], 2)
        assert_v063_ceiling(out)

    def test_fresh_and_stored_plasma_are_not_same_measurement_context(self):
        a = record("A", "100", "C1")
        b = record("B", "200", "C2")
        b["comparability_key"]["preanalytic_handling"] = "FROZEN_MINUS20C_24H_BEFORE_ANALYSIS"
        self.assertNotEqual(hardening_key(a), hardening_key(b))
        out = qualify_hardened_buckets([a, b])
        self.assertEqual(out["hardened_ready_bucket_count"], 0)

    def test_analytical_method_family_is_part_of_key(self):
        a = record("A", "100", "C1")
        b = record("B", "200", "C2")
        b["comparability_key"]["analytical_method_family"] = "LC_MS_MS"
        self.assertNotEqual(hardening_key(a), hardening_key(b))

    def test_unknown_preanalytics_fail_closed(self):
        x = record()
        x["comparability_key"]["preanalytic_handling"] = "UNRESOLVED"
        self.assertFalse(record_can_count_as_distinct_cohort(x))

    def test_unknown_analytical_method_fails_closed(self):
        x = record()
        x["comparability_key"]["analytical_method_family"] = "UNRESOLVED"
        self.assertFalse(record_can_count_as_distinct_cohort(x))

    def test_different_cohort_ids_are_required_even_with_distinct_pmids(self):
        a = record("A", "100", "SAME")
        b = record("B", "200", "SAME")
        out = qualify_hardened_buckets([a, b])
        self.assertEqual(out["hardened_ready_bucket_count"], 0)

    def test_hardening_never_pools_or_averages(self):
        out = qualify_hardened_buckets([record("A", "100", "C1"), record("B", "200", "C2")])
        self.assertFalse(out["pooled_reference_created"])
        self.assertFalse(out["averaging_performed"])
        self.assertTrue(out["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(out["pareto_search"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
