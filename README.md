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
v0.6.5.1 FIRST CONCRETE BLOCKER RESOLUTION       ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH          🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
RESOLUTION_NEAR_PAIRS = 3
REAL_HARDENED_READY_PAIRS = 0
COHORT_INDEPENDENCE_RESOLVED_PAIRS = 0
MEASUREMENT_CONTEXT_RESOLUTION_RECEIPTS = 1
NEW_AUTHORITATIVE_OBSERVATIONS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

## v0.6.5.1 — first blocker actually resolved

The Maastricht near-pair

```text
NCT01826162 ↔ NCT01983046
```

was revisited using the 2019 primary combined baseline analysis. That paper explicitly includes both trial IDs, states that sample collection in all included studies occurred after an overnight fast and measurements followed the same standard operating procedures, and specifies the circulating-SCFA workflow used for the combined baseline analysis.

The resolved dimension is therefore narrowly stated as:

```text
PER_TRIAL_PREANALYTIC_AND_ANALYTICAL_CONTEXT_NOT_YET_BOUND_AS_EXACT_IDENTICAL
→
RESOLVED_FOR_BASELINE_SAMPLES_IN_2019_COMBINED_ANALYSIS_SCOPE
```

This does **not** make the pair comparable-ready.

Remaining blockers:

```text
PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED
DISTINCT_TRIAL_ID_DOES_NOT_ESTABLISH_DISTINCT_COHORT
PER_TRIAL_BASELINE_SCFA_OBSERVATIONS_NOT_YET_SEPARATELY_EXTRACTION_BOUND
```

Hence:

```text
COMMON_REPORTED_SOP != DISTINCT_COHORT_PROOF
COMBINED_DATASET != PER_TRIAL_REFERENCE_DISTRIBUTION
ONE_RESOLVED_BLOCKER != PAIR_ADMISSION
```

The resolution receipt is machine-readable and hash-bound:

- [`evidence/reference_context/MAASTRICHT_SOP_RESOLUTION_RECEIPT_V0_6_5_1.json`](evidence/reference_context/MAASTRICHT_SOP_RESOLUTION_RECEIPT_V0_6_5_1.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_2.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_2.json)
- [`tests/test_maastricht_resolution_v0651.py`](tests/test_maastricht_resolution_v0651.py)

## Other active near-pairs

### OsloMet: NCT03293693 ↔ NCT03658681

The surface measurement context remains close: healthy normal-weight adults, ≥12 h fast, EDTA plasma, rapid cold processing, −80 °C storage and Vitas Analytical Service. However, the NCT03293693 primary paper does not explicitly identify the SCFA analytical method family, while NCT03658681 explicitly binds its SCFA analysis to LC-MS/MS. Therefore `SAME_LAB != SAME_METHOD`, and participant reuse is also unresolved.

### Oslo method contrast: NCT01034436 NW ↔ NCT03658681

Both reports involve fasted EDTA plasma and Vitas, but one explicitly uses GC-MS and the other LC-MS/MS. It is retained as a method contrast rather than exact comparability.

## Resolution frontier cannot admit

Executable v0.6.5 code still enforces:

```text
pair_can_admit_from_resolution_frontier(...) = FALSE
distinct_trial_ids_establish_independent_cohorts(...) = FALSE
same_lab_establishes_same_method(...) = FALSE
```

v0.6.5.1 adds a resolution receipt, not a new admission path. Any future fully resolved pair must return through the established extraction and hardened-comparability kernels.

## Historical reference manifests

```text
REFERENCE_DATASET_V0_1   → 0 authoritative observations
REFERENCE_DATASET_V0_2   → 1 authoritative observation
REFERENCE_DATASET_V0_3   → 10 context-separated authoritative observations
REFERENCE_DATASET_V0_4   → 0 exact comparable multi-study buckets
REFERENCE_DATASET_V0_5   → cohort/preanalytic hardening, 0 ready buckets
REFERENCE_DATASET_V0_6   → hardened-pair search frontier, 0 ready pairs
REFERENCE_DATASET_V0_6_1 → cohort/method resolution frontier, 0 ready pairs
REFERENCE_DATASET_V0_6_2 → one measurement-context blocker resolved; pair still blocked
```

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
DISTINCT_PUBLICATIONS != DISTINCT_COHORTS
DISTINCT_TRIAL_IDS != DISTINCT_COHORTS
COMMON_REPORTED_SOP != DISTINCT_COHORT_PROOF
COMBINED_DATASET != PER_TRIAL_REFERENCE_DISTRIBUTION
SAME_LAB != SAME_METHOD
SEARCH_OR_RESOLUTION_FRONTIER != EVIDENCE_AUTHORITY
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
