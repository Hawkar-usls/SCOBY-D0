# O₂ × N₂ dual-axis gate

Status: **P0 / preregistered / no empirical SCOBY-D0 result yet**.

## Why this gate exists

The current cross-domain mediator program treats oxygen transfer as part of the interface state. A new confound appears when gas composition is changed: an apparent `O₂ + N₂` effect can actually arise from oxygen partial pressure, dissolved-oxygen transfer, carbon-dioxide accumulation/stripping, total-pressure or bubble-transfer effects. At the same time, `nitrogen` in the growth medium is a separate metabolic variable.

Therefore:

```text
N₂(gas) != assimilable nitrogen
```

and the tested state must be decomposed as:

```text
GAS PHYSICS
  pO₂ / dissolved O₂ / transfer
  N₂ gas fraction
  pCO₂ / CO₂ accumulation
  pressure / transfer context

⊕

NUTRIENT NITROGEN
  assimilable-N amount
  N-source identity
  C:N ratio
  buffering / ionic effects
```

## Evidence anchors

- Komagataeibacter/Acetobacter cellulose synthesis is strongly oxygen-sensitive, and controlled oxygen states alter yield and material properties.
- High pCO₂ can reduce BC production, so CO₂ cannot silently co-vary with O₂:N₂ composition.
- Nitrogen-source identity can strongly change BC output independently of carbon-source identity.
- A 2026 K. xylinus study confirms that nitrogen-normalized medium composition changes BC yield and structure.
- A single K. hansenii JR-02 report described BC in nitrogen-free medium and a possible `nifH` sequence. This is **not** genus-wide proof of nitrogen fixation and must remain strain-specific.

## Core questions

1. Does BC follow dissolved-O₂ / transfer state when nutrient-N and CO₂ are bounded?
2. Does changing N₂ gas fraction add predictive power after pO₂, dissolved O₂, pCO₂, transfer and nutrient-N are matched?
3. Does assimilable-N source or C:N change BC independently of gas state?
4. If a residual N₂ effect survives, does the tested strain actually have independently verified N₂-fixation capability?

## Interpretation ladder

```text
O₂/DO changes + BC follows
  -> O₂-transfer mediator candidate

nutrient-N changes + BC follows under matched gas state
  -> separate metabolic nitrogen axis

N₂-associated effect disappears after pO₂/DO/pCO₂ matching
  -> reject N₂-gas-specific mechanism

N₂ residual survives all gas + nutrient controls
  -> open strain-specific N₂ mechanism gate

N₂ fixation directly verified + isotopic/biochemical nitrogen incorporation linked to phenotype
  -> N₂ metabolic-input candidate for that strain only
```

## Integration with causal rescue

The existing causal-mediator rescue should not use a scalar mediator. Its gas-sensitive subvector becomes:

```text
M_gas = [
  pO₂,
  dissolved-O₂ / transfer proxy,
  N₂ gas fraction,
  pCO₂ / CO₂ proxy,
  transfer / pressure context
]
```

while nutrient nitrogen remains separate:

```text
M_N = [
  assimilable-N,
  N-source identity,
  C:N
]
```

A rescue claim is invalid if the intervention restores BC by changing nutrient-N while being interpreted as a gas-mediated rescue, or vice versa.

## TOPA kill rules

- `N₂ fraction change != N₂-specific effect` if O₂ or CO₂ also changed.
- `nitrogen source effect != N₂ gas effect`.
- `possible nifH != verified nitrogen fixation`.
- `nanobubble effect != gas chemistry effect` unless bubble/transfer physics are independently bounded.
- one strain/culture geometry cannot establish a universal O₂+N₂ law.

## Safety

This is a non-operational design record. Any compressed-gas, pressure-vessel, sterile-culture or instrument work requires appropriate laboratory procedures, trained personnel and equipment.
