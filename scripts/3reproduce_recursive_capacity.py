"""
Reproduce Figure 2: Recursive Transfer Capacity Threshold Curves.

Expected input:
data/processed/recursive_capacity_sweep.csv

Required columns:
regime, total_recursive_dims, transfer_rho
"""
import pandas as pd
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig, OUTPUTS

df = numeric(require_csv("recursive_capacity_sweep.csv"), exclude=("regime",))
### milestone7b_plotting_table_with_normalized_stability.csv
required = {"regime", "total_recursive_dims", "transfer_rho"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"recursive_capacity_sweep.csv missing columns: {missing}")

summary = (
    df.groupby(["regime", "total_recursive_dims"], as_index=False)
    .agg(mean_transfer=("transfer_rho", "mean"))
)

plt.figure(figsize=(8.5, 5.2))
for regime, sub in summary.groupby("regime"):
    sub = sub.sort_values("total_recursive_dims")
    plt.plot(sub["total_recursive_dims"], sub["mean_transfer"], marker="o", label=str(regime))

plt.axhline(0.10, linestyle="--", alpha=0.5, label="ρ=0.10")
plt.title("Recursive Transfer Capacity Threshold Curves")
plt.xlabel("Total recursive representational capacity")
plt.ylabel("Transfer performance (Spearman ρ)")
plt.grid(True, alpha=0.3)
plt.legend()
savefig("figure3_rtct_capacity_curves.png")

rows = []
for regime, sub in summary.groupby("regime"):
    hit = sub[sub["mean_transfer"] >= 0.10].sort_values("total_recursive_dims")
    rtct = float(hit["total_recursive_dims"].iloc[0]) if len(hit) else float("nan")
    rows.append({"regime": regime, "RTCT_rho_ge_0_10": rtct})
pd.DataFrame(rows).to_csv(OUTPUTS / "rtct_summary.csv", index=False)
