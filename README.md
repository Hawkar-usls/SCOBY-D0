<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · bacterial cellulose · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 studies a modular SCOBY / acetic-acid-bacteria platform as two separable engineering problems:

1. **production science:** programmable bacterial cellulose and acetate/C₂ production;
2. **context science:** evidence-derived human SCFA context distributions with route, compartment, time and uncertainty kept explicit.

The repository does **not** establish a human feeding system, clinical effect, food safety, or a validated engineered organism.

## Core boundaries

```text
GM_PRODUCER != GM_ACETATE
SAME_MOLECULE != SAME_PHYSIOLOGICAL_EVENT

ACETATE_PRODUCER_PROVENANCE != EVIDENCE_PROVENANCE

METABOLIC_EQUIVALENCE
MUST_NOT_READ
PRODUCER_PROVENANCE

REFERENCE_ADMISSION
MUST_PRESERVE
EVIDENCE_PROVENANCE
```

Producer lineage is excluded from the molecular score when chemistry is matched. Evidence lineage is the opposite: DOI/PMID, cohort, route, compartment, physiological state, sampling window, analytical method, units, uncertainty, sample size and exclusions are admission-critical metadata.

## Research line

```text
                           SCOBY-D0
                              |
               +--------------+--------------+
               |                             |
       PRODUCTION SCIENCE              CONTEXT SCIENCE
               |                             |
       engineered AAB                  human evidence
               |                             |
   cellulose + acetate            reference distributions
               |                             |
               +--------------+--------------+
                              |
                           C2 BUS
                              |
                      candidate matrices
                              |
                         Pareto front
```

This architecture does **not** assume that acetate is complete nutrition or that a simulation optimum is a safe formulation.

## Current objects

- [`evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json`](evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json) — frozen source-blind acetate comparison.
- [`experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json`](experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json) — synthetic provenance-blind optimizer objective.
- [`experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json`](experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json) — evidence-admission and distribution-preservation gate.
- [`evidence/reference_context/REFERENCE_DATASET_V0_1.json`](evidence/reference_context/REFERENCE_DATASET_V0_1.json) — candidate human-primary ledger; **not** a reference standard.
- [`schemas/reference_observation_v0.4.schema.json`](schemas/reference_observation_v0.4.schema.json) — machine-readable observation contract.
- [`src/reference_context.py`](src/reference_context.py) — fail-closed admission, context separation and explicit unit conversion.
- [`tests/test_reference_context.py`](tests/test_reference_context.py) — evidence-provenance and anti-collapse invariants.

## v0.4 reference model

```text
R = {r1, r2, ..., rn}

M* = argmin_M [ E_{r~R} D(Phi(M), r) + lambda*C(M) + gamma*U(M) ]
```

Each `r_i` remains a study- and context-specific observation with uncertainty. v0.4 explicitly forbids collapsing admitted evidence into one “ideal human vector”. Future searches should return a Pareto set rather than assert one biological winner.

```text
PARETO_ADMISSIBLE = [A, B, ...]
NO_UNIQUE_BIOLOGICAL_OPTIMUM_ESTABLISHED
```

`biological_reference_vector` therefore remains:

```text
UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW
```

## Fail-closed evidence invariants

```text
MISSING_UNCERTAINTY => NOT_AUTHORITATIVE
UNIT_CONVERSION => EXPLICIT_AND_TESTED
PLASMA_VALUE != LUMINAL_VALUE
COLONIC_DELIVERY != ORAL_INTAKE
FASTED != POSTPRANDIAL
SINGLE_STUDY != HUMAN_REFERENCE_STANDARD
MEAN_WITHOUT_VARIANCE != REFERENCE_DISTRIBUTION
CONFLICTS_PRESERVED = TRUE
SIMULATION_OPTIMUM != SAFE_HUMAN_FORMULATION
```

A comparable evidence bucket currently requires at least two independent complete primary-human sources. This is an engineering admission threshold, **not** a claim that two studies define universal physiology. Cross-study collapse remains forbidden in v0.4.

## Candidate human evidence ledger

The first ledger contains four deliberately non-authoritative candidate lines:

- Boets et al. 2017 — colonic-delivery stable-isotope SCFA study, PMID `27510655`, PMCID `PMC5233652`;
- Verbeke et al. 2010 — oral 13C-barley crossover study, PMID `20502475`;
- Gill et al. 2021 — dietary/oral acetate pharmacokinetics, PMID `33377265`;
- Costabile et al. 2025 — randomized cereal-fiber plasma-SCFA profiles, PMID `40498116`.

All are retained with route/cohort distinctions. Incomplete uncertainty or assay extraction blocks claim-level admission rather than being guessed.

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
HASH != TRUTH
BIO_DERIVED != AUTOMATICALLY_SAFE
ENGINEERED_PRODUCER != ENGINEERED_PRODUCT_IDENTITY
PURIFIED_ACETATE != FERMENTATION_BROTH
ACETATE != COMPLETE_NUTRITION
COMPUTATIONAL_TARGET != CLINICAL_TARGET
EVIDENCE_BUCKET != HUMAN_REFERENCE_STANDARD
```

No wet-lab genetic-engineering procedure, human dose, infusion rate, medical-device control or clinical recommendation belongs in the current scope.

## Related repositories

- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis) — local authoritative simulation/runtime semantics.
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN) — upstream-derived TWAI/CAN working copy used only as a telemetry/provenance abstraction.
- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry) — archival provenance and evidence-bound snapshots.

## License

Apache License 2.0, matching the repository's existing `LICENSE`. External papers, upstream code and third-party material remain under their respective terms.
