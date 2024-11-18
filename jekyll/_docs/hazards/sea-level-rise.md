---
layout: doc
title: Sea Level Rise
subtitle: Global mean sea level increased by approximately 20cm in the past century, with 1 meter or more of rise expected by 2100. The major physical impacts of rising seas include coastal flooding, erosion of beaches, saltwater intrusion into aquifers, inundation of deltas, and loss of biodiversity in marshes and wetlands.
date: 2023-01-01
lastmod: 2023-08-21
author: TB
tags:
- data
- sea
- sea level
- SLR
---

## Methodology
**Future Sea Level Rise** 

Metric: Expected Sea Level Rise in meters from historic baseline sea levels, within 5km of an asset location.

This indicator quantifies the change in sea level across different climate scenarios and is consistent with projections from the IPCC Sixth Assessment Report. We base our modeling of projected sea level rise on climate model simulations from [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6). 

Projected sea level rise from CMIP6 climate models incorporates the effects of thermal expansion from warming of the ocean, melting of Greenland and Antarctic ice sheets, melting of glaciers and ice caps, and local land subsidence and rebound. Land elevation rebound, whereby land elevation increases in response to ice melt, is more common in high latitude, polar regions.  

This indicator reflects sea level rise relative to a 1995-2014 baseline period for assets within 5km from the coast. An asset’s distance to the nearest coastline is derived using 0.01 degree resolution, satellite-derived estimates of coastline locations from NASA’s [Ocean Color Group](https://oceancolor.gsfc.nasa.gov/docs/distfromcoast/).

**Observed Sea Level Rise**
This indicator reflects observed sea level changes based on satellite data from NASA's Jet Propulsion Lab. A 24-month rolling average is used to reduce high-frequency variability. The satellite data tracks sea surface height anomalies from a collection of different satellite sensors. This product has global coverage (-80 to 80 latitude) from 1993 to present. The data does not incorporate local land subsidence or rebound. 

## Known Limitations
The <i>Sea Level Rise</i> indicator shows the largest sea level rise experienced within 5km of an asset. This is in contrast to coastal flood products, which show flooding at an exact asset location. 

## Sample Assessment
### United States Counties
<p align="center">
<img height="220" src="assets/images/dataguide/SLR_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual sea level rise risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| US Counties with top sea level rise exposure over 2022-2052 |
| State | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| New Jersey| 0.16 | 0.28 | 79 |
| Pennsylvania| 0.13 | 0.28 | 117 |
| Delaware| 0.16 | 0.28 | 79 |
| Virginia| 0.16 | 0.28 | 78 |
| Maryland| 0.16 | 0.28 | 78 |

<hr>

### Indian Towns

<p align="center">
<img height="300" src="assets/images/dataguide/SLR_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual sea level rise risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| Indian Towns with top sea level rise exposure over 2022-2052 |
| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Baleshwar| 0.19 | 0.23 | 16 |
| Bhadrak| 0.19 | 0.23 | 16 |
| Jagatsinghapur| 0.18 | 0.22 | 16 |
| Kendrapara| 0.19 | 0.22 | 16 |
| North 24 Parganas| 0.19 | 0.22 | 17 |


## Data Sources
- [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)
- [Ocean Color Group](https://oceancolor.gsfc.nasa.gov/docs/distfromcoast/)
