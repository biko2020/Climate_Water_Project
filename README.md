# Climate Water Crisis Project: Morocco Data Collection Guide

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
7.  [Week 1: Data Collection Workflow](#week-1-data-collection-workflow)
8.  [Expected Directory Organization](#expected-directory-organization)
9.  [Week 1 Completion Goals](#week-1-completion-goals)
10. [Week 2 Preview](#week-2-preview)
11. [Troubleshooting Tips](#troubleshooting-tips)
12. [Conclusion](#conclusion)

## Introduction

🌍 Focus Region: Morocco's Water Crisis

This project focuses on analyzing the water crisis in Morocco, a region facing severe drought and water scarcity challenges. The project aims to collect, clean, and analyze data related to drought indices, groundwater levels, precipitation, and temperature to understand the trends and patterns of water availability in the region. The analysis will focus on identifying the most vulnerable regions, understanding the impact of drought on groundwater resources, and developing visualizations to communicate the findings effectively.

Morocco is facing a historic water crisis:

    70% less rainfall recently vs average

    Six-year drought – worst in 40 years

    Water availability dropped from 2,600m³ to <600m³/person/year since 1960s

    Agriculture uses 87% of national water resources

    Forecast: 53% decline in precipitation this century

🎯 Target Regions for Analysis
Region	Key Characteristics	Coordinates
Souss-Massa	Argan agriculture, groundwater depletion hotspot	~30.4°N, 9.5°W
Marrakech-Safi	Atlas watershed, agri-tourism pressure	~31.6°N, 8.0°W
Casablanca-Settat	High urban water stress, economic hub	~33.6°N, 7.6°W
Oriental	Semi-arid, transboundary water issues	~34.7°N, 2.9°W
🧰 Phase 1: Work Environment Setup
Tools Required:

    Excel / Google Sheets – data cleaning

    Python (optional) – advanced processing

    Tableau Public (free) – visualizations

Project Structure:

Climate_Water_Project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
├── analysis/
├── visualizations/
└── documentation/

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

    Detection of very dry/wet years

Groundwater Metrics:

    Annual depletion rate (cm/year)

    Lag between rainfall & GW change

    Recovery patterns after wet periods

    Regional depletion comparisons

📅 Week 1: Data Collection Workflow
Day	Task
1-2	Download SPEI for all 4 regions (2000–2024), validate, document
3-4	Download GRACE GW data, focus on Souss-Massa + Marrakech-Safi
5-6	Get precipitation + temperature from World Bank (or NOAA as backup)
7	Integrate datasets, check for missing data, begin visualizations
📂 Expected Directory Organization
```
Climate_Water_Project/
├── data/
│   ├── raw/            # Original downloaded files
│   ├── processed/      # Cleaned datasets
│   │   └── morocco_integrated_dataset.csv
│   └── analysis/       # Charts, graphs, statistical outputs
├── documentation/
│   └── data_sources_and_methods.md
└── visualizations/     # Tableau or matplotlib outputs
```
✅ Week 1 Completion Goals

SPEI data (4 regions, 2000–2024)

GRACE data (2002–2024)

Precipitation + Temperature (2000–2024)

Master integrated dataset

Trend charts (initial)

    Document sources + methodology

🔍 Week 2 Preview

    Correlation analysis: drought ↔ rainfall ↔ groundwater

    Rank regions by vulnerability

    Identify critical drought years (e.g., 2022, 2024)

    Build the narrative: how Morocco’s crisis is evolving

🛠️ Troubleshooting Tips
Issue	Solution
Slow SPEI site	Download 1 region at a time
GRACE too complex	Use percentile maps first
World Bank data missing	Use NOAA as backup
Excel crashes	Use Python or break files by region
Mixed date formats	Standardize to YYYY-MM-DD
Inconsistent coordinates	Convert all to decimal degrees

## Conclusion

This project aims to provide a comprehensive analysis of the water crisis in Morocco by integrating various datasets and applying data analysis techniques. The findings will be used to inform decision-making and develop strategies to mitigate the impact of drought and water scarcity in the region.
