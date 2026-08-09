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
v0.6.5 COHORT + METHOD RESOLUTION FRONTIER      ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH         🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
V0_6_5_RESOLUTION_NEAR_PAIRS = 3
REAL_HARDENED_READY_PAIRS = 0
COHORT_INDEPENDENCE_RESOLVED_PAIRS = 0
METHOD_IDENTITY_RESOLVED_PAIRS = 0
NEW_AUTHORITY_FROM_RESOLUTION_FRONTIER = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

v0.6.5 is deliberately **not** a new admission mechanism. It records what must be resolved before a near-pair may be replayed through the existing hardened admission kernel.

```text
DISTINCT_TRIAL_ID != DISTINCT_COHORT_ESTABLISHED
NONOVERLAPPING_RECRUITMENT_WINDOWS != NO_PARTICIPANT_REUSE_PROOF
SAME_LAB != SAME_ANALYTICAL_METHOD
SIMILAR_PREANALYTICS != EXACT_MEASUREMENT_CONTEXT
RESOLUTION_PRIORITY != ADMISSION_PRIORITY
```

## Priority resolution targets

### Maastricht: NCT01826162 ↔ NCT01983046

Both registrations describe overweight/obese men aged 20–50 without diabetes at Maastricht, and their reported trial windows are sequential rather than overlapping. The later registry explicitly identifies the earlier protocol as the pilot study. Those facts improve provenance but do **not** establish participant independence.

Current blockers include:

```text
PARTICIPANT_REUSE_BETWEEN_PILOT_AND_FOLLOWUP_TRIAL_UNRESOLVED
PER_TRIAL_BASELINE_SCFA_OBSERVATIONS_NOT_SEPARATELY_EXTRACTION_BOUND
PER_TRIAL_PREANALYTIC_AND_ANALYTICAL_CONTEXT_NOT_YET_BOUND_AS_EXACT_IDENTICAL
```

### OsloMet: NCT03293693 ↔ NCT03658681

This is a close measurement-context near-pair:

```text
healthy normal-weight adults
≥12 h fast
EDTA plasma
immediate ice
centrifuge within 10 min at 1500 g / 4 °C / 10 min
−80 °C storage
Vitas Analytical Service
```

But the NCT03293693 primary article does not explicitly identify its SCFA analytical method, while the NCT03658681 primary article binds SCFA measurement to an LC–MS/MS QTRAP5500 / Kinetex Biphenyl negative-MRM workflow. Therefore:

```text
SAME_LAB != SAME_METHOD
```

Participant reuse between the two OsloMet studies is also not explicitly excluded, so the pair remains blocked.

### Oslo method-contrast: NCT01034436 NW ↔ NCT03658681

The 2020 NCT01034436 report includes a healthy normal-weight subgroup with 12-h fasting EDTA plasma, immediate-ice/rapid-cold-centrifugation handling, −80 °C storage and Vitas analysis. Its SCFA method is explicitly GC-MS. NCT03658681 uses LC-MS/MS. This pair is retained as a useful **method contrast**, not as exact comparability.

## Resolution frontier cannot admit

Executable v0.6.5 code enforces:

```text
pair_can_admit_from_resolution_frontier(...) = FALSE

distinct_trial_ids_establish_independent_cohorts(...) = FALSE
same_lab_establishes_same_method(...) = FALSE
```

Even if all blockers on a frontier record were manually removed, v0.6.5 still has no authority to create an admitted observation or a comparable-ready bucket. The pair must return to the established v0.5/v0.6/v0.6.3 replay path.

## Historical reference manifests

```text
REFERENCE_DATASET_V0_1   → 0 authoritative observations
REFERENCE_DATASET_V0_2   → 1 authoritative observation
REFERENCE_DATASET_V0_3   → 10 context-separated authoritative observations
REFERENCE_DATASET_V0_4   → 0 exact comparable multi-study buckets
REFERENCE_DATASET_V0_5   → cohort/preanalytic hardening, 0 ready buckets
REFERENCE_DATASET_V0_6   → hardened-pair search frontier, 0 ready pairs
REFERENCE_DATASET_V0_6_1 → cohort/method resolution frontier, 0 ready pairs
```

## Current objects

- [`experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json`](experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json)
- [`experiments/SCOBY-D0-HARDENED-PAIR-SEARCH-FRONTIER-v0.6.4.json`](experiments/SCOBY-D0-HARDENED-PAIR-SEARCH-FRONTIER-v0.6.4.json)
- [`experiments/SCOBY-D0-COHORT-METHOD-RESOLUTION-FRONTIER-v0.6.5.json`](experiments/SCOBY-D0-COHORT-METHOD-RESOLUTION-FRONTIER-v0.6.5.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_1.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_1.json)
- [`src/cross_study_hardening.py`](src/cross_study_hardening.py)
- [`src/pair_search_frontier.py`](src/pair_search_frontier.py)
- [`src/resolution_frontier.py`](src/resolution_frontier.py)
- [`tests/test_resolution_frontier_v065.py`](tests/test_resolution_frontier_v065.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
DISTINCT_PUBLICATIONS != DISTINCT_COHORTS
DISTINCT_TRIAL_IDS != DISTINCT_COHORTS
SAME_LAB != SAME_METHOD
PROTOCOL_SIMILARITY != COMPARABILITY
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
