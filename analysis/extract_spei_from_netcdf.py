import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import xarray as xr
import pandas as pd
from config.regions import moroccan_regions
from config.regions import clean_filename


def extract_spei_series(netcdf_path, output_dir, start_year=2000, end_year=2024):
    ds = xr.open_dataset(netcdf_path)
    
    for region, (lat, lon) in moroccan_regions.items():
        print(f"Processing {region}...")
        
        # Select nearest grid point
        spei = ds['spei'].sel(lat=lat, lon=lon, method="nearest")
        
        # Convert to DataFrame
        df = spei.to_dataframe().reset_index()
        df = df.rename(columns={'time': 'date', 'spei': 'SPEI'})
        
        # Filter by date
        df = df[(df['date'] >= f'{start_year}-01-01') & (df['date'] <= f'{end_year}-12-31')]
        
        # Save to CSV
        region_file = clean_filename(region)
        output_file = os.path.join(output_dir, f"spei_{region_file}_{start_year}_{end_year}.csv")
        df.to_csv(output_file, index=False)
        print(f"Saved to {output_file}")

if __name__ == "__main__":
    netcdf_file = "data/raw/spei01.nc"
    output_folder = "data/raw"
    
    if os.path.exists(netcdf_file):
        extract_spei_series(netcdf_file, output_folder)
    else:
        print(f" NetCDF file not found at: {netcdf_file}")
