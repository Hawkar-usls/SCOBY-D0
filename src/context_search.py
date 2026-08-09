#!/usr/bin/env python3
"""SCOBY-D0 v0.3 synthetic context-search kernel.

Simulation only. It contains no human dosing and no wet-lab protocol.
"""
from itertools import product

GRID = [0.0, 0.25, 0.5, 0.75, 1.0]
FEATURES = [
    "propionate_proxy",
    "butyrate_proxy",
    "ph_proxy",
    "appearance_profile_proxy",
    "microbiome_contact_proxy",
    "organic_load_proxy",
]
TARGET = {
    "propionate_proxy": 0.25,
    "butyrate_proxy": 0.25,
    "ph_proxy": 0.5,
    "appearance_profile_proxy": 0.75,
    "microbiome_contact_proxy": 1.0,
    "organic_load_proxy": 0.5,
}
WEIGHTS = {
    "propionate_proxy": 1.0,
    "butyrate_proxy": 1.0,
    "ph_proxy": 0.5,
    "appearance_profile_proxy": 0.75,
    "microbiome_contact_proxy": 1.25,
    "organic_load_proxy": 0.25,
}
LAMBDA_COMPLEXITY = 0.02


def score(matrix):
    """Provenance-blind score. Origin/engineered status is deliberately absent."""
    dist = sum(WEIGHTS[k] * (matrix[k] - TARGET[k]) ** 2 for k in FEATURES)
    nonzero = sum(matrix[k] > 0 for k in ("propionate_proxy", "butyrate_proxy"))
    return dist + LAMBDA_COMPLEXITY * nonzero


def search():
    best = None
    for values in product(GRID, repeat=len(FEATURES)):
        matrix = dict(zip(FEATURES, values))
        value = score(matrix)
        key = (round(value, 12), sum(v > 0 for v in values), tuple(values))
        if best is None or key < best[0]:
            best = (key, matrix, value)
    return best[1], best[2]


if __name__ == "__main__":
    matrix, value = search()
    print(matrix)
    print("score=", value)
