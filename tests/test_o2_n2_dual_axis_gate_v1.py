import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_O2_N2_DUAL_AXIS_GATE_1537_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "O2_N2_GAS_NUTRIENT_N_DISCRIMINATION_MATRIX_v1.0.csv"


class TestO2N2DualAxisGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_gate_remains_p0(self):
        self.assertEqual(
            self.gate["status"],
            "PREREGISTERED_GAS_VS_NUTRIENT_N_DISCRIMINATION_NO_EMPIRICAL_BC_EFFECT",
        )
        self.assertEqual(self.gate["current_promotion"], "P0")

    def test_gas_n2_and_nutrient_n_are_separate(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("GASEOUS_N2_NE_ASSIMILABLE_NITROGEN", inv)
        self.assertIn("NITROGEN_SOURCE_EFFECT_NE_N2_GAS_EFFECT", inv)

    def test_co2_is_mandatory_confound(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("CO2_MUST_NOT_BE_SILENTLY_ALLOWED_TO_TRACK_GAS_COMPOSITION", inv)
        kill = " ".join(self.gate["kill_rules"])
        self.assertIn("pCO2", kill)

    def test_dissolved_oxygen_not_equal_gas_fraction(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("O2_FRACTION_NE_DISSOLVED_O2_STATE", inv)

    def test_n2_fixation_is_strain_specific_gate(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("N2_FIXATION_CAPABILITY_MUST_BE_VERIFIED_PER_STRAIN", inv)
        r5 = next(x for x in self.gate["decision_rules"] if x["id"] == "R5_N2_FIXATION_ROUTE")
        self.assertIn("strain-specific", r5["if"])
        self.assertIn("THAT_STRAIN_ONLY", r5["then"])

    def test_matrix_has_gas_and_nutrient_axes(self):
        ids = {r["arm_id"] for r in self.rows}
        self.assertTrue({"G0", "G1", "G2", "G3", "N1", "N2", "X1", "X2", "H1"}.issubset(ids))
        self.assertTrue(any(r["gas_axis"] == "N2_FRACTION_SHIFT_PO2_PCO2_MATCHED" for r in self.rows))
        self.assertTrue(any(r["nutrient_n_axis"] == "MATCHED_TOTAL_N_ALTERNATE_SOURCE" for r in self.rows))

    def test_n2_specific_claim_requires_residual_after_matching(self):
        r4 = next(x for x in self.gate["decision_rules"] if x["id"] == "R4_N2_RESIDUAL")
        for token in ["pO2", "dissolved-O2", "pCO2", "nutrient-N"]:
            self.assertIn(token, r4["if"])

    def test_nanobubble_identity_shortcut_is_blocked(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("NANOBUBBLE_OR_GAS_TRANSFER_EFFECT_NE_CHEMICAL_GAS_IDENTITY_EFFECT", inv)

    def test_next_gate_is_abiotic_first(self):
        self.assertIn("ABIOTIC_GAS_VECTOR_CALIBRATION_FIRST", self.gate["next_gate"])
        self.assertIn("CAUSAL_MEDIATOR_RESCUE_TEST", self.gate["next_gate"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
