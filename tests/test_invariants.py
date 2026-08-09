import unittest

from context_search import TARGET, score, search


class TestSCOBYD0Invariants(unittest.TestCase):
    def test_optimizer_runs(self):
        matrix, value = search()
        self.assertIsInstance(matrix, dict)
        self.assertGreaterEqual(value, 0.0)

    def test_provenance_not_in_scoring_signature(self):
        matrix, _ = search()
        dietary = {"matrix": dict(matrix), "provenance": "dietary_colonic"}
        engineered = {"matrix": dict(matrix), "provenance": "engineered_scoby"}
        self.assertEqual(score(dietary["matrix"]), score(engineered["matrix"]))

    def test_same_matrix_same_score(self):
        matrix, _ = search()
        self.assertEqual(score(matrix), score(dict(matrix)))

    def test_target_is_synthetic_not_clinical(self):
        self.assertEqual(TARGET["microbiome_contact_proxy"], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
