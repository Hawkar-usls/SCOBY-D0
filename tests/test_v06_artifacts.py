import hashlib
import json
import unittest
from pathlib import Path

from reference_admission import admit_dataset_observation, compare_cross_representation_extractions

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class TestV06Artifacts(unittest.TestCase):
    def test_v06_object_hash_recomputes(self):
        obj = load("experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json")
        expected = obj.pop("content_sha256")
        payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), expected)

    def test_exactly_one_ingestion_authoritative_observation(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")
        self.assertEqual(obj["authoritative_observation_count"], 1)
        self.assertEqual(len(obj["observations"]), 1)
        self.assertEqual(obj["authority_scope"], "SCOBY_D0_EVIDENCE_INGESTION_ONLY")

    def test_reference_standard_still_not_established(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")
        self.assertEqual(obj["human_reference_standard"], "NOT_ESTABLISHED")
        self.assertTrue(obj["biological_reference_vector"].startswith("UNSET"))
        self.assertTrue(obj["pareto_search"].startswith("BLOCKED"))

    def test_two_source_representations_are_distinct(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")["observations"][0]
        a, b = obj["extraction_A"], obj["extraction_B"]
        self.assertNotEqual(a["representation_id"], b["representation_id"])
        self.assertNotEqual(a["process_family"], b["process_family"])
        self.assertNotEqual(a["format"], b["format"])

    def test_cross_representation_match_has_no_unresolved_conflict(self):
        c = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")["observations"][0]["cross_representation_comparison"]
        self.assertEqual(c["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")
        self.assertFalse(c["unresolved_conflict"])
        self.assertTrue(c["normalized_value_match"])
        self.assertTrue(c["uncertainty_type_match"])

    def test_ledger_and_authoritative_set_counts_agree(self):
        ledger = load("evidence/reference_context/EXTRACTION_LEDGER_V0_1.json")
        refset = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")
        self.assertEqual(ledger["gate_status"]["authoritative_observations"], refset["authoritative_observation_count"])
        self.assertEqual(ledger["gate_status"]["real_separate_extractor_B_records"], 1)
        self.assertEqual(ledger["gate_status"]["distinct_source_representations"], 2)

    def test_real_ledger_pair_replays_to_cross_representation_match(self):
        ledger = load("evidence/reference_context/EXTRACTION_LEDGER_V0_1.json")
        a, b = ledger["records"]
        out = compare_cross_representation_extractions(a, b)
        self.assertEqual(out["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")
        self.assertEqual(out["authoritative_admission"], "ELIGIBLE_FOR_V0_6_INGESTION_AUTHORITY")

    def test_real_ledger_pair_admits_only_ingestion_authority(self):
        ledger = load("evidence/reference_context/EXTRACTION_LEDGER_V0_1.json")
        a, b = ledger["records"]
        out = admit_dataset_observation(a, b)
        self.assertEqual(out["status"], "AUTHORITATIVE_DATASET_OBSERVATION_ADMITTED")
        self.assertEqual(out["authority_scope"], "SCOBY_D0_EVIDENCE_INGESTION_ONLY")
        self.assertEqual(out["biological_reference_standard"], "NOT_ESTABLISHED")
        self.assertTrue(out["biological_reference_vector"].startswith("UNSET"))
        self.assertTrue(out["pareto_search"].startswith("BLOCKED"))

    def test_reference_dataset_v02_preserves_v01_as_pre_admission_snapshot(self):
        current = load("evidence/reference_context/REFERENCE_DATASET_V0_2.json")
        old = load("evidence/reference_context/REFERENCE_DATASET_V0_1.json")
        self.assertEqual(current["authoritative_observation_count"], 1)
        self.assertEqual(old["authoritative_observations"], [])
        self.assertIn("pre-v0.6", current["lineage_note"])
        self.assertTrue(current["biological_reference_vector"].startswith("UNSET"))

    def test_boets_value_and_sd_are_normalized_by_same_exact_factor(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")["observations"][0]
        factor = obj["normalization"]["exact_transform"]["factor"]
        self.assertEqual(obj["reported_observation"]["estimate"] * factor, obj["normalized_observation"]["estimate"])
        self.assertEqual(obj["reported_observation"]["uncertainty"]["value"] * factor, obj["normalized_observation"]["uncertainty"]["value"])

    def test_external_review_is_not_invented(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json")
        self.assertEqual(obj["external_review"], "NOT_YET_ESTABLISHED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
