---
layout: doc
title: Visual Summary Multimodal Guide
subtitle: The Multimodal feature of Visual Summary enables users to explore datasets that complement Sust Global's core climate risk and financial impact datasets. These complementary datasets span socio-demographic, economic, resilience, biodiversity, and other physical risks. 
date: 2025-05-22
lastmod: 2025-05-22
author: TB
tags:
- dataset
- visual summary
---

## Multimodal Dataset Search

Sust Global’s modeling platform integrates **multimodal data**—a combination of diverse data types from multiple sources—to provide high-resolution, asset-level insights into physical climate risks and financial impacts. This data fusion enables robust, location-specific analysis across hazard types, sectors, and time horizons.

Our [Populous framework](https://www.sustglobal.com/insights/populous-unpacking-the-geospatial-dimension-for-multimodal-insights) ingests a wide array of data — from demographic and economic indicators to detailed climate risk metrics and even signals from a Google-developed foundation model. By combining diverse data sources, we can create models that build a rich, context-aware representation of risk that far surpasses siloed traditional approaches​. 

Here we provide county-level visualization and download access to some of the datasets used in our Populous framework. Many demographic variables listed here are available for specific years, as well as for short-term (1-year) and long-term (decade) changes. Higher resolution versions and additional historical years are available upon request. 

## Data Dictionary

| Dataset                | Units                      | Geographic Coverage | Source                                                                                                                                     |
|------------------------|----------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Insurance Premiums     | USD                        | U.S.                | [Keys and Mulder 2024](https://www.nber.org/system/files/working_papers/w32579/w32579.pdf)                                                 |
| Insurance Nonrenewals  | rate                       | U.S.                | [U.S. Senate Budget Committee](https://www.budget.senate.gov/imo/media/doc/next_to_fall_the_climate-driven_insurance_crisis_is_here__and_getting_worse.pdf) |
| Vacancy Rate           | rate                       | U.S.                | [U.S. Census](https://www.census.gov)                                                                                                                                 |
| Median Income          | USD                        | U.S.                | [U.S. Census](https://www.census.gov)                                                                                                                                 |
| GDP                    | USD                        | U.S.                | [U.S. Bureau of Economic Analysis](https://www.bea.gov)                                                                                                           |
| Population             | count                      | U.S.                | [U.S. Census](https://www.census.gov)                                                                                                                                |
| Commute Time           | minutes                    | U.S.                | [U.S. Census](https://www.census.gov)                                                                                                                                 |
| Poverty Rate           | percent                    | U.S.                | [U.S. Census](https://www.census.gov)                                                                                                                                |
| Biodiversity           | score [0 to 100]           | Global              | [UN Biodiversity Lab](https://unbiodiversitylab.org/en/about/)                                                                                                                       |
| Earthquake             | peak ground acceleration   | Global              | [Global Earthquake Model](https://www.globalquakemodel.org/product/global-seismic-hazard-map)                                                                                                             |
| Hail                   | days/year                  | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov)                                                                                                               |
| Tornadoes              | days/year                  | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov)                                                                                                               |
| Severe Wind            | days/year                  | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov)                                                                                                             |
| Severe Thunderstorms   | days/year                  | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov)                                                                                                               |
| Subsidence             | mm/year                    | Global              | [Davydzenka et al. 2024, Colorado School of Mines](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL104497)                                                                                           |
| Landslide              | annual frequency           | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/)                                                                                                                   |
| Coldwave               | annual frequency           | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/)                                                                                                                   |
| Volcanic Activity      | annual frequency           | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/)                                                                                                                   |
| Tsunami                | annual frequency           | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/)                                                                                                                   |
| Avalanche              | annual frequency           | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/)                                                                                                                   |

## Multimodal Model Integration
We support the development of customized [multimodal modeling workflows](https://www.sustglobal.com/insights/populous-unpacking-the-geospatial-dimension-for-multimodal-insights) tailored to your target variable. These workflows integrate the datasets listed above, our core climate modeling suite, and additional proprietary inputs and model architectures. Contact us to learn more.
