"""
Reproduce Figures 8 and 9:
- Recursive Transport Phase Map
- Spectral Gap Phase Separation
- Optional redundancy threshold behavior

Expected inputs:
data/processed/topology_phase_grid.csv
data/processed/stability_transition_summary.csv
data/processed/fragmentation_transition_curves.csv
"""
import numpy as np
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

grid = numeric(require_csv("topology_phase_grid.csv"), exclude=("phase",))
stability = numeric(require_csv("stability_transition_summary.csv"), exclude=("phase",))
curves = numeric(require_csv("fragmentation_transition_curves.csv"), exclude=("phase",))

required_grid = {"redundancy", "bottleneck_pressure", "mean_phase_code"}
if not required_grid.issubset(grid.columns):
    raise ValueError(f"topology_phase_grid.csv missing columns: {required_grid - set(grid.columns)}")

heat = grid.pivot_table(index="bottleneck_pressure", columns="redundancy", values="mean_phase_code", aggfunc="mean").sort_index()

plt.figure(figsize=(8.5, 5.4))
im = plt.imshow(heat.values, aspect="auto", origin="lower")
plt.title("Recursive Transport Phase Map")
plt.xlabel("Redundancy")
plt.ylabel("Bottleneck pressure")
plt.xticks(np.arange(len(heat.columns)), [str(int(c)) for c in heat.columns])
plt.yticks(np.arange(len(heat.index)), [str(c) for c in heat.index])
cbar = plt.colorbar(im)
cbar.set_label("Mean phase code: 0=frag, 1=trans, 2=robust")
savefig("figure10_recursive_transport_phase_map.png")

if {"phase", "mean_spectral_gap"}.issubset(stability.columns):
    order = ["fragmentation_sensitive", "transitional", "robust"]
    stability["phase"] = stability["phase"].astype(str)
    available = [p for p in order if p in set(stability["phase"])]
    stability = stability.set_index("phase").reindex(available).reset_index()
    plt.figure(figsize=(8, 5.2))
    plt.bar(stability["phase"], stability["mean_spectral_gap"])
    plt.xticks(rotation=15, ha="right")
    plt.ylabel("Mean spectral gap")
    plt.title("Spectral Cohesion Separates Transport Phases")
    plt.grid(True, axis="y", alpha=0.3)
    savefig("figure9_spectral_gap_phase_separation.png")

if {"redundancy", "fragmentation_rate", "robust_rate"}.issubset(curves.columns):
    summary = curves.groupby("redundancy", as_index=False).agg(
        mean_fragmentation_rate=("fragmentation_rate", "mean"),
        mean_robust_rate=("robust_rate", "mean"),
    )
    plt.figure(figsize=(8.5, 5.4))
    plt.plot(summary["redundancy"], summary["mean_fragmentation_rate"], marker="o", label="Fragmentation rate")
    plt.plot(summary["redundancy"], summary["mean_robust_rate"], marker="s", label="Robust rate")
    plt.xlabel("Redundancy")
    plt.ylabel("Mean phase fraction")
    plt.ylim(-0.05, 1.05)
    plt.title("Redundancy Threshold Behavior")
    plt.grid(True, alpha=0.3)
    plt.legend()
    savefig("support_redundancy_threshold_behavior.png")
