---
layout: doc
title: Zonal Climate Risk Statistics on Administrative Boundaries
subtitle: This document provides users with an introduction to Sust Global’s admin boundaries data.
date: 2024-06-05
lastmod: 2025-05-30
author: TA
tags:
- data
- yearly
---

## Why Admin Boundaries?

Administrative divisions or boundaries are sub-sovereign geographical areas, often with their own system of administration or governance. They frequently coincide with economic zones, or concentrations of economic activity. This is useful with regards to physical risk exposure, as isolating physical risk by zone can lead to greater insights. For example, comparing coastal zones, which could be impacted by cyclones, to interior zones, which might be exposed to heatwaves or water stress, gives a more holistic picture across business interests.


## About the Data

Sust Global's admin boundaries dataset provides highly granular physical risk exposure scores, and financial impact metrics, to help risk management and risk reporting teams across financial and sustainability organizations assess the impact of climate change on their portfolios, operational assets and supply chains.

The dataset covers six major climate hazards over two scenarios and four time periods:
- Projections from advanced climate physical hazard modeling leveraging CMIP6 climate models, regional risk zoning, space derived observational datasets and proprietary AI powered modeling techniques, and covering two future climate change scenarios: Medium (SSP2-RCP4.5) and High (SSP5-RCP8.5) physical climate risk metrics across baseline, 2025-2035, 2045-2055 and 2075-2085.
- Physical risk scores and labels reflecting exposure to climate hazards across scenarios and time periods.
- Financial impact metrics reflecting the value of financial impacts and losses from structural damage projected due to changing climate hazard exposure for a given asset within the zip code, expressed as a percentage of the asset value (% metric).
- Financial impact metrics reflecting the value of financial impacts and losses from business interruption projected due to changing climate hazard exposure for a given asset within the zip code, expressed as a percentage of the number of days in a year (% metric).
- Uncertainty bounds representing lower bound and upper bound for financial impact metrics for structural damage and business interruption.
- Six (6) physical climate hazards covered are Coastal and Inland Flooding, Wildfire, Tropical Cyclone, Heatwaves, Water Stress and Sea level Rise.


## Supported Countries

Sust Global currently supports the following countries at the admin two, three, and four level:
- United States of America
- India
- Australia
- Canada
- Great Britain
- Netherlands
- Japan
- Spain
- Germany
- Sweden
- Belgium
- France

Glossary of boundaries by country:

| Code | Country | Admin 2 | Admin 3 | Admin 4 |
| ---- | ------- | ------- | ------- | ------- |
| AUS  | Australia     | local gov      | postal codes   | localities | 
| BEL  | Belgium       | provinces      | districts      | municipalities |
| CAN  | Canada        | counties       | districts      | census subdivisions |
| DEU  | Germany       | districts      | municipalities | towns |
| ESP  | Spain         | provinces      | counties       | municipalities |
| FRA  | France        | departments    | districts      | subdivisions |
| GBR  | Great Britain | counties       | districts      | parishes |
| IND  | India         | divisions      | districts      | subdistricts | 
| JPN  | Japan         | municipalities | municipalities | sub-municipalities | 
| NLD  | Netherlands   | municipalities | districts      | neighborhoods |
| SWE  | Sweden        | municipalities | districts      | districts |
| USA  | United States | counties       | zip codes      | census tracts |


## Supported Data Layers

The supported data layers span physical risk factors, resilience scores, socioeconomic and demographic features, as well as biodiversity scores and other datasets. The full set of supported data layers is detailed in the [Visual Summary Multimodal Guide](https://developers.sustglobal.com/visual-summary-multimodal-guide). 

## Data Dictionary

| Name | Type | Description |
| ---- | ---- | ----------- |
| ID  | STRING | Identifier (is not unique across datasets) |
| LAT | STRING | Latitude |
| LNG | STRING | Longitude |
| ADMIN_PROCESSING_LEVEL | STRING | The admin boundary level to which this dataset corresponds (2,3,4) |
| ADMIN0 | STRING | 3 Letter Country Code |
| ADMIN1 | STRING | Admin 1 boundary name |
| ADMIN2 | STRING | Admin 2 boundary ID |
| ADMIN3 | STRING | Admin 3 boundary ID (if applicable) |
| ADMIN4 | STRING | Admin 4 boundary ID (if applicable) |
| SCENARIO ANALYTICS | OBJ | Contains the climate scenarios ssp245 and ssp585. Each scenario contains hazards wildfire, cyclone, flood, heatwave, water stress and sea level rise. For each hazard, data is windowed for baseline, 2030, 2050, and 2080. In turn the ubd (upper bound) and lbd (lower bound) values indicate the uncertainty for each window. (Special note on heatwave indicator and business interruption: values are normalized by 365 to give them in percents rather than days) |
| SUMMARY_SCORE_30YR     | STRING | In a 30 year window, the maximum risk exposure | 
| SUMMARY_SCORE_15YR     | STRING | In a 15 year window, the maximum risk exposure | 
| INDICATOR_BASELINE     | FLOAT  | The baseline value for the given physical risk indicator |
| INDICATOR_BASELINE_LBD | FLOAT  | The lower bound baseline value for the given physical risk indicator |
| INDICATOR_BASELINE_UBD | FLOAT  | The upper bound baseline value for the given physical risk indicator |
| INDICATOR_2030         | FLOAT  | The value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2030_LBD     | FLOAT  | The lower bound value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2030_UBD     | FLOAT  | The upper bound value averaged from 2025-2035 for the given physical risk indicator |
| INDICATOR_2050         | FLOAT  | The value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2050_LBD     | FLOAT  | The lower bound value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2050_UBD     | FLOAT  | The upper bound value averaged from 2045-2055 for the given physical risk indicator | 
| INDICATOR_2080         | FLOAT  | The value averaged from 2075-2085 for the given physical risk indicator | 
| INDICATOR_2080_LBD     | FLOAT  | The lower bound value averaged from 2075-2085 for the given physical risk indicator | 
| INDICATOR_2080_UBD     | FLOAT  | The upper bound value averaged from 2075-2085 for the given physical risk indicator | 
| STRUCTURAL_DAMAGE_BASELINE         | FLOAT  | The baseline value for the structural damage resulting from risk exposure |
| STRUCTURAL_DAMAGE_BASELINE_LBD     | FLOAT  | The lower bound baseline value for the structural damage resulting from risk exposure | 
| STRUCTURAL_DAMAGE_BASELINE_UBD     | FLOAT  | The upper bound baseline value for the structural damage resulting from risk exposure | 
| STRUCTURAL_DAMAGE_2030             | FLOAT  | The value averaged from 2025-2035 for the structural damage resulting from risk exposure | 
| STRUCTURAL_DAMAGE_2030_LBD         | FLOAT  | The lower bound value averaged from 2025-2035 for the structural damage resulting from risk exposure |  
| STRUCTURAL_DAMAGE_2030_UBD         | FLOAT  | The upper bound value averaged from 2025-2035 for the structural damage resulting from risk exposure |  
| STRUCTURAL_DAMAGE_2050             | FLOAT  | The value averaged from 2045-2055 for the structural damage resulting from risk exposure | 
| STRUCTURAL_DAMAGE_2050_LBD         | FLOAT  | The lower bound value averaged from 2045-2055 for the structural damage resulting from risk exposure |  
| STRUCTURAL_DAMAGE_2050_UBD         | FLOAT  | The upper bound value averaged from 2045-2055 for the structural damage resulting from risk exposure |  
| STRUCTURAL_DAMAGE_2080             | FLOAT  | The value averaged from 2075-2085 for the structural damage resulting from risk exposure | 
| STRUCTURAL_DAMAGE_2080_LBD         | FLOAT  | The lower bound value averaged from 2075-2085 for the structural damage resulting from risk exposure |  
| STRUCTURAL_DAMAGE_2080_UBD         | FLOAT  | The upper bound value averaged from 2075-2085 for the structural damage resulting from risk exposure |  
| BUSINESS_INTERRUPTION_BASELINE     | FLOAT  | The baseline value for the business interruption resulting from risk exposure |
| BUSINESS_INTERRUPTION_BASELINE_LBD | FLOAT  | The lower bound baseline value for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_BASELINE_UBD | FLOAT  | The upper bound baseline value for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2030         | FLOAT  | The value averaged from 2025-2035 for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2030_LBD     | FLOAT  | The lower bound value averaged from 2025-2035 for the business interruption resulting from risk exposure |  
| BUSINESS_INTERRUPTION_2030_UBD     | FLOAT  | The upper bound value averaged from 2025-2035 for the business interruption resulting from risk exposure |  
| BUSINESS_INTERRUPTION_2050         | FLOAT  | The value averaged from 2045-2055 for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2050_LBD     | FLOAT  | The lower bound value averaged from 2045-2055 for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2050_UBD     | FLOAT  | The upper bound value averaged from 2045-2055 for the business interruption resulting from risk exposure |  
| BUSINESS_INTERRUPTION_2080         | FLOAT  | The value averaged from 2075-2085 for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2080_LBD     | FLOAT  | The lower bound value averaged from 2075-2085 for the business interruption resulting from risk exposure | 
| BUSINESS_INTERRUPTION_2080_UBD     | FLOAT  | The upper bound value averaged from 2075-2085 for the business interruption resulting from risk exposure |  

## Scenario Analytics

For more information about individual hazards and climate scenarios, see the [Climate Data Guide](data-guide).


## Example

An example of heat mapping power plants in Idaho is available [here](https://github.com/sustglobal/dev-center/blob/master/jupyter-notebooks/SegmentedDatasetsAnalysis/HeatmappingExample.ipynb).


## Using the Data

You can purchase the data on [Snowflake](https://app.snowflake.com/marketplace/listing/GZ2FQZRVGX1/sust-global-physical-climate-risk).
