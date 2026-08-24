import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_TOPA_PREGNANCY_RECOVERY_STATE_INTERFACE_CROSS_GATE_1352_v1.0.json"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"
LINEAGE_PATH = ROOT / "RESEARCH_LINEAGE.json"


class TestTopaPregnancyRecoveryCrossGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        cls.lineage = json.loads(LINEAGE_PATH.read_text(encoding="utf-8"))

    def test_cross_domain_gate_is_preregistered_not_empirical(self):
        self.assertEqual(
            self.gate["status"],
            "TOPA_CROSS_DOMAIN_AUDIT_PREREGISTERED_NO_EMPIRICAL_PROMOTION",
        )
        self.assertEqual(self.gate["promotion_logic"]["current"], "P0")
        self.assertEqual(
            self.gate["promotion_logic"]["ceiling_for_this_artifact"],
            "P0_TOPA_CROSS_DOMAIN_PREREGISTRATION",
        )

    def test_existing_scoby_p0_ceiling_is_unchanged(self):
        track = self.status["active_tracks"]["extremophile_reentry_matrix_coupling"]
        self.assertEqual(track["current_promotion"], "P0")
        lineage = self.lineage["lineages"]["extremophile_reentry_matrix_line"]
        self.assertEqual(lineage["status"], "ACTIVE_EXPLORATORY_P0_KINETIC_ANCHOR")

    def test_boy_milk_is_not_promoted_to_material_class(self):
        ceiling = set(self.gate["TOPA_claim_ceiling"])
        self.assertIn("BOY_MILK_IS_NOT_A_STABLE_MODERN_MATERIALS_CLASS", ceiling)
        self.assertIn("MALE_INFANT_MILK_MATERIAL_CLASS_NOT_ESTABLISHED", self.gate["janus_forward_reverse"]["break_edges"])

    def test_portable_state_vector_contains_interface_and_oxygen(self):
        vector = set(self.gate["portable_state_vector"])
        self.assertIn("surface_or_interfacial_tension", vector)
        self.assertIn("oxygen_availability_or_transfer_proxy", vector)
        self.assertIn("osmolarity_or_water_activity_proxy", vector)
        self.assertIn("pH", vector)

    def test_source_labels_cannot_shortcut_mechanism(self):
        labels = set(self.gate["source_label_examples_not_allowed_as_causal_shortcuts"])
        self.assertTrue({"MOTHER_OF_SON", "XY_PLACENTA", "EXTREMOPHILE_RECOVERY"}.issubset(labels))
        self.assertEqual(
            self.gate["new_TOPA_rule_for_SCOBY_D0"],
            "MEASURED_MEDIATOR_VECTOR_PRECEDES_SOURCE_LABEL_INTERPRETATION",
        )

    def test_soluble_and_structural_channels_are_not_collapsed(self):
        arch = self.gate["cross_domain_architecture"]
        self.assertIn("pregnancy_lactation_soluble_channel", arch)
        self.assertIn("extremophile_recovery_soluble_channel", arch)
        self.assertIn("placental_structural_channel", arch)
        self.assertIn("distinct causal routes", arch["non_collapse_rule"])

    def test_kill_rules_can_lower_confidence(self):
        text = " ".join(self.gate["kill_rules"]).lower()
        self.assertIn("reject pvlea4 specificity", text)
        self.assertIn("do not attribute the effect to fetal sex", text)
        self.assertIn("independent-donor replication", text)
        self.assertIn("no matrix-mechanism promotion", text)

    def test_topa_receipt_is_bound(self):
        self.assertEqual(
            self.gate["external_topa_receipt"],
            "Hawkar-usls/TOPA:data/TOPA-SCOBY-PLACENTA-MILK-EXTREMOPHILE-STATE-INTERFACE-CROSS-GATE-2026-08-24-v1.0.json",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
