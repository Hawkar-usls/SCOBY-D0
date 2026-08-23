# Extremophile Reentry → Bacterial-Cellulose Matrix Protocol

## Status

**Preregistered mechanistic research track. No Pv11/SCOBY matrix effect has been demonstrated yet.**

Primary machine-readable gate: `JANUS_SCOBY_EXTREMOPHILE_REENTRY_MATRIX_GATE_0018_v1.0.json`  
Condition table: `experiments/POLYPEDILUM_SCOBY_REENTRY_MATRIX_DESIGN_v1.0.csv`

## Core question

Can a biological system that has already resumed function, but has not yet resumed significant population growth, alter the formation of bacterial cellulose?

The target distinction is:

```text
CELL STATE != CELL NUMBER
```

For the Polypedilum/Pv11 anchor, public data support the following temporal separation after rehydration:

```text
~1 h       partial cellular / membrane-associated function detectable
~3 h       RAD16-like recovery-associated transcriptional state
12–24 h    de-novo-protein-dependent functional recovery; repair program continues
0–48 h     live-cell abundance does not significantly increase from the early baseline
~72 h      significant proliferation begins
72–96 h    classical whole-larva work places restoration of nuclear-DNA integrity in this range
```

This creates an unusually useful `R1–R3` window in which recovery-state effects can be sought before population expansion becomes the dominant explanation.

## Reentry abstraction

```text
R0  dormant / desiccated
 ↓
R1  basic function restart
 ↓
R2  repair + reconstruction
 ↓
R3  verified survivor / non-proliferative window
 ↓
R4  proliferation permitted
```

The SCOBY-D0 hypothesis is not that Polypedilum is a natural kombucha symbiont. It is that a transient physiological state in a second biological system may alter the microenvironment experienced by a bacterial-cellulose producer.

```text
REENTRY STATE
    ↓
CONTACT OR SOLUBLE SIGNAL
    ↓
LOCAL pH / O2 / REDOX / HYDRATION / INTERFACE
    ↓
KOMAGATAEIBACTER CELLULOSE DEPOSITION
    ↓
BC MATERIAL PHENOTYPE
```

## Phase A — state screen

Compare matched exposure conditions at the selected rehydration states:

- baseline BC control;
- R1 / ~1 h;
- R2 / ~3 h;
- R2 / ~24 h;
- R3 / ~48 h;
- R4 / ~72 h proliferative comparator.

Primary BC readouts:

- dry cellulose mass;
- pellicle thickness and formation rate;
- water retention;
- porosity or a validated pore-size proxy;
- fibril/bundle morphology where imaging is available;
- mechanical properties where sample quantity permits;
- pH and oxygen state;
- producer viability.

The primary interpretation is based on differences that occur in `R1–R3`, before significant Pv11 population growth is observed in the cited system.

## Phase B — contact versus soluble mechanism

For selected recovery states, compare:

```text
WASHED WHOLE CELLS
        vs
CELL-FREE RECOVERY FRACTION
        vs
MATCHED NONACTIVE CELL CONTROL
```

Interpretation:

- **whole cells only** → contact, adhesion, physical nucleation, cell-surface or local-oxygen mechanism favored;
- **cell-free fraction reproduces the effect** → soluble matrix-modifying chemistry favored;
- **both lose the effect after pH/O2/carryover matching** → classify as microenvironment-mediated rather than a recovery-factor-specific effect;
- **neither reproduces** → no detectable coupling under the tested conditions.

## Critical trehalose boundary

Pv11 anhydrobiosis induction uses high trehalose exposure. Therefore trehalose is both a biologically meaningful survival molecule and a major experimental confound for bacterial-cellulose work.

No Pv11-specific matrix claim is admissible unless the experiment includes:

- quantitatively matched trehalose control;
- matched culture-medium carryover control;
- washing or another validated carryover-removal step for whole-cell conditions;
- pH and oxygen monitoring;
- viable-biomass accounting.

If the trehalose control reproduces the apparent Pv11 phenotype, the Pv11-specific interpretation fails.

## Phase C — transient-state material memory

Only after an early-state matrix effect is reproducible should the project test whether a brief recovery-state exposure leaves a persistent spatial signature in subsequently produced cellulose.

Conceptual design:

```text
baseline BC growth
      ↓
short R1/R2/R3 exposure window
      ↓
return to matched baseline
      ↓
continue cellulose formation
      ↓
map material properties across the growth/time axis
```

A successful result requires a spatially localized material difference that persists after the transient exposure is removed and cannot be explained by bulk pH, oxygen, trehalose, biomass or handling.

Until that gate closes, the phrase **SCOBY biological-state memory** remains a hypothesis only.

## Promotion ladder

```text
P0  kinetic anchor only                      ← CURRENT
P1  early matrix effect reproduced
P2  contact vs soluble mechanism separated
P3  defined factor or defined microenvironment causally reproduces effect
P4  transient state leaves persistent spatial matrix record
```

## Kill rules

1. If matrix changes appear only after the R4/proliferative window, reject a non-proliferative recovery-state mechanism for that effect.
2. If trehalose-matched or medium-matched controls reproduce the effect, reject a Pv11-specific interpretation.
3. If the effect scales only with viable-cell number, classify it as a population-size effect rather than a state effect.
4. If independent BC batches do not reproduce the direction of effect, keep the gate closed.
5. If pH/O2 matching removes the effect, classify it as microenvironment-mediated rather than a defined recovery-factor effect.

## Candidate modifier families

These are mechanistic candidates, not established BC modifiers:

- trehalose / compatible solutes;
- LEA proteins;
- thioredoxin/redox systems;
- PIMT and protein-repair-associated factors;
- membrane and cell-surface state;
- any recovery-state extracellular fraction that survives the mandatory controls.

The project should prioritize **defined-factor reconstruction** only after the cell-free gate identifies a reproducible soluble effect.

## Public evidence anchors

- Gusev et al., PLOS ONE (2010), DOI `10.1371/journal.pone.0014008` — whole-larva physiological recovery precedes restoration of nuclear-DNA integrity.
- Yamada et al., Scientific Reports (2018), DOI `10.1038/s41598-018-36124-6` — Pv11 recovery-associated DNA-repair transcription, including RAD16-like R3 signal and NER-associated recovery.
- Scientific Reports (2025), DOI `10.1038/s41598-025-19627-x` — early membrane/protein function recovery with live-cell abundance stable through 48 h and significant growth beginning around 72 h.
- Advanced Materials (2026), DOI `10.1002/adma.202514125` — independent support for the broader principle that a second living organism can be entrapped by BC and alter spatial cellulose growth through its physiology; this is not evidence for a Polypedilum-specific effect.

## JANUS boundary

```text
KINETIC SEPARATION != CAUSAL CHECKPOINT
SECOND-ORGANISM BC EFFECT != POLYPEDILUM BC EFFECT
TREHALOSE CARRYOVER != RECOVERY SIGNAL
MATRIX CHANGE != MATERIAL MEMORY
FORWARD PASS != PROOF
REVERSE PASS != PROOF
```

The next admissible promotion is `P0 → P1`: a reproducible, controlled early-window BC phenotype before the proliferative confound begins.
