import copy
import json
import unittest
from pathlib import Path

from comparable_context import (
    candidate_is_qualifiable,
    exact_comparability_key,
    qualify_comparable_buckets,
    assert_no_pooling,
)

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "experiments/SCOBY-D0-COMPARABLE-CONTEXT-BUCKET-QUALIFICATION-v0.6.2.json"


def load_gate():
    return json.loads(GATE.read_text(encoding="utf-8"))


class TestComparableContextV062(unittest.TestCase):
    def test_current_real_candidates_produce_zero_ready_buckets(self):
        out = qualify_comparable_buckets(load_gate()["candidates"])
        self.assertEqual(out["comparable_ready_bucket_count"], 0)
        self.assertEqual(len(out["ready_buckets"]), 0)
        assert_no_pooling(out)

    def test_tracer_exposure_mismatch_not_comparable(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][0])
        b = copy.deepcopy(a)
        a["ingestion_status"] = b["ingestion_status"] = "ELIGIBLE"
        a["blockers"] = b["blockers"] = []
        a["comparability_key"]["uncertainty_semantics"] = "SEM"
        b["comparability_key"]["uncertainty_semantics"] = "SEM"
        b["source"]["pmid"] = "DIFFERENT_STUDY"
        b["comparability_key"]["tracer_state"] = "AFTER_2_HOUR_LOW_DOSE_TRACER_INFUSION"
        self.assertNotEqual(exact_comparability_key(a), exact_comparability_key(b))

    def test_serum_and_plasma_are_not_equal_keys(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][0])
        b = copy.deepcopy(a)
        a["comparability_key"]["specimen"] = "PLASMA"
        b["comparability_key"]["specimen"] = "SERUM"
        self.assertNotEqual(exact_comparability_key(a), exact_comparability_key(b))

    def test_unknown_fasting_duration_blocks_candidate(self):
        c = load_gate()["candidates"][3]
        self.assertFalse(candidate_is_qualifiable(c))
        self.assertEqual(c["comparability_key"]["fasting_duration"], "UNRESOLVED")

    def test_ambiguous_specimen_blocks_candidate(self):
        c = load_gate()["candidates"][2]
        self.assertFalse(candidate_is_qualifiable(c))
        self.assertIn("SPECIMEN_TYPE_AMBIGUOUS_FOR_ACETATE_TABLE_VALUE", c["blockers"])

    def test_missing_second_representation_can_block_ingestion_candidate(self):
        c = load_gate()["candidates"][0]
        self.assertFalse(candidate_is_qualifiable(c))
        self.assertIn("SECOND_FULL_SOURCE_REPRESENTATION_NOT_ESTABLISHED", c["blockers"])

    def test_same_study_duplicate_does_not_make_independent_bucket(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][1])
        a["ingestion_status"] = "ELIGIBLE"
        a["blockers"] = []
        b = copy.deepcopy(a)
        b["candidate_id"] = "DUPLICATE_COHORT_SAME_STUDY"
        out = qualify_comparable_buckets([a, b])
        self.assertEqual(out["comparable_ready_bucket_count"], 0)

    def test_two_matching_independent_primary_studies_can_be_ready_not_pooled(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][1])
        a["ingestion_status"] = "ELIGIBLE"
        a["blockers"] = []
        b = copy.deepcopy(a)
        b["candidate_id"] = "SYNTHETIC_SECOND_PRIMARY_STUDY"
        b["source"]["pmid"] = "SYNTHETIC_PMID_2"
        b["source"]["doi"] = "SYNTHETIC_DOI_2"
        out = qualify_comparable_buckets([a, b])
        self.assertEqual(out["comparable_ready_bucket_count"], 1)
        self.assertEqual(out["ready_buckets"][0]["status"], "COMPARABLE_READY_NOT_POOLED")
        assert_no_pooling(out)

    def test_uncertainty_semantics_part_of_exact_key(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][1])
        b = copy.deepcopy(a)
        b["comparability_key"]["uncertainty_semantics"] = "SD"
        self.assertNotEqual(exact_comparability_key(a), exact_comparability_key(b))

    def test_no_averaging_at_v062(self):
        out = qualify_comparable_buckets(load_gate()["candidates"])
        self.assertFalse(out["averaging_performed"])
        self.assertFalse(out["pooled_reference_created"])
        self.assertTrue(out["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(out["pareto_search"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
