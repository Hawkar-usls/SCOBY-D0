<div align="center">

# SCOBY-D0
### Evidence-gated bacterial-cellulose research · marine oil-sorbent R&D · reversible JANUS audit

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Status](https://img.shields.io/badge/Status-Early%20R%26D-orange.svg)
![Marine Gate](https://img.shields.io/badge/Marine%20Gate-M1A%20Pre--registered-0b7285.svg)

`machine-readable` · `claim-bounded` · `forward ↔ reverse` · `retrieve what you deploy`

</div>

## What this repository is

SCOBY-D0 is an open research program built around **bacterial cellulose (BC)** produced by SCOBY-like fermentation systems. The current lead application is a low-cost, retrievable sorbent architecture for oil-on-water cleanup.

The project deliberately separates three questions:

```text
CAN BC BE PRODUCED REPRODUCIBLY?
        ↓
CAN THE MATERIAL SELECTIVELY TAKE UP OIL OVER WATER?
        ↓
CAN THE WHOLE SORBENT BE RETRIEVED, PRESSED AND ACCOUNTED FOR?
```

No field-readiness claim is made until those gates close empirically.

## Active lead track — marine oil-spill sorbent

Current program:

```text
GREEN vs BLACK FEEDSTOCK
        ↓
D0–D3 DRYING / STRUCTURE SCREEN
        ↓
50×50 mm COUPONS
        ↓
OIL / WATER SELECTIVITY
        ↓
PRESS RECOVERY
        ↓
100×100 mm M1A MARINE PADS
        ↓
FRESH WATER vs ARTIFICIAL SEAWATER
        ↓
M1B DYNAMIC SALTWATER
        ↓
1 m RETRIEVABLE BOOM CARTRIDGE
```

### M1A finalists

**Finalist A — performance lead**  
`D3_FREEZE_DRY + MINIMAL_ENVIRONMENTALLY_COMPATIBLE_HYDROPHOBIC_SURFACE_ENGINEERING`

Why it advances: porous BC aerogel architectures are the strongest literature-backed route for high oil uptake, compressibility and oil-over-water selectivity. Main risks are process cost, treatment complexity, leachables and ecotoxicity.

**Finalist B — cost-down challenger**  
`D1_LOW_COMPACTION_AIR_DRY`

Why it advances: lowest-energy and simplest manufacturing path. Main risk is pore collapse/native hydrophilicity causing poor oil-over-water selectivity.

These are **pre-registered finalists, not empirical winners**. Feedstock identity (green vs black tea) remains open until matched Stage-0 data exist.

### Winner rule

A branch becomes the marine winner only after passing the frozen gates for:

- oil uptake in artificial seawater;
- oil/water selectivity;
- retention during retrieval;
- ≥99% material retrieval without hazardous fragmentation;
- contained mechanical oil recovery;
- salinity robustness;
- dynamic-water robustness;
- replication across independent BC batches;
- measured cost per kg of recovered oil.

See [`JANUS_SCOBY_MARINE_DYNAMIC_SALTWATER_BOOM_GATE_0018_v1.0.json`](JANUS_SCOBY_MARINE_DYNAMIC_SALTWATER_BOOM_GATE_0018_v1.0.json) and [`JANUS_SCOBY_M1A_FINALISTS_EXTERNAL_VALIDATION_0036_v1.0.json`](JANUS_SCOBY_M1A_FINALISTS_EXTERNAL_VALIDATION_0036_v1.0.json).

## Product architecture under test

The preferred field concept is **not loose SCOBY pieces**. It is a recoverable boom cartridge:

```text
┌──────────────────────────────────────────┐
│ [BC] [BC] [BC] [BC] [BC] [BC] [BC]    │  removable inserts
└──────────────────────────────────────────┘
──────────── retrieval rope / webbing ─────
      outer containment mesh / sleeve
```

Workflow:

```text
DEPLOY
  → SORB
  → RETRIEVE WHOLE
  → CONTAINED DRAIN / PRESS
  → COLLECT OIL + WATER
  → PHASE SEPARATE
  → CHARACTERIZE RECOVERED OIL
  → CONTROLLED SPENT-BC ROUTE
```

## JANUS method

Every major research artifact is expected to carry both semantic directions:

```text
FORWARD
material → process → result

REVERSE
result → required process → required material
```

A reverse pass may expose missing evidence. It may **not** manufacture it.

```text
FORWARD_PASS != PROOF
REVERSE_PASS != PROOF
FORWARD + REVERSE + SAME_EDGES + EMPIRICAL_DATA = PROMOTION CANDIDATE
HASH_IS_INTEGRITY_NOT_TRUTH
```

## Other research tracks

### BioPapyrus / bacterial-cellulose sheets

Experimental recipes and Egyptian lexical/process comparisons explore how BC can be converted into sheet-like material and how ancient process vocabulary overlaps with washing, pressing, drying, writing, cloth, oil and wringing. These are comparative research artifacts, **not claims that ancient Egyptian papyrus was SCOBY**.

Key files include:

- `JANUS_BIOPAPYRUS_RECIPE_v1.0.json`
- `JANUS_BIOPAPYRUS_EGYPTIAN_HIEROGLYPHIC_MAPPING_v1.0.json`
- `JANUS_SCOBY_EGYPTIAN_OIL_WRING_PROCESS_BRIDGE_v1.0.json`
- `JANUS_SCOBY_EGYPTIAN_SINGLE_TEXT_CLOTH_OIL_MOISTEN_GATE_2332_v1.0.json`

### Legacy C₂ evidence program

The original SCOBY-D0 computational evidence line remains preserved under `evidence/`, `src/` and `tests/`. It contains the v0.2–v0.6.6 context/admission lineage and remains claim-bounded. The marine-material program does not overwrite or retroactively reinterpret that evidence authority.

## Repository map

```text
.
├── README.md
├── LICENSE
├── PROJECT_STATUS.json
├── RESEARCH_LINEAGE.json
├── CONTRIBUTING.md
├── CITATION.cff
├── docs/
│   ├── MARINE_M1A_FINALISTS.md
│   ├── ONE_METER_BOOM_COST_MODEL.md
│   └── OUTREACH_EXTERNAL_VALIDATION.md
├── evidence/                 legacy evidence-authority track
├── experiments/              experiment artifacts
├── schemas/                  machine-readable contracts
├── src/                      computational tooling
├── tests/                    reproducibility tests
└── JANUS_*.json              frozen research receipts / gates
```

## Safety and environmental boundary

First-pass material tests use contained systems and safe surrogate oil. Petroleum/crude-oil work belongs only in appropriately controlled facilities with chemical, fire, environmental and waste controls.

Never:

- release experimental sorbent into open water before the field gate;
- microwave oil-loaded material;
- open-burn contaminated sorbent;
- compost petroleum-loaded sorbent;
- abandon fragments in water or drains.

## External validation

The project is now prepared for external discussion around **independent sorbent testing**, especially salinity/current, retrieval, mechanical recovery and cost-per-recovered-oil. A concise outreach packet is in [`docs/OUTREACH_EXTERNAL_VALIDATION.md`](docs/OUTREACH_EXTERNAL_VALIDATION.md).

## Related repositories

- [JANUS Meta Registry](https://github.com/Hawkar-usls/janus-meta-registry)
- [Janus Genesis](https://github.com/Hawkar-usls/Janus_Genesis)
- [ESP32-TWAI-CAN](https://github.com/Hawkar-usls/ESP32-TWAI-CAN)

## License

Code and original repository documentation are released under the **Apache License 2.0** unless a file states otherwise. External papers, datasets, images and upstream material remain under their own licenses and terms.
