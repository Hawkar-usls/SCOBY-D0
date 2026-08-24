import csv
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_SOURCE_INVARIANT_RESPONSE_SURFACE_GATE_1424_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "SOURCE_INVARIANT_MEDIATOR_RESPONSE_SURFACE_v1.0.csv"
LINEAGE_PATH = ROOT / "RESEARCH_LINEAGE.json"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"


class TestSourceInvariantResponseSurfaceGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.lineage = json.loads(LINEAGE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_gate_remains_p0(self):
        self.assertEqual(
            self.gate["status"],
            "PREREGISTERED_RESPONSE_SURFACE_TEST_NO_EMPIRICAL_BC_EFFECT",
        )
        self.assertEqual(self.gate["current_promotion"], "P0")
        self.assertEqual(self.gate["promotion_logic"]["current"], "P0")

    def test_four_source_families_span_three_zones(self):
        treatment_rows = [r for r in self.rows if r["source_family"] != "BASELINE"]
        self.assertEqual(len(treatment_rows), 12)
        counts = Counter(r["source_family"] for r in treatment_rows)
        expected = {
            "PVLEA4",
            "HUMAN_LACTOFERRIN",
            "HUMAN_LACTOFERRIN_PLUS_DPPC_INTERFACE_MODEL",
            "NON_NUTRITIONAL_SURFACE_TENSION_REFERENCE",
        }
        self.assertEqual(set(counts), expected)
        self.assertTrue(all(counts[x] == 3 for x in expected))
        for family in expected:
            zones = {r["target_zone"] for r in treatment_rows if r["source_family"] == family}
            self.assertEqual(zones, {"Z1_LOW", "Z2_MID", "Z3_HIGH"})

    def test_zone_targets_are_frozen_before_bc_outcomes(self):
        self.assertIn("before any response-surface BC outcomes", self.gate["zone_freeze_rule"])
        for r in self.rows:
            if r["source_family"] != "BASELINE":
                self.assertEqual(r["input_level_status"], "SELECT_FROM_ABIOTIC_CALIBRATION")
                self.assertEqual(r["mediator_match_required"], "true")

    def test_single_match_point_cannot_establish_common_surface(self):
        kill_text = " ".join(self.gate["kill_rules"])
        self.assertIn("Same phenotype at one matched point is not a common mechanism", kill_text)
        self.assertIn("No common response surface without all preregistered mediator zones", kill_text)

    def test_common_surface_requires_within_zone_equivalence_and_between_zone_response(self):
        req = set(self.gate["required_for_source_invariant_surface_candidate"])
        self.assertIn("WITHIN_ZONE_CROSS_FAMILY_BC_EQUIVALENCE_PASSES_FOR_ALL_PREREGISTERED_ZONES", req)
        self.assertIn("BETWEEN_ZONE_BC_RESPONSE_IS_REPRODUCIBLE_AND_NONFLAT_OR_DIRECTIONALLY_ORDERED_AS_PREREGISTERED", req)

    def test_orthogonal_reference_is_required(self):
        req = set(self.gate["required_for_source_invariant_surface_candidate"])
        self.assertIn("ORTHOGONAL_NON_NUTRITIONAL_INTERFACE_REFERENCE_TRACKS_THE_COMMON_RELATION", req)
        refs = [r for r in self.rows if r["orthogonal_role"] == "ORTHOGONAL_INTERFACE_REFERENCE"]
        self.assertEqual(len(refs), 3)

    def test_source_blind_vs_source_aware_holdout_is_preregistered(self):
        model = self.gate["model_comparison_gate"]
        self.assertTrue(model["same_functional_basis_required"])
        self.assertIn("SOURCE_FAMILY", model["source_aware_model"])
        self.assertNotIn("SOURCE_FAMILY", model["source_blind_model"])
        self.assertIn("held-out batch definition", model["model_family_freeze"])

    def test_source_invariant_claim_fails_if_source_aware_wins(self):
        r3 = next(x for x in self.gate["decision_rules"] if x["id"] == "R3_FAMILY_SPECIFIC_CURVES")
        self.assertIn("source-aware holdout prediction materially outperforms source-blind prediction", r3["if"])

    def test_stronger_causality_and_memory_stay_closed(self):
        self.assertEqual(self.gate["future_necessity_gate"]["status"], "CLOSED")
        self.assertEqual(self.gate["material_memory_gate"]["status"], "CLOSED")
        self.assertIn("does not by itself prove full necessity", self.gate["causal_ceiling_after_R5"])

    def test_parent_cross_domain_track_and_old_extremophile_track_remain_p0(self):
        cross = self.status["active_tracks"]["cross_domain_state_interface_equivalence"]
        self.assertEqual(cross["current_promotion"], "P0")
        old = self.status["active_tracks"]["extremophile_reentry_matrix_coupling"]
        self.assertEqual(old["current_promotion"], "P0")

    def test_lineage_binds_response_surface_artifacts(self):
        track = self.lineage["lineages"]["cross_domain_state_interface_line"]
        self.assertEqual(track["status"], "ACTIVE_EXPLORATORY_P0_PREREGISTERED")
        self.assertIn(GATE_PATH.name, track["artifacts"])
        self.assertIn(str(MATRIX_PATH.relative_to(ROOT)), track["artifacts"])
        project = self.status["active_tracks"]["cross_domain_state_interface_equivalence"]
        self.assertEqual(project["response_surface_gate"], GATE_PATH.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
