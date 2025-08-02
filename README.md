# Climate Water Crisis Project: Morocco Data Collection Guide

## Table of Contents



## Introduction

🌍 Focus Region: Morocco's Water Crisis

This project focuses on analyzing the water crisis in Morocco, a region facing severe drought and water scarcity challenges. The project aims to collect, clean, and analyze data related to drought indices, groundwater levels, precipitation, and temperature to understand the trends and patterns of water availability in the region. The analysis will focus on identifying the most vulnerable regions, understanding the impact of drought on groundwater resources, and developing visualizations to communicate the findings effectively.

Morocco is facing a historic water crisis:

    70% less rainfall recently vs average

    Six-year drought – worst in 40 years

    Water availability dropped from 2,600m³ to <600m³/person/year since 1960s

    Agriculture uses 87% of national water resources

    Forecast: 53% decline in precipitation this century

🎯 Target Regions for Analysis:
### Region	Key Characteristics	Coordinates
    - Souss-Massa	Argan agriculture, groundwater depletion hotspot	~30.4°N, 9.5°W
    - Marrakech-Safi	Atlas watershed, agri-tourism pressure	~31.6°N, 8.0°W
    - Casablanca-Settat	High urban water stress, economic hub	~33.6°N, 7.6°W
    - Oriental	Semi-arid, transboundary water issues	~34.7°N, 2.9°W

🧰 Phase 1: Work Environment Setup
Tools Required:

    Excel / Google Sheets – data cleaning 

    Python – advanced processing

    Tableau Public (free) – visualizations

<<<<<<< HEAD
##  Install Required Python Packages
    - pip install pandas numpy matplotlib seaborn plotly requests beautifulsoup4
    - pip install xarray netcdf4 rasterio geopandas folium
    - pip install scipy scikit-learn

# Step 1: Set up your project structure
python setup_project.py


=======
>>>>>>> 03280bf2ae3160a2c376ecbe0011fb1680d7d368
Project Structure:
```
Climate_Water_Project/
├── data/
│   ├── raw/            # Original downloaded files
│   │   ├── spei_beni_mellal-khenifra.csv
│   │   ├── spei_casablanca-settat.csv
│   │   ├── spei_dakhla-oued_ed-dahab.csv
│   │   ├── spei_draa-tafilalet.csv
│   │   ├── spei_fès-meknès.csv
│   │   ├── spei_guelmim-oued_noun.csv
│   │   ├── spei_laayoune-sakia_el_hamra.csv
│   │   ├── spei_marrakech-safi.csv
│   │   ├── spei_oriental.csv
│   │   ├── spei_rabat-sale-kenitra.csv
│   │   ├── spei_souss-massa.csv
│   │   └── spei_tanger-tetouan-al_hoceïma.csv
│   │   └── spei01.nc
│   ├── processed/      # Cleaned datasets
│   ├── final/
│   └── analysis/       # Charts, graphs, statistical outputs
├── analysis/
<<<<<<< HEAD
│   └── extract_spei_from_netcdf.py
├── config/
│   ├── __init__.py
│   └── regions.py
├── documentation/
│   └── manual_download_guide.md
├── results/            # Project Results
├── visualizations/     # Tableau or matplotlib outputs
├── .gitignore          # List of files ignored by git
├── process_data.py     # Script to process the data
├── README.md           # This file
├── requirements.txt    # List of required Python packages
└── setup_project.py    # Script to set up the project structure
```
=======
├── visualizations/
└── documentation/
```
📦 Phase 2: Data Collection
📊 Dataset 1: SPEI Drought Index

Source: Global SPEI Database
Period: 2000–2024
Resolution: 0.5° (~55 km)
Metric: SPEI-12 (12-month drought index)
Download Instructions:

    Go to: https://spei.csic.es/map/maps.html

    Select: SPEI data → Download data

    Use coordinates for each region (see table above)

    Time Scale: SPEI-12

    Format: CSV

Data Example:

Date,SPEI-12
2000-01-01,-0.45
2000-02-01,-0.67

Interpretation:

    SPEI ≥ 0: Normal to wet

    -1.0 to 0: Mild drought

    -2.0 to -1.5: Severe drought

    < -2.0: Extreme drought

🌊 Dataset 2: GRACE Groundwater Data

Source: NASA GRACE/GRACE-FO
Period: 2002–2024
Resolution: 1° grid (~111 km)
Download Instructions:

    Visit: https://nasagrace.unl.edu/

    Go to Data Access → Groundwater Drought Indicator

    Region: Morocco (28°N–36°N, 17°W–1°E)

    Download monthly groundwater storage anomaly & percentile CSVs

Data Example:

Date,Latitude,Longitude,GW_Percentile,GW_Anomaly_cm
2002-01,30.5,-9.0,25,1.2

Interpretation:

    76–100%: Much above normal

    0–10%: Much below normal (drought)

🌧️ Dataset 3: Precipitation

Option A: World Bank Climate Portal
Option B: NOAA CPC Global Precipitation
Variables:

    Monthly & Annual Precipitation (mm)

    Precipitation Anomalies

Data Format (CSV):

Date,Precip_mm
2000-01,12.4

🌡️ Dataset 4: Temperature (World Bank)

    Monthly Mean, Min, Max Temperatures

    Temperature Anomalies

🧹 Phase 3: Data Cleaning Checklist

Remove duplicates

Standardize date format (YYYY-MM-DD)

Handle missing values

Validate coordinates

    Consistent naming for all regions

📈 Key Metrics to Calculate
Drought Metrics:

    Frequency: Months/year with SPEI < -1.0

    Intensity: Avg. SPEI during droughts

    Duration: Consecutive drought months

    Extreme Events: Count of SPEI < -2.0

Precipitation Metrics:

    Annual trend (mm/year)

    Seasonal contrast (Oct–Apr vs May–Sep)

    Inter-annual volatility
>>>>>>> 03280bf2ae3160a2c376ecbe0011fb1680d7d368

# Step 2: Download the NetCDF file and extract SPEI data
python analysis/extract_spei_from_netcdf.py

## Data Sources

*   SPEI data: [Link to original data source] - SPEI data for different regions of Morocco, downloaded from a third-party source. The data is available in CSV format in the `data/raw` directory. The NetCDF file `spei01.nc` also contains SPEI data.
*   Groundwater level data: [Link to original data source] - Groundwater level data for Morocco, downloaded from a third-party source. (Note: The exact source of this data is not specified in the project files.)
*   Precipitation data: [Link to original data source] - Precipitation data for Morocco, downloaded from a third-party source. (Note: The exact source of this data is not specified in the project files.)
*   Temperature data: [Link to original data source] - Temperature data for Morocco, downloaded from a third-party source. (Note: The exact source of this data is not specified in the project files.)

## Analysis Methods

The project uses the following data analysis methods:

*   Data cleaning: Excel/Google Sheets, Python
*   Data processing: Python (pandas, numpy, xarray)
*   Data visualization: Tableau Public, matplotlib

<<<<<<< HEAD
## Project Structure

=======
📅 Week 1: Data Collection Workflow
Day	Task
1-2	Download SPEI for all 4 regions (2000–2024), validate, document
3-4	Download GRACE GW data, focus on Souss-Massa + Marrakech-Safi
5-6	Get precipitation + temperature from World Bank (or NOAA as backup)
7	Integrate datasets, check for missing data, begin visualizations
📂 Expected Directory Organization
>>>>>>> 03280bf2ae3160a2c376ecbe0011fb1680d7d368
```
Climate_Water_Project/
├── data/
│   ├── raw/            # Original downloaded files
│   ├── processed/      # Cleaned datasets
│   │   └── morocco_integrated_dataset.csv
│   └── analysis/       # Charts, graphs, statistical outputs
├── documentation/
│   └── data_sources_and_methods.md
├── results/            # Project Results
└── visualizations/     # Tableau or matplotlib outputs
<<<<<<< HEAD
├── process_data.py     # Script to process the data
├── README.md           # This file
├── requirements.txt    # List of required Python packages
└── setup_project.py    # Script to set up the project structure
```

## How to Run the Project
=======
```
✅ Week 1 Completion Goals

SPEI data (4 regions, 2000–2024)
>>>>>>> 03280bf2ae3160a2c376ecbe0011fb1680d7d368

1.  Set up the project structure: `python setup_project.py`
2.  Download the data from the data sources listed above and place it in the `data/raw` directory.
3.  Extract SPEI data from NetCDF file: `python analysis/extract_spei_from_netcdf.py`
4.  Process the data: `python process_data.py`
5.  Analyze the data and create visualizations using Tableau Public or matplotlib.

## Results

The project is expected to produce the following results:

*   Visualizations of drought indices, groundwater levels, precipitation, and temperature in Morocco.
*   Identification of the most vulnerable regions to drought and water scarcity.
*   Analysis of the impact of drought on groundwater resources.
*   A comprehensive report on the water crisis in Morocco.

## Conclusion

This project aims to provide a comprehensive analysis of the water crisis in Morocco by integrating various datasets and applying data analysis techniques. The findings will be used to inform decision-making and develop strategies to mitigate the impact of drought and water scarcity in the region.

## Create Virtual Environment and Install Packages

To set up the project environment, follow these steps:

1.  Create a virtual environment: `python -m venv .venv`
2.  Activate the virtual environment: `source .venv/bin/activate`
3.  Install the packages from requirements.txt: `pip install -r requirements.txt`
