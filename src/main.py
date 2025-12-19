from extract import extract_weather

def main():
    print("ETL pipeline start")

    raw_file = extract_weather()
    print(f"Extract complete: {raw_file}")


if __name__ == "__main__":
    main()
