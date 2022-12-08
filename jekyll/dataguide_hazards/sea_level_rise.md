---
title: Climate Data Guide - Sea Level Rise
toc: true
permalink: /sea_level_rise.html
---

**Hazard Description**

Global mean sea level increased by approximately 20cm in the past century, with 1 meter or more of rise expected by 2100. The major physical impacts of rising seas include coastal flooding, erosion of beaches, saltwater intrusion into aquifers, inundation of fertile deltas, and loss of biodiversity in marshes and wetlands.

## Methodology
**Sea Level Rise** 

Our <i>Sea Level Rise</i> indicator refers to the change in sea level across different climate scenarios and is consistent with projections from the IPCC Sixth Assessment Report. We base our modeling of projected sea level rise on both climate model simulations from [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6). 

Projected sea level rise from CMIP6 climate models incorporates the effects of thermal expansion from warming of the ocean, melting of Greenland and Antarctic ice sheets, melting of glaciers and ice caps, and local land subsidence and rebound. Land elevation rebound, whereby land elevation increases in response to ice melt, is more common in high latitude, polar regions.  

We express sea level rise relative to a 1995-2014 baseline period for assets within 5km from the coast. An asset’s distance to the nearest coastline is derived using 0.01 degree resolution, satellite-derived estimates of coastline locations from NASA’s [Ocean Color Group](https://oceancolor.gsfc.nasa.gov/docs/distfromcoast/).

## Known Limitations
The <i>Sea Level Rise</i> indicator shows the largest sea level rise experienced within 5km of an asset.  This is in contrast to coastal flood products, which show flooding at an exact asset location.

**Sample Assessment**

<p align="center">
<img height="220" src="assets/images/dataguide/SLR_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D7: United States Counties, Projected mean annual sea level rise risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| New Jersey| 0.16 | 0.28 | 79 |
| Pennsylvania| 0.13 | 0.28 | 117 |
| Delaware| 0.16 | 0.28 | 79 |
| Virginia| 0.16 | 0.28 | 78 |
| Maryland| 0.16 | 0.28 | 78 |

<p>
Table 4A: US States with top sea level rise exposure over the upcoming 30 years
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/SLR_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D8: Indian towns, Projected mean annual sea level rise risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Baleshwar| 0.19 | 0.23 | 16 |
| Bhadrak| 0.19 | 0.23 | 16 |
| Jagatsinghapur| 0.18 | 0.22 | 16 |
| Kendrapara| 0.19 | 0.22 | 16 |
| North 24 Parganas| 0.19 | 0.22 | 17 |

<p>
Table 4B: Indian towns with top sea level rise exposure over the upcoming 30 years
</p>

**Data Sources**
- [CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)
- [Ocean Color Group](https://oceancolor.gsfc.nasa.gov/docs/distfromcoast/)

**References**
- 


<hr>
<hr>
Old stuff
<hr>
<hr>

**Indicators**
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
| Arizona | Yuma | 0.56 | 0.91 | 63 |
| California | Imperial | 0.57 | 0.89 | 55 |
| Arizona | La Paz | 0.37 | 0.84 | 126 |
| Washington | Grant | 0.43 | 0.81 | 86 |
| Arizona | Maricopa | 0.55 | 0.79 | 42 |


<p>
Table 5A: US Counties with top water stress exposure
</p>

<p align="center">
<img height="300" src="assets/images/dataguide/water_stress_unified_score_australia_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D10: Australian Towns, Projected mean annual water stress risk exposure over 1980-2010 and 2022-2052 with SSP5-RCP8.5 scenario.
</p>

| State | Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Western Australia | Wanneroo | 0.54 | 0.74 | 39 |
| Western Australia | Joondalup | 0.55 | 0.74 | 36 |
| Western Australia | Cockburn | 0.35 | 0.73 | 110 |
| Western Australia | Bayswater | 0.34 | 0.73 | 114 |
| Western Australia | Cambridge | 0.48 | 0.73 | 54 |


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