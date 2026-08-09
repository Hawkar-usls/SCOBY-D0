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
v0.6.3 COHORT + PREANALYTIC HARDENING
  ↓
v0.6.4 HARDENED PAIR SEARCH FRONTIER
  ↓
v0.6.5 COHORT + METHOD RESOLUTION FRONTIER
  ↓
v0.6.5.1 FIRST CONCRETE BLOCKER RESOLUTION
  ↓
v0.6.5.2 PUBLIC PRIMARY-EVIDENCE BOUNDARY        ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH          🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
REAL_HARDENED_READY_PAIRS = 0
COHORT_INDEPENDENCE_RESOLVED_PAIRS = 0
MEASUREMENT_CONTEXT_RESOLUTION_RECEIPTS = 1
PUBLIC_EVIDENCE_BOUNDARY_RECEIPTS = 1
NEW_AUTHORITATIVE_OBSERVATIONS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

## Maastricht pair: what is resolved

For `NCT01826162 ↔ NCT01983046`, v0.6.5.1 established from the 2019 combined baseline analysis that the contributing studies used a common reported baseline sample-collection/measurement SOP and a specified circulating-SCFA workflow in that analysis scope.

```text
MEASUREMENT_CONTEXT
= PASS_IN_DEFINED_2019_COMBINED_ANALYSIS_SCOPE
```

This did not establish cohort independence or separate per-trial reference distributions.

## v0.6.5.2 — public evidence boundary

A further primary-source pass checked both trial registrations, the individual primary publications, and the 2019 combined analysis.

Publicly established:

```text
NCT01826162 = pilot protocol MEC 11-3-079
NCT01983046 = later follow-up protocol that explicitly references the pilot
trial windows are sequential
published participant counts differ
NCT01983046 Figure 2 exposes plasma-SCFA curves as mean ± SEM
2019 combined analysis includes both trials and uses a common baseline SOP
```

Still **not** publicly established:

```text
PARTICIPANT_OVERLAP_OR_NONOVERLAP
SEPARATE_DIRECT_REPORTED_PER_TRIAL_BASELINE_SCFA_DISTRIBUTIONS
```

The 2019 paper states that underlying intervention-study data are not suitable for public deposition because of ethical/privacy restrictions and may be available to qualified researchers through controlled request. SCOBY-D0 has not accessed those private data and does not infer missing values from their existence.

Therefore:

```text
PUBLIC_SEARCH_EXHAUSTION != NEGATIVE_PROOF_OF_OVERLAP
ABSENCE_OF_OVERLAP_STATEMENT != DISTINCT_COHORT_PROOF
RESTRICTED_DATA != PERMISSION_TO_INFER_MISSING_VALUES
FIGURE_VISIBILITY != DIRECT_REPORTED_NUMERIC_VALUE
```

No figure digitization was promoted in v0.6.5.2. If digitization is ever used, it must return through the existing v0.5 `FIGURE_DIGITIZATION` lineage with an explicit method and extraction error; it still would not solve cohort independence.

The boundary receipt is machine-readable:

- [`evidence/reference_context/MAASTRICHT_PUBLIC_EVIDENCE_BOUNDARY_V0_6_5_2.json`](evidence/reference_context/MAASTRICHT_PUBLIC_EVIDENCE_BOUNDARY_V0_6_5_2.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_3.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_3.json)
- [`tests/test_public_evidence_boundary_v0652.py`](tests/test_public_evidence_boundary_v0652.py)

## Remaining Maastricht blockers

```text
PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED
DISTINCT_TRIAL_ID_DOES_NOT_ESTABLISH_DISTINCT_COHORT
PER_TRIAL_BASELINE_SCFA_OBSERVATIONS_NOT_YET_SEPARATELY_EXTRACTION_BOUND
```

At this point the honest next evidence is either controlled/author-level evidence for participant identity and per-trial baseline SCFA, or a pivot to another near-pair. Internet similarity is no longer sufficient.

## Other active near-pairs

### OsloMet: NCT03293693 ↔ NCT03658681

The measurement surface remains close: healthy normal-weight adults, ≥12 h fast, EDTA plasma, rapid cold processing, −80 °C storage and Vitas Analytical Service. The NCT03293693 primary paper still does not identify the SCFA analytical method family, while NCT03658681 explicitly uses LC-MS/MS. `SAME_LAB != SAME_METHOD`; participant reuse also remains unresolved.

### Oslo method contrast: NCT01034436 NW ↔ NCT03658681

Both use fasted EDTA plasma and Vitas, but the primary reports bind SCFA measurement to GC-MS versus LC-MS/MS. The pair remains a method contrast, not exact comparability.

## Historical reference manifests

```text
REFERENCE_DATASET_V0_1   → 0 authoritative observations
REFERENCE_DATASET_V0_2   → 1 authoritative observation
REFERENCE_DATASET_V0_3   → 10 context-separated authoritative observations
REFERENCE_DATASET_V0_4   → 0 exact comparable multi-study buckets
REFERENCE_DATASET_V0_5   → cohort/preanalytic hardening, 0 ready buckets
REFERENCE_DATASET_V0_6   → hardened-pair search frontier, 0 ready pairs
REFERENCE_DATASET_V0_6_1 → cohort/method resolution frontier, 0 ready pairs
REFERENCE_DATASET_V0_6_2 → one Maastricht measurement-context blocker resolved
REFERENCE_DATASET_V0_6_3 → public evidence boundary reached; pair still blocked
```

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
DISTINCT_PUBLICATIONS != DISTINCT_COHORTS
DISTINCT_TRIAL_IDS != DISTINCT_COHORTS
COMMON_REPORTED_SOP != DISTINCT_COHORT_PROOF
PUBLIC_SEARCH_EXHAUSTION != NEGATIVE_PROOF
RESTRICTED_DATA != INFERRED_DATA
FIGURE_VISIBILITY != DIRECT_REPORTED_VALUE
SEARCH_OR_RESOLUTION_RECEIPT != EVIDENCE_AUTHORITY
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
