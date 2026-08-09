import hashlib
import json
import unittest
from pathlib import Path

from multicontext_admission import load_ledger, replay_all

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class TestMultiContextV061(unittest.TestCase):
    def test_experiment_hash_recomputes(self):
        obj = load("experiments/SCOBY-D0-MULTICONTEXT-REFERENCE-EXPANSION-v0.6.1.json")
        expected = obj.pop("content_sha256")
        payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), expected)

    def test_nine_new_observations_are_unique(self):
        ledger = load_ledger()
        ids = [x["id"] for x in ledger["observations"]]
        self.assertEqual(len(ids), 9)
        self.assertEqual(len(set(ids)), 9)

    def test_all_real_pairs_replay_and_admit_ingestion_only(self):
        rows = replay_all()
        self.assertEqual(len(rows), 9)
        for row in rows:
            self.assertEqual(row["comparison"]["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")
            self.assertEqual(row["admission"]["status"], "AUTHORITATIVE_DATASET_OBSERVATION_ADMITTED")
            self.assertEqual(row["admission"]["authority_scope"], "SCOBY_D0_EVIDENCE_INGESTION_ONLY")
            self.assertEqual(row["admission"]["biological_reference_standard"], "NOT_ESTABLISHED")

    def test_two_new_primary_studies_use_distinct_representation_processes(self):
        ledger = load_ledger()
        self.assertEqual(len(ledger["study_bindings"]), 2)
        for study in ledger["study_bindings"].values():
            self.assertNotEqual(study["A"]["representation_id"], study["B"]["representation_id"])
            self.assertNotEqual(study["A"]["process_family"], study["B"]["process_family"])

    def test_sd_and_iqr_remain_distinct(self):
        ledger = load_ledger()
        kinds = {x["uncertainty"]["type"] for x in ledger["observations"]}
        self.assertEqual(kinds, {"SD", "IQR"})

    def test_rate_of_appearance_is_not_concentration(self):
        ledger = load_ledger()
        metrics = {x["metric"] for x in ledger["observations"]}
        self.assertIn("endogenous_rate_of_appearance", metrics)
        self.assertIn("concentration", metrics)
        self.assertGreater(len(metrics), 1)

    def test_plasma_and_fecal_are_separate(self):
        ledger = load_ledger()
        compartments = {x["compartment"] for x in ledger["observations"]}
        self.assertIn("PLASMA", compartments)
        self.assertIn("FECAL", compartments)
        self.assertIn("SYSTEMIC_RATE_OF_APPEARANCE_FROM_PLASMA_TRACER", compartments)

    def test_high_and_low_diet_arms_are_not_collapsed(self):
        ledger = load_ledger()
        arms = {x.get("arm") for x in ledger["observations"] if x["study"] == "GILL_2022_DIET"}
        self.assertEqual(arms, {"HIGH_SCFA_DIET", "LOW_SCFA_DIET"})

    def test_reference_manifest_counts_and_ceiling(self):
        obj = load("evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_2.json")
        self.assertEqual(obj["authoritative_observation_count"], 10)
        self.assertEqual(obj["primary_human_study_count"], 3)
        self.assertEqual(obj["human_reference_standard"], "NOT_ESTABLISHED")
        self.assertTrue(obj["biological_reference_vector"].startswith("UNSET"))
        self.assertTrue(obj["pareto_search"].startswith("BLOCKED"))

    def test_reference_dataset_preserves_six_context_buckets(self):
        obj = load("evidence/reference_context/REFERENCE_DATASET_V0_3.json")
        self.assertEqual(sum(obj["context_buckets"].values()), 10)
        self.assertEqual(len(obj["context_buckets"]), 6)
        self.assertFalse(obj["cross_context_collapse_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
