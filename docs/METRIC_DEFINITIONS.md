# METRIC_DEFINITIONS.md

## Proof RIX Phase I — Canonical Metric Definitions

### Recursive Capacity Efficiency (RCE)

Meaningful transport retained per recursive capacity.

```math
RCE = T / C
```

### Transport Robustness Score (TRS)

Stability of transport organization under perturbation.

```math
TRS = 1 - D_p
```

### Bottleneck Dominance (BD)

Degree to which transport depends on concentrated pathways.

```math
BD = max(B_e)
```

### Phase Stability Index (PSI)

Distance from fragmentation-sensitive phase boundaries.

```math
PSI = S - F
```

### Recursive Transfer Capacity Threshold (RTCT)

Minimum recursive representational capacity required to achieve a specified transfer threshold.

Common thresholds:

| Threshold | Interpretation |
|---|---|
| ρ ≥ 0.05 | weak transfer |
| ρ ≥ 0.10 | meaningful transfer |
| ρ ≥ 0.15 | strong transfer |
