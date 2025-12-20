from pathlib import Path


def load_to_csv(df):
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = processed_dir / "weather_daily.csv"
    
    df.to_csv(file_path, index=False, encoding="utf-8")
    
    return file_path