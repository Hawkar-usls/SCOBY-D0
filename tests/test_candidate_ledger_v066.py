import json
import unittest
from pathlib import Path

from candidate_ledger import (
    assert_candidate_ledger_ceiling,
    candidate_can_admit_from_ledger,
    canonical_payload_sha256,
    key_differences,
    measurement_key_is_fully_bound,
    rank_candidate_pairs,
    replay_candidates_through_v063,
)
from cross_study_hardening import ALL_FIELDS


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "evidence" / "reference_context" / "HARDENED_CANDIDATE_LEDGER_V0_6_6.json"


def load_ledger():
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))


def by_id(ledger, candidate_id):
    return next(c for c in ledger["candidates"] if c["candidate_id"] == candidate_id)


class TestCandidateLedgerV066(unittest.TestCase):
    def setUp(self):
        self.ledger = load_ledger()

    def test_ledger_hash_recomputes(self):
        self.assertEqual(canonical_payload_sha256(self.ledger), self.ledger["content_sha256"])

    def test_ledger_field_order_is_exact_v063_surface(self):
        self.assertEqual(tuple(self.ledger["hardened_key_fields"]), ALL_FIELDS)

    def test_ledger_has_no_admission_authority(self):
        for candidate in self.ledger["candidates"]:
            self.assertFalse(candidate_can_admit_from_ledger(candidate))

    def test_masld_measurement_key_is_fully_bound(self):
        c = by_id(self.ledger, "MASLD_2024_HEALTHY_CONTROL_ACETATE")
        self.assertTrue(measurement_key_is_fully_bound(c))
        self.assertEqual(c["numeric_observation"]["estimate"], 57.6)
        self.assertEqual(c["numeric_observation"]["uncertainty_semantics"], "SD")

    def test_usda_measurement_key_is_fully_bound_and_conversion_bound(self):
        c = by_id(self.ledger, "USDA_NPS_2024_HEALTHY_ACETATE")
        self.assertTrue(measurement_key_is_fully_bound(c))
        self.assertEqual(c["numeric_observation"]["estimate"], 80.0)
        self.assertEqual(c["numeric_observation"]["source_estimate"], 0.08)

    def test_two_complete_singles_are_not_exact_pair(self):
        a = by_id(self.ledger, "MASLD_2024_HEALTHY_CONTROL_ACETATE")
        b = by_id(self.ledger, "USDA_NPS_2024_HEALTHY_ACETATE")
        self.assertEqual(
            key_differences(a, b),
            ["fasting_duration", "preanalytic_handling", "analytical_method_family"],
        )

    def test_four_hour_fast_is_not_twelve_hour_water_only(self):
        a = by_id(self.ledger, "MASLD_2024_HEALTHY_CONTROL_ACETATE")
        b = by_id(self.ledger, "USDA_NPS_2024_HEALTHY_ACETATE")
        self.assertNotEqual(a["measurement_key"]["fasting_duration"], b["measurement_key"]["fasting_duration"])

    def test_sd_is_not_ci95(self):
        a = by_id(self.ledger, "USDA_NPS_2024_HEALTHY_ACETATE")
        b = by_id(self.ledger, "RYEWEIGHT2_2026_BASELINE_ACETATE")
        self.assertEqual(a["measurement_key"]["uncertainty_semantics"], "SD")
        self.assertEqual(b["measurement_key"]["uncertainty_semantics"], "CI95")
        self.assertNotEqual(a["measurement_key"]["uncertainty_semantics"], b["measurement_key"]["uncertainty_semantics"])

    def test_edta_is_not_heparin_plasma(self):
        a = by_id(self.ledger, "MASLD_2024_HEALTHY_CONTROL_ACETATE")
        b = by_id(self.ledger, "RYEWEIGHT2_2026_BASELINE_ACETATE")
        self.assertNotEqual(a["measurement_key"]["specimen"], b["measurement_key"]["specimen"])

    def test_fristedt_method_authority_is_not_biological_cohort(self):
        c = by_id(self.ledger, "FRISTEDT_2024_HUMAN_PLASMA_METHOD_AUTHORITY")
        self.assertEqual(c["candidate_class"], "METHOD_AUTHORITY_ONLY")
        self.assertEqual(c["cohort_independence_status"], "NOT_A_SINGLE_COHORT")
        self.assertFalse(measurement_key_is_fully_bound(c))

    def test_protocol_method_binding_is_not_numeric_observation(self):
        c = by_id(self.ledger, "DRB_2025_HEALTHY_PLASMA_ORGANIC_ACIDS")
        self.assertEqual(c["candidate_class"], "PROTOCOL_METHOD_BOUND_NUMERIC_UNBOUND")
        self.assertIsNone(c["numeric_observation"])
        self.assertFalse(measurement_key_is_fully_bound(c))

    def test_ranking_is_discovery_only(self):
        ranked = rank_candidate_pairs(self.ledger["candidates"])
        self.assertGreater(len(ranked), 0)
        self.assertTrue(all(x["admission_effect"] == "NONE" for x in ranked))
        self.assertEqual(self.ledger["dry_run_state"]["admission_mutations"], 0)

    def test_real_ledger_replays_fail_closed_and_ceiling_stays_closed(self):
        result = replay_candidates_through_v063(self.ledger["candidates"])
        self.assertEqual(result["hardened_ready_bucket_count"], 0)
        self.assertFalse(result["candidate_ledger_admission_authority"])
        self.assertFalse(result["pooled_reference_created"])
        self.assertFalse(result["averaging_performed"])
        self.assertTrue(result["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(result["pareto_search"], "BLOCKED")
        assert_candidate_ledger_ceiling(self.ledger)


if __name__ == "__main__":
    unittest.main()
