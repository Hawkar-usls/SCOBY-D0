# Cross-domain defined interface-equivalence test

## Question

Can distinct defined biological-state-associated inputs produce the same bacterial-cellulose phenotype when their measurable interface/microenvironment state is matched?

This test does **not** compare provenance labels such as `MOTHER_OF_SON`, `XY_PLACENTA`, or `EXTREMOPHILE_RECOVERY` as if those labels were causal variables. It asks whether a portable measured mediator layer explains the BC response.

```text
DEFINED INPUT
  -> EARLY INTERFACE / OXYGEN STATE
  -> BC DEPOSITION
  -> STRUCTURE / MECHANICS
```

## Candidate families

- PvLEA4: defined extremophile-recovery protein candidate.
- Human lactoferrin: defined milk-side protein with direct air/water + phospholipid interfacial precedent.
- Human lactoferrin + DPPC: deliberately simplified protein-lipid interface model; it is **not** claimed to recreate human milk or MFGM.
- Non-nutritional surface-tension reference: independent interface perturbation control.

Specificity/confound controls include vehicle, DPPC-only, generic soluble protein, trehalose and lactose.

## Stage A — abiotic calibration

No BC producer is present. Each candidate family is profiled for:

- surface/interfacial tension;
- dissolved oxygen or oxygen-transfer proxy;
- pH;
- osmolality or water-activity proxy;
- total protein / phospholipid / carbohydrate load where relevant.

The purpose is to find cross-family match points for the **measured mediator vector**. Candidate levels may be selected only from these mediator measurements plus solubility, stability and reagent feasibility.

**Freeze rule:** all Stage-B treatment levels and pair-match tolerances are locked before any BC outcome is inspected.

**Tolerance rule:** matching tolerance must come from instrument repeatability, technical replication or an independent calibration set. The tolerance may not be widened after seeing BC outcomes.

If a cross-family mediator match cannot be obtained, the equivalence question is blocked rather than rescued post hoc.

## Stage B — locked BC challenge

The same frozen BC-producing system is used across all ten arms in `experiments/CROSS_DOMAIN_DEFINED_INTERFACE_EQUIVALENCE_MATRIX_v1.0.csv`.

Mechanism is read before substantial pellicle formation:

```text
INPUT
  -> surface/interfacial tension
  -> O2 state / transfer proxy
  -> pellicle onset
  -> dry BC mass
  -> structure
  -> mechanics
```

### Primary material endpoint

`dry_BC_mass` under one frozen matched-batch harvest rule.

### Co-primary mechanism endpoints

- surface/interfacial tension before substantial pellicle formation;
- dissolved oxygen or oxygen-transfer proxy before substantial pellicle formation.

### Secondary endpoints

- pellicle onset time;
- thickness;
- water holding / wet-state retention;
- pore/fiber architecture where an orthogonal imaging method is available;
- mechanical response where feasible;
- cellulose identity by an orthogonal material method.

## Equivalence, not absence of significance

`p > 0.05` does not establish that two BC outcomes are equivalent.

A shared-mediator claim requires a preregistered equivalence margin and a confidence interval or equivalent bounded decision rule. The margin must be fixed before treatment outcomes using one of:

1. historical batch variability;
2. an independent pilot;
3. an engineering minimum-difference-of-interest rationale.

The same treatment outcomes being judged may not be used to manufacture the equivalence margin.

## Decision tree

```text
CAN DISTINCT INPUTS BE MEDIATOR-MATCHED?
  |
  +-- NO -> CALIBRATION BLOCKED; NO SOURCE-LABEL CONCLUSION
  |
  +-- YES
       |
       v
DO MATCHED INPUTS PRODUCE EQUIVALENT BC?
       |
       +-- YES -> SHARED INTERFACE MEDIATOR CANDIDATE
       |
       +-- NO  -> SOURCE-SPECIFIC OR MISSING-MEDIATOR RESIDUAL
```

Then attack specificity:

- generic protein phenocopies candidate protein -> no PvLEA4/lactoferrin specificity;
- DPPC-only phenocopies lactoferrin+DPPC -> phospholipid/interface effect;
- non-nutritional interface reference phenocopies candidate -> defined microenvironment candidate;
- residual survives measured matching -> identify a new mediator or defined source-specific factor before any promotion.

## Human-material boundary

This gate uses **defined components only**. It does not use donor human milk or placental tissue and is not a human-material culture protocol.

The older placenta/milk branch remains a separate institution-only question. Fetal sex remains a covariate/provenance variable unless a measured composition-property relation is replicated across donors.

## Material-memory boundary

`BIOLOGICAL STATE -> PHYSICAL INTERFACE -> MATERIAL MEMORY` remains **closed** at this stage.

A future material-memory gate requires a transient, time-bounded mediator exposure to leave a persistent, spatially localizable BC layer difference after the mediator is removed or changed. A final bulk difference alone is not memory.

## Current evidence ceiling

```text
P0
PVLEA4 -> BC = UNMEASURED
LACTOFERRIN -> BC = UNMEASURED
LACTOFERRIN+DPPC -> BC = UNMEASURED
SHARED INTERFACE MEDIATOR = PREREGISTERED CANDIDATE
MATERIAL MEMORY = CLOSED
```
