from extract.weather_extract import extract_weather
from extract.dust_extract import extract_dust

def main():
    print("ETL pipeline start")
    
    weather_raw = extract_weather()
    dust_raw = extract_dust()
    

if __name__ == "__main__":
    main()
