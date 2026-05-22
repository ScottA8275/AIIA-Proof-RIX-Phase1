"""
Proof RIX Phase I
Canonical Reproduction Runner

Runs all canonical Milestones 7–10
reproducibility scripts.
"""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    "reproduce_recursive_capacity.py",
    "reproduce_fragmentation_boundaries.py",
    "reproduce_gb1_recursive_compression.py",
    "reproduce_gb1_perturbation.py",
    "reproduce_comparative_transport_regimes.py",
    "reproduce_predictive_topology.py",
    "reproduce_causal_interventions.py",
    "reproduce_phase_boundary_map.py",
]


def run_script(script_name):

    script_path = ROOT / "scripts" / script_name

    print("\n" + "=" * 70)
    print(f"RUNNING: {script_name}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=ROOT,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"\nFAILED: {script_name}"
        )

    print(f"COMPLETED: {script_name}")


def main():

    print("\n")
    print("=" * 70)
    print("PROOF RIX PHASE I REPRODUCTION")
    print("=" * 70)

    for script in SCRIPTS:
        run_script(script)

    print("\n")
    print("=" * 70)
    print("ALL REPRODUCTIONS COMPLETED")
    print("=" * 70)

    print("\nCanonical figures written to:")
    print("figures/phase1/")


if __name__ == "__main__":
    main()