---
title: Climate Data Guide
toc: true
---

## Introduction
This Data Guide will provide you with an introduction to Sust Global’s data capabilities. We will provide an overview of climate scenarios and our data specification and capabilities. We will introduce you to climate analytics on each of the hazards and show how they can be used to generate business intelligence insights, and also list some measures you can take to adapt and mitigate climate risk.

The world needs validated Climate Analytics. Without data that is consistently validated and objectively true, business decision-making becomes murky, disclosures and reporting become meaningless and managing for the changing climate becomes impossible.

Sust Global's mission is to enable leading businesses with the Climate analytics required to make strategic decisions in our ever-changing world. We take comprehensive measures to ensure data is validated, objectively true, and precise, so you can focus on your work. Sust Global enables users to access asset level,property level or portfolio level Climate Analytics for physical risk assessments across forward-looking time horizons and multiple climate scenarios. 

Our Climate Analytics covers risk from multiple perils: wildfire, flood, cyclone, heatwave, sea level rise and water stress. Through data transformations on ensembles of frontier General Circulation Models (GCMs), asset-level risk exposure is delivered as a time series for each specific asset. Using the latest satellite and sensor observations, we bias-correct the projections from the model ensembles to account for the most recent risk exposure observations. Asset level or regional processing – in conjunction with near real-time observation ingestion with artificial intelligence driven resolution enhancement, served using a scalable cloud-native data platform – allows our users to investigate risk exposure across small or large collections of assets or properties or regions. 

**Data Validation**: For every hazard, we derive asset level exposure data from forward looking indicators based on models from frontier climate science. We benchmark and validate data from these indicators on their hindcast (projections over historic time periods) against observations to qualify the most performant functional models used in our model ensembles.

## Climate Scenarios
Sust Global covers climate scenario analysis following climate scenario definitions set forth from the Intergovernmental Panel for Climate Change - Coupled Model Intercomparison Project-Phase 6 [IPCC CMIP6](https://www.carbonbrief.org/explainer-how-shared-socioeconomic-pathways-explore-future-climate-change/). The IPCC AR6/CMIP6 combines frontier climate science from world leading scientific institutions with realistic climate scenario modeling. The IPCC has finalized the third part of the Sixth Assessment Report, Climate Change 2022: Mitigation of Climate Change on 4 April 2022. Climate scenarios can be thought of as a bundling of working hypotheses on the evolution of human development over the coming years. 

This guide covers the exposure of climate related hazards relating to three distinct climate scenarios:
1. **Strong Mitigation**: This scenario covers the optimal sustainable path, also referred to as the Green Road (SSP1-RCP2.6). It encompasses socioeconomic and representative emissions pathways consistent with a gradual and pervasive global shift towards a more sustainable future. Carbon emissions begin to decline around 2020 and global mean temperatures rise approximately 1.8°C by 2100, a key goal of the Paris Climate Agreement.
2. **Middle of the Road**: This scenario covers a middle path, with challenges to climate mitigation (SSP2-RCP4.5). In this scenario, environmental systems experience degradation, and climate change worsens through the end of the century. In this scenario, overall emissions continue to rise through mid-century before beginning to decline.This is a likely scenario if governments and policy reflect a strong sense of urgency towards climate adaptation. Global mean temperatures rise approximately 2.4°C by 2100, but greater emissions raise the risk of tipping points.
3. **High Emissions**: This scenario covers a future where the world continues on its current trajectory, also referred to as Fossil-Fueled Growth (SSP5-RCP8.5). Global markets are increasingly integrated and both total population and per-capita consumption increase. Emissions peak around 2090 and global mean temperatures rising approximately 4.3°C by 2100.

Sust Global’s data product provides asset level exposure to specific climate related hazards. In the following sections, we will cover descriptions of each of the hazards covered. Climate Explorer, Sust Global’s dashboard product provides asset level exposure insights to specific hazards. These insights are presented as time series, summary heatmaps across a portfolio of assets and sorting of assets based on their exposure to a specific hazard.

## Wildfire

**Description**

Wildfire is an uncontrolled fire, caused by a combination of combustible fuels (such as dead, dry wood) and ignition sources (such as human activity or lightning).  It is strongly influenced by prevailing weather conditions, and typically occurs where human activity meets an accumulation of wild fuel.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/wildfire_unified_prob_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D1: United States Counties, Projected mean annual wildfire risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Idaho | Custer |0.033 | 0.082 |143.75 |
| California | Colusa | 0.073 |	0.081	|11.12 |
| California | Glenn | 0.062	|0.072| 15.89 |
| Deer Lodge | Montana | 0.022 | 0.059 | 	170.14 |
| Valley | Idaho | 0.0296 | 0.054 | 83.2560 |

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
| Bastar | 0.151 | 0.083 | -45.39 |
| Bijapur | 0.126| 0.071| -43.81 |
| Dantewada | 0.1 | 0.075 | -25.25 |
| Garhchiroli | 0.15 | 0.078 | -48.05 |
| Kondagaon | 0.101| 0.07 | -31.06 |

<p>
Table 1B: Indian towns with top wildfire exposure projected over upcoming 30 years
</p>


**Indicators**

We present 4 indicators for wildfire: observed wildfire, burned area fraction, wildfire susceptibility and unified wildfire exposure. 

1. **Observed Wildfire**: We use satellite derived observations to provide asset level exposure to active wildfires. The observations are made using NASA MODIS satellites and processed using an active fire algorithm to produce the [MCD64A](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf). This covers the historical period of 2001 to present. This indicator shows the years in which a wildfire occurred within 1 kilometer of an asset.
2. **Burned Area Fraction**: We represent annual fire risk by ensembling CMIP6 model simulations of monthly wildfire burned area [% of grid cell]. [CMIP6 Wildfire models](https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf) incorporate factors such as temperature, precipitation, land cover type, and population to simulate fire occurrence and the associated area burned. For example, wildfire occurrence includes both lightning and human-induced ignitions, and high temperatures and drought lead to drier fuels and increased likelihood of fire. We use Sust Global's proprietary methodologies for wildfire super resolution ([NeurIPS2020 technical reference](https://www.climatechange.ai/papers/neurips2020/45)) on top of the model ensemble to enable high resolution wildfire projections. These projections are further processed using the latest satellite-derived land cover maps, filtering for the urban-wildland interface to further refine the projections.
3. **Wildfire Susceptibility**: This indicator relates to wildfire weather and the probability of wildfire under various weather conditions using the [Keetch-Byram Drought Index (KBDI)](https://twc.tamu.edu/kbdi).  This approach has several advantages for modeling fire dynamics as previously demonstrated.  Weather has been [previously shown](https://iopscience.iop.org/article/10.1088/2515-7620/abd836) to be a major determinant of fire probability, and changing weather patterns are the primary reason wildfires will be a major hazard of climate change. Thus, in contrast to the Burned Area Fraction Indicator, this indicator does not use direct CMIP6 simulations of wildfire occurrence.  Instead, the Wildfire susceptibility estimates future fire risk using simulations of fire weather, combined with millions of historic observations of how weather affects fire risk. 
4. **Unified wildfire exposure**: This indicator combines the projections from the burned area fraction and the susceptibility score, benchmarked against the observed wildfire indicator to create a unified measure of wildfire probability at a specific location.  It can be interpreted as the probability of wildfire occurring within one kilometer of an asset location within a given year. The unified wildfire indicator when aggregated over a period of time (10 yrs) provides for a measure of probability of wildfire occurrence within 1 kilometer of the asset over the next 10 years. 

Each of the indicators: observed active fires, burned area fraction and the wildfire susceptibility provide a unique view into wildfire exposure. The observed fires demonstrate historic exposure of the asset to past occurrences of wildfire. Burned area fraction provides an indication of potential for exposure of the area around the asset to wildfire and wildfire susceptibility provides an indicator of wildfire probability based on environmental and weather conditions. The unified wildfire exposure indicator brings these indicators together towards a single annualized wildfire probability score. 

The wildfire projections from Sust Global draw on the latest, cutting edge simulations from the climate community of both fire occurrence and fire weather.  We then perform several value-adding steps, including using neural networks for super-resolving our estimates, as well as calibrating our models using millions of observations of historic fire.  We use native-resolution satellite imagery to fit and validate our models, and our unified indicator provides a more accurate multi-model ensemble view of fire risk.  Finally, our models are designed to be accurate globally, as opposed to many products that are restricted to only specific regions.

**Data Usage**

The burned area fraction is most suitable for when assessing wildfire exposure to the asset as well as burnable area in the region around the asset. Wildfire susceptibility is suitable when accounting for near term and long term risk exposure potential. The unified indicator is more suited as a single indicator of wildfire exposure probability.

We have benchmarked wildfire exposure in the Pacific Northwest of the United States to characterize areas of high wildfire risk potential and used the extent of exposure in these wildfire prone land parcels in this region as a reference to benchmark other regions when characterizing them as LOW/MEDIUM/HIGH.

On the Climate Explorer dashboard, we present the unified wildfire exposure indicator for forward looking projections. All indicators are accessible using the API or the CSV datasets available as a zip file through Climate Explorer.

## Inland Flood

**Description**

Inland flooding captures the likelihood of the asset being exposed to flooding from inland storms.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/flood_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D3: United States Counties, Projected mean annual flood risk exposure over 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Panola | Mississippi | 0.0 | 0.081 | N/A |
| Garza | Texas | 0.029 | 0.072 | 141.3|
| Sutter | California | 0.0 | 0.07 | N/A |
| Outagamie | Wisconsin | 0.07 | 0.069 | -1.02|
| Clay | Illinois | 0.043 | 0.064 | 47.619|

<p>
Table 2A: US Counties with top flood exposure projected over upcoming 30 years
</p>

<p align="center">
<img height="500" src="assets/images/dataguide/england_floods_585_2022_2052.png">
</p>

<p align="center">
Fig D4: English Counties, Projected mean annual flood risk exposure over 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | 
| Aberdeen City | 	0.12 | 0.06 | -50.0| 
| Bolton | 0.004 | 0.036 | 800.0| 
| Manchester | 0.003 | 0.032 | 800.0| 
| Essex | 0.0 | 0.029 | N/A| 
| Manchester | 0.0 | 0.022 | N/A| 

<p>
Table 2B: England counties with top flood exposure projected over upcoming 30 years
</p>

**Indicators**

We present two indicators: observed flooding and flood potential
1. **Observed floods**: Indicates whether flood was observed in a given year by satellites at the location of an asset. It is derived from NASA MODIS data, for the period 2012 to present.  
2. **Flood potential**: Indicates the potential flood exposure from 2022 - 2100 expressed as a probability at the asset level. A value of 0.1 indicates that we could expect a flooding event in one of the next 10 years at this asset location.

The output metric we use for inland flooding exposure ranges from 0 (low risk) to 1 (high risk). We derive this index from the collection of many simulations of flood inundated areas. We take into account multiple meteorological variables like precipitation, land surface pressure, humidity and elevation.

We only cover only SSP5-RCP8.5 at the moment in the flood potential indicator.

**Data Usage**

We count the number of years where floods exceed a probability threshold (5% in this case) over the forward looking window (5 yr/15 yr/30 yr) and use that count to categorize the asset to LOW/MED/HIGH. LOW would be values between 0 and 1, MED would be values 2 and 3 and for assets with >3 years of flooding potential exceeding 5% probability, we would set to HIGH.

On Climate Explorer, we count the number of years where floods exceed a probability threshold (5% in this case) over a decade to create a count across each decade for the forward looking time series.

The flood projections are hindcast over the range of 1980-2020 and benchmarked against observations of flooding at a global scale to validate and filter the climate models used in the inland flood projections.

## Tropical Cyclone

**Description**

Tropical cyclones, also referred to as hurricanes and typhoons, are one of the costliest natural disasters fueled by climate change. Since 1980, tropical cyclones in the U.S. have caused $997 billion in damages (NOAA), exceeding damages from all other weather disasters. Cyclone impacts can be widespread, including coastal and inland flooding and wind damage. These damages can directly affect assets as well as critical local infrastructure.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/cyclones_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D5: United States Counties, Projected mean annual cyclone risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>


| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| North Carolina | Dare | 0.317 | 0.302 | -4.36 |
| North Carolina | Hyde | 0.296 | 0.28 | -5.55 |
| North Carolina | Carteret | 0.286 | 0.361 | -8.92 |
| North Carolina | Tyrell | 0.243 | 0.25 | 2.98 |
| North Carolina | Pamilco | 0.27 | 0.247 | -8.35 |

<p>
Table 3A: US Counties with top cyclone exposure over the upcoming 30 years
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/cyclones_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D6: Indian Towns, Projected mean annual cyclone risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>


| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Puri | 0.25 | 0.233 | -6.56 |
| Srikakulam | 0.265 | 0.245 | -7.39 |
| Visakhapatnam | 0.276| 0.257 | -6.92 |
| Vizianagaram | 0.26 | 0.236 | -9.06 |

<p>
Table 3B: Indian Towns with top cyclone exposure over the upcoming 30 years
</p>

**Indicators**

We provide two indicators, one for observed cyclone exposure and another for projected cyclone frequency. 
1. **Observed tropical cyclones**: we use cyclone tracks from the International Best Track Archive for Climate Stewardship (IBTrACS). The IBTrACS archive combines tropical cyclone datasets from global agencies and harmonizes them into a single dataset. It is endorsed by the World Meteorological Organization as the official data source for cyclone track data. For observed tropical cyclones, we filter points to only include Category 3, 4, and 5 storm points. We then assume a constant ‘impact radius’ of 150 miles/ 241km.
2. **Forward looking Cyclone Pojections**: We quantify current and forward-looking cyclone exposure by focusing on the frequency of extreme tropical cyclones. Extreme tropical cyclones, referred to as Category 3, 4, and 5 storms on the Saffir-Simpson hurricane scale, are defined as having maximum sustained winds above 110mph/178km/h. We focus on these extreme storms because of their heightened destructive potential relative to weaker storms. Since the number represents a frequency, it indicates the expected number of CAT3/4/5 cyclones over a year. By aggregating the values over a time range of 15 years, the user can arrive at a projected number of cyclones exposed to the asset over the 15 year window.  

For forward-looking cyclone exposure, Sust Global combines the latest CMIP6-based cyclone track simulations with our proprietary bias-correction methodology to enable more accurate assessment of local exposure. The CMIP6 cyclone tracks are unique because they are based on high-resolution simulations specifically designed to enable more reliable assessment of climate risk from weather phenomena like tropical cyclones. These simulations are only achievable due to recent advancements in supercomputing power.  

The CMIP6-based cyclone track simulations are drawn from research led by Dr. Malcolm Roberts of the UK Met Office ([technical reference](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020GL088662)). The simulations are based on CMIP6 HighResMIP simulations with resolutions as high as 25km. The CMIP6 HighResMIP project is co-chaired by Roberts. The authors applied two different cyclone track algorithms to determine when an input set of CMIP6 oceanic and atmospheric conditions over time and space constitutes a high likelihood of a tropical cyclone track.

**Data Usage**

We have identified three regions for model evaluation known to have high historical exposure to extreme cyclones: the Gulf of Mexico, South Asia, and China. We have used these regions to benchmark and calibrate risk exposure to the different categories of HIGH, MEDIUM and LOW

For forward looking cyclone exposure, our methodology translates these storm track points into geospatial polygons indicative of cyclone exposure. When determining asset exposure, we assume an ‘impact radius’ of 150 miles (241km) from the cyclone center to better capture coastal and inland flooding exposure. The simulations are only available for SSP5-8.5 to 2050.

## Sea Level Rise

**Description**

This hazard refers to rising sea levels. The major physical impacts of a rise in sea level include erosion of beaches, inundation of deltas as well as flooding and loss of many marshes and wetlands.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/SLR_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D7: United States Counties, Projected mean annual sea level rise risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| New Jersey| 0.158 | 0.284 | 78.77 |
| Pennsylvania| 0.131 | 0.283 | 116.83 |
| Delaware| 0.158 | 0.283 | 79.11 |
| Virginia| 0.159 | 0.283 | 77.88 |
| Maryland| 0.159 | 0.283 | 78.11 |


<p>
Table 4A: US States with top sea level rise exposure over the upcoming 30 years
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/SLR_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D8: Indian towns, Projected mean annual wildfire risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Baleshwar| 0.186 | 0.216 | 15.92 |
| Bhadrak| 0.186 | 0.216 | 15.92 |
| Jagatsinghapur| 0.183 | 0.212 | 15.93 |
| Kendrapara| 0.186 | 0.216 | 15.92 |
| North 24 Parganas| 0.189 | 0.22 | 16.84 |

<p>
Table 4B: Indian towns with top sea level rise exposure over the upcoming 30 years
</p>

**Indicator**

The sea level rise indicator refers to the change in sea level from the changing climate across different climate scenarios. We base our modeling of projected sea level rise on both climate model simulations and an asset’s distance to the coast. Projected sea level rise from CMIP6 climate models incorporates the effects of thermal expansion from warming of the ocean, since water expands as it warms, which is expected to be the primary component of future sea level rise. The models do not incorporate the secondary contributions of melting glaciers and ice caps since they cannot reliably simulate them, so the sea level simulations are conservative estimates of total sea level rise. The sea level rise is calculated by combining the monthly CMIP6 local sea level fluctuations due to ocean dynamics and global sea level rise from thermal expansion. We center the sea level rise over the baseline period 1980-2010. 

We enable asset level assessments of exposure to physical hazard from sea level rise. We express sea level rise relative to a 1980-2010 baseline period for assets within 5km from the coast. An asset’s distance to the nearest coastline is derived using 0.01 degree resolution, satellite-derived estimates of coastline locations from NASA’s Ocean Color Group. Assets beyond 5km from the nearest coastline are assumed to have no sea level risk in our assessments, though we can change this 5km threshold if needed. Technically the coastline product is at 0.04 degree resolution, but the providers converted it to 0.01 degree using bilinear interpolation and say the uncertainty is up to 1km

The models do not incorporate the secondary contributions of melting glaciers and ice caps since they cannot reliably simulate them, so the sea level simulations are conservative estimates of total sea level rise.

## Water Stress

**Description**

Water is a requirement for societal development and progress. Water availability, or in its absence water scarcity, plays a critical role across sectors, including manufacturing, mining, agriculture, and electricity generation. Climate change coupled with increasing demand will have substantial impacts on water availability across the globe. Rigorous, high resolution water supply and demand data is therefore needed to enable reliable assessment of companies’ water scarcity exposure directly and throughout their supply chains. Projections of future water availability can help companies and investors prepare for the complex economic and social challenges related to water stress.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/water_stress_unified_score_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D9: United States Counties, Projected mean annual water stress risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| California | Imperial | 0.527 | 0.577 | 9.6 |
| Arizona | Yuma | 0.496 | 0.556 | 11.53 |
| California | San Diego | 0.531 | 0.549 | 3.51 |
| California | Riverside | 0.532 | 0.548 | 2.97 |
| California | Orange | 0.527 | 0.538 | 2.12 |

<p>
Table 5A: US Counties with top water stress exposure
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/water_stress_unified_score_australia_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D10: Australian Towns, Projected mean annual water stress risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| Township | Locale | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| South Australia | Playford| 0.344 | 0.642 | 86.43 |
| South Australia | Prospect | 0.275 | 0.641 | 132.71 |
| Victoria | Gannawarra | 0.302 | 0.641 | 112.23 |
| New South Wales | Jerilderie | 0.302 | 0.638 | 86.14 |
| South Australia | Marion | 0.539 | 0.638 | 18.27 |


<p>
Table 5B: Australian towns with top water stress exposure over the upcoming 30 years
</p>

**Indicators**

We provide 4 indicators: historic water stress, projected droughts, projected water stress score, projected unified water stress.

1. **Water stress score indicator**: We model current and forward-looking water stress scores using the World Resource Institute’s Aqueduct model. The state-of-the-art Aqueduct model has been extensively used by researchers in academia and industry to assess portfolio water risk. The water stress score is indicative of competition for local water resources. It is calculated as the ratio of water withdrawal to renewable water availability.
2. **Drought indicator**: This indicator is based on a drought index derived from CMIP6 monthly simulations of precipitation and temperature. The drought index, also referred to as the standardized precipitation evapotranspiration index, represents the magnitude of precipitation deficits (negative magnitude) or surplus (positive magnitude) over the preceding 12-month period, after accounting for temperature-driven effects on evapotranspiration. Our selection of a 12-month period reflects long-term precipitation patterns and better relates to reservoirs, groundwater, and streamflow.  
3. **Unified water stress indicator**: This indicator combines the water stress score and the drought indicator to one single indicator for water stress, using a weighted mean, with weights derived from the methodology designed by the World Resources Institute in their [Global Aqueduct Methodology](https://doi.org/10.46830/writn.18.00146) (Page 35, Table 3). This provides a comparable 0.0 to 1.0 range to indicate exposure to water stress.
4. **Historic water stress indicator**: We use the same methodology as the unified water stress indicator, except with observed rather than modeled datasets of water stress and drought.

Water stress scores account for the availability and consumption of water at the specific location. The drought indicator accounts for environmental variables that create acute water shortage over a period of time. Both are chronic physical climate hazard indicators.

Our water stress indicator is based on the world leading WRI water stress methodology ([link](https://www.wri.org/data/aqueduct-global-maps-30-data)) and our drought indicator is based on the latest frontier climate research from the CMIP6([link](https://link.springer.com/article/10.1007/s00382-017-3740-8)). 

**Data Usage**

A key avenue for mitigating water stress not considered in the modeling framework is the transport of water between watersheds. Such transport can help meet water demand, but it comes at a cost. Transporting water requires large amounts of energy, increasing greenhouse gas emissions, along with the development of transportation infrastructure. Water transport also carries with it a host of geopolitical and equity considerations. 

- Water stress scores are more suitable for use for assessments of impact from the changing climate to human water needs
- Drought indicator is most useful for water stress impacts to agriculture and commodities 
- The unified water stress indicator is most useful across generic use cases

## Heatwave

**Description**

Heatwaves represent an extended period of perilously warm weather at a specific location or region.

**Sample Assessment**

<p align="center">
<img height="300" src="assets/images/dataguide/heatwaves_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D11: United States Counties, Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>


| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Florida | Miami-Dade | 0.69 | 38.12 | 449.83 |
| Idaho | Cassia | 7.88 | 34.18 | 333.29 |
| Utah | Summit | 8.107 | 34.13 | 325.86 |
| Utah | Morgan | 8.1 | 34.083 | 320.78 |
| Utah | Box Elder | 8.04 | 33.72 | 318.96 |

<p>
Table 6A: US Counties with top heatwave exposure
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/heatwaves_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D12: Indian towns, Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>

| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Jaipur | 7.85 | 21.3 | 171.59 |
| Lakshwadeep | 8.2 | 90.8 | 997.28 |
| Nagpur | 7.85 | 21.51 | 174.1 |
| Sikar | 7.8 | 21.2 | 173.07 |
| Tonk | 7.8 | 21.65 | 178.3 |

<p>
Table 6B: Indian cities/towns with top heatwave exposure
</p>

**Indicator**

We calculate the number of days per year exceeding a temperature threshold. The temperature threshold at a given location is based on the 98th percentile of daily conditions during a baseline period between 1980 and 2100. Because this temperature threshold varies spatially, the heatwave metric indicates anomalously high temperatures relative to what is typical at the local level. 

**Data Usage**

The heatwave indicator is derived from the world’s frontier climate research as part of the CMIP6. The user can interpret this metric at a specific asset location or region as the number of days in a calendar year of unusually warm weather

## Fundamental Variables

**Description**

These fundamental indicators represent fundamental climate variables aggregated annually at a specific location or region across different scenarios from 1980 to 2100.

**Indicators**

We present 3 fundamental indicators:

1. **Annual Temperature**: This fundamental indicator represents mean daily temperature for a given year. 
2. **Annual Precipitation**: This fundamental indicator represents total precipitation, including rain and rain-equivalent snowfall, for a given year. 
3. **Extreme Precipitation**: This fundamental indicator represents the number of days in a given year where precipitation exceeds 2 inches (50.8mm). 

**Data Usage**
The fundamental indicators are derived from the world’s frontier climate research as part of the CMIP6. The user can interpret this metric as a measure of fundamental climate. 

## Summarization Labeling

| Hazard | Unit | LOW Range (low) | LOW Range (high) | MEDIUM Range (low) | MEDIM Range (high) | HIGH Range (low) | HIGH Range (high) |  
| - | - | - | - | - | - |  - | - | 
| Wildfire | Probability | 0.0 | 0.01 | 0.01 | 0.05 | 0.05 | 1.0 |
| Inland Flood | Number of years with probability exceeding threshold @@ | 0 | 0 | 1 | 3 | 3 | 30 |
| Cyclone | Probability | 0.0 | 0.1 | 0.1 | 0.2 | 0.2 | 1.0 |
| Water Stress | Score | 0.0 | 0.3 | 0.3 | 0.6 | 0.6 | 1.0 |
| Heatwave | Number of days in year | 0 | 30 | 30 | 50 | 50 | 366 |
| Sea Level Rise | Relative change in meters | 0.0 | 0.1 | 0.1 | 0.3 | 0.3 | 3.0 |

<p>
Table 7: Hazard summarization labeling ranges 
</p>

@@ For floods, we count the number of years where floods exceed a probability threshold (5% in this case) over the forward looking window (5 yr/15 yr/30 yr) and use that count to categorize the asset to LOW/MED/HIGH. LOW would be values between 0 and 1, MED would be values 2 and 3 and for assets with >3 years of flooding potential exceeding 5% probability, we would set to HIGH

## Indicator Metadata

| hazard    |  indicator    |  unit   |   value_min  |  value_max  |  value_norm  |  spatial_resolution (in meters) |
| - | - | - | - | - |- |- |
| wildfire | obs_score | score | 0.0 | 1.0 | 1.0 | 500.0 |
| wildfire | burned_area_norm   | score | 0.0 | 1.0 | 0.1 | 300.0 |
| wildfire | fire_kbdi_susceptability | score | 0.0 | 1.0 | 0.1 | 300.0 |
| wildfire | unified_prob | probability | 0.0 | 1.0 | 0.5 | 300.0 |
| flood_potential | obs_score | score | 0.0 | 1.0 | 1.0 | 250.0 |
| flood_potential | inland_flood_prob | probability | 0.0 | 1.0 |  1.0 | 4000.0 |
| cyclone | obs_freq | frequency | 0.0 | 7.0 | 2.0 | 1000.0 |
| cyclone | prob  | probability | 0.0 | 1.0 | 0.5 | 50000.0 |
| heatwave | freq | day | 0.0 | 366.0 | 200.0 | 25000.0 |
| sea_level_rise | change | meter | 0.0 | 100.0 | 0.75 | 100000.0 |
| water_stress | obs_score | score | 0.0 | 1.0 | 1.0 | 500.0 |
| water_stress | spei_norm | score |  0.0 |  1.0 |  1.0 |  25000.0 |
| water_stress | score | score | 0.0 | 1.0 | 1.0 | 500.0 |
| water_stress | unified_score | score | 0.0 | 1.0 | 1.0 | 500.0 |
| fundamental | temp | degree_celsius | -60.0 | 50.0 | 50.0 | 100000.0 |
| fundamental | precip | millimeter | 0.0 | 10000.0 | 10000.0 | 100000.0 |
| fundamental | extreme_precip | day | 0.0 | 366.0 | 366.0 | 100000.0 |

<p>
Table 8: Hazard and indicator metadata 
</p>

## Regional statistics using polygon processing

Processing of large area geographies into climate risk scores requires statistical reductions, such as taking the average risk over the area in question.  The table below details the reductions used at Sust Global to arrive at regional risk.

By default, geospatial polygons are reduced by a mean statistic.  The following exceptions are noted below:

| hazard    |  spatial statistic |
| - | - |
| Wildfire | mean |
| Inland Flood | weighted mean^^ |
| Cyclone | max^ |
| Water Stress | mean |
| Heatwave | mean |
| Sea Level Rise | max |

<p>
Table 9: spatial statistics for polygon aggregation 
</p>

^ For cyclones, the maximum value across a region corresponds to a cyclone striking anywhere in that region.  Similarly for sea level rise, a maximum value over a region corresponds to the maximum sea level rise experienced in that region.

^^ Waterstress scores are derived from the WRI Aqueduct product, based on administrative areas and watersheds.  A weighted average is appropriate for reducing regions which intersect multiple differing regions.





