# Contributing to SCOBY-D0

SCOBY-D0 accepts contributions that make the evidence chain clearer, safer or more reproducible.

## Core rule

```text
NEW IDEA
  → DEFINE CLAIM
  → DEFINE NEGATIVE CONTROL
  → DEFINE MEASUREMENT
  → RUN FORWARD
  → RUN REVERSE
  → RECORD BREAK EDGE
  → PROMOTE ONLY IF GATES CLOSE
```

## Contributions we want

- reproducible BC production measurements;
- drying/porosity comparisons;
- oil-over-water sorption data;
- artificial-seawater and dynamic-water tests;
- retrieval and fragmentation data;
- mechanical press-recovery measurements;
- leachate/ecotoxicity characterization;
- lifecycle, energy and cost models;
- better controls and falsification tests;
- machine-readable experiment receipts.

## Required experiment metadata

At minimum record:

- sample ID and independent batch ID;
- feedstock and fermentation history;
- wash endpoint;
- wet/dry mass;
- drying/treatment history;
- dimensions/density;
- water salinity and temperature;
- oil/surrogate identity;
- exposure and drain times;
- motion history if dynamic;
- uptake, water uptake, retention, retrieval and press recovery;
- deviations from protocol.

## Claim boundaries

Do not submit claims that imply:

- field readiness without field-gate data;
- crude-oil safety from vegetable-oil tests;
- environmental safety of a surface treatment without leachate/ecotoxicity evidence;
- Ancient Egyptian SCOBY identity from lexical/process similarity;
- human clinical safety/efficacy from the legacy computational track.

## JANUS bidirectional requirement

Major research JSONs should include a `janus_tranception` block with forward, reverse, mirror status and promotion rule.

```text
HASH_IS_INTEGRITY_NOT_TRUTH
RANKING_IS_NOT_ADMISSION
FINALIST_IS_NOT_WINNER
```

## License

By contributing material intended for inclusion in this repository, you agree that it may be distributed under Apache-2.0 unless explicitly marked otherwise and compatible with repository policy.
