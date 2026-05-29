"""
Reproduce Figure 6: Predictive Recursive Transport Phase Diagram.

Expected input:
data/processed/phase_boundary_predictions.csv

Required columns:
system, robustness_score, fragmentation_risk, predicted_phase_region
"""
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

df = numeric(require_csv("phase_boundary_predictions.csv"), exclude=("system", "predicted_phase_region", "interpretation"))
required = {"system", "robustness_score", "fragmentation_risk", "predicted_phase_region"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"phase_boundary_predictions.csv missing columns: {missing}")

colors = {"robust": "tab:green", "fragmentation_sensitive": "tab:red", "transitional": "tab:orange"}

plt.figure(figsize=(8, 6))
for _, row in df.iterrows():
    plt.scatter(row["robustness_score"], row["fragmentation_risk"], s=250, color=colors.get(row["predicted_phase_region"], "tab:gray"), alpha=0.8)
    plt.text(row["robustness_score"] + 0.02, row["fragmentation_risk"] + 0.02, row["system"], fontsize=10)

plt.axvline(0.5, linestyle="--", alpha=0.4)
plt.axhline(0.5, linestyle="--", alpha=0.4)
plt.xlabel("Robustness score")
plt.ylabel("Fragmentation risk")
plt.title("Predictive Recursive Transport Phase Diagram")
plt.grid(True, alpha=0.3)
savefig("support_predictive_phase_diagram.png")
