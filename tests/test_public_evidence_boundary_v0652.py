import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "evidence/reference_context/MAASTRICHT_PUBLIC_EVIDENCE_BOUNDARY_V0_6_5_2.json"


def load_boundary():
    return json.loads(BOUNDARY.read_text(encoding="utf-8"))


def payload_hash(obj):
    payload = dict(obj)
    payload.pop("content_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class TestPublicEvidenceBoundaryV0652(unittest.TestCase):
    def test_boundary_hash_recomputes(self):
        b = load_boundary()
        self.assertEqual(payload_hash(b), b["content_sha256"])

    def test_pair_remains_exact_maastricht_pair(self):
        self.assertEqual(load_boundary()["pair_id"], "NCT01826162__NCT01983046")

    def test_public_search_does_not_resolve_overlap(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertEqual(r["participant_overlap_or_nonoverlap"], "UNRESOLVED_FROM_PUBLIC_PRIMARY_EVIDENCE")
        self.assertIn("PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED", load_boundary()["remaining_blockers"])

    def test_public_search_does_not_bind_separate_direct_baselines(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertEqual(r["separate_per_trial_direct_reported_baseline_scfa_distributions"], "NOT_ESTABLISHED_FROM_PUBLIC_PRIMARY_EVIDENCE")
        self.assertIn("PER_TRIAL_BASELINE_SCFA_OBSERVATIONS_NOT_YET_SEPARATELY_EXTRACTION_BOUND", load_boundary()["remaining_blockers"])

    def test_figure_digitization_not_silently_promoted(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertFalse(r["figure_digitization_performed"])
        self.assertIn("FIGURE_DIGITIZATION", r["reason_figure_digitization_not_promoted"])
        self.assertIn("extraction error", r["reason_figure_digitization_not_promoted"])

    def test_restricted_data_does_not_authorize_inference(self):
        findings = set()
        for source in load_boundary()["public_sources_checked"]:
            findings.update(source["findings"])
        self.assertIn("INTERVENTION_STUDY_DATA_NOT_PUBLICLY_DEPOSITED_DUE_ETHICAL_AND_PRIVACY_RESTRICTIONS", findings)
        self.assertIn("CONTROLLED_DATA_ACCESS_AVAILABLE_TO_QUALIFIED_RESEARCHERS_BY_REQUEST", findings)
        self.assertIn("RESTRICTED_DATA_NE_PERMISSION_TO_INFER_MISSING_VALUES", load_boundary()["invariants"])

    def test_no_external_request_is_invented(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertFalse(r["external_controlled_data_request_sent"])
        self.assertEqual(r["author_contact_or_private_dataset_evidence"], "NOT_ACCESSED")

    def test_boundary_is_not_admission(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertFalse(r["pair_comparable_ready"])
        self.assertFalse(r["admission_mutation"])
        self.assertEqual(r["new_authoritative_observations"], 0)
        self.assertFalse(r["pooled_reference_created"])
        self.assertFalse(r["averaging_performed"])

    def test_vector_and_pareto_remain_closed(self):
        r = load_boundary()["resolution_attempt_result"]
        self.assertTrue(r["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(r["pareto_search"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
