import json
from datetime import date, timedelta
from pathlib import Path

RAW_DIR = Path("data/raw/dust")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def extract_dust():
    today = date.today()
    days = [(today - timedelta(days=i)).isoformat() for i in range(3)]
    
    dummy_data = {
        "data": [
            {"date": d, "pm10": 30 + i * 5, "pm25": 15 + i * 3} for i, d in enumerate(days)
        ]
    }
    
    file_path = RAW_DIR / "dust.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dummy_data, f, ensure_ascii=False, indent=2)
        
    print("[Extract] dust data saved")
    return file_path
