<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · evidence lineage · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 separates production science from context science. It does not establish a human feeding system, clinical effect, food safety, a universal human SCFA reference vector, or a validated engineered organism.

## Core boundaries

```text
GM_PRODUCER != GM_ACETATE
SAME_MOLECULE != SAME_PHYSIOLOGICAL_EVENT
ACETATE_PRODUCER_PROVENANCE != EVIDENCE_PROVENANCE
CITATION_LOCATOR != EXTRACTION_PROVENANCE
```

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
v0.6.2 COMPARABLE-CONTEXT QUALIFICATION        ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH         🔒 BLOCKED
```

## Current evidence state

v0.6.1 established **10 ingestion-authoritative observations from 3 primary human studies**, retained in **6 context buckets**. v0.6.2 asks a stricter question: do at least two independent primary studies support observations with an **exactly matching context key**?

```text
AUTHORITATIVE_OBSERVATIONS = 10
PRIMARY_HUMAN_STUDIES_WITH_INGESTION_AUTHORITY = 3
EXISTING_CONTEXT_BUCKETS = 6

COMPARABLE_CANDIDATE_STUDIES_EXAMINED = 4
EXACT_MULTI_STUDY_COMPARABLE_BUCKETS = 0
CROSS_STUDY_AGGREGATION = BLOCKED
```

The exact comparability key contains:

```text
population_health_class
specimen
route_or_exposure
fasting_duration
tracer_state
analyte
metric
units
uncertainty_semantics
```

A bucket becomes `COMPARABLE_READY_NOT_POOLED` only when at least two independent primary studies have complete, exactly matching keys.

## v0.6.2 — negative result is preserved

The first target family was superficially simple:

```text
HEALTHY_FASTING_PERIPHERAL_ACETATE_CONCENTRATION
```

Four primary-study candidates were examined, but no exact multi-study bucket qualified.

Key blockers include:

```text
TRACER_EXPOSURE_MISMATCH
SPECIMEN_IDENTITY_DIFFERENCE
POPULATION_CLASS_DIFFERENCE
FASTING_DURATION_UNRESOLVED
UNCERTAINTY_SEMANTICS_DIFFERENCE_OR_UNRESOLVED
SECOND_SOURCE_REPRESENTATION_MISSING
```

For example, a 12-h fasting plasma acetate value obtained after a low-dose isotope-tracer baseline is **not silently merged** with an untraced fasting plasma value. Serum and plasma remain distinct unless an equivalence rule is predeclared and independently supported. Missing fasting duration is preserved as unresolved rather than inferred.

## Fail-closed comparability invariants

```text
PLASMA != FECAL
SERUM != PLASMA            unless equivalence is predeclared + supported
RATE_OF_APPEARANCE != CONCENTRATION
TRACER != NO_TRACER
UNKNOWN_FASTING_DURATION != 12_HOURS
SD != SE != SEM != IQR != RANGE
SAME_STUDY_MULTIPLE_COHORTS != TWO_INDEPENDENT_STUDIES
UNRESOLVED_KEY_FIELD => NOT_COMPARABLE
TWO_INDEPENDENT_PRIMARY_STUDIES_REQUIRED_FOR COMPARABLE_READY
COMPARABLE_READY != POOLED_REFERENCE
NO_AVERAGING_AT_V0_6_2
```

This negative qualification does not invalidate any study and does not remove any of the 10 existing ingestion-authoritative observations. It only prevents an unjustified cross-study collapse.

## Current reference state

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
REFERENCE_DATASET_V0_4 → comparability qualification: 0 exact multi-study buckets
```

## Current objects

- [`experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json`](experiments/SCOBY-D0-EVIDENCE-DERIVED-REFERENCE-CONTEXT-v0.4.json)
- [`experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json`](experiments/SCOBY-D0-EVIDENCE-EXTRACTION-LINEAGE-v0.5.json)
- [`experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json`](experiments/SCOBY-D0-AUTHORITATIVE-REFERENCE-ADMISSION-v0.6.json)
- [`experiments/SCOBY-D0-MULTICONTEXT-REFERENCE-EXPANSION-v0.6.1.json`](experiments/SCOBY-D0-MULTICONTEXT-REFERENCE-EXPANSION-v0.6.1.json)
- [`experiments/SCOBY-D0-COMPARABLE-CONTEXT-BUCKET-QUALIFICATION-v0.6.2.json`](experiments/SCOBY-D0-COMPARABLE-CONTEXT-BUCKET-QUALIFICATION-v0.6.2.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_4.json`](evidence/reference_context/REFERENCE_DATASET_V0_4.json)
- [`src/comparable_context.py`](src/comparable_context.py)
- [`tests/test_comparable_context_v062.py`](tests/test_comparable_context_v062.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
EXTRACTION_REPLAY_PASS != BIOLOGICAL_TRUTH
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
MULTIPLE_OBSERVATIONS != BIOLOGICAL_REFERENCE_VECTOR
COMPARABLE_READY != POOLED_REFERENCE
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
