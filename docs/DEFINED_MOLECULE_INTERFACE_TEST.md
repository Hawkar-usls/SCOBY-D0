# Defined molecule → interface → bacterial cellulose test

## Purpose

This experiment asks a narrow causal question:

```text
RECOVERY STATE
    ↓
DEFINED MOLECULE (PvLEA4)
    ↓
DEFINED PHYSICAL PROPERTY
    ↓
AIR–LIQUID INTERFACE / OXYGEN OR DIRECT MATRIX INTERACTION
    ↓
CELLULOSE PHENOTYPE
    ↓
FALSIFIER
```

The experiment does **not** test whether *Polypedilum vanderplanki* can live in SCOBY and does not claim that PvLEA4 modifies bacterial cellulose.

## Why the interface is now a first-class variable

Three independent literature observations create a testable bridge without proving it:

1. PvLEA4 is a highly hydrophilic molecular-shield protein with dose-dependent anti-aggregation behavior under water stress.
2. LEA proteins from other systems can preferentially adsorb to air–water interfaces.
3. Static Komagataeibacter cellulose production is concentrated at the air–liquid interface and is sensitive to oxygen supply and surface tension.

Therefore a PvLEA4-associated BC phenotype could arise through at least two very different mechanisms:

```text
A) PvLEA4 → interface change → O2 geometry → BC
B) PvLEA4 → direct surface/fibril interaction → BC
```

These mechanisms must not be collapsed.

## Frozen condition map

The machine-readable matrix is in:

`experiments/PVLEA4_TREHALOSE_BC_DEFINED_FACTOR_MATRIX_v1.0.csv`

The required arms are:

- BC baseline;
- vehicle/buffer match;
- trehalose-matched control;
- generic soluble-protein control;
- PvLEA4 LOW/MID/HIGH frozen dose tiers;
- PvLEA4 + trehalose interaction arm;
- a validated non-nutritional surface-tension reference condition.

LOW/MID/HIGH are relative preregistered tiers. Exact concentrations must be fixed before BC outcomes are inspected. Outcome-driven dose tuning is forbidden.

## Measurement order

The order matters because temporal precedence is part of the causal test.

### Layer 0 — input state

Record defined factor identity, protein exposure, trehalose, vehicle, pH and osmolarity/proxy.

### Layer 1 — interface state

Measure surface tension and an oxygen readout/proxy before substantial pellicle formation. Interfacial rheology is desirable when available.

### Layer 2 — production

Primary endpoint: dry BC mass under a frozen harvest rule.

Secondary production readouts: formation rate and pellicle thickness.

### Layer 3 — structure

Water-holding capacity, porosity/pore proxy, fibril or bundle morphology, and crystallinity where available.

### Layer 4 — mechanics

Tensile/compression measurements only when enough material exists; lack of mechanics data does not invalidate Layers 1–3.

## Mechanistic classification

### Result A — PvLEA4-specific candidate

```text
PvLEA4 ≠ baseline
PvLEA4 ≠ vehicle
PvLEA4 ≠ trehalose
PvLEA4 ≠ generic protein
```

and the direction reproduces across independent BC batches.

This permits a defined-factor candidate claim, not yet direct binding.

### Result B — interface-mediated

```text
PvLEA4 changes surface tension / interface state first
        ↓
BC phenotype follows
        ↓
independent surface-tension reference phenocopies direction
```

Classification:

`DEFINED_MICROENVIRONMENT_CAUSAL_CANDIDATE`

Do **not** call this direct LEA–cellulose binding.

### Result C — possible direct/non-interface mechanism

PvLEA4 changes BC after pH, osmolarity, trehalose, oxygen, surface tension and generic-protein effects are matched or separated.

Next test would then require a direct cellulose/protein or producer-surface interaction assay.

### Result D — trehalose explains it

If trehalose alone reproduces the phenotype, reject PvLEA4-specific interpretation.

### Result E — generic protein explains it

If the generic soluble protein reproduces the phenotype, classify the effect as generic protein/interface behavior rather than LEA-specific.

### Result F — no reproducible effect

If independent BC batches do not reproduce the direction, keep the gate closed.

## Promotion boundary

```text
P0  preregistered defined-factor test
P1  reproducible controlled BC phenotype
P2  interface vs non-interface mechanism discriminated
P3  defined factor or defined microenvironment causally reproduces effect
P4  transient exposure leaves a persistent spatial material record
```

This artifact starts and remains at **P0** until real data exist.

## Core falsification rule

The strongest negative result is useful:

> If PvLEA4 has no residual BC effect after trehalose, generic protein, pH, osmolarity, oxygen and interface matching, reject the proposed defined PvLEA4 matrix-modifier mechanism under the tested conditions.

## Safety boundary

Contained non-pathogenic bacterial-cellulose/material research only. No environmental release or field deployment is authorized by this protocol.
