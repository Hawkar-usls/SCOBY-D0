import unittest
from reference_context import (
    ReferenceCollapseForbidden,
    bucket_can_be_evidence_bound,
    collapse_reference_vector,
    comparable,
    convert_value,
    is_admissible,
    preserve_conflicts,
    validate_observation,
)

def obs(**overrides):
    base = {
        "source_type":"PRIMARY_HUMAN",
        "source_lineage":{"title":"Primary study","year":2025,"pmid":"123","doi":"10.1/x"},
        "cohort":"healthy adults",
        "sample_size":12,
        "route":"ORAL_FOOD",
        "compartment":"PLASMA",
        "physiological_state":"POSTPRANDIAL",
        "sampling_times_or_window":{"minutes":[0,60,120]},
        "analytical_method":"LC-MS/MS",
        "analyte":"ACETATE",
        "estimate":100.0,
        "units":"umol/L",
        "uncertainty":{"kind":"SD","value":20.0},
        "exclusions":"explicit source-bound exclusions",
    }
    base.update(overrides)
    return base

class TestEvidenceReferenceV04(unittest.TestCase):
    def test_missing_uncertainty_fails_closed(self):
        x = obs(uncertainty=None)
        self.assertIn("MISSING_UNCERTAINTY", validate_observation(x))
        self.assertFalse(is_admissible(x))

    def test_mean_without_variance_is_not_admissible(self):
        x = obs(uncertainty={"kind":"SD","value":None})
        self.assertFalse(is_admissible(x))

    def test_unit_conversion_is_explicit(self):
        c = convert_value(1000.0, "umol/L", "mmol/L")
        self.assertEqual(c["output_value"], 1.0)
        self.assertEqual(c["factor"], 0.001)
        self.assertTrue(c["conversion_explicit"])

    def test_unsupported_unit_conversion_fails(self):
        with self.assertRaises(ValueError):
            convert_value(1.0, "mg/day", "mmol/L")

    def test_plasma_is_not_luminal(self):
        self.assertFalse(comparable(obs(compartment="PLASMA"), obs(compartment="COLON_LUMEN")))

    def test_colonic_delivery_is_not_oral_intake(self):
        self.assertFalse(comparable(obs(route="COLON_DELIVERY_CAPSULE"), obs(route="ORAL_FOOD")))

    def test_fasted_is_not_postprandial(self):
        self.assertFalse(comparable(obs(physiological_state="FASTED"), obs(physiological_state="POSTPRANDIAL")))

    def test_single_study_cannot_define_evidence_bound_bucket(self):
        self.assertFalse(bucket_can_be_evidence_bound([obs()], minimum_sources=2))

    def test_two_independent_complete_sources_can_form_bucket_not_vector(self):
        a = obs(source_lineage={"title":"A","year":2020,"pmid":"1","doi":"10.1/a"})
        b = obs(source_lineage={"title":"B","year":2021,"pmid":"2","doi":"10.1/b"})
        self.assertTrue(bucket_can_be_evidence_bound([a,b], minimum_sources=2))
        with self.assertRaises(ReferenceCollapseForbidden):
            collapse_reference_vector([a,b])

    def test_conflicts_are_preserved_not_averaged(self):
        a = obs(estimate=80.0)
        b = obs(estimate=140.0, source_lineage={"title":"B","year":2021,"pmid":"2","doi":"10.1/b"})
        out = preserve_conflicts([a,b])
        self.assertEqual([x["estimate"] for x in out], [80.0,140.0])

    def test_evidence_provenance_is_required(self):
        x = obs(source_lineage={"title":"A","year":2020,"pmid":"","doi":""})
        errors = validate_observation(x)
        self.assertIn("MISSING_LINEAGE_PMID", errors)
        self.assertIn("MISSING_LINEAGE_DOI", errors)

    def test_producer_provenance_is_not_an_observation_field_requirement(self):
        self.assertTrue(is_admissible(obs()))
        self.assertNotIn("producer_provenance", obs())

if __name__ == "__main__":
    unittest.main(verbosity=2)
