from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
FIGURES = ROOT / "figures" / "phase1"
OUTPUTS = ROOT / "outputs"

FIGURES.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

def require_csv(filename: str) -> pd.DataFrame:
    path = DATA / filename
    if not path.exists():
        raise FileNotFoundError(
            f"Missing required input CSV: {path}\n"
            f"Place the canonical processed file at data/processed/{filename}"
        )
    return pd.read_csv(path)

def savefig(name: str):
    path = FIGURES / name
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"saved: {path}")

def numeric(df: pd.DataFrame, exclude=("condition", "system", "phase", "intervention", "regime")) -> pd.DataFrame:
    df = df.copy()
    for c in df.columns:
        if c not in exclude:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def normalize_bool(series):
    return (
        series.astype(str)
        .str.lower()
        .map({"true": 1, "false": 0, "1": 1, "0": 0, "yes": 1, "no": 0})
        .fillna(pd.to_numeric(series, errors="coerce"))
    )
