# One-meter SCOBY boom — cost and recovery model

This model is intentionally parameterized. Do not insert literature adsorption values as field performance.

## Geometry

Reference architecture:

```text
1.0 m containment sleeve
+ modular BC inserts
+ end closures
+ retrieval rope/webbing
```

The sleeve and rope are accounted separately from dry BC.

## Inputs

```text
m_bc                 dry BC mass per meter [kg]
q_oil                measured oil uptake in dynamic artificial seawater [kg oil / kg dry BC]
f_retention          fraction retained through retrieval/drain [0..1]
f_press              fraction of retained oil recovered by one contained press [0..1]
c_bc                  BC production + drying + treatment cost [currency/kg dry BC]
c_sleeve              mesh/sleeve + closures cost per meter
c_rope                 retrieval webbing/rope cost per meter
c_processing           deployment/retrieval/press consumables per meter
E_bc                   process energy per kg dry BC [kWh/kg]
E_operation            deployment/press energy per meter [kWh]
```

## Core equations

```text
sorbed_oil_kg_per_m = m_bc * q_oil
retained_oil_kg_per_m = sorbed_oil_kg_per_m * f_retention
recovered_oil_kg_per_m = retained_oil_kg_per_m * f_press

material_cost_per_m = m_bc * c_bc + c_sleeve + c_rope
all_in_test_cost_per_m = material_cost_per_m + c_processing

cost_per_kg_recovered_oil = all_in_test_cost_per_m / recovered_oil_kg_per_m
energy_per_m = m_bc * E_bc + E_operation
energy_per_kg_recovered_oil = energy_per_m / recovered_oil_kg_per_m
```

## Required reporting

For every M2 cartridge record:

- dry BC mass per meter;
- sleeve/rope mass and cost;
- saturated lift mass;
- dynamic seawater q_oil;
- retention fraction;
- press recovery fraction;
- recovered oil per meter;
- fragment escape / retrieval fraction;
- cost per meter;
- cost per kg recovered oil;
- energy per kg recovered oil.

## Comparison rule

Always compare against at least one commercially available sorbent architecture measured under the same local procedure when possible.

```text
CHEAPER_PER_KG_RECOVERED_OIL > HIGHER_LAB_G_PER_G
```

only after both options pass the same environmental and retrieval gates.
