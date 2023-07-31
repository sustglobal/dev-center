---
title: Climate Data Guide
toc: true
---

## About the Data Guide
Sust Global enables users to access physical risk data across multiple perils and forward-looking time horizons. We take comprehensive measures to ensure data is validated and precise, so users can make climate-informed decisions. 

This document provides users with an introduction to Sust Global’s data capabilities. This includes an overview of climate modeling and scenario development, and how to use our hazard and indicator data to derive intelligence and insights.

Our Climate Analytics covers risk from multiple perils: 
- [Wildfire](./wildfire.html)
- [Flood](./flood.html)
- [Cyclones](./cyclones.html)
- [Heatwave](./heatwaves.html)
- [Sea Level Rise (SLR)](./sea_level_rise.html)
- [Water Stress](./waterstress.html) 

We also include expected financial loss information from the above physical perils, via our [Financial Risk Analysis](./var.html) methodology.

We do this by integrating General Circulation Models (GCMs) from the latest international modeling efforts (CMIP6) with high-resolution historic observations from satelites and sensors, using the latest machine-learning and artificial intelligence methods. This allows us to deliver spatial resolution that is orders of magnitudes finer than GCMs alone. Analysis sites can be supplied in the form of either points or regions/polygons, and risk exposure is delivered as a time series for each specific asset. 

**Data Validation**: For every hazard, we derive asset level exposure data from forward looking indicators based on models from frontier climate science. We benchmark and validate data from these indicators on their hindcast (projections over historic time periods) against observations to qualify the most performant functional models used in our model ensembles.

## Climate Scenarios
To model future climate change, some assumptions about society are needed - particularly, the quantity of planet-warming greenhouse gases that will be emitted over the coming decades.  There are established conventions for this, known as "Shared Socioeconomic Pathways", or SSPs, that are used to standardize this assumption across models.  These climate scenarios can be thought of as a bundling of working hypotheses on the evolution of human development over the coming years. For an overview of climate scenario definitions, as set forth by the Intergovernmental Panel for Climate Change (IPCC), see this article [Carbon Brief](https://www.carbonbrief.org/explainer-how-shared-socioeconomic-pathways-explore-future-climate-change/). 

Sust Global's data covers three of the most representative scenarios from the IPCC: 
1. **Strong Mitigation (SSP1)**: SSP1 covers the optimal sustainable path, also referred to as the Green Road (SSP1-RCP2.6). It encompasses socioeconomic and representative emissions pathways consistent with a sustained and pervasive global shift towards a more sustainable future. Carbon emissions begin to decline around 2020 and global mean temperatures rise approximately 1.8°C by 2100, a key goal of the Paris Climate Agreement.
2. **Middle of the Road (SSP2)**: SSP2 covers a middle path, with challenges to climate mitigation (SSP2-RCP4.5). In this scenario, In this scenario, overall emissions continue to rise through mid-century before beginning to decline, environmental systems experience severe degradation, and climate change worsens through the end of the century. This is widely considered the likely scenario if governments and policy reflect a strong sense of urgency towards climate adaptation. Global mean temperatures rise approximately 2.4°C by 2100, but greater emissions raise the risk of tipping points.
3. **High Emissions (SSP5)**: SSP5 reflects a future where the world continues on its current trajectory, also referred to as Fossil-Fueled Growth (SSP5-RCP8.5). In this scenario, both total population and per-capita consumption increase. Emissions peak around 2090 and global mean temperatures rising approximately 4.3°C by 2100.

Sust Global currently draws on a wide range of public and private scientific datasets, which may not perfectly represent the SSPs listed above.  In cases where not all of the above SSPs are available, we use our best judgement at supplying the appropriate data.  The following substitutions currently apply to our use of SSPs:
- **Floods**: SSP1 is currently not available from the underlying data product, and our product is using SSP2 in place of SSP1 (SSP2 is duplicated in this product).
- **Waterstress**: SSP1 is currently not available from the underlying data product, and our product is using SSP2 in place of SSP1 (SSP2 is duplicated in this product).
- **Heatwaves**: SSP1 is currently not available from the underlying data product, and our product is using SSP2 in place of SSP1 (SSP2 is duplicated in this product).
- **Cyclones**: SSP1 and SSP2 are currently not available from the underlying data product, and our product is using SSP5 in place of SSP1/2 (SSP5 is duplicated in this product).

## Data Bounds and Model Uncertainty
Climate change is a fundamentally uncertain phenomena.  This is why CMIP6 uses an entire suite of different models, created by different institutions around the world, with a wide variety of designs and modeling strategies.  We supply uncertainty data in the form of upper and lower bounds for all hazards and projects, which represent projections from outlier models. 

With the exception of cyclones, we supply the 84th and 16th percentile, approximately ±2 standard deviation.  For cyclones, we supply ±1 standard deviation.

## Fundamental Variables

**Description**

In addition to physical hazards products, Sust Global supplies fundamental indicators for fundamental climate variables aggregated annually across different scenarios from 1980 to 2100.

1. **Annual Temperature**: Mean annual daily temperature. 
2. **Annual Precipitation**: Total annual precipitation, including rain and rain-equivalent snowfall. 
3. **Extreme Precipitation**: Number of days in a given year where precipitation exceeds 2 inches (50.8mm). 



## Summarization Labeling

To create summarization labels we analyze a representative sample of global points, and define breakpoints that best represent the overall risk distribution.  Summarization labels are calculated based on the maximum risk over the 2023-2052 period, and bucketed using the following values:

| Hazard                        | Unit                                           | Low Range      | Medium Range    | High Range |
| -                             | -                                              | -              | -               | -          |
| Wildfire                      | Probability                                    | 0.0 - 0.000075 | 0.000075 - 0.01 | 0.01 - 1.0 |
| Inland Flood                  | Probability                                    | 0.0 - 0.01     | 0.01 - 0.05     | 0.05 - 1.0 |
| Cyclone                       | Probability                                    | 0.0 - 0.01     | 0.01 - 0.05     | 0.05 - 1.0 |
| Water Stress                  | Score                                          | 0.0 - 0.3      | 0.3 - 0.6       | 0.6 -  1.0 |
| Heatwave                      | Number of days in year                         | 0 - 30         | 30 - 50         | 50 - 366   |
| Sea Level Rise                | Relative change in meters                      | 0.0 - 0.375    | 0.375 - 0.75    | 0.75 - 3.0 |
| Financial Risk Analysis (VaR) | Annualized Percent of Value at Risk (0 to 1.0) | 0.0 - 0.01     | 0.01 - 0.05     | 0.05 - 1.0 |

<p>
<b>Table 1</b>: Hazard summarization labeling ranges 
</p>



## Indicator Metadata

| hazard          | indicator                | unit           | value_min | value_max | value_norm | spatial_resolution (in meters) |
| -               | -                        | -              | -         | -         | -          | -                              |
| wildfire        | obs_score                | score          | 0.0       | 1.0       | 1.0        | 500.0                          |
| wildfire        | unified_prob             | probability    | 0.0       | 1.0       | 0.5        | 300.0                          |
| flood_potential | obs_score                | score          | 0.0       | 1.0       | 1.0        | 250.0                          |
| flood_potential | inland_flood_prob        | probability    | 0.0       | 1.0       | 0.5        | 1000.0                         |
| cyclone         | obs_freq                 | frequency      | 0.0       | 7.0       | 2.0        | 1000.0                         |
| cyclone         | prob                     | probability    | 0.0       | 1.0       | 0.5        | 10000.0                        |
| heatwave        | obs_freq                 | day            | 0.0       | 366.0     | 200.0      | 10000.0                        |
| heatwave        | freq                     | day            | 0.0       | 366.0     | 200.0      | 25000.0                        |
| sea_level_rise  | obs_change               | meter          | -2.0      | 2.0       | 1.0        | 18500.0                        |
| sea_level_rise  | change                   | meter          | 0.0       | 100.0     | 1.0        | 100000.0                       |
| water_stress    | obs_score                | score          | 0.0       | 1.0       | 1.0        | 500.0                          |
| water_stress    | spei_norm                | score          | 0.0       | 1.0       | 1.0        | 25000.0                        |
| water_stress    | score                    | score          | 0.0       | 1.0       | 1.0        | 500.0                          |
| water_stress    | unified_score            | score          | 0.0       | 1.0       | 1.0        | 500.0                          |
| fundamental     | temp                     | degree_celsius | -60.0     | 50.0      | 50.0       | 100000.0                       |
| fundamental     | precip                   | millimeter     | 0.0       | 10000.0   | 10000.0    | 100000.0                       |
| fundamental     | extreme_precip           | day            | 0.0       | 366.0     | 366.0      | 100000.0                       |

<p>
<b>Table 2</b>: Hazard and indicator metadata 
</p>



## Regional statistics using polygon processing

Processing of large area geographies into climate risk scores requires statistical reductions, such as taking the average risk over the area in question.  The table below details the reductions used at Sust Global to arrive at regional risk.

By default, geospatial polygons are reduced by a mean statistic.  The following exceptions are noted below:

| hazard         | spatial statistic |
| -              | -                 |
| Wildfire       | mean              |
| Cyclone        | max^              |
| Inland Flood   | mean              |
| Water Stress   | weighted mean^^   |
| Heatwave       | mean              |
| Sea Level Rise | max^               |

<p>
<b>Table 3</b>: spatial statistics for polygon aggregation 
</p>

- <i>^ For cyclones, using the maximum value across a region corresponds to a cyclone striking anywhere in that region.  Similarly for sea level rise, a maximum value over a region corresponds to the maximum sea level rise experienced in that region.</i>
- <i>^^ Waterstress scores are derived from the WRI Aqueduct product, based on administrative areas and watersheds.  A weighted average is appropriate for reducing regions which intersect multiple differing regions.</i>


