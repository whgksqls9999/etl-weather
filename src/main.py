
from extract.dust_extract import DustExtractor
from extract.weather_extract import WeatherExtractor
from load.csv_loader import load_to_csv
from transform.dust_transform import transform_dust
from transform.merge_transform import merge_weather_dust
from transform.weather_transform import transform_weather

def main():
    print("ETL pipeline start")
    
    weather_extractor = WeatherExtractor()
    dust_extractor = DustExtractor()
    
    weather_raw = weather_extractor.run()
    dust_raw = dust_extractor.run()
    
    weather_df = transform_weather(weather_raw)
    dust_df = transform_dust(dust_raw)
    
    merged_df = merge_weather_dust(weather_df, dust_df)
    
    load_to_csv(merged_df)
    

if __name__ == "__main__":
    main()
