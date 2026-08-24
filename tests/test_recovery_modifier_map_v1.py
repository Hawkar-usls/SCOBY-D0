import csv
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODIFIER = ROOT / "JANUS_SCOBY_RECOVERY_MODIFIER_TO_BC_MAP_0921_v1.0.json"
PROVENANCE = ROOT / "JANUS_SCOBY_THREE_LINEAGE_REENTRY_PROVENANCE_0921_v1.0.json"
CSV_PATH = ROOT / "experiments" / "POLYPEDILUM_RECOVERY_MODIFIER_BC_PREDICTIONS_v1.0.csv"


class TestRecoveryModifierMapV1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modifier = json.loads(MODIFIER.read_text(encoding="utf-8"))
        cls.provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
        with CSV_PATH.open(encoding="utf-8", newline="") as fh:
            cls.rows = list(csv.DictReader(fh))

    def test_modifier_map_cannot_promote_beyond_candidate_map(self):
        self.assertEqual(self.modifier["promotion_rule"]["current"], "P0")
        self.assertEqual(self.modifier["promotion_rule"]["ceiling_for_this_artifact"], "CANDIDATE_MAP_ONLY")

    def test_trehalose_is_priority_one_and_mandatory_confound(self):
        families = {x["id"]: x for x in self.modifier["candidate_families"]}
        self.assertEqual(families["M1_TREHALOSE"]["priority"], 1)
        self.assertIn("trehalose-matched", families["M1_TREHALOSE"]["critical_control"].lower())
        self.assertIn("TREHALOSE_IS_BOTH_CANDIDATE_AND_MANDATORY_CONFOUND", self.modifier["claim_boundary"])

    def test_defined_factor_required_for_p3(self):
        self.assertIn("NO_DEFINED_FACTOR_NO_P3_PROMOTION", self.modifier["decision_tree"])

    def test_three_lineages_are_primary_bound(self):
        classes = {x["lineage"]: x["evidence_class"] for x in self.provenance["lineages"]}
        self.assertEqual(classes["Bacillus_subtilis_spore"], "PRIMARY_CAUSAL_CHECKPOINT_ANCHOR")
        self.assertEqual(classes["Adineta_vaga"], "PRIMARY_COMPARTMENT_SPECIFIC_REPAIR_TIMING_ANCHOR")
        self.assertEqual(classes["Polypedilum_vanderplanki_Pv11"], "PRIMARY_KINETIC_ANCHOR_CAUSAL_GATE_OPEN")

    def test_cross_lineage_general_causal_claim_stays_open(self):
        self.assertEqual(
            self.provenance["cross_lineage_result"]["status"],
            "P0_PROVENANCE_BOUND_CONVERGENT_REENTRY_ARCHITECTURE",
        )
        self.assertIn(
            "DNA_REPAIR_CAUSES_THE_REENTRY_DELAY_IN_POLYPEDILUM",
            self.provenance["cross_lineage_result"]["open"],
        )

    def test_adineta_preprint_cannot_upgrade_authority(self):
        adineta = next(x for x in self.provenance["lineages"] if x["lineage"] == "Adineta_vaga")
        self.assertEqual(
            adineta["current_2026_supportive_update"]["status"],
            "PREPRINT_SUPPORTIVE_NOT_AUTHORITY_UPGRADE",
        )

    def test_prediction_csv_matches_five_candidate_families(self):
        self.assertEqual(len(self.rows), 5)
        self.assertEqual(self.rows[0]["candidate"], "TREHALOSE")
        self.assertEqual(self.rows[-1]["candidate"], "LIL_MEMBRANE_STATE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
