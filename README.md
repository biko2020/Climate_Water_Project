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

##  Install Required Python Packages
    - pip install pandas numpy matplotlib seaborn plotly requests beautifulsoup4
    - pip install xarray netcdf4 rasterio geopandas folium
    - pip install scipy scikit-learn

# Step 1: Set up your project structure
python setup_project.py


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

## Project Structure

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
├── process_data.py     # Script to process the data
├── README.md           # This file
├── requirements.txt    # List of required Python packages
└── setup_project.py    # Script to set up the project structure
```

## How to Run the Project

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
