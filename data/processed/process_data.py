import os
import pandas as pd
from config.regions import moroccan_regions, clean_filename

raw_dir = "data/raw"
processed_dir = "data/processed"

def clean_spei_data():
    for region in moroccan_regions:
        fname = f"spei_{clean_filename(region)}_2000_2024.csv"
        raw_path = os.path.join(raw_dir, fname)
        processed_path = os.path.join(processed_dir, fname)

        df = pd.read_csv(raw_path)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['SPEI'] = pd.to_numeric(df['SPEI'], errors='coerce')
        df = df.dropna().drop_duplicates()

        df.to_csv(processed_path, index=False)
        print(f"✔ Cleaned: {fname}")

if __name__ == "__main__":
    os.makedirs(processed_dir, exist_ok=True)
    clean_spei_data()
