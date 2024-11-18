---
layout: doc
title: Nature Data User Guide
subtitle: Sust Global's Nature API is a RESTful API interface to Sust Global's durability (non-permanence) indicators for nature based carbon projects. This guide helps users understand the indicators and datasets accessible using the API.
date: 2023-11-17
lastmod: 2024-03-05
author: GE
tags:
- dataset
- quickstart
---

## About the Data Guide 

Sust Global enables users to access durability risks to nature based carbon projects across multiple perils on historic and forward-looking time horizons. We take comprehensive measures to ensure data is validated and precise, so users can make climate-informed durability assessments.

Sust Global's durability analytics enable users to evaluate **Forest Carbon** and **Blue Carbon** projects. In the following sections, we provide the summary descriptions for each of the durability indicators for these project types. We list several scientific references on context regarding the relevance of these indicators to carbon sequestration potential for each of these project types.

### Forest Carbon Indicators

The following indicators, are derived as a summary score through a spatial average over the specified project area.

1. **wildfire_observed_baseline_mean**: Observed wildire risk expsure as a percentage fraction over the 2000-2022 window for validation and benchmarking performance. 
2. **wildfire_ssp585_baseline_mean**: Projected wildfire risk expsure probablity over the 2000-2022 window. This indicator is useful for validation and benchmarking performance against observations. 
3. **wildfire_ssp585_2050_mean**: Projected wildfire risk expsure probablity over the 2040-2070 window.
4. **wildfire_carbon_loss_baseline_mean**: Projected carbon loss on exposure to a wildfire as a fraction of present day biomass estimated as an average over the  2000-2020 window for validation and benchmarking performance.
5. **water_balance_ssp585_2050_mean**: Projected net water balance over the 2022-2072 window.
6. **pest_disease_baseline_mean**: Outlining mean projected pest and disease risk as a probablity of incidence. 
7. **seismic_baseline_mean**: Outlining mean projected siesmic risk exposure as a probablity of incidence. 

### Blue Carbon Indicators

The following indicators, are derived as a summary score through a spatial average over the specified project area.

1. **cyclone_ssp585_baseline_mean**: Projected cyclone risk expsure probablity of a CAT1+ cyclone over the 2000-2020 window for validation and benchmarking performance. 
2. **cyclone_ssp585_2050_mean**: Projected cyclone risk expsure probablity of a CAT1+ cyclone over the 2040-2070 window.  
3. **cyclone_observed_baseline_mean**: Observed cyclone risk exposure of a CAT1+ cyclone over Jan 2010 to Jan 2023.
4. **extreme_precip_ssp585_baseline_mean**: Projected extreme precipitation over the 2000-2020 window for validation and benchmarking performance. 
5. **extreme_precip_ssp585_2050_mean**: Projected extreme precipitation over the 2040-2070. 
6. **sea_level_rise_ssp585_baseline_mean**: Projected sea level rise over the 2000-2020 window for validation and benchmarking performance. 
7. **sea_level_rise_ssp585_2050_mean**: Projected sea level rise over the 2040-2070 window.
8. **pest_disease_baseline_mean**: Outlining mean projected pest and disease risk as a probablity of incidence. 
9. **seismic_baseline_mean**: Outlining mean projected siesmic risk exposure as a probablity of incidence.  

## References

1. T. Ballard, et al, Widespread increases in future wildfire risk to global forest carbon offset projects revealed by explainable AI, ICLR 2023, [link](https://www.climatechange.ai/papers/iclr2023/33).
2. M. Cooper, Predicting Wildfire Risk Under Novel 21st-Century Climate Conditions, AAAI 2022, [link](https://www.climatechange.ai/papers/aaaifss2022/15).
3. F. Giuseppe, et al, Combining fire radiative power observations with the fire weather index improves the estimation of fire emissions, Atmos. Chem. Phys. Discuss. 2018, [link](https://doi.org/10.5194/acp-2017-790).
4. R. Early, et al, Global threats from invasive alien species in the twenty-first century and national response capacities, Nature Communications 2016 [link](https://www.nature.com/articles/ncomms12485).
5. The Global Earthquake Model (GEM) Global Seismic Hazard Map (version 2018.1), [link](https://www.globalquakemodel.org/gem-maps/global-earthquake-hazard-map).
6. A. John, Quantifying CMIP6 model uncertainties in extreme precipitation projections, Weather and Climate Extremes, 2022, [link](https://www.sciencedirect.com/science/article/pii/S2212094722000238).
7. N Bloemendaal, et al, Generation of a global synthetic tropical cyclone hazard dataset using STORM, Scientific Data 2020, [link](https://www.nature.com/articles/s41597-020-0381-2).
8. R. Hofste, et al, Aqueduct 3.0: Updated Decision-Relevant Global Water Risk Indicators, 2019 [link](https://www.wri.org/research/aqueduct-30-updated-decision-relevant-global-water-risk-indicators)
9. Hermans et al, Projecting Global Mean Sea-Level Change Using CMIP6 Models, GRL, 2021, [link](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020GL092064).
10. Lovelock et al, The vulnerability of Indo-Pacific mangrove forests to sea-level rise, Nature, 2015 [link](https://www.nature.com/articles/nature15538).
11. Imbert, D. Hurricane disturbance and forest dynamics in east Caribbean mangroves, Ecosphere, 2018 [link](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecs2.2231).
12. Hou, J., Yuan, Y, Li, T. and Ren, Z. Tsunami hazard analysis for Chinese coast from potential earthquakes in the western North Pacific, Geomatics, 2020, [link](https://www.tandfonline.com/doi/pdf/10.1080/19475705.2020.1766579).

## Citing Sust Global API

From a concept to adoption by an emerging group of early adopters, many people have invested time and energy in developing and enabling access to Sust Global's capabilities. Please cite Sust Global when using our data and insights. To cite Sust Global's data in publications, please use the following:

```
Sust Inc (2021). Sust Global Application Programming Interface: Transforming frontier climate science to actionable data. https://developers.sustglobal.com.
```

```
@Misc{,
  author       = {Sust Global Team},
  organization = {Sust Inc},
  title        = {Sust Global Application Programming Interface: Transforming frontier climate science to actionable data},
  year         = {2021--},
  url          = "https://developers.sustglobal.com"
}
```
