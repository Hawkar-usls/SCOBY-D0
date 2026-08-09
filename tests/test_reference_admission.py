import copy
import unittest

from reference_admission import admit_dataset_observation, compare_cross_representation_extractions


def record(extractor_id, representation_id, representation_role, provider, fmt, process_family, process_id):
    return {
        "observation_id": "BOETS_2017_ACETATE_SYSTEMIC_AVAILABILITY",
        "extractor_id": extractor_id,
        "source_identity": {
            "title": "Systemic availability and metabolism of colonic-derived short-chain fatty acids in healthy subjects: a stable isotope study",
            "year": 2017,
            "pmid": "27510655",
            "doi": "10.1113/JP272613",
        },
        "citation_locator": {"type": "RESULTS_TEXT_AND_FIGURE", "locator": "source-specific exact locator"},
        "reported_observation": {
            "estimate": 36.0,
            "uncertainty": {"type": "SD", "value": 21.0},
            "units": "percent",
            "n": 12,
        },
        "context": {
            "route": "COLON_DELIVERY_CAPSULE",
            "compartment": "PLASMA",
            "physiological_state": "MIXED_PROTOCOL",
            "time_window": "SOURCE_DEFINED_12_H_PLASMA_FOLLOWUP",
        },
        "extraction": {
            "method": "DIRECT_REPORTED_VALUE",
            "derived": False,
            "digitized_from_figure": False,
            "unit_conversion": {
                "applied": True,
                "source_unit": "percent",
                "target_unit": "fraction",
                "exact_transform": {"kind": "MULTIPLY_EXACT", "factor": 0.01},
            },
        },
        "normalized_observation": {
            "estimate": 0.36,
            "uncertainty": {"type": "SD", "value": 0.21},
            "units": "fraction",
        },
        "extraction_provenance": {
            "representation_id": representation_id,
            "representation_role": representation_role,
            "provider": provider,
            "format": fmt,
            "stable_locator": "stable-locator",
            "process_family": process_family,
            "process_id": process_id,
        },
    }


def pair():
    a = record(
        "EXTRACTOR_A_PMC",
        "PMC_PUBLISHED_FULL_TEXT_HTML",
        "PUBLISHED_VERSION",
        "NCBI_PMC",
        "HTML",
        "STRUCTURED_HTML_SOURCE_BINDING",
        "PMC_STRUCTURED_BINDING_V1",
    )
    b = record(
        "EXTRACTOR_B_GLASGOW_PDF_TEXT",
        "UNIVERSITY_GLASGOW_ACCEPTED_MANUSCRIPT_PDF_TEXT",
        "ACCEPTED_MANUSCRIPT",
        "UNIVERSITY_OF_GLASGOW_ENLIGHTEN",
        "PDF_TEXT_LAYER",
        "PDF_TEXT_LAYER_NUMERIC_EXTRACTION",
        "GLASGOW_PDF_TEXT_REGEX_V1",
    )
    return a, b


class TestReferenceAdmissionV06(unittest.TestCase):
    def test_cross_representation_match_is_eligible(self):
        a, b = pair()
        out = compare_cross_representation_extractions(a, b)
        self.assertEqual(out["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")
        self.assertEqual(out["authoritative_admission"], "ELIGIBLE_FOR_V0_6_INGESTION_AUTHORITY")

    def test_v06_admits_ingestion_authority_only(self):
        a, b = pair()
        out = admit_dataset_observation(a, b)
        self.assertTrue(out["authoritative_observation"])
        self.assertEqual(out["authority_scope"], "SCOBY_D0_EVIDENCE_INGESTION_ONLY")
        self.assertEqual(out["biological_reference_standard"], "NOT_ESTABLISHED")
        self.assertTrue(out["biological_reference_vector"].startswith("UNSET"))
        self.assertTrue(out["pareto_search"].startswith("BLOCKED"))

    def test_same_representation_fails_closed(self):
        a, b = pair(); b["extraction_provenance"]["representation_id"] = a["extraction_provenance"]["representation_id"]
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "NOT_DISTINCT_SOURCE_REPRESENTATIONS")

    def test_same_process_family_fails_closed(self):
        a, b = pair(); b["extraction_provenance"]["process_family"] = a["extraction_provenance"]["process_family"]
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "NOT_DISTINCT_PROCESS_FAMILIES")

    def test_same_extractor_id_fails_closed(self):
        a, b = pair(); b["extractor_id"] = a["extractor_id"]
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "NOT_SEPARATE_EXTRACTOR_IDS")

    def test_normalization_replay_failure_blocks(self):
        a, b = pair(); b["normalized_observation"]["estimate"] = 0.37
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "NORMALIZATION_REPLAY_FAIL")

    def test_numeric_conflict_is_preserved_not_averaged(self):
        a, b = pair(); b["reported_observation"]["estimate"] = 35.0; b["normalized_observation"]["estimate"] = 0.35
        out = compare_cross_representation_extractions(a, b)
        self.assertEqual(out["status"], "EXTRACTION_CONFLICT_PRESERVED")
        self.assertEqual(out["left"]["normalized_observation"]["estimate"], 0.36)
        self.assertEqual(out["right"]["normalized_observation"]["estimate"], 0.35)

    def test_uncertainty_semantics_must_match(self):
        a, b = pair(); b["reported_observation"]["uncertainty"]["type"] = "SE"; b["normalized_observation"]["uncertainty"]["type"] = "SE"
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "EXTRACTION_CONFLICT_PRESERVED")

    def test_context_mismatch_is_conflict(self):
        a, b = pair(); b["context"]["route"] = "ORAL_FOOD"
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "EXTRACTION_CONFLICT_PRESERVED")

    def test_source_identity_mismatch_blocks(self):
        a, b = pair(); b["source_identity"]["pmid"] = "99999999"; b["source_identity"]["doi"] = "10.9999/not-the-paper"
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "PRIMARY_SOURCE_IDENTITY_MISMATCH")

    def test_pmid_match_allows_doi_missing_in_one_representation(self):
        a, b = pair(); b["source_identity"]["doi"] = None
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")

    def test_doi_match_allows_pmid_missing_in_one_representation(self):
        a, b = pair(); b["source_identity"]["pmid"] = None
        self.assertEqual(compare_cross_representation_extractions(a, b)["status"], "CROSS_REPRESENTATION_EXTRACTION_MATCH")

    def test_external_review_not_invented(self):
        a, b = pair(); out = admit_dataset_observation(a, b)
        self.assertEqual(out["external_review"], "NOT_YET_ESTABLISHED")

    def test_one_authoritative_observation_is_not_reference_vector(self):
        a, b = pair(); out = admit_dataset_observation(a, b)
        self.assertTrue(out["authoritative_observation"])
        self.assertNotIn("reference_vector", out)
        self.assertEqual(out["biological_reference_standard"], "NOT_ESTABLISHED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
