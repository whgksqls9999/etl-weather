import json
from pathlib import Path
import pandas as pd


def transform_weather(raw_file_path: Path) -> Path:
    # raw JSON 로드
    with open(raw_file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    daily = raw_data["daily"]

    df = pd.DataFrame({
        "date": daily["time"],
        "temp_max": daily["temperature_2m_max"],
        "temp_min": daily["temperature_2m_min"],
        "temp_mean": daily["temperature_2m_mean"],
    })
    
    # 파생 컬럼
    df["temp_range"] = df["temp_max"] - df["temp_min"]

    # 저장 경로
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    output_path = processed_dir / "weather_daily.csv"
    df.to_csv(output_path, index=False)

    return output_path
