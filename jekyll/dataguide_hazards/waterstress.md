---
title: Climate Data Guide - Water Stress
toc: true
permalink: /waterstress.html
---

**Hazard Description**

Water is a requirement for societal development and progress, and its availability plays a critical role across a wide variety of activities.  This includes food security, human health, electricity generation, manufacturing and mining. Changing water availability due to climate change, coupled with increasing demand from population growth and economic activity, will have substantial impacts across the globe. Rigorous, high resolution water supply and demand data is therefore needed to enable assessment of water risk exposure, both directly and throughout supply chains. Projections of future water availability can help companies and investors prepare for the complex economic and social challenges related to water stress.

## Methodologies
**Unified Water Stress** 
This indicator combines the water stress score and the drought indicator to one single indicator for water stress, using a weighted mean, with weights derived from the methodology designed by the World Resources Institute in their [Global Aqueduct Methodology](https://doi.org/10.46830/writn.18.00146) (Page 35, Table 3). This provides a comparable 0.0 to 1.0 range to indicate exposure to water stress.

Unified Water Stress is the recommended default indicator for future water stress risk.

**Aqueduct Water Stress Score**: The World Resource Institute’s <i>Aqueduct</i> models future water stress risk. This state-of-the-art model has been extensively used by researchers in academia and industry to assess portfolio water risk. The water stress score is calculated as the ratio of water withdrawal to renewable water availability, and is indicative of competition for local water resources. 

**SPEI Drought**: Standardized Precipitation Evapotranspiration Index (SPEI) is a drought index base on precipitation and temperature.  Our product applied this index to NASA's Global Downscaled Daily Projections [GDDP](https://www.nasa.gov/nex/gddp). SPEI represents the magnitude of precipitation deficits or surplus over the preceding 12-month period, after accounting for temperature-driven effects on evapotranspiration. 

**Historic Water Stress**
We use the same methodology as the unified water stress indicator, except with observed rather than modeled datasets of water stress and drought.

## Known Limitations
...
Unified Water Stress does not have a tangible interpretation, in the same way that other metrics do (probability, heatwave days, m SLR).
Our modeling framework does not account for water transport between watersheds, which helps to meet demand in dry regions at the cost of transportation.

## Sample Assessment
### United State Counties

<p align="center">
<img height="300" src="assets/images/dataguide/water_stress_unified_score_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual water stress risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| US Counties with top waterstress exposure over 2022-2052 |
| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Arizona | Yuma | 0.56 | 0.91 | 63 |
| California | Imperial | 0.57 | 0.89 | 55 |
| Arizona | La Paz | 0.37 | 0.84 | 126 |
| Washington | Grant | 0.43 | 0.81 | 86 |
| Arizona | Maricopa | 0.55 | 0.79 | 42 |

<hr>

### Australian Towns
<p align="center">
<img height="300" src="assets/images/dataguide/water_stress_unified_score_australia_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual water stress risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| Australian Towns with top water stres risk over 2022-2052 |
| State | Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Western Australia | Wanneroo | 0.54 | 0.74 | 39 |
| Western Australia | Joondalup | 0.55 | 0.74 | 36 |
| Western Australia | Cockburn | 0.35 | 0.73 | 110 |
| Western Australia | Bayswater | 0.34 | 0.73 | 114 |
| Western Australia | Cambridge | 0.48 | 0.73 | 54 |


**Data Sources**
- [Aqueduct](https://www.wri.org/data/aqueduct-global-maps-30-data)
- [NASA Global Downscaled Daily Projections - GDDP](https://www.nasa.gov/nex/gddp) 

**References**
- [Global Aqueduct Methodology](https://doi.org/10.46830/writn.18.00146) (Page 35, Table 3)
- [SPEI](https://link.springer.com/article/10.1007/s00382-017-3740-8)
