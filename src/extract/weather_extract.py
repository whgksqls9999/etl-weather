import requests
import json
from datetime import datetime
from pathlib import Path

RAW_DIR = Path("data/raw/weather")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 37.5665,      # 서울
        "longitude": 126.9780,
        "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean",
        "timezone": "Asia/Seoul"
    }

    response = requests.get(url, params=params) 
    response.raise_for_status()

    data = response.json()

    file_path = RAW_DIR / "weather.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("[Extract] Weather data saved")
    return file_path
