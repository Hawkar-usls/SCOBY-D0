# O2-transfer × assimilable-N carbon-allocation switch test

## Question

Does a reproducible interaction between oxygen-transfer state and assimilable-nitrogen availability create a narrow region in which Komagataeibacter remains active while a larger fraction of consumed carbon is recovered as extracellular bacterial cellulose?

This is **not** an optimization screen for maximum BC mass. The target is a mechanistic transition in allocation.

## Why the test exists

The 2026 nanobubble study (DOI `10.1016/j.ijbiomac.2026.150572`) showed that much higher oxygen transfer can strongly increase cell density without a proportional increase in BNC productivity. Separately, nitrogen availability/source strongly changes BC production (`10.1007/s00253-025-13702-z`; `10.3389/fmicb.2019.01958`). Together these results make an O2-transfer × assimilable-N interaction a stronger hypothesis than either axis alone.

## Factor definition

The oxygen factor is the **measured transfer state**, not nominal gas composition:

- dissolved-O2 profile;
- kLa or a validated transfer proxy;
- OTR or a validated transfer proxy.

The nitrogen factor is the **amount of assimilable nitrogen**. One defined nitrogen-source identity is frozen across the primary surface so that amount is not confused with source chemistry.

The primary discovery grid is:

```text
               N1 LOW      N2 MID      N3 HIGH
O1 LOW           A1          A2           A3
O2 MID           A4          A5           A6
O3 HIGH          A7          A8           A9
```

CO2 state, carbon source/starting carbon, pH, osmolality, strain, inoculum, temperature, geometry, shear/mixing context, nitrogen-source identity and buffer/ionic context are fixed or bounded.

## Primary endpoint

`BC_CARBON_ALLOCATION_PROXY`

```text
measured carbon recovered in dry BC
-----------------------------------
measured substrate carbon consumed
```

BC dry mass alone is insufficient for a carbon-allocation claim.

At minimum the experiment should account for:

- substrate carbon consumed;
- carbon recovered in dry BC;
- biomass/cell-carbon proxy;
- major measured organic-acid or other carbon sinks;
- CO2 carbon when quantified.

If carbon-balance closure is incomplete, the result remains a **partial allocation proxy** and must not be described as full metabolic flux.

## Cell-state protection

A candidate switch must not simply be a starvation/death boundary. A preregistered activity or viability readout and an independent biomass/cell-count readout are therefore required.

A region where BC allocation rises only because biomass collapses is classified as `STRESS_OR_STARVATION_ARTIFACT_CANDIDATE`, not as an allocation switch.

## Model gate

Three model families are frozen before confirmatory outcomes:

1. additive: `allocation ~ O2 + N`;
2. interaction: `allocation ~ O2 + N + O2:N`;
3. a predeclared piecewise or sigmoidal switch candidate.

A p-value alone does not promote the switch. The interaction/switch model must materially improve held-out prediction over the additive model by a predictive margin frozen before confirmation.

## Stage B: deterministic ridge densification

The 3×3 discovery grid is intentionally coarse. If a candidate transition appears, Stage B may densify it only by a frozen deterministic rule:

1. identify the largest adjacent change in the preregistered allocation endpoint;
2. add a midpoint;
3. add lower and upper flanks;
4. add one O2-axis control and one N-axis control.

No hand-picked point is allowed after inspecting material morphology or preferred outcomes.

## Stage C: independent confirmation

The ridge point and both flanks are repeated on fully independent batches. A one-batch ridge is not promotable.

## TOPA decision logic

```text
NO INTERACTION
  -> NO O2×N SWITCH SUPPORT

BC MASS CHANGES, ALLOCATION DOES NOT
  -> PRODUCTION EFFECT, NOT CARBON SWITCH

RIDGE + CELL ACTIVITY COLLAPSE
  -> STRESS / STARVATION CANDIDATE

RIDGE + PARTIAL CARBON BALANCE
  -> PARTIAL ALLOCATION PROXY ONLY

REPRODUCIBLE RIDGE + NONCOLLAPSED CELLS
+ HELD-OUT INTERACTION ADVANTAGE
  -> DOMAIN-BOUNDED O2×N ALLOCATION-SWITCH CANDIDATE
```

A later bidirectional rescue must move the mediator vector across and back over the ridge without changing nitrogen-source identity or source-factor availability before stronger causal-switch language is permitted.

## Claim ceiling

Even a full pass does not establish:

- a universal biological law;
- full metabolic flux without closed carbon balance;
- a gaseous-N2-specific effect;
- nitrogen fixation;
- material memory;
- any human-milk or placental effect.

Current promotion remains `P0`.

## Safety scope

This file is a non-operational preregistration. Any gas-transfer, pressure or culture work remains subject to appropriate laboratory SOPs. No donor human milk, placenta or human tissue is part of this gate.
