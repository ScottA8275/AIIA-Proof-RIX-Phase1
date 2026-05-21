# AIIA-Proof-RIX-Phase1: Recursive Transport Topology

**Admissibility-Constrained Recursive Organization in Biological Systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

Proof RIX Phase 1 investigates whether biological organization emerges from **admissibility-constrained recursive transport topology** rather than unconstrained local similarity.

### Core Thesis
Admissibility constraints induce recursive transport geometry governed by **redundancy**, **rerouting capacity**, **bottleneck concentration**, and **spectral cohesion**. This topology determines transfer compatibility, compression efficiency, perturbation robustness, and measurable phase regions.

### Key Results

- Compatible systems preserve meaningful ortholog transfer at **~2–4 recursive dimensions**.
- Incompatible systems require ~8–16× higher capacity and show fragmentation.
- **Clustering enhancement** reduced maximum edge betweenness by **nearly three orders of magnitude**.
- Dramatic regime separation in perturbation drift: GB1 (~0.0048) vs GFP (~1444.7).
- Transport behavior is **predictable and causally manipulable** from topology structure.

### Repository Structure

proof_rix_phase1_repo/  
├── README.md  
├── LICENSE  
├── requirements.txt  
├── run_all.sh                  # Main reproducibility script  
├── src/rix/                    # Your existing core code (keep as-is)  
│   ├── graph_construction.py  
│   ├── recursive_coarsening.py  
│   ├── transport_metrics.py  
│   ├── curvature.py  
│   └── ... (your current modules)  
│  
├── experiments/                # Configuration-driven runs  
│   ├── configs/                # YAML files for each milestone  
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
