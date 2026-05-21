# AIIA-Proof-RIX-Phase1: Recursive Transport Topology

**Recursive Transport Topology in Biological Systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

**Admissibility-constrained recursive organization induces compact, transferable, and causally manipulable transport geometry.**

### Core Thesis
Biological organization is governed by **admissibility-constrained recursive transport topology** — not merely local feature similarity.

This topology is characterized by four key primitives:
- **Redundancy**
- **Rerouting capacity**
- **Bottleneck concentration**
- **Spectral cohesion**

These primitives determine transfer compatibility, compression efficiency, perturbation robustness, and measurable transport phase regions.

### Key Results

- Compatible systems preserve meaningful ortholog transfer using as few as **~2–4 recursive dimensions**.
- Incompatible systems require substantially higher capacity (~16+ dimensions) and exhibit fragmentation.
- **Clustering enhancement** reduced maximum edge betweenness by **nearly three orders of magnitude**.
- Dramatic separation in perturbation drift: **GB1 (~0.0048)** vs **GFP (~1444.7)**.
- Transport behavior is **predictable from topology** and **causally manipulable** through targeted interventions.

### Repository Contents

- **Milestones 2–10** — Complete experimental progression
- **Core library** (`src/rix/`) — Reusable recursive geometry engine
- **Reproducible scripts** — Configuration-driven milestone runners
- **Data** — Processed GFP and GB1 datasets
- **Results** — All key figures and metric outputs
- **Documentation** — Detailed methodology and metric definitions

### Repository Structure

proof_rix_phase1_repo/  
├── README.md  
├── LICENSE  
├── requirements.txt  
├── run_reproduce.sh  # Main reproducibility script  
├── src/  # Core code   
│   ├── graph_construction.py  
│   ├── recursive_coarsening.py  
│   ├── transport_metrics.py  
│   ├── curvature.py  
│   └── ... (your current modules)  
│  
├── experiments/  # Configuration-driven runs  
│   ├── scripts/  
│   │   ├── run_milestone_02.py  
│   │   ├── run_milestone_03a.py  
│   │   └── ...  
│   └── main.py                 # Entry point  
│  
├── data/  
├── results/  
├── docs/  
└── benchmarks/  

### Quick Start

```bash
git clone https://github.com/ScottA8275/AIIA-Proof-RIX-Phase1.git
cd proof_rix_phase1_repo

pip install -r requirements.txt

# Reproduce key results
bash reproduce.sh  
