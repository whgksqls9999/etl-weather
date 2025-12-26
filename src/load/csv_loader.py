from pathlib import Path

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_to_csv(df, filename="merged_data.csv"):
    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"[Load] Data saved to {path}")