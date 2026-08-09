import copy
import hashlib
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
MANIFEST = ROOT / "evidence/reference_context/REFERENCE_DATASET_V0_4.json"


def load_gate():
    return json.loads(GATE.read_text(encoding="utf-8"))


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


class TestComparableContextV062(unittest.TestCase):
    def test_gate_hash_recomputes(self):
        obj = load_gate()
        expected = obj.pop("content_sha256")
        payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), expected)

    def test_current_real_candidates_produce_zero_ready_buckets(self):
        out = qualify_comparable_buckets(load_gate()["candidates"])
        self.assertEqual(out["comparable_ready_bucket_count"], 0)
        self.assertEqual(len(out["ready_buckets"]), 0)
        assert_no_pooling(out)

    def test_reference_manifest_preserves_existing_authority_without_pooling(self):
        m = load_manifest()
        self.assertEqual(m["authoritative_observation_count"], 10)
        self.assertEqual(m["exact_comparable_buckets_with_two_independent_primary_studies"], 0)
        self.assertFalse(m["cross_study_aggregation_allowed"])
        self.assertFalse(m["pooled_reference_created"])
        self.assertFalse(m["averaging_performed"])
        self.assertTrue(m["biological_reference_vector"].startswith("UNSET"))

    def test_tracer_exposure_mismatch_not_comparable(self):
        g = load_gate()
        a = copy.deepcopy(g["candidates"][0])
        b = copy.deepcopy(a)
        a["ingestion_status"] = b["ingestion_status"] = "ELIGIBLE"
        a["blockers"] = b["blockers"] = []
        a["comparability_key"]["fasting_duration"] = "12_HOURS"
        a["comparability_key"]["uncertainty_semantics"] = "SEM"
        b["comparability_key"]["fasting_duration"] = "12_HOURS"
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

    def test_scheppach_fasting_duration_is_fail_closed_on_primary_abstract(self):
        c = load_gate()["candidates"][0]
        self.assertFalse(candidate_is_qualifiable(c))
        self.assertTrue(c["comparability_key"]["fasting_duration"].startswith("UNRESOLVED"))
        self.assertIn("FASTING_DURATION_NOT_EXPLICIT_IN_PRIMARY_ABSTRACT_FOR_21_CONTROLS", c["blockers"])

    def test_unknown_fasting_duration_blocks_akanji_candidate(self):
        c = load_gate()["candidates"][3]
        self.assertFalse(candidate_is_qualifiable(c))
        self.assertEqual(c["comparability_key"]["fasting_duration"], "UNRESOLVED")

    def test_mcdougal_is_serum_context_not_plasma(self):
        c = load_gate()["candidates"][2]
        self.assertEqual(c["comparability_key"]["specimen"], "SERUM")
        self.assertIn("NO_SECOND_INDEPENDENT_PRIMARY_STUDY_WITH_EXACT_MATCHING_SERUM_CONTEXT", c["blockers"])
        self.assertFalse(candidate_is_qualifiable(c))

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
