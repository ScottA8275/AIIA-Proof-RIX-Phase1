"""
Reproduce Figure 5: GB1 robustness profile.

Expected input:
data/processed/gb1_perturbation_summary.csv

Required columns:
perturbation, mean_phenotype_drift, curvature_variance, largest_component_fraction
"""
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

df = numeric(require_csv("gb1_perturbation_summary.csv"))
required = {"perturbation", "mean_phenotype_drift", "curvature_variance", "largest_component_fraction"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"gb1_perturbation_summary.csv missing columns: {missing}")

df = df.sort_values("perturbation")

fig, ax1 = plt.subplots(figsize=(9, 5.4))
ax1.plot(df["perturbation"], df["mean_phenotype_drift"], marker="o", label="Phenotype drift")
ax1.set_xlabel("Recursive constraint perturbation")
ax1.set_ylabel("Mean phenotype drift")
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()
ax2.plot(df["perturbation"], df["curvature_variance"], marker="s", linestyle="--", label="Curvature variance")
ax2.set_ylabel("Curvature variance")
plt.title("GB1 Robustness Profile")
savefig("figure6_gb1_robustness_profile.png")
