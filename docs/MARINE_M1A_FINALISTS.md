# SCOBY-D0 — Marine M1A Finalists

## Decision

Two branches advance into the marine pad program as **finalists**, not winners.

### A — D3 performance lead

`FREEZE_DRY_BC + MINIMAL_ENVIRONMENTALLY_COMPATIBLE_HYDROPHOBIC_SURFACE_ENGINEERING`

Purpose: maximize the probability of passing oil-over-water selectivity, retention and press-recovery gates.

Main risks: freeze-drying cost, coating complexity, leachables/ecotoxicity and scale-up.

### B — D1 cost-down challenger

`LOW_COMPACTION_AIR_DRY_BC`

Purpose: test whether a dramatically cheaper process can pass the same hard marine gates without expensive aerogel processing.

Main risks: native BC hydrophilicity, pore collapse and poor oil/water selectivity.

## Controls

- `D2_FREEZE_DRY_UNMODIFIED` — isolates the benefit of preserved porosity from the benefit of hydrophobic treatment.
- one commercial oil-sorbent pad — external market reference.

## Feedstock

Green tea vs black tea remains **OPEN**. The Stage-0 matched screen chooses feedstock. Tea identity is not part of the field claim and must not be promoted from literature-only differences.

## M1A matrix

Use 100×100 mm pads. Run matched fresh-water and artificial-seawater conditions first. Keep the fluid history, drain time, sample conditioning and weighing procedure frozen across branches.

Primary metrics:

- oil uptake, g/g;
- water uptake, g/g;
- oil/water selectivity;
- retention after retrieval/passive drain;
- retrieval fraction / fragment loss;
- buoyancy;
- single-press recovery fraction;
- salinity penalty;
- cost per kg recovered oil.

## Winner rule

A branch cannot win on maximum g/g alone.

First it must pass every hard M1 gate. Then compare surviving branches on a Pareto surface:

```text
MINIMIZE  cost_per_kg_recovered_oil
MINIMIZE  energy_per_kg_recovered_oil
MAXIMIZE  oil_water_selectivity
MAXIMIZE  recovered_oil_per_dry_kg
MAXIMIZE  retrieval_fraction
MAXIMIZE  mechanical_integrity
```

No arbitrary weighted score is required.

## JANUS reverse audit

```text
FORWARD
BC branch
→ marine pad
→ selective uptake
→ retrieve
→ press
→ recovered oil
→ cost accounting
→ winner

REVERSE
winner
→ requires measured cost/recovery
→ requires full retrieval
→ requires marine selectivity
→ requires reproducible pad
→ requires defined BC branch
```

Current state: `DESIGN_LOOP_CLOSED_EMPIRICAL_WINNER_OPEN`.
