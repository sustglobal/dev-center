---
layout: doc
title: Heatwaves
subtitle: Heatwaves represent an extended period of perilously warm weather at a specific location or region. They are associated with excess mortality and other human health risks, greatly increased electricity demand, agricultural impacts, and disruption to many types of economic activity. 
date: 2023-01-01
lastmod: 2023-08-20
author: TB
tags:
- data
- heat
- heatwave
---

## Methodologies
**Future Heatwave Days** 

Metric: Total days in a given year exceeding the historic 98th percentile for temperature.

This indicator utilizes NASA Global Downscaled Daily Projections ([GDDP](https://www.nasa.gov/nex/gddp)) to estimate the number of days exceeding the historic 98th percentile of annual temperatures at an asset location. This temperature threshold varies spatially, based on the 98th percentile of a given location during the years 1980 to 2010. As such, the heatwave metric indicates anomalously high temperatures relative to each location's historical temperature distribution. 

**Observed Heatwave Days** 
This indicator presents the same heatwave metric as the future heatwave product but instead is based on observed temperature data from the European Centre for Medium-Range Weather Forecasts's ERA5-Land datasets. 

## Known Limitations
- There are many ways to define a heatwave, based on intensity, duration, and potentially other factors. Our indicator uses a 98th percentile intensity, and a 1 day duration, which is appropriate for most use cases.  
- SSP1 is currently not available from the underlying data product, and our product is using SSP2 in place of SSP1 (SSP2 is duplicated in this product).


## Sample Assessment
### United States Counties

<p align="center">
<img height="500" src="assets/images/dataguide/heatwaves_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>

| US Counties with top cyclone exposure over 2022-2052 |
| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Florida | Miami-Dade | 0.69 | 38.12 | 450 |
| Idaho | Cassia | 7.88 | 34.18 | 333 |
| Utah | Summit | 8.11 | 34.13 | 326 |
| Utah | Morgan | 8.1 | 34.08 | 321 |
| Utah | Box Elder | 8.04 | 33.72 | 319 |

<hr>

### Indian Towns
<p align="center">
<img height="500" src="assets/images/dataguide/heatwaves_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>

| Indian Towns with top heatwave exposure over 2022-2052 |
| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Jaipur | 7.85 | 21.3 | 172 |
| Lakshwadeep | 8.2 | 90.8 | 997 |
| Nagpur | 7.85 | 21.51 | 174|
| Sikar | 7.8 | 21.2 | 173 |
| Tonk | 7.8 | 21.65 | 178 |

## Data Sources
- [NASA Global Downscaled Daily Projections - GDDP](https://www.nasa.gov/nex/gddp) 
