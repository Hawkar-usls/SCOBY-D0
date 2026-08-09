<div align="center">

# SCOBY-D0
### Provenance-blind C₂ context engineering · bacterial cellulose · computational biomanufacturing

`simulation-first` · `machine-readable` · `claim-bounded` · `no human dosing`

</div>

## Status

**Early research / computational hypothesis.** SCOBY-D0 studies a modular SCOBY / acetic-acid-bacteria platform as two separable engineering problems:

1. **materials:** bacterial cellulose as a programmable bio-derived substrate;
2. **C₂ context:** acetate as a common carbon carrier whose physiological meaning depends on route, matrix, exposure and microbiome context rather than producer provenance alone.

The current repository does **not** establish a human feeding system, clinical effect, food safety, or a validated engineered organism.

## Core boundary

```text
GM_PRODUCER != GM_ACETATE

SAME_MOLECULE != SAME_PHYSIOLOGICAL_EVENT

METABOLIC_EQUIVALENCE
MUST_NOT_READ
PROVENANCE
```

If purified acetate is chemically matched, producer lineage is metadata, not an extra molecular feature. Differences may still arise from concentration-time profile, route, counter-ion, pH, microbiome contact, co-metabolites, contaminants, or the broader fermentation matrix.

## Research line

```text
                           SCOBY-D0
                              |
               +--------------+--------------+
               |                             |
      bacterial cellulose                 acetate
               |                             |
      materials / sensing                 C2 BUS
               |                             |
      SkinGPT / composites        context reconstruction
                                             |
                         +-------------------+-------------------+
                         |                   |                   |
                      protein             lipids             chemicals
```

This architecture does **not** assume that acetate is complete nutrition. It treats acetate as a candidate C₂ interface for downstream biomanufacturing and as a controlled variable in computational context models.

## Current objects

- [`evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json`](evidence/ACETATE-SOURCE-EQUIVALENCE-v0.2.json) — frozen evidence-bound interpretation of the source-blind acetate comparison.
- [`experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json`](experiments/SKYBU-C2-CONTEXT-RECONSTRUCTION-v0.3.json) — preregistered computational search objective.
- [`src/context_search.py`](src/context_search.py) — synthetic benchmark kernel.
- [`tests/test_invariants.py`](tests/test_invariants.py) — anti-bias and execution invariants.
- [`PROJECT_STATUS.json`](PROJECT_STATUS.json) — machine-readable maturity and claim ceiling.

## v0.3 objective

```text
M* = argmin_M D(Phi(acetate + M), Phi(reference_context)) + lambda * complexity(M)
```

`PROVENANCE` is excluded from the feature vector. The current executable self-test uses **dimensionless synthetic proxies only**. It verifies optimizer mechanics and provenance blindness; it is not a model of a healthy-human target.

## Evidence anchors

- *Acetobacter pasteurianus* metabolic engineering can alter acetic-acid productivity without implying a new acetate molecular species; `adhA + pqqABCDE` was reported to raise average productivity by about 32% (PMID: 33174682).
- A stable-isotope study in 12 healthy subjects reported `36 ± 21%` systemic availability for **colonic-administered** acetate and substantial acetate→butyrate microbial interconversion; this is not a universal post-meal fraction (PMCID: PMC5233652).
- Kombucha fermentation is a variable microbial/metabolite matrix and requires process quality control (PMID: 39234548).
- Genetic programming of bacterial-cellulose-producing *Komagataeibacter* is experimentally established (PMCID: PMC4914174).

## Claim ceiling

```text
SIMULATION_PASS != IN_VIVO_VALIDATION
HASH != TRUTH
BIO_DERIVED != AUTOMATICALLY_SAFE
ENGINEERED_PRODUCER != ENGINEERED_PRODUCT_IDENTITY
PURIFIED_ACETATE != FERMENTATION_BROTH
ACETATE != COMPLETE_NUTRITION
COMPUTATIONAL_TARGET != CLINICAL_TARGET
```

No wet-lab genetic-engineering procedure, human dose, infusion rate, medical-device control or clinical recommendation belongs in the current scope.

## Related repositories

- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis) — local authoritative simulation/runtime semantics.
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN) — upstream-derived TWAI/CAN working copy used only as a telemetry/provenance abstraction.
- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry) — archival provenance and evidence-bound snapshots.

## License

Apache License 2.0, matching the repository's existing `LICENSE`. External papers, upstream code and third-party material remain under their respective terms.
