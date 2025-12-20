from extract import extract_weather
from transform import transform_weather
from load import load_to_csv

def main():
    print("ETL pipeline start")

    raw_file = extract_weather()
    print(f"Extract complete: {raw_file}")

    df = transform_weather(raw_file)
    print(f"Transfrom complete: {df.head()}")
    
    processed_file = load_to_csv(df)
    print(f"Load complete: {processed_file}")

if __name__ == "__main__":
    main()
