import requests
import json
from datetime import datetime
from pathlib import Path

from extract.base import BaseExtractor



class WeatherExtractor(BaseExtractor):
    def fetch(self) -> dict:
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
        
        return data
    
    @property
    def name(self) -> str:
        return "weather"