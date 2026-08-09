<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · evidence lineage · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 separates two problems:

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
v0.5  EXTRACTION LINEAGE        ← current
  ↓
v0.6  AUTHORITATIVE REFERENCE SET
  ↓
v0.7  UNCERTAINTY-AWARE PARETO SEARCH
```

`v0.5` intentionally keeps:

```text
AUTHORITATIVE_OBSERVATIONS = 0
BIOLOGICAL_REFERENCE_VECTOR = UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW
V0_6_ADMISSION = BLOCKED
```

## v0.5 — extraction lineage

A citation locator answers **where a number came from**. v0.5 additionally records **how that source value became a dataset value**.

```text
paper
  ↓
source-reported observation
  ↓
extraction method
  ↓
derivation / digitization / exact unit transform
  ↓
normalized observation
  ↓
replay check
```

Three methods are kept distinct:

```text
DIRECT_REPORTED_VALUE
!=
DERIVED_VALUE
!=
FIGURE_DIGITIZATION
```

Fail-closed invariants include:

```text
SD != SE != CI95 != IQR != RANGE
UNCERTAINTY_TYPE_REQUIRED
DERIVED_VALUE => DERIVATION_REQUIRED
FIGURE_DIGITIZATION => DIGITIZATION_METHOD_REQUIRED
FIGURE_DIGITIZATION => EXTRACTION_ERROR_REQUIRED
UNIT_CONVERSION => SOURCE_UNIT + TARGET_UNIT + EXACT_TRANSFORM
NORMALIZED_VALUE MUST_BE_REPLAYABLE_FROM SOURCE_OBSERVATION
SAME_EXTRACTOR != INDEPENDENT_EXTRACTION
EXTRACTION_CONFLICT = PRESERVED
EXTRACTION_MATCH != AUTHORITATIVE_ADMISSION
```

## Double extraction

v0.5 supports comparison of two separately performed extractions of the same observation.

```text
EXTRACTOR_A → observation_A
EXTRACTOR_B → observation_B
                 ↓
          canonical comparison
```

If they match, status becomes `EXTRACTION_MATCH`, but admission remains blocked until v0.6. If they disagree, the conflict is retained verbatim and **must not be averaged away**.

The repository does not pretend that duplicating one agent's extraction creates independence. The first real Boets record therefore has:

```text
EXTRACTOR_A = CAPTURED_AS_CANDIDATE
EXTRACTOR_B = NOT_YET_ESTABLISHED
AUTHORITATIVE_ADMISSION = BLOCKED_UNTIL_V0_6
```

## Current evidence object

For Boets et al. 2017 (PMID `27510655`, DOI `10.1113/JP272613`), the source directly reports colonic-derived acetate systemic availability as `36 ± 21%`, mean ± SD, in 12 healthy subjects. The record is bound to the Results passage immediately before Figure 2 and Figure 2B and is classified as `DIRECT_REPORTED_VALUE`, not figure digitization.

This remains a **candidate extraction record**, not a universal postprandial reference value.

## Current objects

- [`evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json`](evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json)
- [`experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json`](experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json)
- [`experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json`](experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_1.json`](evidence/reference_context/REFERENCE_DATASET_V0_1.json)
- [`experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json`](experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json)
- [`evidence/reference_context/EXTRACTION_LEDGER_V0_1.json`](evidence/reference_context/EXTRACTION_LEDGER_V0_1.json)
- [`schemas/extraction_record_v0.5.schema.json`](schemas/extraction_record_v0.5.schema.json)
- [`src/extraction_lineage.py`](src/extraction_lineage.py)
- [`tests/test_extraction_lineage.py`](tests/test_extraction_lineage.py)
- [`PROJECT_STATUS.json`](PROJECT_STATUS.json)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
EXTRACTION_REPLAY_PASS != BIOLOGICAL_TRUTH
EXTRACTION_MATCH != INDEPENDENT_BIOLOGICAL_REPLICATION
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
