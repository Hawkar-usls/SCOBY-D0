import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "evidence/reference_context/OSLO_PUBLIC_METHOD_COHORT_EVIDENCE_BOUNDARY_V0_6_5_4.json"


def load_boundary():
    return json.loads(BOUNDARY.read_text(encoding="utf-8"))


def canonical_hash(obj):
    payload = dict(obj)
    payload.pop("content_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class TestOsloPublicEvidenceBoundaryV0654(unittest.TestCase):
    def test_boundary_hash_recomputes(self):
        b = load_boundary()
        self.assertEqual(canonical_hash(b), b["content_sha256"])

    def test_both_scfa_methods_remain_unresolved(self):
        r = load_boundary()["public_search_result"]
        self.assertEqual(r["NCT03293693_scfa_method"], "UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE")
        self.assertEqual(r["NCT03658681_scfa_method"], "UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE")
        self.assertEqual(r["method_identity"], "NOT_ESTABLISHED")

    def test_shared_vitas_lab_does_not_establish_method_identity(self):
        r = load_boundary()["public_search_result"]
        self.assertEqual(r["same_commercial_lab"], "VITAS_ANALYTICAL_SERVICE")
        self.assertIn("SAME_LAB_IMPLIES_SAME_METHOD", r["inference_prohibited"])
        self.assertIn("SAME_LAB_NE_SAME_METHOD", load_boundary()["invariants"])

    def test_two_unknown_methods_do_not_match(self):
        b = load_boundary()
        self.assertIn("TWO_UNRESOLVED_METHODS_NE_METHOD_IDENTITY", b["invariants"])
        self.assertIn("UNKNOWN_A_AND_UNKNOWN_B_NE_ESTABLISHED_EQUALITY", b["invariants"])
        self.assertIn("METHOD_IDENTITY_NOT_ESTABLISHED", b["remaining_blockers"])

    def test_nonoverlapping_study_periods_do_not_prove_nonreuse(self):
        r = load_boundary()["public_search_result"]
        self.assertTrue(r["study_periods_nonoverlapping"])
        self.assertIn("NONOVERLAPPING_STUDY_PERIODS_IMPLY_NO_PARTICIPANT_REUSE", r["inference_prohibited"])
        self.assertEqual(r["participant_overlap_or_nonoverlap"], "UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE")

    def test_distinct_ethics_approvals_do_not_prove_distinct_cohorts(self):
        r = load_boundary()["public_search_result"]
        self.assertTrue(r["ethics_approvals_distinct"])
        self.assertIn("DISTINCT_ETHICS_APPROVALS_IMPLY_DISTINCT_COHORTS", r["inference_prohibited"])
        self.assertIn("DISTINCT_ETHICS_APPROVALS_NE_DISTINCT_COHORT_PROOF", load_boundary()["invariants"])

    def test_adjacent_bile_acid_method_remains_separate_from_scfa(self):
        b = load_boundary()
        nct036 = next(x for x in b["checked_public_primary_evidence"] if x["trial_id"] == "NCT03658681" and x["source_type"] == "PRIMARY_ARTICLE")
        self.assertIn("LC_MS_MS_QTRAP5500_KINETEX_BIPHENYL_METHOD_EXPLICITLY_BOUND_TO_NINE_BILE_ACIDS", nct036["established"])
        self.assertIn("SCFA_ANALYTICAL_METHOD_FAMILY", nct036["not_established"])
        self.assertIn("ADJACENT_BILE_ACID_METHOD_NE_SCFA_METHOD", b["invariants"])

    def test_boundary_does_not_mutate_authority_or_pool(self):
        s = load_boundary()["state_after_boundary"]
        self.assertEqual(s["authoritative_observations"], 10)
        self.assertEqual(s["real_hardened_ready_pairs"], 0)
        self.assertEqual(s["new_authoritative_observations"], 0)
        self.assertFalse(s["admission_mutation"])
        self.assertFalse(s["pooled_reference_created"])
        self.assertFalse(s["averaging_performed"])

    def test_vector_and_pareto_remain_closed(self):
        s = load_boundary()["state_after_boundary"]
        self.assertTrue(s["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(s["pareto_search"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
