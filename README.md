<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · evidence lineage · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 separates:

1. **production science** — programmable bacterial cellulose and acetate/C₂ production;
2. **context science** — human SCFA evidence with route, compartment, time, uncertainty and extraction lineage kept explicit.

The repository does **not** establish a human feeding system, clinical effect, food safety, a universal human SCFA reference vector, or a validated engineered organism.

## Core boundaries

```text
GM_PRODUCER != GM_ACETATE
SAME_MOLECULE != SAME_PHYSIOLOGICAL_EVENT

ACETATE_PRODUCER_PROVENANCE != EVIDENCE_PROVENANCE
CITATION_LOCATOR != EXTRACTION_PROVENANCE

METABOLIC_EQUIVALENCE MUST_NOT_READ PRODUCER_PROVENANCE
REFERENCE_ADMISSION MUST_PRESERVE EVIDENCE_PROVENANCE
```

## Research ladder

```text
v0.2  SOURCE INVARIANCE
  ↓
v0.3  SYNTHETIC CONTEXT SEARCH
  ↓
v0.4  EVIDENCE ADMISSION
  ↓
v0.5  EXTRACTION LINEAGE
  ↓
v0.6  AUTHORITATIVE REFERENCE OBSERVATION   ← current
  ↓
v0.7  UNCERTAINTY-AWARE PARETO SEARCH
```

## v0.6 — what became authoritative

For the first time, one observation is admitted as **authoritative inside the SCOBY-D0 evidence-ingestion layer**:

```text
BOETS_2017_ACETATE_SYSTEMIC_AVAILABILITY
reported   = 36 ± 21 percent, mean ± SD, n=12
normalized = 0.36 ± 0.21 fraction
route      = COLON_DELIVERY_CAPSULE
compartment= PLASMA
```

This does **not** mean a universal human reference value. It means that the repository can replay and cross-check how this source observation entered the dataset.

Two distinct representations and extraction processes are retained:

```text
A: published PMC full-text HTML
   → STRUCTURED_HTML_SOURCE_BINDING

B: University of Glasgow accepted-manuscript PDF text layer
   → PDF_TEXT_LAYER_NUMERIC_EXTRACTION

A == B on reported value, SD, n, context and normalized value
```

The accepted manuscript reports that results are means ± SD and gives the same `36 ± 21%` acetate systemic-availability result for the 12-subject colon-delivery study. The PDF route is not treated as independent biological replication; it is an independent evidence-ingestion path for the same primary study.

## Authority semantics

```text
AUTHORITATIVE_DATASET_OBSERVATION
!=
HUMAN_REFERENCE_STANDARD

CROSS_REPRESENTATION_EXTRACTION_MATCH
!=
INDEPENDENT_BIOLOGICAL_REPLICATION

ONE_AUTHORITATIVE_OBSERVATION
!=
REFERENCE_DISTRIBUTION
```

Current state:

```text
AUTHORITATIVE_OBSERVATIONS = 1
HUMAN_REFERENCE_STANDARD   = NOT_ESTABLISHED
EXTERNAL_REVIEW             = NOT_YET_ESTABLISHED
BIOLOGICAL_REFERENCE_VECTOR = UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW
PARETO_SEARCH               = BLOCKED
```

## v0.4/v0.5 invariants remain active

v0.6 extends the earlier gates; it does not replace them.

```text
PLASMA_VALUE != LUMINAL_VALUE
COLONIC_DELIVERY != ORAL_INTAKE
FASTED != POSTPRANDIAL
SINGLE_STUDY != HUMAN_REFERENCE_STANDARD
MEAN_WITHOUT_VARIANCE != REFERENCE_DISTRIBUTION
SD != SE != CI95 != IQR != RANGE
DIRECT_REPORTED_VALUE != DERIVED_VALUE != FIGURE_DIGITIZATION
NORMALIZED_VALUE MUST_BE_REPLAYABLE_FROM SOURCE_OBSERVATION
EXTRACTION_CONFLICT = PRESERVED
BIOLOGICAL_REFERENCE_VECTOR = STILL_NOT_COLLAPSED
```

## Dataset lineage

`REFERENCE_DATASET_V0_1.json` is intentionally preserved unchanged as the pre-v0.6 candidate-ledger snapshot with zero authoritative observations.

`REFERENCE_DATASET_V0_2.json` is the current manifest and links:

- the preserved v0.1 candidate ledger;
- the extraction ledger;
- the first ingestion-authoritative observation set.

This makes the transition from `0 → 1` authoritative observations auditable instead of rewriting history.

## Current objects

- [`evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json`](evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json)
- [`experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json`](experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json)
- [`experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json`](experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json)
- [`experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json`](experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json)
- [`experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json`](experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_1.json`](evidence/reference_context/REFERENCE_DATASET_V0_1.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_2.json`](evidence/reference_context/REFERENCE_DATASET_V0_2.json)
- [`evidence/reference_context/EXTRACTION_LEDGER_V0_1.json`](evidence/reference_context/EXTRACTION_LEDGER_V0_1.json)
- [`evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json`](evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_1.json)
- [`src/extraction_lineage.py`](src/extraction_lineage.py)
- [`src/reference_admission.py`](src/reference_admission.py)
- [`tests/test_reference_admission.py`](tests/test_reference_admission.py)
- [`tests/test_v06_artifacts.py`](tests/test_v06_artifacts.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
EXTRACTION_REPLAY_PASS != BIOLOGICAL_TRUTH
EXTRACTION_MATCH != INDEPENDENT_BIOLOGICAL_REPLICATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
HASH != TRUTH
ACETATE != COMPLETE_NUTRITION
SIMULATION_OPTIMUM != SAFE_HUMAN_FORMULATION
BIOLOGICAL_REFERENCE_VECTOR = UNSET
```

No wet-lab genetic-engineering procedure, human dose, infusion rate, medical-device control or clinical recommendation belongs in the current scope.

## Related repositories

- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis)
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN)
- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry)

## License

Apache License 2.0. External papers, upstream code and third-party material remain under their respective terms.
