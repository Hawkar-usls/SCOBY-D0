import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "evidence/reference_context/MAASTRICHT_SOP_RESOLUTION_RECEIPT_V0_6_5_1.json"


def load_receipt():
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def payload_hash(obj):
    payload = dict(obj)
    payload.pop("content_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class TestMaastrichtResolutionV0651(unittest.TestCase):
    def test_receipt_hash_recomputes(self):
        r = load_receipt()
        self.assertEqual(payload_hash(r), r["content_sha256"])

    def test_exact_pair_bound(self):
        self.assertEqual(load_receipt()["pair_id"], "NCT01826162__NCT01983046")

    def test_one_method_context_blocker_is_resolved(self):
        t = load_receipt()["blocker_transition"]
        self.assertEqual(t["from"], "PER_TRIAL_PREANALYTIC_AND_ANALYTICAL_CONTEXT_NOT_YET_BOUND_AS_EXACT_IDENTICAL")
        self.assertEqual(t["to"], "RESOLVED_FOR_BASELINE_SAMPLES_IN_2019_COMBINED_ANALYSIS_SCOPE")

    def test_cohort_independence_remains_unresolved(self):
        r = load_receipt()
        self.assertEqual(r["pair_state"]["cohort_independence"], "UNRESOLVED")
        self.assertIn("PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED", r["remaining_blockers"])

    def test_per_trial_numeric_distributions_remain_unbound(self):
        r = load_receipt()
        self.assertEqual(r["pair_state"]["per_trial_numeric_observations"], "NOT_SEPARATELY_BOUND")
        self.assertIn("PER_TRIAL_BASELINE_SCFA_OBSERVATIONS_NOT_YET_SEPARATELY_EXTRACTION_BOUND", r["remaining_blockers"])

    def test_resolution_does_not_admit_pair(self):
        s = load_receipt()["pair_state"]
        self.assertFalse(s["comparable_ready"])
        self.assertFalse(s["admission_mutation"])
        self.assertEqual(s["new_authoritative_observations"], 0)

    def test_no_pooling_or_averaging(self):
        s = load_receipt()["pair_state"]
        self.assertFalse(s["pooled_reference_created"])
        self.assertFalse(s["averaging_performed"])

    def test_vector_and_pareto_stay_closed(self):
        s = load_receipt()["pair_state"]
        self.assertTrue(s["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(s["pareto_search"], "BLOCKED")

    def test_source_bindings_cover_trials_sop_method_and_collection(self):
        locators = {x["locator"] for x in load_receipt()["evidence"]["source_bindings"]}
        self.assertIn("Methods / Used data sets", locators)
        self.assertIn("Methods / Study design", locators)
        self.assertIn("Methods / Analysis of faecal and circulating SCFA", locators)
        self.assertIn("Methods / Blood collection and biochemical analysis", locators)


if __name__ == "__main__":
    unittest.main(verbosity=2)
