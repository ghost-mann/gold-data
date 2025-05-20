from extract import fetch_xauusd_data
from transform import transform_data
from load import load_data
import pandas as pd

def run_etl():
    print("Starting ETL pipeline...")

    # extraction
    print("Starting data extraction...")

    try:
        raw_data = fetch_xauusd_data()

        if 'values' not in raw_data:
            print("No data found, Check api configuration or usage!")
            return
    except Exception as e:
        print(f"Error while fetching data: {e}")
        return

    # transformation
    print("Starting data transformation...")
    df = pd.DataFrame(raw_data['values'])
    df = transform_data(df)

    # load
    print("Starting data loading...")
    load_data(df)

    print("ETL pipeline finished successfully!")

if __name__ == "__main__":
    run_etl()
