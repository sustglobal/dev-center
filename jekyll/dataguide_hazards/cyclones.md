---
title: Climate Data Guide - Cyclones
toc: true
permalink: /cyclones.html
---

**Hazard Description**

Tropical cyclones, also referred to as hurricanes and typhoons, are one of the costliest natural disasters. Since 1980, tropical cyclones in the U.S. have caused $997 billion in damages (NOAA), exceeding damages from all other weather disasters. Cyclone impacts can be widespread, including coastal and inland flooding and wind damage. These damages can affect livelihoods, assets, critical infrastructure, and economic activity.

## Methodologies
**Future Cyclone Projections** 

We quantify current and forward-looking cyclone exposure by focusing on the probability of cyclones. This value represents the expected number of cyclones over a year, of any intensity. 

For forward-looking cyclone exposure, Sust Global combines the latest CMIP6-based cyclone track simulations with our proprietary bias-correction methodology to enable more accurate assessment of local exposure. The CMIP6 cyclone tracks are unique because they are based on high-resolution simulations specifically designed to enable more reliable assessment of climate risk from weather phenomena like tropical cyclones. These simulations are only achievable due to recent advancements in supercomputing power.  

The CMIP6-based cyclone track simulations are drawn from research led by Dr. Malcolm Roberts of the UK Met Office ([technical reference](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020GL088662)). The simulations are based on CMIP6 HighResMIP simulations with resolutions as high as 25km. The CMIP6 HighResMIP project is co-chaired by Roberts. The authors applied two different cyclone track algorithms to determine when an input set of CMIP6 oceanic and atmospheric conditions over time and space constitutes a high likelihood of a tropical cyclone track.

**Observed tropical cyclones**

We use cyclone tracks from the International Best Track Archive for Climate Stewardship ([IBTrACS](https://www.ncei.noaa.gov/products/international-best-track-archive)). The IBTrACS archive combines tropical cyclone datasets from global agencies and harmonizes them into a single dataset. It is endorsed by the World Meteorological Organization as the official data source for cyclone track data. For observed tropical cyclones, we filter points to only include Category 3, 4, and 5 storm points. We then assume a constant ‘impact radius’ of 150 miles/ 241km.

## Known Limitations
Future cyclones, particularly the impact of climate change on frequency and intensity, is uncertain.  This is a very active area of research in the climate resilience community. For more information, see this [Atlantic article](https://www.theatlantic.com/science/archive/2022/09/climate-change-impact-hurricane-ian/671604/?utm_medium=email&_hsmi=2&_hsenc=p2ANqtz-90aWgEMe64CvrUI9IdvZw4nDF2AgK90jY4P-xHHeVouG1KBG-KSXRPTRb24d_9r3-3INFei7HCbHhKm3NffMPc_E9xDw3r5S-tHcPrg_8z2gmmo4U&utm_content=2&utm_source=hs_email) on the state of cyclone science. 

## Sample Assessments
### United States Counties

<p align="center">
<img height="250" src="assets/images/dataguide/cyclones_usa_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual cyclone risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| US Counties with top cyclone exposure over 2022-2052 |
| State | County Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - | - |
| North Carolina | Dare | 0.31 | 0.3 | -4 |
| North Carolina | Hyde | 0.29 | 0.28 | -6 |
| North Carolina | Carteret | 0.28 | 0.36 | -9 |
| North Carolina | Tyrell | 0.24 | 0.25 | 3 |
| North Carolina | Pamilco | 0.27 | 0.25 | -8 |

<hr>

### Indian Towns

<p align="center">
<img height="300" src="assets/images/dataguide/cyclones_india_1980_2020_v_2022-2052.png">
</p>

<p align="center">
Projected mean annual cyclone risk exposure over 1980-2010 (left) and 2022-2052 (right) with SSP5-RCP8.5 scenario.
</p>

| Indian Towns with top cyclone exposure over 2022-2052 |
| Region Name | Score (1980-2020) | Score (2022-2052) | Percent Change | 
| - | - | - | - |
| Puri | 0.25 | 0.23 | -7 |
| Srikakulam | 0.27 | 0.25 | -7 |
| Visakhapatnam | 0.28| 0.26 | -7 |
| Vizianagaram | 0.26 | 0.24 | -9 |

## Data Sources
- [Future Cyclones, HighRes-MIP]([technical reference](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020GL088662))
- [IBTrACS](https://www.ncei.noaa.gov/products/international-best-track-archive)

## References
- [The Atlantic -  Honestly? The Link Between Climate Change and Hurricanes Is Complicated](https://www.theatlantic.com/science/archive/2022/09/climate-change-impact-hurricane-ian/671604/?utm_medium=email&_hsmi=2&_hsenc=p2ANqtz-90aWgEMe64CvrUI9IdvZw4nDF2AgK90jY4P-xHHeVouG1KBG-KSXRPTRb24d_9r3-3INFei7HCbHhKm3NffMPc_E9xDw3r5S-tHcPrg_8z2gmmo4U&utm_content=2&utm_source=hs_email)
- [Future Cyclone Science](https://www.c2es.org/content/hurricanes-and-climate-change/?utm_medium=email&_hsmi=2&_hsenc=p2ANqtz-_NS-tc51pVP_ZsIZIdzAF746tfTIJ48PGKJ2JbNw4i5MqVZTn9XhhDZXlN83CYjA-eBMDLykl8YZW5CfyD1XPYDp2y2L5xCMTG7OUgoUVvOga6SKg&utm_content=2&utm_source=hs_email)
