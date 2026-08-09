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
v0.6.5.2 MAASTRICHT PUBLIC PRIMARY-EVIDENCE BOUNDARY
  ↓
v0.6.5.3 OSLO SCFA METHOD PROVENANCE CORRECTION
  ↓
v0.6.5.4 OSLO PUBLIC METHOD + COHORT EVIDENCE BOUNDARY ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH                 🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
REAL_HARDENED_READY_PAIRS = 0
COHORT_INDEPENDENCE_RESOLVED_PAIRS = 0
PUBLIC_EVIDENCE_BOUNDARY_RECEIPTS = 2
PROVENANCE_CORRECTION_RECEIPTS = 1
NEW_AUTHORITATIVE_OBSERVATIONS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

## v0.6.5.4 — Oslo public evidence boundary

The corrected Oslo near-pair is:

```text
NCT03293693 ↔ NCT03658681
```

The checked primary record establishes a close surface measurement context. Both studies were sponsored by Oslo Metropolitan University and concern healthy adults. The NCT03293693 primary article reports ≥12 h fasting, EDTA plasma, immediate ice handling, centrifugation within 10 min at 1500 g / 4 °C / 10 min, −80 °C storage, and shipment to Vitas Analytical Service. The NCT03658681 primary article reports ≥12 h fasting and acetate/propionate/butyrate measured in EDTA plasma at Vitas.

But neither checked primary article names the **SCFA analytical-method family**.

```text
NCT03293693 SCFA method = UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE
NCT03658681 SCFA method = UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE
METHOD_IDENTITY = NOT_ESTABLISHED
```

The nearby NCT03658681 `LC-MS/MS / QTRAP5500 / Kinetex Biphenyl` workflow remains explicitly bound to **bile acids**, not SCFA.

## Cohort independence also remains unresolved

The trial registrations establish different reported study periods and the primary papers use distinct ethics approvals. Those are useful provenance facts, but they do not explicitly state that participants were never reused between studies.

```text
NONOVERLAPPING_STUDY_PERIODS != NO_PARTICIPANT_REUSE_PROOF
DISTINCT_ETHICS_APPROVALS != DISTINCT_COHORT_PROOF
ABSENCE_OF_OVERLAP_STATEMENT != COHORT_INDEPENDENCE
```

Therefore:

```text
PARTICIPANT_OVERLAP_OR_NONOVERLAP
= UNRESOLVED_FROM_CHECKED_PUBLIC_PRIMARY_EVIDENCE
```

## Unknown + unknown is not a match

This boundary explicitly forbids a subtle false-positive route:

```text
TWO_UNRESOLVED_METHODS != METHOD_IDENTITY
UNKNOWN_A == UNKNOWN_B != ESTABLISHED_EQUALITY
SAME_LAB != SAME_METHOD
```

A method may become comparable only after study-bound method provenance is established for both observations. Shared Vitas provenance cannot substitute for that evidence.

## Current boundary objects

- [`evidence/reference_context/OSLO_SCFA_METHOD_PROVENANCE_CORRECTION_V0_6_5_3.json`](evidence/reference_context/OSLO_SCFA_METHOD_PROVENANCE_CORRECTION_V0_6_5_3.json)
- [`evidence/reference_context/OSLO_PUBLIC_METHOD_COHORT_EVIDENCE_BOUNDARY_V0_6_5_4.json`](evidence/reference_context/OSLO_PUBLIC_METHOD_COHORT_EVIDENCE_BOUNDARY_V0_6_5_4.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_5.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_5.json)
- [`tests/test_oslo_public_evidence_boundary_v0654.py`](tests/test_oslo_public_evidence_boundary_v0654.py)

## Historical state is preserved

The historical v0.6.5 object that contained the later-corrected NCT03658681 method binding is not rewritten. v0.6.5.3 carries the correction; v0.6.5.4 records the remaining public-evidence boundary.

```text
HISTORICAL_OBJECT_NOT_REWRITTEN
CORRECTION_RECEIPT != ADMISSION
PUBLIC_EVIDENCE_BOUNDARY != ADMISSION
```

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
ADJACENT_METHOD_TEXT != ANALYTE_METHOD_BINDING
SCFA_MEASUREMENT != BILE_ACID_MEASUREMENT
TWO_UNRESOLVED_METHODS != METHOD_IDENTITY
DISTINCT_TRIAL_IDS != DISTINCT_COHORTS
NONOVERLAPPING_STUDY_PERIODS != COHORT_INDEPENDENCE
DISTINCT_ETHICS_APPROVALS != COHORT_INDEPENDENCE
SAME_LAB != SAME_METHOD
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
