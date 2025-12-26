from extract.weather_extract import extract_weather
from extract.dust_extract import extract_dust
from transform.dust_transform import transform_dust
from transform.merge_transform import merge_weather_dust
from transform.weather_transform import transform_weather

def main():
    print("ETL pipeline start")
    
    weather_raw = extract_weather()
    dust_raw = extract_dust()
    
    weather_df = transform_weather(weather_raw)
    dust_df = transform_dust(dust_raw)
    merged_df = merge_weather_dust(weather_df, dust_df)
    

if __name__ == "__main__":
    main()
