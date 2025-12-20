import json
from pathlib import Path
import pandas as pd


def transform_weather(raw_file_path: Path) -> Path:
    # raw JSON 로드
    with open(raw_file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Validate        
    if "daily" not in raw_data:
        raise ValueError("Missing 'daily' in raw data")
    
    required_keys = ["time", "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean"]

    daily = raw_data["daily"]
    
    for key in required_keys:
        if key not in daily:
            raise ValueError(f"Missing '{key}' in daily data")

    df = pd.DataFrame({
        "date": daily["time"],
        "temp_max": daily["temperature_2m_max"],
        "temp_min": daily["temperature_2m_min"],
        "temp_mean": daily["temperature_2m_mean"],
    })
    
    # 파생 컬럼
    df["temp_range"] = df["temp_max"] - df["temp_min"]

    return df
