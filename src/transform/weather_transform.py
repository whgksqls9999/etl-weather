import json
import pandas as pd

def transform_weather(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
        
    df = pd.DataFrame({
        "data": raw["daily"]["time"],
        "temp_max": raw["daily"]["temperature_2m_max"]
    })
    
    print("[Transform] Weather transformed")
    return df
    