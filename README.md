<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · evidence lineage · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 separates production science from context science. It does not establish a human feeding system, clinical effect, food safety, universal human SCFA reference vector, or validated engineered organism.

## Research ladder

```text
v0.2   SOURCE INVARIANCE
  ↓
v0.3   SYNTHETIC CONTEXT SEARCH
  ↓
v0.4   EVIDENCE ADMISSION
  ↓
v0.5   EXTRACTION LINEAGE
  ↓
v0.6   FIRST INGESTION-AUTHORITATIVE OBSERVATION
  ↓
v0.6.1 MULTICONTEXT AUTHORITATIVE EXPANSION
  ↓
v0.6.2 EXACT COMPARABLE-CONTEXT QUALIFICATION
  ↓
v0.6.3 COHORT + PREANALYTIC HARDENING          ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH         🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
V0_6_2_EXACT_MULTI_STUDY_BUCKETS = 0
V0_6_3_HARDENED_READY_BUCKETS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

v0.6.3 closes two additional routes to false comparability:

```text
DIFFERENT_PUBLICATION != INDEPENDENT_COHORT
SAME_BIOLOGICAL_CONTEXT != SAME_MEASUREMENT_CONTEXT
```

A multi-study bucket now requires established distinct cohorts, not merely distinct PMID/DOI values. Confirmed participant overlap blocks the independent-study count; unresolved overlap does not count as established cohort independence.

The exact measurement-context key now also contains:

```text
preanalytic_handling
analytical_method_family
```

This is necessary because measured acetate can depend materially on sample handling. A primary 1979 Clinical Chemistry study reported a change in measured plasma acetate after defined frozen storage, so fresh and stored specimens are not silently treated as the same measurement context.

## Hardened invariants

```text
CONFIRMED_PARTICIPANT_OVERLAP => NOT_INDEPENDENT
UNRESOLVED_PARTICIPANT_OVERLAP != DISTINCT_COHORT_ESTABLISHED
FRESH_SPECIMEN != STORED_SPECIMEN unless a validated transform is predeclared
UNKNOWN_PREANALYTIC_HANDLING => NOT_COMPARABLE
UNKNOWN_ANALYTICAL_METHOD => NOT_COMPARABLE
SERUM != PLASMA unless equivalence is predeclared + supported
TRACER != NO_TRACER
UNKNOWN_FASTING_DURATION != 12_HOURS
SD != SE != SEM != IQR != RANGE
COMPARABLE_READY != POOLED_REFERENCE
NO_AVERAGING_AT_V0_6_3
```

A synthetic positive fixture may become `COMPARABLE_READY_NOT_POOLED` only when two primary sources have distinct established cohort IDs and an identical complete hardened key. v0.6.3 itself never averages those observations.

## Evidence state remains bounded

```text
HUMAN_REFERENCE_STANDARD = NOT_ESTABLISHED
EXTERNAL_REVIEW = NOT_YET_ESTABLISHED
BIOLOGICAL_REFERENCE_VECTOR = UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW
PARETO_SEARCH = BLOCKED
```

Historical manifests remain preserved:

```text
REFERENCE_DATASET_V0_1 → 0 authoritative observations
REFERENCE_DATASET_V0_2 → 1 authoritative observation
REFERENCE_DATASET_V0_3 → 10 context-separated authoritative observations
REFERENCE_DATASET_V0_4 → 0 exact comparable multi-study buckets
REFERENCE_DATASET_V0_5 → cohort/preanalytic hardening active, still 0 ready buckets
```

## Current objects

- [`experiments/SCOBY-D0-COMPARABLE-CONTEXT-BUCKET-QUALIFICATION-v0.6.2.json`](experiments/SCOBY-D0-COMPARABLE-CONTEXT-BUCKET-QUALIFICATION-v0.6.2.json)
- [`experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json`](experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_5.json`](evidence/reference_context/REFERENCE_DATASET_V0_5.json)
- [`src/comparable_context.py`](src/comparable_context.py)
- [`src/cross_study_hardening.py`](src/cross_study_hardening.py)
- [`tests/test_comparable_context_v062.py`](tests/test_comparable_context_v062.py)
- [`tests/test_cross_study_hardening_v063.py`](tests/test_cross_study_hardening_v063.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
EXTRACTION_REPLAY_PASS != BIOLOGICAL_TRUTH
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
DISTINCT_PUBLICATIONS != DISTINCT_COHORTS
COMPARABLE_READY != POOLED_REFERENCE
MULTIPLE_OBSERVATIONS != BIOLOGICAL_REFERENCE_VECTOR
HASH != TRUTH
ACETATE != COMPLETE_NUTRITION
SIMULATION_OPTIMUM != SAFE_HUMAN_FORMULATION
```

No wet-lab genetic-engineering procedure, human dose, infusion rate, medical-device control, or clinical recommendation belongs in the current scope.

## Related repositories

- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis)
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN)
- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry)

## License

Apache License 2.0. External papers, upstream code, and third-party material remain under their respective terms.
