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
v0.6.4 HARDENED PAIR SEARCH FRONTIER          ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH        🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
V0_6_3_HARDENED_READY_BUCKETS = 0
V0_6_4_FRONTIER_PAIRS = 3
REAL_HARDENED_READY_PAIRS = 0
NEW_AUTHORITY_FROM_FRONTIER = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

v0.6.4 makes literature discovery itself claim-bounded:

```text
PROTOCOL_SIMILARITY != COMPARABILITY
DISTINCT_PUBLICATION != DISTINCT_COHORT
FRONTIER_RANK != ADMISSION_PRIORITY
FRONTIER_OBJECT != ADMISSION_CHANNEL
```

The frontier currently preserves three tempting pairings and their exact blockers:

1. **Pomare 1985 ↔ Akanji 1991** — both use oral 20 g lactulose and peripheral acetate measurements, but fasting duration, specimen semantics, uncertainty semantics, peak timing, population class and measurement context do not match exactly.
2. **Pouteau 1998 ↔ Galuppo 2021** — both use 20 g lactulose plus continuous IV acetate tracer, but adult/youth populations, tracer isotope, tracer duration/dose and measurement context differ.
3. **Galuppo 2021 ↔ Galuppo 2023** — very high surface protocol similarity, but participant overlap is confirmed. Distinct papers therefore do **not** provide independent human cohorts.

The third pair is retained as a real-world adversarial case:

```text
PROTOCOL_MATCH = HIGH
PUBLICATION_IDENTITY = DISTINCT
COHORT_INDEPENDENCE = FAIL_CONFIRMED_OVERLAP
VERDICT = PROTOCOL_MATCH_BUT_INDEPENDENCE_FAIL
```

## Hardened comparability still applies

```text
CONFIRMED_PARTICIPANT_OVERLAP => NOT_INDEPENDENT
UNRESOLVED_PARTICIPANT_OVERLAP != DISTINCT_COHORT_ESTABLISHED
FRESH_SPECIMEN != STORED_SPECIMEN unless validated equivalence exists
UNKNOWN_PREANALYTIC_HANDLING => NOT_COMPARABLE
UNKNOWN_ANALYTICAL_METHOD => NOT_COMPARABLE
SERUM != PLASMA unless equivalence is predeclared + supported
TRACER != NO_TRACER
SD != SE != SEM != IQR != RANGE
COMPARABLE_READY != POOLED_REFERENCE
```

A frontier ranking may prioritize what to inspect next, but executable code forbids it from changing admission status, authoritative-observation counts, pooled-reference state, biological vector state, or Pareto state.

## Historical reference manifests

```text
REFERENCE_DATASET_V0_1 → 0 authoritative observations
REFERENCE_DATASET_V0_2 → 1 authoritative observation
REFERENCE_DATASET_V0_3 → 10 context-separated authoritative observations
REFERENCE_DATASET_V0_4 → 0 exact comparable multi-study buckets
REFERENCE_DATASET_V0_5 → cohort/preanalytic hardening, 0 ready buckets
REFERENCE_DATASET_V0_6 → hardened-pair search frontier, 0 ready pairs
```

## Current objects

- [`experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json`](experiments/SCOBY-D0-CROSS-STUDY-INDEPENDENCE-PREANALYTIC-HARDENING-v0.6.3.json)
- [`experiments/SCOBY-D0-HARDENED-PAIR-SEARCH-FRONTIER-v0.6.4.json`](experiments/SCOBY-D0-HARDENED-PAIR-SEARCH-FRONTIER-v0.6.4.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6.json`](evidence/reference_context/REFERENCE_DATASET_V0_6.json)
- [`src/cross_study_hardening.py`](src/cross_study_hardening.py)
- [`src/pair_search_frontier.py`](src/pair_search_frontier.py)
- [`tests/test_cross_study_hardening_v063.py`](tests/test_cross_study_hardening_v063.py)
- [`tests/test_pair_search_frontier_v064.py`](tests/test_pair_search_frontier_v064.py)

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
DISTINCT_PUBLICATIONS != DISTINCT_COHORTS
PROTOCOL_SIMILARITY != COMPARABILITY
SEARCH_FRONTIER != EVIDENCE_AUTHORITY
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
