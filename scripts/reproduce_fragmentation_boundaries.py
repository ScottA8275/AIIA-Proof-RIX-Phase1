"""
Reproduce Figure 3: Recursive Transport Fragmentation Boundaries and Phase Regions.

Expected input:
data/processed/fragmentation_phase_regions.csv

Required columns:
perturbation, capacity, phase

Allowed phases:
fragmented, transitional, rerouting, coherent

Optional:
spearman, reaches_rho_0.10
"""

import numpy as np
import matplotlib.pyplot as plt
from _utils import require_csv, savefig


df = require_csv("fragmentation_phase_regions.csv")
### perturbation_phase_transition_table.csv

required = {"perturbation", "capacity", "phase"}
missing = required - set(df.columns)

if missing:
    raise ValueError(
        f"fragmentation_phase_regions.csv missing columns: {missing}"
    )


# ---------------------------------------------------------
# Canonical phase ordering
# ---------------------------------------------------------
# 0 = fragmented
# 1 = transitional
# 2 = rerouting
# 3 = coherent

phase_map = {
    "fragmented": 0,
    "transitional": 1,
    "rerouting": 2,
    "coherent": 3,
}

df["phase_code"] = (
    df["phase"]
    .astype(str)
    .str.lower()
    .map(phase_map)
)

if df["phase_code"].isna().any():
    raise ValueError(
        "Unknown phases found: "
        f"{df.loc[df['phase_code'].isna(), 'phase'].unique()}"
    )


# ---------------------------------------------------------
# Build phase grid
# ---------------------------------------------------------

grid = (
    df.pivot_table(
        index="perturbation",
        columns="capacity",
        values="phase_code",
        aggfunc="mean",
    )
    .sort_index()
)

capacities = list(grid.columns)
perturbations = list(grid.index)


# ---------------------------------------------------------
# Optional RTCT overlay
# ---------------------------------------------------------

rtct_capacity = None

if "reaches_rho_0.10" in df.columns:
    rtct_hits = df[df["reaches_rho_0.10"].astype(bool)]

    if len(rtct_hits):
        rtct_capacity = float(
            rtct_hits["capacity"].min()
        )

elif "spearman" in df.columns:
    rtct_hits = df[df["spearman"] >= 0.10]

    if len(rtct_hits):
        rtct_capacity = float(
            rtct_hits["capacity"].min()
        )


# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(
    grid.values,
    aspect="auto",
    origin="lower",
)

ax.set_title(
    "Recursive Transport Fragmentation Boundaries and Phase Regions"
)

ax.set_xlabel(
    "Total Recursive Capacity"
)

ax.set_ylabel(
    "Perturbation"
)

ax.set_xticks(
    np.arange(len(capacities))
)

ax.set_xticklabels(
    [str(int(c)) if float(c).is_integer() else str(c) for c in capacities]
)

ax.set_yticks(
    np.arange(len(perturbations))
)

ax.set_yticklabels(
    [str(p) for p in perturbations]
)


# ---------------------------------------------------------
# Add light gridlines between cells
# ---------------------------------------------------------

ax.set_xticks(
    np.arange(-0.5, len(capacities), 1),
    minor=True,
)

ax.set_yticks(
    np.arange(-0.5, len(perturbations), 1),
    minor=True,
)

ax.grid(
    which="minor",
    color="white",
    linestyle="-",
    linewidth=0.6,
    alpha=0.35,
)

ax.tick_params(
    which="minor",
    bottom=False,
    left=False,
)


# ---------------------------------------------------------
# RTCT overlay if available
# ---------------------------------------------------------

if rtct_capacity is not None and rtct_capacity in capacities:
    rtct_idx = capacities.index(rtct_capacity)

    ax.axvline(
        rtct_idx,
        color="white",
        linestyle="--",
        linewidth=2,
        alpha=0.9,
    )

    ax.text(
        rtct_idx + 0.1,
        len(perturbations) - 0.6,
        "RTCT\nρ ≥ 0.10",
        color="white",
        fontsize=9,
        va="top",
        ha="left",
        bbox=dict(
            facecolor="black",
            alpha=0.35,
            edgecolor="none",
            boxstyle="round,pad=0.25",
        ),
    )


# ---------------------------------------------------------
# Colorbar
# ---------------------------------------------------------

cbar = fig.colorbar(
    im,
    ax=ax,
)

cbar.set_label(
    "Phase code: 0=fragmented, 1=transitional, 2=rerouting, 3=coherent"
)

cbar.set_ticks(
    [0, 1, 2, 3]
)

cbar.set_ticklabels(
    [
        "Fragmented",
        "Transitional",
        "Rerouting",
        "Coherent",
    ]
)


savefig(
    "figure3_fragmentation_boundary_regions.png"
)