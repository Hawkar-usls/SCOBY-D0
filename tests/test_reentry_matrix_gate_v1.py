import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_EXTREMOPHILE_REENTRY_MATRIX_GATE_0018_v1.0.json"
DESIGN_PATH = ROOT / "experiments" / "POLYPEDILUM_SCOBY_REENTRY_MATRIX_DESIGN_v1.0.csv"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"
LINEAGE_PATH = ROOT / "RESEARCH_LINEAGE.json"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


class TestExtremophileReentryMatrixGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = load_json(GATE_PATH)
        cls.status = load_json(STATUS_PATH)
        cls.lineage = load_json(LINEAGE_PATH)
        with DESIGN_PATH.open("r", encoding="utf-8", newline="") as handle:
            cls.design = list(csv.DictReader(handle))

    def test_gate_is_preregistered_not_empirical(self):
        self.assertEqual(
            self.gate["status"],
            "PREREGISTERED_MECHANISTIC_GATE_NO_EMPIRICAL_SCOBY_EFFECT_YET",
        )
        self.assertEqual(self.gate["promotion_ladder"]["current"], "P0")
        self.assertIn(
            "PV11_TO_SCOBY_MATRIX_MODULATION_IS_UNTESTED",
            self.gate["claim_ceiling"],
        )

    def test_trehalose_and_medium_carryover_controls_are_mandatory(self):
        controls = set(self.gate["mandatory_controls"])
        self.assertIn("TREHALOSE_MATCHED_CONTROL", controls)
        self.assertIn("MEDIUM_CARRYOVER_MATCHED_CONTROL", controls)
        self.assertIn("PH_AND_DISSOLVED_OXYGEN_TRACKING", controls)
        self.assertEqual(self.gate["trehalose_confound"]["status"], "CRITICAL")

    def test_reentry_axis_preserves_function_before_proliferation(self):
        by_time = {
            row["time_after_rehydration"]: row
            for row in self.gate["polypedilum_time_axis"]
        }
        self.assertEqual(by_time["1 h"]["state"], "R1")
        self.assertEqual(by_time["3 h"]["state"], "R2")
        self.assertEqual(by_time["48 h"]["state"], "R3")
        self.assertEqual(by_time["72 h"]["state"], "R4")
        self.assertIn("without significant growth", by_time["48 h"]["anchor"])
        self.assertIn("proliferation begins", by_time["72 h"]["anchor"])

    def test_design_contains_whole_and_cell_free_recovery_conditions(self):
        ids = {row["condition_id"] for row in self.design}
        expected = {
            "R1_1H_WHOLE",
            "R1_1H_CFF",
            "R2_3H_WHOLE",
            "R2_3H_CFF",
            "R2_24H_WHOLE",
            "R2_24H_CFF",
            "R3_48H_WHOLE",
            "R3_48H_CFF",
            "R4_72H_WHOLE",
            "R4_72H_CFF",
            "TREHALOSE_MATCH",
            "MEDIUM_MATCH",
            "NONACTIVE_CELL_CTRL",
        }
        self.assertTrue(expected.issubset(ids))

    def test_kill_rules_fail_closed(self):
        text = "\n".join(self.gate["kill_rules"]).lower()
        self.assertIn("trehalose", text)
        self.assertIn("proliferative", text)
        self.assertIn("independent bc batches", text)
        self.assertIn("pH and oxygen".lower(), text)

    def test_project_status_keeps_marine_lead_and_reentry_p0(self):
        tracks = self.status["active_tracks"]
        self.assertEqual(tracks["marine_oil_sorbent"]["priority"], 1)
        self.assertEqual(tracks["extremophile_reentry_matrix_coupling"]["priority"], 2)
        self.assertEqual(
            tracks["extremophile_reentry_matrix_coupling"]["current_promotion"],
            "P0",
        )

    def test_lineage_binds_all_new_artifacts(self):
        track = self.lineage["lineages"]["extremophile_reentry_matrix_line"]
        artifacts = set(track["artifacts"])
        self.assertIn(GATE_PATH.name, artifacts)
        self.assertIn(
            "experiments/POLYPEDILUM_SCOBY_REENTRY_MATRIX_DESIGN_v1.0.csv",
            artifacts,
        )
        self.assertIn("docs/EXTREMOPHILE_REENTRY_MATRIX_PROTOCOL.md", artifacts)
        self.assertEqual(track["status"], "ACTIVE_EXPLORATORY_P0_KINETIC_ANCHOR")

    def test_cross_lineage_generalization_remains_bounded(self):
        ctx = self.gate["imported_cross_lineage_context"]
        self.assertEqual(ctx["status"], "CONTEXT_ONLY_NOT_REVERIFIED_IN_THIS_REPOSITORY")
        self.assertIn("cannot be promoted", ctx["rule"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
