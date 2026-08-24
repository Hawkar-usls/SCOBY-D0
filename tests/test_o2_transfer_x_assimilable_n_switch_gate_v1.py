import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_O2_TRANSFER_X_ASSIMILABLE_N_SWITCH_GATE_1550_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "O2_TRANSFER_X_ASSIMILABLE_N_SWITCH_MATRIX_v1.0.csv"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"
MEDIATION_PATH = ROOT / "CAUSAL_MEDIATION_STATUS.json"


class TestO2TransferXAssimilableNSwitchGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        cls.mediation = json.loads(MEDIATION_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_gate_stays_p0(self):
        self.assertEqual(
            self.gate["status"],
            "P0_PREREGISTERED_O2_TRANSFER_X_ASSIMILABLE_N_SWITCH_NO_DATA",
        )
        self.assertEqual(self.gate["current_promotion"], "P0")
        self.assertEqual(self.gate["claim_ceiling"]["current"], "P0")
        self.assertEqual(
            self.status["active_tracks"]["cross_domain_state_interface_equivalence"]["current_promotion"],
            "P0",
        )

    def test_stage_a_is_complete_3x3(self):
        a = [r for r in self.rows if r["stage"] == "STAGE_A"]
        self.assertEqual(len(a), 9)
        combos = {(r["o2_transfer_zone"], r["assimilable_n_zone"]) for r in a}
        expected = {
            (o, n)
            for o in ["O1_LOW", "O2_MID", "O3_HIGH"]
            for n in ["N1_LOW", "N2_MID", "N3_HIGH"]
        }
        self.assertEqual(combos, expected)

    def test_n_source_identity_is_frozen(self):
        a = [r for r in self.rows if r["stage"] == "STAGE_A"]
        self.assertEqual(
            {r["n_source_identity"] for r in a},
            {"ONE_DEFINED_ASSIMILABLE_N_SOURCE_IDENTITY_FROZEN"},
        )
        self.assertIn(
            "ASSIMILABLE_N_AMOUNT_NE_N_SOURCE_IDENTITY",
            self.gate["central_invariants"],
        )

    def test_oxygen_factor_is_transfer_not_gas_fraction(self):
        axis = self.gate["factors"]["o2_transfer_axis"]
        self.assertIn("measured oxygen-transfer state", axis["rule"])
        self.assertIn("O2_GAS_FRACTION_NE_O2_TRANSFER_STATE", self.gate["central_invariants"])

    def test_co2_and_context_are_bounded(self):
        self.assertIn("pCO2_or_validated_CO2_proxy", self.gate["fixed_or_bounded_context"])
        self.assertIn("mixing_or_shear_context", self.gate["fixed_or_bounded_context"])
        for r in self.rows:
            if r["stage"] == "STAGE_A":
                self.assertEqual(r["co2_state"], "FIXED_OR_BOUNDED")

    def test_bc_mass_is_not_carbon_flux(self):
        inv = set(self.gate["central_invariants"])
        self.assertIn("BC_MASS_NE_CARBON_FLUX", inv)
        self.assertIn(
            "CARBON_ALLOCATION_CLAIM_REQUIRES_MEASURED_CARBON_BALANCE_OR_MUST_BE_LABELLED_PARTIAL_PROXY",
            inv,
        )
        self.assertEqual(self.gate["primary_endpoint"]["name"], "BC_CARBON_ALLOCATION_PROXY")

    def test_switch_requires_noncollapsed_cells(self):
        req = set(self.gate["switch_candidate_definition"])
        self.assertIn(
            "CELL_ACTIVITY_OR_VIABILITY_REMAINS_WITHIN_PREDECLARED_NONCOLLAPSE_BOUND",
            req,
        )
        r2 = next(x for x in self.gate["decision_rules"] if x["id"] == "R2_CELL_COLLAPSE")
        self.assertIn("STRESS_OR_STARVATION", r2["then"])

    def test_additive_vs_interaction_is_heldout_predictive(self):
        model = self.gate["model_gate"]
        self.assertIn("O2_TRANSFER:ASSIMILABLE_N", model["interaction_model"])
        text = " ".join(model["promotion_requires"]).replace("_", " ")
        self.assertIn("heldout prediction", text)
        self.assertIn("additive model", text)

    def test_stage_b_is_algorithmic_not_hand_tuned(self):
        b = [r for r in self.rows if r["stage"] == "STAGE_B"]
        self.assertEqual(len(b), 5)
        self.assertIn("frozen deterministic rule", self.gate["stage_b_selection_rule"]["rule"])
        self.assertTrue(all("GRADIENT" in r["selection_rule"] or "CONTROL" in r["selection_rule"] or "FLANK" in r["selection_rule"] for r in b))

    def test_stage_c_is_independent_confirmation(self):
        c = [r for r in self.rows if r["stage"] == "STAGE_C"]
        self.assertEqual(len(c), 3)
        self.assertTrue(all("INDEPENDENT_BATCH" in r["selection_rule"] for r in c))

    def test_full_pass_is_domain_bounded(self):
        ceiling = self.gate["claim_ceiling"]
        self.assertEqual(
            ceiling["full_gate_pass_allows"],
            "DOMAIN_BOUNDED_O2_TRANSFER_X_ASSIMILABLE_N_ALLOCATION_SWITCH_CANDIDATE",
        )
        self.assertIn("UNIVERSAL_BIOLOGICAL_LAW", ceiling["does_not_allow"])
        self.assertIn("MATERIAL_MEMORY", ceiling["does_not_allow"])

    def test_mediation_status_binds_switch_gate(self):
        self.assertEqual(
            self.mediation["o2_transfer_x_assimilable_n_switch_gate"],
            GATE_PATH.name,
        )
        self.assertEqual(
            self.mediation["o2_transfer_x_assimilable_n_switch_state"],
            "PREREGISTERED_3X3_PLUS_RIDGE_CONFIRMATION_NO_DATA",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
