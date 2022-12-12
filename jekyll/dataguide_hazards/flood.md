---
title: Climate Data Guide - Floods
toc: true
permalink: /flood.html
---

**Hazard Description**

Flooding captures the likelihood of a location being directly exposed to flooding, both from precipitation-based inland flooding and from coastal flooding.  Flooding is among the deadlier natural disasters and poses direct risks to human health, infrastructure, and economic activity.

## Methodologies

**Flood potential**

Indicates the potential flood exposure from 2022 - 2100 expressed as a probability at the asset level. A value of 0.1 indicates that there is a 10% chance of flooding at any depth at that location.

The output metric we use for inland flooding exposure ranges from 0 (low risk) to 1 (high risk). We derive this index from the collection of many simulations of flood inundated areas. We take into account multiple meteorological variables like precipitation, land surface pressure, humidity and elevation.

We only cover only SSP5-RCP8.5 at the moment in the flood potential indicator.

## Known Limitations
Floods are difficult to observe by satelite, due primarily to cloud cover.  No historic flood database is comprehensive, even for recent years in the satelite period.

## Sample Assessment
### United States Counties

<p align="center">
<img height="300" src="assets/images/dataguide/flood_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual flood risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| US Counties with top flood exposure over 2022-2052 |
| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Panola | Mississippi | 0.0 | 0.08 | N/A |
| Garza | Texas | 0.03 | 0.07 | 141|
| Sutter | California | 0.0 | 0.07 | N/A |
| Outagamie | Wisconsin | 0.07 | 0.07 | -1|
| Clay | Illinois | 0.04 | 0.06 | 47|

### English Counties
<p align="center">
<img height="500" src="assets/images/dataguide/england_floods_585_2022_2052.png">
</p>

<p align="center">
Projected mean annual flood risk exposure over over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| England Counties with top cyclone exposure over 2022-2052 |
| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | 
| Aberdeen City | 	0.12 | 0.06 | -50| 
| Bolton | 0.0 | 0.04 | 800| 
| Manchester | 0.0 | 0.03 | 800| 
| Essex | 0.0 | 0.03 | N/A| 
| Manchester | 0.0 | 0.02 | N/A| 


## Data Sources
- [Aqueduct](https://www.wri.org/data/aqueduct-global-maps-30-data)
- [NASA Global Downscaled Daily Projections - GDDP](https://www.nasa.gov/nex/gddp) 

## References
- [Global Aqueduct Methodology](https://doi.org/10.46830/writn.18.00146) (Page 35, Table 3)
- [SPEI](https://link.springer.com/article/10.1007/s00382-017-3740-8)
