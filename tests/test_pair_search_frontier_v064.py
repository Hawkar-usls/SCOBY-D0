import copy
import hashlib
import json
import unittest
from pathlib import Path

from pair_search_frontier import (
    assert_frontier_ceiling,
    pair_is_admissible_from_frontier,
    ranked_frontier,
    validate_frontier,
)

ROOT = Path(__file__).resolve().parents[1]
FRONTIER_PATH = ROOT / "experiments/SCOBY-D0-HARDENED-PAIR-SEARCH-FRONTIER-v0.6.4.json"


def load_frontier():
    return json.loads(FRONTIER_PATH.read_text(encoding="utf-8"))


class TestPairSearchFrontierV064(unittest.TestCase):
    def test_frontier_hash_recomputes(self):
        obj = load_frontier()
        expected = obj.pop("content_sha256")
        payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), expected)

    def test_real_frontier_is_valid_and_has_zero_ready_pairs(self):
        f = load_frontier()
        self.assertEqual(validate_frontier(f), [])
        self.assertEqual(f["frontier_state"]["pair_count"], 3)
        self.assertEqual(f["frontier_state"]["real_hardened_ready_pairs"], 0)
        assert_frontier_ceiling(f)

    def test_frontier_cannot_admit_any_pair(self):
        for pair in load_frontier()["pairs"]:
            self.assertFalse(pair_is_admissible_from_frontier(pair))

    def test_ranking_cannot_mutate_admission_state(self):
        f = load_frontier()
        before = copy.deepcopy(f["frontier_state"])
        ranked = ranked_frontier(f)
        self.assertEqual(len(ranked), 3)
        self.assertEqual(f["frontier_state"], before)
        self.assertTrue(all(not pair_is_admissible_from_frontier(p) for p in ranked))

    def test_yale_pair_is_adversarial_overlap_case(self):
        pair = next(p for p in load_frontier()["pairs"] if p["pair_id"] == "GALUPPO_2021__GALUPPO_2023")
        self.assertEqual(pair["adversarial_case"]["protocol_match"], "HIGH")
        self.assertEqual(pair["adversarial_case"]["publication_identity"], "DISTINCT")
        self.assertEqual(pair["adversarial_case"]["cohort_independence"], "FAIL_CONFIRMED_OVERLAP")
        self.assertIn("PARTICIPANT_OVERLAP_CONFIRMED", pair["blockers"])
        self.assertEqual(pair["verdict"], "PROTOCOL_MATCH_BUT_INDEPENDENCE_FAIL")

    def test_distinct_publications_do_not_override_overlap(self):
        pair = next(p for p in load_frontier()["pairs"] if p["pair_id"] == "GALUPPO_2021__GALUPPO_2023")
        self.assertNotEqual(pair["source_A"]["pmid"], pair["source_B"]["pmid"])
        self.assertFalse(pair_is_admissible_from_frontier(pair))

    def test_pomare_akanji_preserves_fasting_and_uncertainty_mismatches(self):
        pair = next(p for p in load_frontier()["pairs"] if p["pair_id"] == "POMARE_1985__AKANJI_1991")
        self.assertIn("FASTING_DURATION_16H_VS_UNRESOLVED", pair["blockers"])
        self.assertIn("UNCERTAINTY_SEMANTICS_SEM_VS_SD", pair["blockers"])
        self.assertIn("SPECIMEN_VENOUS_BLOOD_VS_PLASMA", pair["blockers"])

    def test_pouteau_yale_preserves_tracer_protocol_mismatch(self):
        pair = next(p for p in load_frontier()["pairs"] if p["pair_id"] == "POUTEAU_1998__GALUPPO_2021")
        self.assertIn("TRACER_ISOTOPE_1_13C_ACETATE_VS_D3_ACETATE", pair["blockers"])
        self.assertIn("TRACER_DURATION_7H_VS_10H", pair["blockers"])
        self.assertEqual(pair["verdict"], "NOT_HARDENED_COMPARABLE")

    def test_frontier_must_keep_vector_unset_and_pareto_blocked(self):
        state = load_frontier()["frontier_state"]
        self.assertTrue(state["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(state["pareto_search"], "BLOCKED")
        self.assertFalse(state["pooled_reference_created"])
        self.assertFalse(state["averaging_performed"])

    def test_missing_blocker_invalidates_frontier(self):
        f = load_frontier()
        f["pairs"][0]["blockers"] = []
        errs = validate_frontier(f)
        self.assertTrue(any(e.startswith("BLOCKERS_REQUIRED") for e in errs))

    def test_frontier_authority_mutation_fails_validation(self):
        f = load_frontier()
        f["frontier_state"]["new_authoritative_observations"] = 1
        self.assertIn("FRONTIER_MUST_NOT_CREATE_AUTHORITATIVE_OBSERVATIONS", validate_frontier(f))


if __name__ == "__main__":
    unittest.main(verbosity=2)
