<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · evidence lineage · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 separates production science from context science. The repository does **not** establish a human feeding system, clinical effect, food safety, a universal human SCFA reference vector, or a validated engineered organism.

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
v0.6  FIRST INGESTION-AUTHORITATIVE OBSERVATION
  ↓
v0.6.1 MULTICONTEXT AUTHORITATIVE EXPANSION   ← current
  ↓
v0.7  UNCERTAINTY-AWARE PARETO SEARCH        🔒 BLOCKED
```

## v0.6.1 — context-specific authority

The current dataset contains **10 ingestion-authoritative observations from 3 primary human studies**, preserved in **6 distinct context buckets**.

New context families include:

```text
ORAL_INULIN + STANDARD_BREAKFAST + IV STABLE-ISOTOPE TRACER
→ systemic SCFA rate-of-appearance observations

21-D HIGH-SCFA DIET
→ fecal total-SCFA concentration
→ plasma propionate concentration
→ plasma butyrate concentration

21-D LOW-SCFA DIET
→ separate fecal/plasma observations
```

The project explicitly forbids treating these as interchangeable:

```text
PLASMA != FECAL
RATE_OF_APPEARANCE != CONCENTRATION
HIGH_SCFA_DIET != LOW_SCFA_DIET
SD != IQR
NO_CROSS_CONTEXT_AVERAGING
NO_CROSS_STUDY_COLLAPSE
```

Every new v0.6.1 observation is replayed through two source representations/process families and the existing v0.6 admission kernel. Cross-representation agreement establishes **SCOBY-D0 evidence-ingestion authority only**; it is not biological replication or external review.

## Current reference state

```text
AUTHORITATIVE_OBSERVATIONS = 10
PRIMARY_HUMAN_STUDIES       = 3
CONTEXT_BUCKETS              = 6
AUTHORITY_SCOPE              = SCOBY_D0_EVIDENCE_INGESTION_ONLY
HUMAN_REFERENCE_STANDARD    = NOT_ESTABLISHED
EXTERNAL_REVIEW              = NOT_YET_ESTABLISHED
BIOLOGICAL_REFERENCE_VECTOR = UNSET_PENDING_PRIMARY_DATA_AND_EXTERNAL_REVIEW
PARETO_SEARCH                = BLOCKED
```

The old manifests are preserved rather than rewritten:

```text
REFERENCE_DATASET_V0_1 → pre-v0.6 snapshot, 0 authoritative observations
REFERENCE_DATASET_V0_2 → first admission, 1 authoritative observation
REFERENCE_DATASET_V0_3 → multicontext state, 10 authoritative observations
```

## Current objects

- [`experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json`](experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json)
- [`experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json`](experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json)
- [`experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json`](experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json)
- [`experiments/SCOBY-D0-MULTICONTEXT-REFERENCE-EXPANSION-v0.6.1.json`](experiments/SCOBY-D0-MULTICONTEXT-REFERENCE-EXPANSION-v0.6.1.json)
- [`evidence/reference_context/MULTICONTEXT_EXTRACTION_LEDGER_V0_1.json`](evidence/reference_context/MULTICONTEXT_EXTRACTION_LEDGER_V0_1.json)
- [`evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_2.json`](evidence/reference_context/AUTHORITATIVE_REFERENCE_OBSERVATIONS_V0_2.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_3.json`](evidence/reference_context/REFERENCE_DATASET_V0_3.json)
- [`src/reference_admission.py`](src/reference_admission.py)
- [`src/multicontext_admission.py`](src/multicontext_admission.py)
- [`tests/test_multicontext_v061.py`](tests/test_multicontext_v061.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
EXTRACTION_REPLAY_PASS != BIOLOGICAL_TRUTH
CROSS_REPRESENTATION_MATCH != BIOLOGICAL_REPLICATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
MULTIPLE_OBSERVATIONS != BIOLOGICAL_REFERENCE_VECTOR
ACETATE != COMPLETE_NUTRITION
SIMULATION_OPTIMUM != SAFE_HUMAN_FORMULATION
```

No wet-lab genetic-engineering procedure, human dose, infusion rate, medical-device control or clinical recommendation belongs in the current scope.

## Related repositories

- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis)
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN)
- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry)

## License

Apache License 2.0. External papers, upstream code and third-party material remain under their respective terms.
