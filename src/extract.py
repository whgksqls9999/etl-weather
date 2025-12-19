import requests
import json
from datetime import datetime
from pathlib import Path


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

    # 저장 경로
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = raw_dir / f"weather_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return file_path
