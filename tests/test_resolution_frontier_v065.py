import copy
import json
import unittest
from pathlib import Path

from resolution_frontier import (
    canonical_payload_sha256,
    distinct_trial_ids_establish_independent_cohorts,
    pair_can_admit_from_resolution_frontier,
    resolution_summary,
    same_lab_establishes_same_method,
    validate_frontier,
)

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "experiments/SCOBY-D0-COHORT-METHOD-RESOLUTION-FRONTIER-v0.6.5.json"


def load_frontier():
    return json.loads(FRONTIER.read_text(encoding="utf-8"))


def pair(pair_id):
    return next(p for p in load_frontier()["near_pairs"] if p["pair_id"] == pair_id)


class TestResolutionFrontierV065(unittest.TestCase):
    def test_real_frontier_validates_and_has_zero_ready_pairs(self):
        f = load_frontier()
        validate_frontier(f)
        self.assertEqual(f["frontier_state"]["real_hardened_ready_pairs"], 0)
        self.assertEqual(f["frontier_state"]["near_pair_count"], 3)

    def test_frontier_hash_recomputes(self):
        f = load_frontier()
        self.assertEqual(canonical_payload_sha256(f), f["content_sha256"])

    def test_resolution_frontier_cannot_admit(self):
        for p in load_frontier()["near_pairs"]:
            self.assertFalse(pair_can_admit_from_resolution_frontier(p))

    def test_distinct_trial_ids_do_not_prove_distinct_cohorts(self):
        p = pair("NCT01826162__NCT01983046")
        self.assertNotEqual(p["source_A"]["trial_id"], p["source_B"]["trial_id"])
        self.assertFalse(distinct_trial_ids_establish_independent_cohorts(p))
        self.assertIn("PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED", p["blockers"])

    def test_nonoverlapping_trial_windows_do_not_clear_overlap_blocker(self):
        p = pair("NCT01826162__NCT01983046")
        self.assertIn("NONOVERLAPPING_REPORTED_TRIAL_WINDOWS", p["positive_resolution_evidence"])
        self.assertIn("PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED", p["blockers"])

    def test_same_lab_does_not_prove_same_method(self):
        p = pair("NCT03293693__NCT03658681")
        self.assertEqual(p["source_A"]["lab"], p["source_B"]["lab"])
        self.assertFalse(same_lab_establishes_same_method(p))
        self.assertEqual(p["source_A"]["analytical_method_family"], "UNRESOLVED_IN_PRIMARY_ARTICLE")
        self.assertIn("SAME_LAB_DOES_NOT_ESTABLISH_SAME_METHOD", p["blockers"])

    def test_oslo_near_pair_preserves_method_and_cohort_blockers(self):
        p = pair("NCT03293693__NCT03658681")
        self.assertIn("PARTICIPANT_REUSE_NOT_EXPLICITLY_EXCLUDED", p["blockers"])
        self.assertIn("SCFA_ANALYTICAL_METHOD_UNRESOLVED_FOR_NCT03293693", p["blockers"])
        self.assertGreaterEqual(resolution_summary(p)["positive_evidence_count"], 6)
        self.assertFalse(resolution_summary(p)["admissible_from_frontier"])

    def test_vitas_method_contrast_is_not_exact_comparability(self):
        p = pair("NCT01034436_NW__NCT03658681")
        self.assertEqual(p["source_A"]["lab"], p["source_B"]["lab"])
        self.assertEqual(p["source_A"]["analytical_method_family"], "GC_MS")
        self.assertEqual(p["source_B"]["analytical_method_family"], "LC_MS_MS")
        self.assertIn("ANALYTICAL_METHOD_FAMILY_GC_MS_VS_LC_MS_MS", p["blockers"])

    def test_removing_blockers_does_not_turn_frontier_into_admission_channel(self):
        p = copy.deepcopy(pair("NCT03293693__NCT03658681"))
        p["blockers"] = []
        self.assertFalse(pair_can_admit_from_resolution_frontier(p))

    def test_forbidden_authority_mutation_fails_validation(self):
        f = load_frontier()
        f["frontier_state"]["new_authoritative_observations"] = 1
        f.pop("content_sha256", None)
        with self.assertRaises(ValueError):
            validate_frontier(f)

    def test_vector_and_pareto_remain_closed(self):
        s = load_frontier()["frontier_state"]
        self.assertTrue(s["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(s["pareto_search"], "BLOCKED")
        self.assertFalse(s["pooled_reference_created"])
        self.assertFalse(s["averaging_performed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
