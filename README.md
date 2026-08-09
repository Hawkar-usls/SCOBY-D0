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
v0.6.5.2 PUBLIC PRIMARY-EVIDENCE BOUNDARY
  ↓
v0.6.5.3 OSLO SCFA METHOD PROVENANCE CORRECTION   ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH            🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
REAL_HARDENED_READY_PAIRS = 0
COHORT_INDEPENDENCE_RESOLVED_PAIRS = 0
PROVENANCE_CORRECTION_RECEIPTS = 1
NEW_AUTHORITATIVE_OBSERVATIONS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

## v0.6.5.3 — Oslo SCFA method correction

The historical v0.6.5 resolution frontier is preserved unchanged. A later primary-source re-audit found that one analytical-method binding in that historical object was incorrect.

For `NCT03658681`, the primary Methods text says that acetate, propionate and butyrate were measured in EDTA plasma at Vitas Analytical Service. The nearby `LC-MS/MS / QTRAP5500 / Kinetex Biphenyl` method is introduced for **nine bile acids**, not for SCFA.

Therefore the corrected binding is:

```text
NCT03658681 SCFA method
LC_MS_MS_QTRAP5500_KINETEX_BIPHENYL_NEGATIVE_MRM
→ UNRESOLVED_IN_PRIMARY_ARTICLE

NCT03658681 bile-acid method
= LC_MS_MS_QTRAP5500_KINETEX_BIPHENYL_NEGATIVE_MRM
```

For `NCT03293693`, the primary article reports fasting EDTA-plasma SCFA, immediate ice handling, rapid cold centrifugation, −80 °C storage and shipment to Vitas, but does not name the SCFA analytical-method family. It therefore remains:

```text
NCT03293693 SCFA method = UNRESOLVED_IN_PRIMARY_ARTICLE
```

This produces a new anti-bias boundary:

```text
TWO_UNRESOLVED_METHODS != METHOD_IDENTITY
UNKNOWN_A == UNKNOWN_B != ESTABLISHED_EQUALITY
SAME_LAB != SAME_METHOD
```

The older Oslo method-contrast record is corrected too. The `NCT01034436` primary report explicitly binds fasting EDTA-plasma SCFA to **GC-MS** at Vitas, but `NCT03658681` is now unresolved rather than LC-MS/MS:

```text
historical: GC_MS vs LC_MS_MS
corrected:  GC_MS vs UNRESOLVED
verdict:    METHOD_IDENTITY_UNRESOLVED_NOT_CONFIRMED_METHOD_CONTRAST
```

## Why the historical object is not rewritten

```text
HISTORICAL_OBJECT_NOT_REWRITTEN
CORRECTION_RECEIPT != ADMISSION
CORRECTION_OF_PROVENANCE != CHANGE_IN_BIOLOGICAL_TRUTH
```

The v0.6.5 object remains an auditable historical state. The correction is a separate machine-readable receipt:

- [`evidence/reference_context/OSLO_SCFA_METHOD_PROVENANCE_CORRECTION_V0_6_5_3.json`](evidence/reference_context/OSLO_SCFA_METHOD_PROVENANCE_CORRECTION_V0_6_5_3.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_4.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_4.json)
- [`tests/test_oslo_method_provenance_correction_v0653.py`](tests/test_oslo_method_provenance_correction_v0653.py)

## Maastricht state remains unchanged

The Maastricht pair `NCT01826162 ↔ NCT01983046` still has one measurement-context blocker resolved in the defined 2019 combined-analysis scope, while participant independence and separate direct-reported per-trial baseline SCFA distributions remain unresolved from public primary evidence.

```text
PUBLIC_SEARCH_EXHAUSTION != NEGATIVE_PROOF_OF_OVERLAP
RESTRICTED_DATA != PERMISSION_TO_INFER_MISSING_VALUES
FIGURE_VISIBILITY != DIRECT_REPORTED_NUMERIC_VALUE
```

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
REFERENCE_DATASET_V0_6_3 → Maastricht public evidence boundary
REFERENCE_DATASET_V0_6_4 → Oslo method-provenance correction, no admission change
```

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
ADJACENT_METHOD_TEXT != ANALYTE_METHOD_BINDING
SCFA_MEASUREMENT != BILE_ACID_MEASUREMENT
TWO_UNRESOLVED_METHODS != METHOD_IDENTITY
DISTINCT_TRIAL_IDS != DISTINCT_COHORTS
SAME_LAB != SAME_METHOD
CORRECTION_RECEIPT != EVIDENCE_AUTHORITY
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
