"""
Reproduce Figure 2: Recursive Basin Phenotype Preservation.

Expected input:
data/processed/recursive_basin_regime_statistical_lock.csv

Required columns:
gene, rix_value, random_mean
"""
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

INPUT_CSV = "recursive_basin_regime_statistical_lock.csv"


df = numeric(
    require_csv(INPUT_CSV),
    exclude=("gene", "condition", "system", "phase", "intervention", "regime"),
)

required = {"gene", "rix_value", "random_mean"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"{INPUT_CSV} missing columns: {missing}")

plot_df = df.dropna(subset=["gene", "rix_value", "random_mean"]).copy()
if plot_df.empty:
    raise ValueError(
        f"{INPUT_CSV} contains no plottable rows after requiring gene, rix_value, and random_mean"
    )

plot_df = plot_df.sort_values("gene")

plt.figure(figsize=(8, 6))
x = range(len(plot_df))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    plot_df["rix_value"],
    width=width,
    label="RIX",
)
plt.bar(
    [i + width / 2 for i in x],
    plot_df["random_mean"],
    width=width,
    label="Random",
)

plt.xticks(list(x), plot_df["gene"])
plt.ylabel("Mean within-basin phenotype std")
plt.title("Recursive Basin Phenotype Preservation")
plt.legend()

savefig("figure2_phenotype_basin_preservation.png")
