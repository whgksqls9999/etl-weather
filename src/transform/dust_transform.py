import json
import pandas as pd

def transform_dust(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    df = pd.DataFrame(raw["data"])
    
    print("[Transform] Dust transformed")
    return df
        