import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_CAUSAL_MEDIATOR_RESCUE_GATE_1429_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "CAUSAL_MEDIATOR_RESCUE_MATRIX_v1.0.csv"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"


class TestCausalMediatorRescueGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_current_evidence_ceiling_remains_p0(self):
        self.assertEqual(
            self.gate["status"],
            "P0_PREREGISTERED_CAUSAL_MEDIATION_GATE_NO_EMPIRICAL_EFFECT",
        )
        self.assertEqual(self.gate["claim_ceiling"]["current"], "P0")
        cross = self.status["active_tracks"]["cross_domain_state_interface_equivalence"]
        self.assertEqual(cross["current_promotion"], "P0")

    def test_source_factor_must_remain_present_during_rescue(self):
        requirements = set(self.gate["compensator_requirements"])
        self.assertIn(
            "DOES_NOT_CHANGE_SOURCE_FACTOR_IDENTITY_OR_REMOVE_SOURCE_FACTOR_FROM_SYSTEM",
            requirements,
        )
        rescue = next(r for r in self.rows if r["arm_id"] == "C3")
        self.assertEqual(rescue["source_factor"], "SOURCE_FACTOR")
        self.assertEqual(rescue["compensator"], "COMPENSATOR")

    def test_compensator_is_selected_without_bc_outcome_feedback(self):
        requirements = set(self.gate["compensator_requirements"])
        self.assertIn("SELECTED_WITHOUT_BC_OUTCOME_FEEDBACK", requirements)
        sequence = self.gate["preregistered_sequence"]
        self.assertLess(
            sequence.index("FREEZE_DOSES_TOLERANCES_AND_EQUIVALENCE_MARGIN"),
            sequence.index("STAGE_C_LOCKED_BC_RESCUE_CHALLENGE"),
        )

    def test_rescue_requires_mediator_and_bc_return(self):
        r3 = self.gate["promotion_logic"]["R3"]
        self.assertIn("MEDIATOR_RESCUED", r3)
        self.assertIn("BC_RETURNS_WITHIN_FROZEN_EQUIVALENCE_BOUND", r3)

    def test_orthogonal_sufficiency_and_counter_rescue_are_present(self):
        by_id = {r["arm_id"]: r for r in self.rows}
        self.assertEqual(by_id["C5"]["orthogonal_reference"], "ORTHOGONAL_MEDIATOR_REFERENCE")
        self.assertEqual(by_id["C6"]["orthogonal_reference"], "ORTHOGONAL_MEDIATOR_REFERENCE")
        self.assertEqual(by_id["C6"]["compensator"], "COUNTER_RESCUE")
        self.assertIn("BIDIRECTIONAL_MEDIATOR_CONTROL", self.gate["promotion_logic"]["R4"])

    def test_dirty_compensator_kills_rescue_claim(self):
        kill = " ".join(self.gate["kill_rules"])
        self.assertIn("COMPENSATOR_ONLY_CHANGES_BC_MATERIALLY", kill)
        self.assertIn("COMPENSATOR_CHANGES_SOURCE_FACTOR_IDENTITY_OR_AVAILABILITY", kill)

    def test_mediator_rescue_without_bc_rescue_blocks_mediation(self):
        self.assertIn(
            "MEDIATOR_RESCUED_BUT_BC_REMAINS_SOURCE_SHIFTED",
            self.gate["promotion_logic"]["R2"],
        )

    def test_full_pass_is_domain_bounded_not_universal_law(self):
        ceiling = self.gate["claim_ceiling"]
        self.assertEqual(
            ceiling["full_gate_pass_allows"],
            "STRONG_CAUSAL_MEDIATOR_CANDIDATE_WITHIN_TESTED_DOMAIN",
        )
        self.assertIn("UNIVERSAL_BIOLOGICAL_LAW", ceiling["does_not_allow"])
        self.assertIn("MATERIAL_MEMORY", ceiling["does_not_allow"])

    def test_no_human_material_is_used(self):
        self.assertIn("no donor human milk", self.gate["safety_scope"].lower())
        self.assertIn("no donor human milk", self.gate["safety_scope"].lower())
        self.assertNotIn("DONOR_HUMAN_MILK", {r["source_factor"] for r in self.rows})


if __name__ == "__main__":
    unittest.main(verbosity=2)
