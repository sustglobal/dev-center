---
title: Climate Data Guide - Wildfire
toc: true
permalink: /wildfire.html
---

**Hazard Description**

Wildfire is an uncontrolled fire, caused by a combination of combustible fuels (such as dead, dry wood) and ignition sources (such as human activity or lightning).  It is strongly influenced by prevailing weather conditions, and typically occurs where human activity meets an accumulation of wild fuel along the Wildland Urban Interface (WUI).

## Methodologies
**Unified Wildfire**
This indicator combines the projections from Burned Area Fraction (BAF) and the KBDI Susceptibility Score (KBDI), benchmarked against the observed wildfire indicator to create a measure of wildfire probability at a specific location.  It can be interpreted as the probability of wildfire occurring within one kilometer of an asset location within a given year. 

Unified Wildfire is the recommended default indicator for future fire risk.

**KBDI Susceptibility Score**: This indicator measures wildfire weather, or the probability of wildfire under various weather conditions, using the [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi).  This approach has several advantages for modeling fire dynamics as previously demonstrated.  Weather has been [previously shown](https://iopscience.iop.org/article/10.1088/2515-7620/abd836) to be a major determinant of fire probability, and changing weather patterns are the primary reason wildfires will be a major hazard of climate change. Thus, in contrast to the Burned Area Fraction Indicator, this indicator does not use direct CMIP6 simulations of wildfire occurrence.  Instead, the Wildfire susceptibility estimates future fire risk using simulations of fire weather, combined with millions of historic observations of how weather affects fire risk. 

**Burned Area Fraction**: Starting from CMIP6 model simulations of monthly wildfire burned area -- which incorporate factors such as temperature, precipitation, land cover type, and population to simulate fire occurrence and severity -- we use proprietary artificial intelligence to enhance resolution. These projections are further processed using the latest satellite-derived land cover maps, filtering for the urban-wildland interface to further refine the projections.

**Observational Dataset**: We use satellite derived observations to provide high-resolution exposure to wildfires. The observations are made using NASA MODIS satellites and processed using an active fire algorithm to produce the [MCD64A](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf). This covers the historical period of 2001 to present. This indicator shows the years in which a wildfire occurred within 1 kilometer of an asset.

## Risk Scoring
We have benchmarked wildfire exposure in the Pacific Northwest of the United States to characterize areas of high wildfire risk potential and used the extent of exposure in these wildfire prone land parcels in this region as a reference to benchmark other regions when characterizing them as LOW/MEDIUM/HIGH.

## Known Limitations
In addition to capturing historic wildfires, the satellite record also includes agricultural and prescribed burning.  This can cause a higher estimate of wildfire risk in areas where these activities are common.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/wildfire_unified_prob_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D1: United States Counties, Projected mean annual wildfire risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Idaho | Custer |0.03 | 0.08 |143 |
| California | Colusa | 0.07 |	0.08	|11 |
| California | Glenn | 0.06	|0.07| 15 |
| Deer Lodge | Montana | 0.02 | 0.06 | 	170 |
| Valley | Idaho | 0.03 | 0.05 | 83 |

<p>
Table 1A: US Counties with top wildfire exposure projected over upcoming 30 years
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/wildfire_unified_prob_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D2: Indian towns, projected mean annual wildfire risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | 
| Bastar | 0.15 | 0.08 | -45 |
| Bijapur | 0.12| 0.07| -43 |
| Dantewada | 0.1 | 0.08 | -25 |
| Garhchiroli | 0.15 | 0.08 | -48 |
| Kondagaon | 0.1| 0.07 | -31 |

<p>
Table 1B: Indian towns with top wildfire exposure projected over upcoming 30 years
</p>

**Data Sources**
- [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)
- [MCD64A Observations](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf)

**References**
- [NeurIPS2020 technical reference](https://www.climatechange.ai/papers/neurips2020/45)
- [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi)


<hr>
<hr>
Old stuff
<hr>
<hr>

**Indicators**

We present 4 indicators for wildfire: observed wildfire, burned area fraction, wildfire susceptibility and unified wildfire exposure. 

1. **Observed Wildfire**: We use satellite derived observations to provide asset level exposure to active wildfires. The observations are made using NASA MODIS satellites and processed using an active fire algorithm to produce the [MCD64A](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf). This covers the historical period of 2001 to present. This indicator shows the years in which a wildfire occurred within 1 kilometer of an asset.
2. **Burned Area Fraction**: We represent annual fire risk by ensembling CMIP6 model simulations of monthly wildfire burned area [% of grid cell]. [CMIP6 Wildfire models](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf) incorporate factors such as temperature, precipitation, land cover type, and population to simulate fire occurrence and the associated area burned. For example, wildfire occurrence includes both lightning and human-induced ignitions, and high temperatures and drought lead to drier fuels and increased likelihood of fire. We use Sust Global's proprietary methodologies for wildfire super resolution ([NeurIPS2020 technical reference](https://www.climatechange.ai/papers/neurips2020/45)) on top of the model ensemble to enable high resolution wildfire projections. These projections are further processed using the latest satellite-derived land cover maps, filtering for the urban-wildland interface to further refine the projections.
3. **Wildfire Susceptibility**: This indicator relates to wildfire weather and the probability of wildfire under various weather conditions using the [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi).  This approach has several advantages for modeling fire dynamics as previously demonstrated.  Weather has been [previously shown](https://iopscience.iop.org/article/10.1088/2515-7620/abd836) to be a major determinant of fire probability, and changing weather patterns are the primary reason wildfires will be a major hazard of climate change. Thus, in contrast to the Burned Area Fraction Indicator, this indicator does not use direct CMIP6 simulations of wildfire occurrence.  Instead, the Wildfire susceptibility estimates future fire risk using simulations of fire weather, combined with millions of historic observations of how weather affects fire risk. 
4. **Unified wildfire exposure**: This indicator combines the projections from the burned area fraction and the susceptibility score, benchmarked against the observed wildfire indicator to create a unified measure of wildfire probability at a specific location.  It can be interpreted as the probability of wildfire occurring within one kilometer of an asset location within a given year. The unified wildfire indicator when aggregated over a period of time (10 yrs) provides for a measure of average annual probability of wildfire occurrence within 1 kilometer of the asset over the next 10 years. 

Each of the indicators: observed active fires, burned area fraction and the wildfire susceptibility provide a unique view into wildfire exposure. The observed fires demonstrate historic exposure of the asset to past occurrences of wildfire. Burned area fraction provides an indication of potential for exposure of the area around the asset to wildfire and wildfire susceptibility provides an indicator of wildfire probability based on environmental and weather conditions. The unified wildfire exposure indicator brings these indicators together towards a single annualized wildfire probability score. 

The wildfire projections from Sust Global draw on the latest, cutting edge simulations from the climate community of both fire occurrence and fire weather.  We then perform several value-adding steps, including using neural networks for super-resolving our estimates, as well as calibrating our models using millions of observations of historic fire.  We use native-resolution satellite imagery to fit and validate our models, and our unified indicator provides a more accurate multi-model ensemble view of fire risk.  Finally, our models are designed to be accurate globally, as opposed to many products that are restricted to only specific regions.

**Data Usage**

The burned area fraction is most suitable for when assessing wildfire exposure to the asset as well as burnable area in the region around the asset. Wildfire susceptibility is suitable when accounting for near term and long term risk exposure potential. The unified indicator is more suited as a single indicator of wildfire exposure probability.

We have benchmarked wildfire exposure in the Pacific Northwest of the United States to characterize areas of high wildfire risk potential and used the extent of exposure in these wildfire prone land parcels in this region as a reference to benchmark other regions when characterizing them as LOW/MEDIUM/HIGH.

On the Climate Explorer dashboard, we present the unified wildfire exposure indicator for forward looking projections. All indicators are accessible using the API or the CSV datasets available as a zip file through Climate Explorer.
