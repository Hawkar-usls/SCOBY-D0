import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_CROSS_DOMAIN_INTERFACE_EQUIVALENCE_GATE_1416_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "CROSS_DOMAIN_DEFINED_INTERFACE_EQUIVALENCE_MATRIX_v1.0.csv"
LINEAGE_PATH = ROOT / "RESEARCH_LINEAGE.json"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"


class TestCrossDomainInterfaceEquivalenceGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.lineage = json.loads(LINEAGE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_gate_is_preregistered_and_stays_p0(self):
        self.assertEqual(
            self.gate["status"],
            "PREREGISTERED_CROSS_DOMAIN_EQUIVALENCE_TEST_NO_EMPIRICAL_BC_EFFECT",
        )
        self.assertEqual(self.gate["current_promotion"], "P0")
        self.assertEqual(self.gate["promotion_logic"]["current"], "P0")

    def test_ten_arm_matrix_is_frozen(self):
        self.assertEqual(len(self.rows), 10)
        self.assertEqual({r["condition_id"] for r in self.rows}, {f"C{i}" for i in range(10)})

    def test_distinct_defined_families_exist(self):
        identities = {r["input_identity"] for r in self.rows}
        for required in {
            "PVLEA4",
            "HUMAN_LACTOFERRIN",
            "DPPC_ONLY",
            "HUMAN_LACTOFERRIN_PLUS_DPPC",
            "GENERIC_SOLUBLE_PROTEIN",
            "TREHALOSE",
            "LACTOSE",
            "NON_NUTRITIONAL_SURFACE_TENSION_REFERENCE",
        }:
            self.assertIn(required, identities)

    def test_stage_a_precedes_bc_outcomes(self):
        stage_a = self.gate["stage_A_abiotic_calibration"]
        self.assertFalse(stage_a["bc_producer_present"])
        self.assertIn("frozen before Stage-B BC outcomes", stage_a["dose_lock_rule"])
        self.assertIn("Outcome-driven widening of tolerances is forbidden", stage_a["pair_match_tolerance_rule"])

    def test_core_mediator_vector_is_measured(self):
        core = set(self.gate["portable_mediator_vector"]["pair_match_core"])
        self.assertEqual(
            core,
            {
                "surface_or_interfacial_tension",
                "dissolved_oxygen_or_oxygen_transfer_proxy",
                "pH",
                "osmolality_or_water_activity_proxy",
            },
        )

    def test_equivalence_is_not_nonsignificance(self):
        logic = self.gate["equivalence_logic"]
        self.assertEqual(logic["not_equal_to"], "failure_to_reject_a_difference_test")
        self.assertIn("p > 0.05 alone is not evidence of equivalence", logic["required"])
        self.assertIn("frozen before treatment outcomes", logic["equivalence_margin_rule"])

    def test_source_label_shortcuts_are_killed(self):
        kill_text = " ".join(self.gate["kill_rules"])
        self.assertIn("No empirical BC promotion from source labels alone", kill_text)
        self.assertIn("MOTHER_OF_SON", kill_text)
        self.assertIn("XY_PLACENTA", kill_text)
        self.assertIn("generic protein", kill_text)
        self.assertIn("DPPC alone", kill_text)

    def test_no_human_material_in_this_gate(self):
        boundary = self.gate["human_material_boundary"]
        self.assertFalse(boundary["human_milk_used_in_this_gate"])
        self.assertFalse(boundary["placental_tissue_used_in_this_gate"])
        self.assertTrue(boundary["defined_components_only"])

    def test_material_memory_remains_closed(self):
        self.assertEqual(
            self.gate["material_memory_future_gate"]["status"],
            "CLOSED_UNTIL_SHARED_OR_SOURCE_SPECIFIC_CAUSAL_MEDIATOR_IS_REPLICATED",
        )

    def test_old_extremophile_ceiling_is_preserved(self):
        old_line = self.lineage["lineages"]["extremophile_reentry_matrix_line"]
        self.assertEqual(old_line["status"], "ACTIVE_EXPLORATORY_P0_KINETIC_ANCHOR")
        old_track = self.status["active_tracks"]["extremophile_reentry_matrix_coupling"]
        self.assertEqual(old_track["current_promotion"], "P0")

    def test_new_cross_domain_track_is_bound_and_p0(self):
        track = self.lineage["lineages"]["cross_domain_state_interface_line"]
        self.assertEqual(track["status"], "ACTIVE_EXPLORATORY_P0_PREREGISTERED")
        self.assertIn(GATE_PATH.name, track["artifacts"])
        self.assertIn(str(MATRIX_PATH.relative_to(ROOT)), track["artifacts"])
        project = self.status["active_tracks"]["cross_domain_state_interface_equivalence"]
        self.assertEqual(project["current_promotion"], "P0")
        self.assertEqual(project["lead_gate"], GATE_PATH.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
