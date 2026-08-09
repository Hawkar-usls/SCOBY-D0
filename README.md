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
v0.6.5–v0.6.5.4 BLOCKER RESOLUTION + EVIDENCE BOUNDARIES
  ↓
v0.6.6 HARDENED CANDIDATE LEDGER                    ← current
  ↓
v0.7   UNCERTAINTY-AWARE PARETO SEARCH              🔒 BLOCKED
```

## Current state

```text
AUTHORITATIVE_OBSERVATIONS = 10
EXISTING_CONTEXT_BUCKETS = 6
LITERATURE_CANDIDATES = 6
MEASUREMENT_KEY_FULLY_BOUND_SINGLES = 2
EXACT_ELEVEN_FIELD_MATCHING_PAIRS = 0
REAL_HARDENED_READY_PAIRS = 0
NEW_AUTHORITATIVE_OBSERVATIONS = 0
POOLED_REFERENCE = NOT_CREATED
BIOLOGICAL_REFERENCE_VECTOR = UNSET
PARETO_SEARCH = BLOCKED
```

## v0.6.6 — exact-key candidate ledger

The ledger uses the same literal 11-field surface as the existing v0.6.3 admission kernel:

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
preanalytic_handling
analytical_method_family
```

It is a **discovery object, not an admission path**. Ranking a candidate pair can only tell us where to search next.

```text
CANDIDATE_LEDGER != EVIDENCE_AUTHORITY
SINGLE_FULLY_BOUND != COMPARABLE_READY
RANKING != ADMISSION
```

### Fully bound single #1 — MASLD 2024 healthy controls

For the healthy-control arm of PMID `38262952` / PMCID `PMC10804800`:

```text
HEALTHY
EDTA_PLASMA
FASTING_BASELINE
AT_LEAST_4_HOURS
NO_TRACER
ACETATE
CONCENTRATION
umol/L
SD
EDTA_IMMEDIATE_ICE_CENTRIFUGE_WITHIN_2_HOURS_STORE_MINUS80C
BEVITAL_ISOTOPE_LABELED_GC_MS_MS_AUTOMATED_WORKUP

acetate = 57.6 ± 25.6 µmol/L
n = 50
```

### Fully bound single #2 — USDA Nutritional Phenotyping Study 2024

For PMID `39173973` / PMCID `PMC11600052` / `NCT02367287`:

```text
HEALTHY
EDTA_PLASMA
FASTING_BASELINE
12_HOURS_WATER_ONLY
NO_TRACER
ACETATE
CONCENTRATION
umol/L
SD
EDTA_REFRIGERATED_CENTRIFUGE_4C_1300G_10MIN_STORE_MINUS80C
COLUMBIA_3NPH_UPLC_MS_MS_XEVO_TQS_POSITIVE_ESI_MRM

reported acetate = 0.08 ± 0.08 nmol/µL
normalized acetate = 80 ± 80 µmol/L
n = 315
```

These are both strong **single measurement contexts**, but they are not a hardened pair:

```text
AT_LEAST_4_HOURS != 12_HOURS_WATER_ONLY
MASLD_PREANALYTICS != USDA_PREANALYTICS
BEVITAL_GC_MS_MS != COLUMBIA_3NPH_UPLC_MS_MS
```

No averaging or method-family collapsing is allowed to erase those differences.

## Other ledger candidates

- **RyeWeight2 / NCT04203758** — heparin plasma and Fristedt-2024 method are study-bound; baseline acetate is reported as geometric mean + 95% CI, but exact SCFA fasting duration and preanalytics remain unresolved in the current binding.
- **Bain 2022** — useful GC-MS / tube-comparison method context, but fasting and a clean lithium-heparin group estimate with uncertainty are not bound.
- **Defatted-rice-bran crossover** — protocol binds lithium-heparin plasma and a targeted stable-isotope LCMS organic-acid workflow, but baseline fasting and direct acetate estimate/uncertainty remain unbound.
- **Fristedt 2024** — method authority only; an aggregate method-validation plasma set is not a distinct biological cohort.

```text
METHOD_AUTHORITY_ONLY != BIOLOGICAL_COHORT
PROTOCOL != NUMERIC_OBSERVATION
SD != CI95
EDTA_PLASMA != HEPARIN_PLASMA
```

## Machine-readable objects

- [`evidence/reference_context/HARDENED_CANDIDATE_LEDGER_V0_6_6.json`](evidence/reference_context/HARDENED_CANDIDATE_LEDGER_V0_6_6.json)
- [`evidence/reference_context/REFERENCE_DATASET_V0_6_6.json`](evidence/reference_context/REFERENCE_DATASET_V0_6_6.json)
- [`src/candidate_ledger.py`](src/candidate_ledger.py)
- [`tests/test_candidate_ledger_v066.py`](tests/test_candidate_ledger_v066.py)

Ledger content SHA-256:

```text
d28cdcbac1e9cf401e3eb2074a4fb7cb6e85387207e867901f37d2cc528a292d
```

The hash identifies this object version; it does not establish biological truth.

## Next gate

Find a second primary human cohort matching **one complete 11-field key literally**, then separately establish pair-specific cohort independence and replay both records through the existing v0.5 extraction lineage and v0.6.3 hardened kernel.

```text
DO_NOT_RELAX_KEY_FIELDS_TO_CREATE_A_MATCH
DISTINCT_PUBLICATION != DISTINCT_COHORT_ESTABLISHED
COMPARABLE_READY != POOLED_REFERENCE
```

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD
CANDIDATE_LEDGER != EVIDENCE_AUTHORITY
SINGLE_FULLY_BOUND != COMPARABLE_READY
METHOD_AUTHORITY != BIOLOGICAL_COHORT
PROTOCOL != NUMERIC_OBSERVATION
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
