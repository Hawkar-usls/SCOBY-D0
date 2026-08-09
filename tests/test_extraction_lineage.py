import copy
import unittest
from extraction_lineage import (
    UNCERTAINTY_TYPES, compare_independent_extractions,
    normalized_matches_replay, validate_extraction_record,
)

def direct_record(**overrides):
    base = {
        "observation_id":"OBS-1",
        "extractor_id":"EXTRACTOR_A",
        "source_identity":{"pmid":"27510655","doi":None},
        "citation_locator":{"type":"figure","locator":"Figure 2B"},
        "reported_observation":{
            "estimate":0.36,
            "uncertainty":{"type":"SD","value":0.21},
            "units":"fraction",
            "n":12,
        },
        "context":{
            "route":"COLON_DELIVERY_CAPSULE",
            "compartment":"PLASMA",
            "physiological_state":"MIXED_PROTOCOL",
            "time_window":"SOURCE_DEFINED",
        },
        "extraction":{
            "method":"DIRECT_REPORTED_VALUE",
            "derived":False,
            "digitized_from_figure":False,
            "unit_conversion":{"applied":False},
        },
        "normalized_observation":{
            "estimate":0.36,
            "uncertainty":{"type":"SD","value":0.21},
            "units":"fraction",
        },
    }
    base.update(overrides)
    return base

class TestExtractionLineageV05(unittest.TestCase):
    def test_direct_record_replays(self):
        x=direct_record()
        self.assertEqual(validate_extraction_record(x),[])
        self.assertTrue(normalized_matches_replay(x))

    def test_uncertainty_types_are_not_collapsed(self):
        self.assertTrue({"SD","SE","CI95","IQR","RANGE"}.issubset(UNCERTAINTY_TYPES))
        x=direct_record()
        x["normalized_observation"]["uncertainty"]["type"]="SE"
        self.assertFalse(normalized_matches_replay(x))

    def test_missing_uncertainty_type_fails(self):
        x=direct_record()
        x["reported_observation"]["uncertainty"]["type"]=""
        self.assertIn("UNCERTAINTY_TYPE_REQUIRED",validate_extraction_record(x))

    def test_derived_requires_derivation(self):
        x=direct_record()
        x["extraction"]={"method":"DERIVED_VALUE","derived":True,"digitized_from_figure":False,"unit_conversion":{"applied":False}}
        self.assertIn("MISSING_DERIVATION_OPERATION",validate_extraction_record(x))

    def test_replayable_ratio_derivation(self):
        x=direct_record()
        x["reported_observation"]["estimate"]=0.5
        x["reported_observation"]["uncertainty"]={"type":"OTHER_EXPLICIT","value":0.01}
        x["extraction"]={
            "method":"DERIVED_VALUE","derived":True,"digitized_from_figure":False,
            "derivation":{"operation":"RATIO","inputs":[{"id":"A","value":36.0},{"id":"B","value":100.0}],
                          "rounding_rule":"NONE_BEFORE_FINAL","derivation_replayable":True},
            "unit_conversion":{"applied":False},
        }
        x["normalized_observation"]={"estimate":0.36,"uncertainty":{"type":"OTHER_EXPLICIT","value":0.01},"units":"fraction"}
        self.assertTrue(normalized_matches_replay(x))

    def test_figure_digitization_requires_method_and_error(self):
        x=direct_record()
        x["extraction"]={"method":"FIGURE_DIGITIZATION","derived":False,"digitized_from_figure":True,"unit_conversion":{"applied":False}}
        errs=validate_extraction_record(x)
        self.assertIn("DIGITIZATION_METHOD_REQUIRED",errs)
        self.assertIn("EXTRACTION_ERROR_REQUIRED",errs)

    def test_conversion_requires_source_target_transform(self):
        x=direct_record()
        x["extraction"]["unit_conversion"]={"applied":True}
        errs=validate_extraction_record(x)
        self.assertIn("MISSING_CONVERSION_SOURCE_UNIT",errs)
        self.assertIn("MISSING_CONVERSION_TARGET_UNIT",errs)
        self.assertIn("MISSING_CONVERSION_EXACT_TRANSFORM",errs)

    def test_exact_conversion_replays_estimate_and_uncertainty(self):
        x=direct_record()
        x["reported_observation"]={"estimate":360.0,"uncertainty":{"type":"SD","value":210.0},"units":"per_mille","n":12}
        x["extraction"]["unit_conversion"]={
            "applied":True,"source_unit":"per_mille","target_unit":"fraction",
            "exact_transform":{"kind":"MULTIPLY_EXACT","factor":0.001},
        }
        x["normalized_observation"]={"estimate":0.36,"uncertainty":{"type":"SD","value":0.21},"units":"fraction"}
        self.assertTrue(normalized_matches_replay(x))

    def test_normalized_value_must_match_replay(self):
        x=direct_record()
        x["normalized_observation"]["estimate"]=0.37
        self.assertFalse(normalized_matches_replay(x))

    def test_same_extractor_is_not_independent(self):
        a=direct_record(); b=copy.deepcopy(a)
        self.assertEqual(compare_independent_extractions(a,b)["status"],"NOT_INDEPENDENT")

    def test_two_independent_matching_extractions_still_blocked_until_v06(self):
        a=direct_record(); b=copy.deepcopy(a); b["extractor_id"]="EXTRACTOR_B"
        out=compare_independent_extractions(a,b)
        self.assertEqual(out["status"],"EXTRACTION_MATCH")
        self.assertEqual(out["authoritative_admission"],"STILL_BLOCKED_UNTIL_V0_6")

    def test_conflict_preserved_not_averaged(self):
        a=direct_record(); b=copy.deepcopy(a); b["extractor_id"]="EXTRACTOR_B"
        b["reported_observation"]["estimate"]=0.35
        b["normalized_observation"]["estimate"]=0.35
        out=compare_independent_extractions(a,b)
        self.assertEqual(out["status"],"EXTRACTION_CONFLICT_PRESERVED")
        self.assertEqual(out["left"]["normalized_observation"]["estimate"],0.36)
        self.assertEqual(out["right"]["normalized_observation"]["estimate"],0.35)

if __name__=="__main__":
    unittest.main(verbosity=2)
