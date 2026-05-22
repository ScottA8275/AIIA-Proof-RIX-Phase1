# AIIA-Proof-RIX-Phase1: Recursive Transport Topology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

## Admissibility-constrained recursive organization induces compact, transferable, and causally manipulable transport geometry.

---

# Overview

The Proof RIX Phase I program demonstrates that biological organization is governed by **admissibility-constrained recursive transport topology** rather than unconstrained feature similarity.

Across Milestones 2–10:

* compatible systems preserve meaningful transfer using as few as **~2–4 recursive dimensions**,
* incompatible systems require substantially higher recursive capacity and exhibit fragmentation under perturbation,
* and topology manipulation causally changes transport behavior.

The framework establishes a reproducible transport-topology theory based on four key primitives:

* **Redundancy**
* **Rerouting capacity**
* **Bottleneck concentration**
* **Spectral cohesion**

Together, these primitives govern:

* recursive compression efficiency,
* transfer compatibility,
* perturbation robustness,
* fragmentation behavior,
* and recursive transport phase regions.

---

# Core Scientific Claims

## Recursive Compression

Compatible systems preserve meaningful transport organization under extremely low recursive representational capacity.

Key result:

* meaningful ortholog transfer retained at approximately **2–4 recursive dimensions**.

---

## Fragmentation Boundaries

Recursive perturbation induces measurable transport fragmentation regions.

Systems separate into:

* coherent,
* transitional,
* rerouting,
* and fragmented

recursive transport regimes.

---

## Comparative Transport Regimes

GB1 and GFP occupy fundamentally different recursive transport-topology regimes:

| System | Dominant Regime                       |
| ------ | ------------------------------------- |
| GFP    | sparse / bottleneck-sensitive         |
| GB1    | dense / redundant / rerouting-capable |

---

## Predictive Topology

Transport robustness and fragmentation behavior are predictable from topology structure.

Topology metrics:

* redundancy,
* bottleneck dominance,
* and spectral cohesion

predict recursive transport stability.

---

## Causal Intervention

Synthetic topology interventions causally alter recursive transport behavior.

Most notably:

* clustering enhancement reduced maximum edge betweenness by nearly **three orders of magnitude**.

---

# Canonical Metrics

The public reproducibility layer centers on five canonical metrics:

| Metric                                       | Purpose                                            |
| -------------------------------------------- | -------------------------------------------------- |
| Recursive Capacity Efficiency (RCE)          | transfer retained per recursive capacity           |
| Transport Robustness Score (TRS)             | perturbation stability                             |
| Bottleneck Dominance (BD)                    | transport concentration stress                     |
| Phase Stability Index (PSI)                  | distance from fragmentation boundaries             |
| Recursive Transfer Capacity Threshold (RTCT) | minimum recursive capacity for meaningful transfer |

Detailed definitions are provided in:

```text
docs/METRIC_DEFINITIONS.md
```

---

# Canonical Phase I Figures

| Figure                                    | Claim                                                                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Figure 2 — RTCT Capacity Curves           | Compatible systems preserve transfer under low recursive capacity                                                      |
| Figure 3 — Fragmentation Boundary Regions | Recursive transport systems separate into coherent, transitional, rerouting, and fragmented regions under perturbation |
| Figure 4 — Comparative Transport Regimes  | GB1 and GFP occupy distinct recursive transport regimes                                                                |
| Figure 5 — GB1 Robustness Profile         | Dense redundant topology stabilizes perturbation transport                                                             |
| Figure 6 — Predictive Phase Diagram       | Topology metrics predict transport phase behavior                                                                      |
| Figure 7 — Clustering Intervention        | Synthetic clustering enhancement causally reduces bottleneck dominance                                                 |
| Figure 8 — Recursive Transport Phase Map  | Recursive transport behavior organizes into measurable phase regions                                                   |
| Figure 9 — Spectral Gap Phase Separation  | Spectral cohesion quantitatively separates transport regimes                                                           |

Supporting figures are also included for:

* GB1 recursive compression,
* phenotype locality,
* and additional perturbation diagnostics.

---

# Repository Structure

```text
proof_rix_phase1_repro/
│
├── README.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── Dockerfile
├── CITATION.cff
│
├── data/
│   └── processed/
│
├── scripts/
│   ├── run_all_reproductions.py
│   ├── reproduce_recursive_capacity.py
│   ├── reproduce_fragmentation_boundaries.py
│   ├── reproduce_gb1_recursive_compression.py
│   ├── reproduce_gb1_perturbation.py
│   ├── reproduce_comparative_transport_regimes.py
│   ├── reproduce_predictive_topology.py
│   ├── reproduce_causal_interventions.py
│   └── reproduce_phase_boundary_map.py
│
├── figures/
│   └── phase1/
│
├── outputs/
│
├── configs/
│
└── docs/
    └── METRIC_DEFINITIONS.md
```

---

# Quick Start

## Clone Repository

```bash
git clone https://github.com/ScottA8275/AIIA-Proof-RIX-Phase1.git
cd proof_rix_phase1_repro
```

---

## Install Requirements

### pip

```bash
pip install -r requirements.txt
```

### conda

```bash
conda env create -f environment.yml
conda activate proof_rix_phase1
```

---

# Reproduce Canonical Phase I Figures

Run the complete deterministic reproduction pipeline:

```bash
python scripts/run_all_reproductions.py
```

Generated figures will be written to:

```text
figures/phase1/
```

---

# Expected Processed Inputs

Place canonical processed CSVs in:

```text
data/processed/
```

Canonical required inputs are listed in:

```text
configs/input_manifest.yaml
```

---

# Reproducibility Philosophy

This repository is designed to reproduce the locked scientific claims of Proof RIX Phase I rather than the complete internal research history.

The package emphasizes:

* deterministic figure regeneration,
* canonical metrics,
* interpretable transport-topology analysis,
* and recursive phase-boundary reproducibility.

The repository intentionally exposes:

* frozen processed datasets,
* canonical figure-generation scripts,
* public metric definitions,
* and deterministic transport-topology workflows.

The repository intentionally does not expose:

* exploratory internal variants,
* abandoned geometry heuristics,
* unfinished recursive operators,
* or full internal research infrastructure.

This distinction preserves both:

* scientific reproducibility,
* and conceptual clarity.

---

# Reproducibility Status

## Proof RIX Phase I

### Reproducibility Layer: LOCKED (Version 1.0)

This repository represents the canonical public reproducibility layer for:

* Milestones 7–10,
* recursive transport topology,
* and recursive phase-boundary analysis.

---

# Citation

If you use this repository or reproducibility package, please cite:

```text
Proof RIX Phase I Reproducibility Package
AIIA Technologies
Version 1.0
```

Detailed citation metadata is provided in:

```text
CITATION.cff
```

---

# License

This project is released under the MIT License.

See:

```text
LICENSE
```
