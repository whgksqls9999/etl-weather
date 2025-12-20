from extract import extract_weather
from transform import transform_weather

def main():
    print("ETL pipeline start")

    raw_file = extract_weather()
    print(f"Extract complete: {raw_file}")

    processed_file = transform_weather(raw_file)
    print(f"Transfrom complete: {processed_file}")

if __name__ == "__main__":
    main()
