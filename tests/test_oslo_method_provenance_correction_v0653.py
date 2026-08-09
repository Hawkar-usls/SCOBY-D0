import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORRECTION = ROOT / "evidence/reference_context/OSLO_SCFA_METHOD_PROVENANCE_CORRECTION_V0_6_5_3.json"
HISTORICAL = ROOT / "experiments/SCOBY-D0-COHORT-METHOD-RESOLUTION-FRONTIER-v0.6.5.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(obj):
    payload = dict(obj)
    payload.pop("content_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def corrected_pair(pair_id):
    return next(x for x in load(CORRECTION)["affected_records"] if x["pair_id"] == pair_id)


class TestOsloMethodProvenanceCorrectionV0653(unittest.TestCase):
    def test_correction_hash_recomputes(self):
        c = load(CORRECTION)
        self.assertEqual(canonical_hash(c), c["content_sha256"])

    def test_historical_object_is_preserved_not_rewritten(self):
        c = load(CORRECTION)
        h = load(HISTORICAL)
        self.assertFalse(c["parent_state"]["historical_object_rewritten"])
        self.assertEqual(h["content_sha256"], c["parent_state"]["historical_frontier_sha256"])

    def test_nct036_scfa_method_is_corrected_to_unresolved(self):
        p = corrected_pair("NCT03293693__NCT03658681")
        self.assertEqual(p["corrected_binding"]["NCT03658681_scfa_method"], "UNRESOLVED_IN_PRIMARY_ARTICLE")

    def test_nct036_lcms_method_remains_bound_to_bile_acids(self):
        p = corrected_pair("NCT03293693__NCT03658681")
        self.assertEqual(
            p["corrected_binding"]["NCT03658681_bile_acid_method"],
            "LC_MS_MS_QTRAP5500_KINETEX_BIPHENYL_NEGATIVE_MRM",
        )

    def test_two_unknown_methods_do_not_establish_identity(self):
        p = corrected_pair("NCT03293693__NCT03658681")
        self.assertEqual(p["corrected_binding"]["NCT03293693_scfa_method"], "UNRESOLVED_IN_PRIMARY_ARTICLE")
        self.assertEqual(p["corrected_binding"]["NCT03658681_scfa_method"], "UNRESOLVED_IN_PRIMARY_ARTICLE")
        self.assertIn("TWO_UNRESOLVED_METHODS_DO_NOT_ESTABLISH_METHOD_IDENTITY", p["corrected_blockers"])
        self.assertIn("UNKNOWN_A_AND_UNKNOWN_B_NE_ESTABLISHED_EQUALITY", load(CORRECTION)["new_invariants"])

    def test_adjacent_bile_acid_method_cannot_leak_to_scfa(self):
        inv = load(CORRECTION)["new_invariants"]
        self.assertIn("ADJACENT_METHOD_TEXT_NE_ANALYTE_METHOD_BINDING", inv)
        self.assertIn("SCFA_MEASUREMENT_NE_BILE_ACID_MEASUREMENT", inv)

    def test_nct010_scfa_gc_ms_binding_is_preserved(self):
        p = corrected_pair("NCT01034436_NW__NCT03658681")
        self.assertEqual(p["corrected_binding"]["NCT01034436_scfa_method"], "GC_MS")
        self.assertEqual(p["corrected_binding"]["NCT03658681_scfa_method"], "UNRESOLVED_IN_PRIMARY_ARTICLE")
        self.assertEqual(p["corrected_verdict"], "METHOD_IDENTITY_UNRESOLVED_NOT_CONFIRMED_METHOD_CONTRAST")

    def test_correction_does_not_mutate_authority(self):
        s = load(CORRECTION)["state_after_correction"]
        self.assertEqual(s["authoritative_observations"], 10)
        self.assertEqual(s["new_authoritative_observations"], 0)
        self.assertFalse(s["admission_mutation"])
        self.assertEqual(s["real_hardened_ready_pairs"], 0)

    def test_no_pooling_or_averaging(self):
        s = load(CORRECTION)["state_after_correction"]
        self.assertFalse(s["pooled_reference_created"])
        self.assertFalse(s["averaging_performed"])

    def test_vector_and_pareto_remain_closed(self):
        s = load(CORRECTION)["state_after_correction"]
        self.assertTrue(s["biological_reference_vector"].startswith("UNSET"))
        self.assertEqual(s["pareto_search"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
