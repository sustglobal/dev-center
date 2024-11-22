---
layout: doc
title: Sust Global CSV Visual Summary Dataset Guide
subtitle: This section will go through the dataset available for download and explain the methodology behind it. We will also show you how to use and interpret the numbers, which includes a written interpretation of the datasets.
date: 2024-11-15
lastmod: 2024-11-18
author: TA
tags:
- csv
- dataset
- visual summary
---

## Before Getting Started

 Please note that you must change the sections of text in brackets **[  ]** to suit the specific values, hazards and scenarios you are describing.

## What are the CSV datasets?

Comma separated value (CSV) files contain the physical climate risk and financial impact analysis information from Visual Summary Dashboard product, which can be used for strategic planning needs. The CSV files are useful if you would like to use the underlying data to create your own graphs or charts for a report or presentation, to undergo further analysis (such as data aggregations, comparisons between assets etc.) or as an input into your Excel models.

Likewise, the data is provided in geojson format for your convenience.

## Data Dictionary

| Name | Type | Description |
| ---- | ---- | ----------- |
| ENTITY_ID  | STRING | User provided identifier (Optional) |
| ENTITY_NAME  | STRING | User provided asset name (Optional) |
| LNG | STRING | Latitude |
| LAT | STRING | Longitude |
| LABEL:TEXT | STRING | User provided supplementary columns (Optional) |
| TYPE | STRING | User provided asset type (Optional; Default = General) |
| SCENARIO | STRING | Carbon emissions scenario (ssp245 or ssp585) |
| HAZARD | STRING | Climate hazard (wildfire, cyclone, flood, heatwave, water_stress, sea_level_rise) |
| SUMMARY_SCORE_30YR     | FLOAT | In a 30 year window (2024-2055), the maximum risk exposure | 
| SUMMARY_LABEL_30YR     | STRING | Low/Medium/High label determined by SUMMARY_SCORE_30YR | 
| SUMMARY_SCORE_15YR     | FLOAT | In a 15 year window (2024-2039), the maximum risk exposure | 
| SUMMARY_LABEL_15YR     | STRING | Low/Medium/High label determined by SUMMARY_SCORE_15YR | 
| INDICATOR_BASELINE     | FLOAT  | The baseline value averaged from 1980-2010 for the given physical risk indicator |
| INDICATOR_BASELINE_LBD | FLOAT  | The lower bound baseline value averaged from 1980-2010 for the given physical risk indicator |
| INDICATOR_BASELINE_UBD | FLOAT  | The upper bound baseline value averaged from 1980-2010 for the given physical risk indicator |
| INDICATOR_2030         | FLOAT  | The value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2030_LBD     | FLOAT  | The lower bound value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2030_UBD     | FLOAT  | The upper bound value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2050         | FLOAT  | The value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2050_LBD     | FLOAT  | The lower bound value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2050_UBD     | FLOAT  | The upper bound value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2080         | FLOAT  | The value averaged from 2075-2085 for the given physical risk indicator | 
| INDICATOR_2080_LBD     | FLOAT  | The lower bound value averaged from 2075-2085 for the given physical risk indicator | 
| INDICATOR_2080_UBD     | FLOAT  | The upper bound value averaged from 2075-2085 for the given physical risk indicator | 
| STRUCTURAL_DAMAGE_BASELINE         | FLOAT  | The baseline value averaged from 1980-2010 for the structural damage resulting from risk exposure. Range 0 to 1. |
| STRUCTURAL_DAMAGE_BASELINE_LBD     | FLOAT  | The lower bound baseline value averaged from 1980-2010 for the structural damage resulting from risk exposure. Range 0 to 1. | 
| STRUCTURAL_DAMAGE_BASELINE_UBD     | FLOAT  | The upper bound baseline value averaged from 1980-2010 for the structural damage resulting from risk exposure. Range 0 to 1. | 
| STRUCTURAL_DAMAGE_2030             | FLOAT  | The value averaged from 2025-2034 for the structural damage resulting from risk exposure. Range 0 to 1. | 
| STRUCTURAL_DAMAGE_2030_LBD         | FLOAT  | The lower bound value averaged from 2025-2034 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| STRUCTURAL_DAMAGE_2030_UBD         | FLOAT  | The upper bound value averaged from 2025-2034 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| STRUCTURAL_DAMAGE_2050             | FLOAT  | The value averaged from 2045-2054 for the structural damage resulting from risk exposure. Range 0 to 1. | 
| STRUCTURAL_DAMAGE_2050_LBD         | FLOAT  | The lower bound value averaged from 2045-2054 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| STRUCTURAL_DAMAGE_2050_UBD         | FLOAT  | The upper bound value averaged from 2045-2054 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| STRUCTURAL_DAMAGE_2080             | FLOAT  | The value averaged from 2075-2084 for the structural damage resulting from risk exposure. Range 0 to 1. | 
| STRUCTURAL_DAMAGE_2080_LBD         | FLOAT  | The lower bound value averaged from 2075-2084 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| STRUCTURAL_DAMAGE_2080_UBD         | FLOAT  | The upper bound value averaged from 2075-2084 for the structural damage resulting from risk exposure. Range 0 to 1. |  
| BUSINESS_INTERRUPTION_BASELINE     | FLOAT  | The baseline value averaged from 1980-2010 for the business interruption resulting from risk exposure. Range 0 to 1. |
| BUSINESS_INTERRUPTION_BASELINE_LBD | FLOAT  | The lower bound baseline value averaged from 1980-2010 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_BASELINE_UBD | FLOAT  | The upper bound baseline value averaged from 1980-2010 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2030         | FLOAT  | The value averaged from 2025-2034 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2030_LBD     | FLOAT  | The lower bound value averaged from 2025-2034 for the business interruption resulting from risk exposure. Range 0 to 1. |  
| BUSINESS_INTERRUPTION_2030_UBD     | FLOAT  | The upper bound value averaged from 2025-2034 for the business interruption resulting from risk exposure. Range 0 to 1. |  
| BUSINESS_INTERRUPTION_2050         | FLOAT  | The value averaged from 2045-2054 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2050_LBD     | FLOAT  | The lower bound value averaged from 2045-2054 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2050_UBD     | FLOAT  | The upper bound value averaged from 2045-2054 for the business interruption resulting from risk exposure. Range 0 to 1. |  
| BUSINESS_INTERRUPTION_2080         | FLOAT  | The value averaged from 2075-2084 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2080_LBD     | FLOAT  | The lower bound value averaged from 2075-2084 for the business interruption resulting from risk exposure. Range 0 to 1. | 
| BUSINESS_INTERRUPTION_2080_UBD     | FLOAT  | The upper bound value averaged from 2075-2084 for the business interruption resulting from risk exposure. Range 0 to 1. |  

## Scenario Analytics

For more information about individual hazards, climate scenarios, summarization labeling (Low/Medium/High), and structural damage and business interruption modeling, see the [Climate Data Guide](data-guide).
