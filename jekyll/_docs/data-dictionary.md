---
layout: doc
title: Annualized Data Dictionary
subtitle: This document provides users with an introduction to Sust Global’s annualized data.
date: 2024-06-05
lastmod: 2024-06-06
author: TA
tags:
- data
- yearly
---

## About the Data

The Sust Global Annualized US dataset provides county, zip code, and census tract level physical risk exposure scores and financial impact metrics to help risk management and risk reporting teams across financial and sustainability organizations assess the impact of climate change on their portfolios, operational assets and supply chains.

The dataset covers six major climate hazards over two scenarios and four time periods for the United States.

- Projections from advanced climate physical hazard modeling leveraging CMIP6 climate models, Regional risk zoning, space derived observational datasets and proprietary AI powered modeling techniques, and covering two future climate change scenarios: Medium (SSP2-RCP4.5) and High (SSP5-RCP8.5) physical climate risk metrics across baseline, 2025-2035, 2045-2055 and 2075-2085.
- County, zip code, and census tract level physical risk scores and labels reflecting exposure to climate hazards across scenarios and time periods.
- County, zip code, and census tract level financial impact metrics reflecting the value of financial impacts
and losses from structural damage projected due to changing climate hazard exposure for a given asset within the zip code, expressed as a percentage of the asset value (% metric).
- County, zip code, and census tract level financial impact metrics reflecting the value of financial impacts
and losses from business interruption projected due to changing climate hazard exposure for a given asset within the zip code, expressed as a percentage of the number of days in a year (% metric).
- Uncertainty bounds representing lower bound and upper bound for financial impact metrics for structural damage and business interruption.
- Six (6) physical climate hazards covered are Coastal and Inland Flooding, Wildfire, Tropical Cyclone, Heatwaves, Water Stress and Sea level Rise.

## Data Dictionary

| Name | Type | Description |
| ---- | ---- | ----------- |
| ID | STRING | Identifier (is not unique across datasets) |
| LAT | STRING | Latitude |
| LNG | STRING | Longitude |
| ADMIN_PROCESSING_LEVEL | STRING | The admin boundary level to which this dataset corresponds (2,3,4) |
| ADMIN0 | STRING | 3 Letter Country Code |
| ADMIN1 | STRING | Admin 1 boundary name |
| ADMIN2 | STRING | Admin 2 boundary ID |
| ADMIN3 | STRING | Admin 3 boundary ID (if applicable) |
| ADMIN4 | STRING | Admin 4 boundary ID (if applicable) |
| SCENARIO ANALYTICS | OBJ | Contains the climate scenarios ssp245 and ssp585. Each scenario contains hazards wildfire, cyclone, flood, heatwave, water stress and sea level rise. For each hazard, data is windowed for baseline, 2030, 2050, and 2080. In turn the ubd (upper bound) and lbd (lower bound) values indicate the uncertainty for each window. (Special note on heatwave indicator and business interruption: values are normalized by 365 to give them in percents rather than days) |

## Scenario Analytics

For more information about individual hazards and climate scenarios, see the [Climate Data Guide](data-guide).
