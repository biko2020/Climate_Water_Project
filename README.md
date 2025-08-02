# Climate Water Crisis Project: Morocco Data Analysis

## Table of Contents

1.  [Introduction](#introduction)
2.  [Target Regions for Analysis](#target-regions-for-analysis)
3.  [Phase 1: Work Environment Setup](#phase-1-work-environment-setup)
4.  [Phase 2: Data Collection](#phase-2-data-collection)
    *   [Dataset 1: SPEI Drought Index](#dataset-1-spei-drought-index)
    *   [Dataset 2: GRACE Groundwater Data](#dataset-2-grace-groundwater-data)
    *   [Dataset 3: Precipitation](#dataset-3-precipitation)
    *   [Dataset 4: Temperature (World Bank)](#dataset-4-temperature-world-bank)
5.  [Phase 3: Data Cleaning Checklist](#phase-3-data-cleaning-checklist)
6.  [Key Metrics to Calculate](#key-metrics-to-calculate)
7.  [Troubleshooting Tips](#troubleshooting-tips)
8.  [Conclusion](#conclusion)

## Introduction

🌍 Focus Region: Morocco's Water Crisis

This project analyzes the escalating water crisis in Morocco, a region grappling with severe drought and water scarcity. By collecting, cleaning, and analyzing data related to drought indices, groundwater levels, precipitation patterns, and temperature variations, the project aims to:

*   Identify the regions most vulnerable to water scarcity.
*   Assess the impact of drought on groundwater resources.
*   Develop compelling visualizations to effectively communicate key findings.

Morocco is facing a critical water situation:

*   Rainfall has decreased by 70% compared to the average.
*   The country is experiencing a six-year drought, the worst in four decades.
*   Water availability has plummeted from 2,600m³ to less than 600m³/person/year since the 1960s.
*   Agriculture consumes 87% of the nation's water resources.
*   A 53% decline in precipitation is projected for this century.

🎯 Target Regions for Analysis:

| Region                      | Key Characteristics                               | Coordinates          |
| --------------------------- | ------------------------------------------------- | -------------------- |
| Souss-Massa                 | Argan agriculture, groundwater depletion hotspot  | ~30.4°N, 9.5°W       |
| Marrakech-Safi              | Atlas watershed, agri-tourism pressure            | ~31.6°N, 8.0°W       |
| Casablanca-Settat           | High urban water stress, economic hub             | ~33.6°N, 7.6°W       |
| Oriental                    | Semi-arid, transboundary water issues             | ~34.7°N, 2.9°W       |
| Fès-Meknès                  | Agricultural region                               | ~34.0°N, 4.9°W       |
| Rabat-Salé-Kénitra          | Coastal region with high population density      | ~34.0°N, 6.8°W       |
| Béni Mellal-Khénifra        | Mountainous region, important for water resources | ~32.5°N, 6.4°W       |
| Drâa-Tafilalet              | Desert region, oases                              | ~31.2°N, 5.5°W       |
| Tanger-Tétouan-Al Hoceïma   | Northern region, Rif mountains                    | ~35.0°N, 5.5°W       |
| Guelmim-Oued Noun           | Southern region, Saharan influence                | ~28.9°N, 10.0°W      |
| Laâyoune-Sakia El Hamra    | Western Sahara region                             | ~27.2°N, 13.1°W      |
| Dakhla-Oued Ed-Dahab        | Southernmost region, Atlantic coast                | ~23.7°N, 15.9°W      |

🧰 Phase 1: Work Environment Setup

Tools Required:

*   Excel / Google Sheets – data cleaning
*   Python – advanced processing
*   Tableau Public (free) – visualizations

## Install Required Python Packages

```bash
pip install pandas numpy matplotlib seaborn plotly requests beautifulsoup4
pip install xarray netcdf4 rasterio geopandas folium
pip install scipy scikit-learn
```

# Step 1: Set up your project structure

```bash
python setup_project.py
```

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
│   ├── final/           # Integrated datasets
│   └── analysis/        # Charts, graphs, statistical outputs
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

```bash
python analysis/extract_spei_from_netcdf.py
```

## Data Sources

*   SPEI data: [SPEI Data Source](https://spei.csic.es/index.html) - SPEI data for different regions of Morocco, available in CSV format in the `data/raw` directory and as a NetCDF file `spei01.nc`.
*   Groundwater level data: [GRACE Data Source](https://grace.jpl.nasa.gov/)
*   Precipitation data: [Precipitation Data Source](https://www.worldbank.org/en/data)
*   Temperature data: [Temperature Data Source](https://www.worldbank.org/en/data)

## Analysis Methods

The project employs the following data analysis methods:

*   Data cleaning: Excel/Google Sheets, Python
*   Data processing: Python (pandas, numpy, xarray)
*   Data visualization: Tableau Public, matplotlib

## How to Run the Project

1.  Set up the project structure: `python setup_project.py`
2.  Download the data from the data sources listed above and place it in the `data/raw` directory.
3.  Extract SPEI data from NetCDF file: `python analysis/extract_spei_from_netcdf.py`
4.  Process the data: `python process_data.py`
5.  Analyze the data and create visualizations using Tableau Public or matplotlib.

## Results

The project aims to produce the following results:

*   Visualizations of drought indices, groundwater levels, precipitation, and temperature in Morocco.
*   Identification of regions most vulnerable to drought and water scarcity.
*   Assessment of the impact of drought on groundwater resources.
*   A comprehensive report on the water crisis in Morocco, informing decision-making and strategies to mitigate the impact of drought and water scarcity in the region.

## Conclusion

This project provides a comprehensive analysis of the water crisis in Morocco by integrating diverse datasets and applying robust data analysis techniques. The findings will inform decision-making and support the development of targeted strategies to mitigate the impact of drought and water scarcity in the region.

## Create Virtual Environment and Install Packages

To set up the project environment, follow these steps:

1.  Create a virtual environment: `python -m venv .venv`
2.  Activate the virtual environment: `source .venv/bin/activate`
3.  Install the packages from requirements.txt: `pip install -r requirements.txt`
