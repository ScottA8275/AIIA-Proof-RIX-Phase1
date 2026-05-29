"""
Reproduce Figure 7: Clustering Enhancement Intervention.

Expected input:
data/processed/synthetic_transport_manipulation.csv

Required columns:
system, intervention, max_edge_betweenness
"""
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

df = numeric(require_csv("synthetic_transport_manipulation.csv"), exclude=("system", "intervention", "predicted_phase"))
required = {"system", "intervention", "max_edge_betweenness"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"synthetic_transport_manipulation.csv missing columns: {missing}")

baseline = df[df["intervention"] == "baseline"].sort_values("system")
cluster = df[df["intervention"] == "cluster_enhanced"].sort_values("system")

if len(baseline) == 0 or len(cluster) == 0:
    raise ValueError("synthetic_transport_manipulation.csv must include baseline and cluster_enhanced interventions")

plt.figure(figsize=(8, 5))
x = range(len(cluster))
plt.plot(list(x), baseline["max_edge_betweenness"], marker="o", label="Baseline")
plt.plot(list(x), cluster["max_edge_betweenness"], marker="o", label="Cluster enhanced")
plt.xticks(list(x), cluster["system"])
plt.ylabel("Maximum edge betweenness")
plt.title("Clustering Enhancement Eliminates Bottleneck-Dominated Transport")
plt.grid(True, alpha=0.3)
plt.legend()
savefig("figure8_clustering_intervention.png")
