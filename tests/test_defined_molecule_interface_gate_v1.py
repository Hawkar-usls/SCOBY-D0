import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "JANUS_SCOBY_DEFINED_MOLECULE_INTERFACE_GATE_0929_v1.0.json"
MATRIX_PATH = ROOT / "experiments" / "PVLEA4_TREHALOSE_BC_DEFINED_FACTOR_MATRIX_v1.0.csv"
LINEAGE_PATH = ROOT / "RESEARCH_LINEAGE.json"
STATUS_PATH = ROOT / "PROJECT_STATUS.json"


class TestDefinedMoleculeInterfaceGateV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = json.loads(GATE_PATH.read_text(encoding="utf-8"))
        cls.lineage = json.loads(LINEAGE_PATH.read_text(encoding="utf-8"))
        cls.status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        with MATRIX_PATH.open(newline="", encoding="utf-8") as f:
            cls.rows = list(csv.DictReader(f))

    def test_gate_remains_p0_without_data(self):
        self.assertEqual(
            self.gate["status"],
            "PREREGISTERED_DEFINED_FACTOR_TEST_NO_EMPIRICAL_BC_EFFECT",
        )
        self.assertEqual(self.gate["promotion_logic"]["current"], "P0")
        self.assertEqual(
            self.gate["promotion_logic"]["this_artifact_ceiling_without_data"],
            "P0_PREREGISTERED_DEFINED_FACTOR_TEST",
        )

    def test_required_confound_controls_exist(self):
        condition_ids = {row["condition_id"] for row in self.rows}
        self.assertEqual(condition_ids, {f"C{i}" for i in range(9)})
        names = {row["condition"] for row in self.rows}
        self.assertIn("TREHALOSE_MATCH", names)
        self.assertIn("GENERIC_SOLUBLE_PROTEIN_MATCH", names)
        self.assertIn("VEHICLE_BUFFER_MATCH", names)
        self.assertIn("NON_NUTRITIONAL_SURFACE_TENSION_REFERENCE", names)

    def test_three_frozen_pvlea4_tiers_exist(self):
        names = {row["condition"] for row in self.rows}
        self.assertTrue({"PVLEA4_LOW", "PVLEA4_MID", "PVLEA4_HIGH"}.issubset(names))
        self.assertIn("outcome-driven dose tuning is forbidden", self.gate["dose_rule"].lower())

    def test_interface_is_measured_before_interpretation(self):
        interface = set(self.gate["readout_layers"]["L1_interface"])
        self.assertIn("surface_tension", interface)
        self.assertIn("dissolved_oxygen_or_oxygen_proxy", interface)
        self.assertEqual(
            self.gate["co_primary_mechanism_endpoint"],
            "surface_tension with oxygen proxy before substantial pellicle formation",
        )

    def test_primary_bc_endpoint_is_frozen(self):
        self.assertEqual(
            self.gate["primary_endpoint"],
            "dry_BC_mass normalized to matched batch and harvest rule",
        )

    def test_kill_rules_reject_false_specificity(self):
        text = " ".join(self.gate["kill_rules"])
        self.assertIn("trehalose alone", text)
        self.assertIn("generic soluble protein", text)
        self.assertIn("surface-tension reference", text)
        self.assertIn("independent-batch replication", text)

    def test_no_direct_binding_claim_without_assay(self):
        breaks = set(self.gate["janus_forward_reverse"]["break_edges"])
        self.assertIn("PVLEA4_DIRECT_CELLULOSE_BINDING_UNMEASURED", breaks)
        d5 = next(x for x in self.gate["decision_rules"] if x["id"] == "D5_DIRECT_OR_NONINTERFACE_CANDIDATE")
        self.assertIn("REQUIRES_BINDING_OR_SURFACE_ASSAY", d5["classification"])

    def test_old_reentry_evidence_ceiling_is_not_weakened(self):
        track = self.lineage["lineages"]["extremophile_reentry_matrix_line"]
        self.assertEqual(track["status"], "ACTIVE_EXPLORATORY_P0_KINETIC_ANCHOR")
        project_track = self.status["active_tracks"]["extremophile_reentry_matrix_coupling"]
        self.assertEqual(project_track["current_promotion"], "P0")

    def test_lineage_and_status_bind_new_gate(self):
        track = self.lineage["lineages"]["extremophile_reentry_matrix_line"]
        self.assertIn(GATE_PATH.name, track["artifacts"])
        self.assertIn(str(MATRIX_PATH.relative_to(ROOT)), track["artifacts"])
        project_track = self.status["active_tracks"]["extremophile_reentry_matrix_coupling"]
        self.assertEqual(project_track["defined_molecule_gate"], GATE_PATH.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
