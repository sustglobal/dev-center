---
title: Climate Data Guide - Wildfire
toc: true
permalink: /wildfire.html
---

**Hazard Description**

Wildfire is an uncontrolled fire, caused by a combination of combustible fuels (such as dead, dry wood) and ignition sources (such as human activity or lightning).  It is strongly influenced by prevailing weather conditions, and typically occurs where human activity meets an accumulation of wild fuel along the Wildland Urban Interface (WUI).

## Methodologies
**Unified Wildfire**
This indicator combines the projections from Burned Area Fraction (BAF) and the Keetch-Byram Drought Index Susceptibility Score (KBDI), benchmarked against the observed wildfire indicator to create a measure of wildfire probability at a specific location.  It can be interpreted as the probability of wildfire occurring within one kilometer of an asset location within a given year. 

Unified Wildfire is the recommended default indicator for future fire risk.

**KBDI Susceptibility Score**: This indicator measures wildfire weather, or the probability of wildfire under various weather conditions, using the [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi).  This approach has several advantages for modeling fire dynamics as previously demonstrated.  Weather has been [previously shown](https://iopscience.iop.org/article/10.1088/2515-7620/abd836) to be a major determinant of fire probability, and changing weather patterns are the primary reason wildfires will be a major hazard of climate change. Thus, in contrast to the Burned Area Fraction Indicator, this indicator does not use direct CMIP6 simulations of wildfire occurrence.  Instead, the Wildfire susceptibility estimates future fire risk using simulations of fire weather, combined with millions of historic observations of how weather affects fire risk. 

**Burned Area Fraction**: Starting from CMIP6 model simulations of monthly wildfire burned area -- which incorporate factors such as temperature, precipitation, land cover type, and population to simulate fire occurrence and severity -- we use proprietary artificial intelligence to enhance resolution. These projections are further processed using the latest satellite-derived land cover maps, filtering for the urban-wildland interface to further refine the projections.

**Observational Dataset**: We use satellite derived observations to provide high-resolution exposure to wildfires. The observations are made using NASA MODIS satellites and processed using an active fire algorithm to produce the [MCD64A](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf). This covers the historical period of 2001 to present. This indicator shows the years in which a wildfire occurred within 1 kilometer of an asset.

## Known Limitations
In addition to capturing historic wildfires, the satellite record also includes agricultural and prescribed burning.  This can cause a higher estimate of wildfire risk in areas where these activities are common.

## Sample Assessment
### United States Counties

<p align="center">
<img height="300" src="assets/images/dataguide/wildfire_unified_prob_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual wildfire risk exposure 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| US Counties with top wildfire exposure over 2022-2052 |
| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Idaho | Custer |0.03 | 0.08 |143 |
| California | Colusa | 0.07 |	0.08	|11 |
| California | Glenn | 0.06	|0.07| 15 |
| Deer Lodge | Montana | 0.02 | 0.06 | 	170 |
| Valley | Idaho | 0.03 | 0.05 | 83 |

<hr>

### Indian Towns
<p align="center">
<img height="300" src="assets/images/dataguide/wildfire_unified_prob_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual wildfire risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| Indian Towns with top wildfire exposure over 2022-2052 |
| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | 
| Bastar | 0.15 | 0.08 | -45 |
| Bijapur | 0.12| 0.07| -43 |
| Dantewada | 0.1 | 0.08 | -25 |
| Garhchiroli | 0.15 | 0.08 | -48 |
| Kondagaon | 0.1| 0.07 | -31 |


## Data Sources
- [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)
- [MCD64A Observations](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf)

## References
- [NeurIPS2020 technical reference](https://www.climatechange.ai/papers/neurips2020/45)
- [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi)
