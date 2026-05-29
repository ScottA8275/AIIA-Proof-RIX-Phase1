"""
Reproduce Figure 4: Comparative Transport Regimes.

Expected input:
data/processed/comparative_transport_summary.csv

Required columns:
system, fragmentation_observed
"""
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, normalize_bool, savefig

df = numeric(require_csv("comparative_transport_summary.csv"), exclude=("system", "transport_type"))
required = {"system", "fragmentation_observed"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"comparative_transport_summary.csv missing columns: {missing}")

frag = normalize_bool(df["fragmentation_observed"])

plt.figure(figsize=(8, 5))
plt.bar(df["system"], frag)
plt.ylim(0, 1.2)
plt.yticks([0, 1], ["No", "Yes"])
plt.ylabel("Fragmentation observed")
plt.title("Comparative Transport Regimes")
plt.grid(True, axis="y", alpha=0.3)
savefig("figure7_comparative_transport_regimes.png")
