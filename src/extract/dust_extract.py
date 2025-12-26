import json
from datetime import date, timedelta
from pathlib import Path

from extract.base import BaseExtractor


class DustExtractor(BaseExtractor):
    def fetch(self) -> dict:
        today = date.today()
        days = [(today - timedelta(days=i)).isoformat() for i in range(3)]
        
        dummy_data = {
            "data": [
                {"date": d, "pm10": 30 + i * 5, "pm25": 15 + i * 3} for i, d in enumerate(days)
            ]
        }
        
        return dummy_data
    
    @property
    def name(self) -> str:
        return "dust"
