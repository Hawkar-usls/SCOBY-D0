# v0.6.1 source notes

This file records the public primary-human source lines used by the v0.6.1 multicontext ingestion expansion. It is provenance metadata, not a clinical recommendation.

## Boets et al. 2015 — inulin / stable-isotope dilution

- PMID: `26516911`
- PMCID: `PMC4663568`
- DOI: `10.3390/nu7115440`
- Cohort: 12 healthy adults.
- Context: oral inulin with a standard breakfast; stable-isotope dilution workflow; blood/breath follow-up over 12 h.
- Directly reported endogenous rates of appearance, mean ± SD:
  - acetate: `13.3 ± 4.8 µmol·kg⁻¹·min⁻¹`
  - propionate: `0.27 ± 0.09 µmol·kg⁻¹·min⁻¹`
  - butyrate: `0.28 ± 0.12 µmol·kg⁻¹·min⁻¹`
- Representations used for ingestion replay: NCBI PMC published full-text HTML and MDPI publisher full-text HTML.

These rate-of-appearance values are not concentrations and must not be merged with plasma or fecal concentration observations.

## Gill et al. 2022 — randomized high-/low-SCFA diet

- PMID: `36084000`
- PMCID: `PMC9630882`
- DOI: `10.1093/ajcn/nqac246`
- Cohort: 20 healthy adults, randomized crossover.
- Context: 21-day high-SCFA diet vs matched low-SCFA diet.
- Directly reported median (IQR) observations:
  - fecal total SCFA: high `86.6 (59.0)` vs low `75.4 (56.2) µmol/g`
  - plasma propionate: high `9.87 (12.3)` vs low `4.72 (7.6) µmol/L`
  - plasma butyrate: high `2.85 (1.35)` vs low `2.02 (1.29) µmol/L`
- Representations used for ingestion replay: NCBI PMC full-text HTML and NCBI PubMed structured published abstract.

High and low diet arms remain separate contexts. IQR is preserved as IQR and is never re-labelled as SD, SE, or CI.

## Claim ceiling

`INGESTION_AUTHORITY != HUMAN_REFERENCE_STANDARD`

`CROSS_REPRESENTATION_MATCH != BIOLOGICAL_REPLICATION`

No observation in this file is a safe formulation target, human dose, or universal healthy-human value.
