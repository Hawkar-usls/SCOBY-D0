# Causal mediator rescue test

## Question
Can the measured interface/O2 mediator be restored toward baseline while a source factor remains present, and does the bacterial-cellulose phenotype follow that rescue?

This gate follows the source-invariant response-surface work. It is not allowed to run by outcome-driven tuning.

## Logic

```text
SOURCE FACTOR
   ↓
MEDIATOR SHIFT
   ↓
BC SHIFT

SOURCE FACTOR + ORTHOGONAL COMPENSATOR
   ↓
MEDIATOR RESTORED TOWARD BASELINE
   ↓
DOES BC ALSO RETURN?
```

A second route tests sufficiency:

```text
NO SOURCE FACTOR
   +
ORTHOGONAL MEDIATOR REFERENCE
   ↓
SAME MEDIATOR SHIFT?
   ↓
SAME BC DIRECTION?
```

## Stage A — source calibration
Confirm that the chosen source factor reproducibly changes the mediator vector before substantial pellicle formation. No rescue agent is selected from BC outcomes.

## Stage B — compensator calibration
Select a compensator using abiotic mediator measurements only. It must restore the mediator vector toward baseline while leaving the source factor present and without materially shifting pH/osmolality outside frozen tolerances. It must not be chosen because it produces a preferred BC result.

## Stage C — locked BC challenge
Run the frozen matrix in `experiments/CAUSAL_MEDIATOR_RESCUE_MATRIX_v1.0.csv`.

Primary endpoint: `dry_BC_mass` under one frozen harvest rule.

Mechanism endpoints are recorded early: surface/interfacial tension, dissolved oxygen or transfer proxy, pH, and osmolality/water-activity proxy.

## Rescue interpretation

A rescue claim requires both:
1. the mediator vector returns within a preregistered rescue tolerance; and
2. the BC endpoint returns within a preregistered equivalence bound.

`p > 0.05` is not equivalence.

## Bidirectional criterion
The strongest result in this gate requires both rescue and orthogonal reproduction. A source-free orthogonal route must reproduce the mediator shift and BC direction, and a counter-rescue must reverse both.

## Kill rules
- compensator alone materially changes BC;
- compensator removes, binds, degrades, or otherwise changes source-factor availability;
- BC rescues without mediator rescue;
- mediator rescues without BC rescue;
- source-aware held-out prediction materially outperforms the source-blind mediator model.

Any of these blocks strong mediation language.

## Evidence ceiling
A complete pass can support only:

`STRONG_CAUSAL_MEDIATOR_CANDIDATE_WITHIN_TESTED_DOMAIN`

It does not establish a universal biological law, human-milk/placental causality, or material memory.
