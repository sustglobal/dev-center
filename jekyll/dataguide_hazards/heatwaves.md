---
title: Climate Data Guide - Heatwaves
toc: true
permalink: /heatwaves.html
---

**Hazard Description**

Heatwaves represent an extended period of perilously warm weather at a specific location or region. They are associated with excess mortality and other human health risks, greatly increased electricity demand, agricultural impacts, and disruption to many types of economic activity. 

## Methodologies
**Heatwave Days per Year** 
This indicator uses NASA Global Downscaled Daily Projections ([GDDP](https://www.nasa.gov/nex/gddp)) to estimate the number of days exceeding the historic 98th percentile of annual temperatures. This temperature threshold varies spatially, based on the 98th percentile of a given location.  As such, the heatwave metric indicates anomalously high temperatures relative to what was locally typical in the past. 

## Risk Scoring
Where did we benchmark heatwave days per year?

## Known Limitations
There are many ways to define a heatwave, based on intensity, duration, and potentially other factors. Our indicator uses a 98th percentile intensity, and a 1 day duration, which is appropriate for most use cases.  

**Sample Assessment**

<p align="center">
<img height="500" src="assets/images/dataguide/heatwaves_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D11: United States Counties, Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>


| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| Florida | Miami-Dade | 0.69 | 38.12 | 450 |
| Idaho | Cassia | 7.88 | 34.18 | 333 |
| Utah | Summit | 8.11 | 34.13 | 326 |
| Utah | Morgan | 8.1 | 34.08 | 321 |
| Utah | Box Elder | 8.04 | 33.72 | 319 |

<p>
Table 6A: US Counties with top heatwave exposure
</p>

<p align="center">
<img height="500" src="assets/images/dataguide/heatwaves_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Fig D12: Indian towns, Projected mean annual heatwaves risk exposure over 2022-2052 with the SSP5-RCP8.5 scenario.
</p>

| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Jaipur | 7.85 | 21.3 | 172 |
| Lakshwadeep | 8.2 | 90.8 | 997 |
| Nagpur | 7.85 | 21.51 | 174|
| Sikar | 7.8 | 21.2 | 173 |
| Tonk | 7.8 | 21.65 | 178 |

<p>
Table 6B: Indian cities/towns with top heatwave exposure
</p>

**Data Sources**
- [NASA Global Downscaled Daily Projections - GDDP](https://www.nasa.gov/nex/gddp) 

**References**
- [Global Aqueduct Methodology](https://doi.org/10.46830/writn.18.00146) (Page 35, Table 3)
- [SPEI](https://link.springer.com/article/10.1007/s00382-017-3740-8)


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