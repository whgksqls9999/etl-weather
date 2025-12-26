from abc import ABC, abstractmethod
from pathlib import Path
import json

class BaseExtractor(ABC):
    raw_dir = Path("data/raw")
    
    def run(self) -> Path:        
        data = self.fetch()
        file_path = self.save(data)
        
        return file_path
    
    @abstractmethod    
    def fetch(self) -> dict:
        pass
    
    def save(self, data: dict) -> Path:
        file_path = self.raw_dir / f"{self.name}" / f"{self.name}.json"
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return file_path
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    