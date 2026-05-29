"""
Reproduce supporting GB1 recursive compression/locality figures.

Expected inputs:
data/processed/gb1_compression_summary.csv
data/processed/gb1_locality_summary.csv
"""
import numpy as np
import matplotlib.pyplot as plt
from _utils import require_csv, numeric, savefig

compression = numeric(require_csv("gb1_compression_summary.csv"))
locality = numeric(require_csv("gb1_locality_summary.csv"))

if not {"condition", "nodes", "edges"}.issubset(compression.columns):
    raise ValueError("gb1_compression_summary.csv requires condition,nodes,edges")

plt.figure(figsize=(8, 5))
x = np.arange(len(compression))
width = 0.35
plt.bar(x - width/2, compression["nodes"], width, label="Nodes")
plt.bar(x + width/2, compression["edges"], width, label="Edges")
plt.xticks(x, compression["condition"].astype(str), rotation=10)
plt.ylabel("Count")
plt.title("Recursive Biological Compression and Phenotype-local Basin Structure")
plt.grid(True, axis="y", alpha=0.3)
plt.legend()
savefig("figure5_gb1_recursive_compression.png")

if {"condition", "mean_within_basin_std"}.issubset(locality.columns):
    plt.figure(figsize=(7, 5))
    plt.bar(locality["condition"], locality["mean_within_basin_std"])
    plt.xticks(rotation=15, ha="right")
    plt.ylabel("Mean within-basin phenotype std")
    plt.title("GB1 Phenotype Locality")
    plt.grid(True, axis="y", alpha=0.3)
    savefig("support_gb1_phenotype_locality.png")
