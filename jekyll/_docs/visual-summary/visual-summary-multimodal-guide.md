---
layout: doc
title: Visual Summary Multimodal Guide
subtitle: The Multimodal feature of Visual Summary enables users to explore datasets that complement Sust Global's core climate risk and financial impact datasets. These complementary datasets span socio-demographic, economic, resilience, biodiversity, and other physical risks. 
date: 2025-05-22
lastmod: 2025-05-28
author: TB
tags:
- dataset
- visual summary
---

## Multimodal Dataset Search

Sust Global’s modeling platform integrates *multimodal data*—a combination of diverse data types from multiple sources—to provide high-resolution, asset-level insights into physical climate risks and financial impacts. This data fusion enables robust, location-specific analysis across hazard types, sectors, and time horizons.

Our [Populous framework](https://www.sustglobal.com/insights/populous-unpacking-the-geospatial-dimension-for-multimodal-insights) ingests a wide array of data — from demographic and economic indicators to detailed climate risk metrics and even signals from a Google-developed foundation model. By combining diverse data sources, we can create models that build a rich, context-aware representation of risk that far surpasses siloed traditional approaches​. 

Here we provide **county-level** visualization and download access to some of the datasets used in our Populous framework. Many demographic variables listed here are available for specific years, as well as for short-term (1-year) and long-term (decade) changes. Higher resolution versions and additional historical years are available upon request. 

## Data Dictionary
| Dataset                  | Summary Description | Units                      | Refresh Rate | Geographic Coverage | Source |
|--------------------------|---------------------|----------------------------|--------------|---------------------|--------|
| Population               | total population                    | count                      | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| GDP                      | gross domestic product                    | USD                        | annual       | U.S.                | [U.S. Bureau of Economic Analysis](https://www.bea.gov) |
| Median Income            | median household income                    | USD                        | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Poverty Rate             | percent living below poverty line                    | percent                    | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| College Education        | percent of population with bachelors or higher degree                    | %                          | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Commute Time             | average commute time                    | minutes                    | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Total Housing Units      | total residential units                    | count                      | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Home Construction Year   | median residential construction year                    | year                       | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Vacancy Rate             | residential vacancy rate                    | rate                       | annual       | U.S.                | [U.S. Census](https://www.census.gov) |
| Insurance Premiums       | median residential insurance premium                    | USD                        | annual       | U.S.                | [Keys and Mulder 2024](https://www.nber.org/system/files/working_papers/w32579/w32579.pdf) |
| Insurance Nonrenewals    | residential insurance nonrenewal rate                    | rate                       | annual       | U.S.                | [U.S. Senate Budget Committee](https://www.budget.senate.gov/imo/media/doc/next_to_fall_the_climate-driven_insurance_crisis_is_here__and_getting_worse.pdf) |

| Social Resilience        | resilience based on multiple population attributes                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Economic Resilience      | resilience based on population financial well-being                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Infrastructure Resilience| resilience based on built environment                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Institutional Resilience | resilience based on governance and disaster preparedness                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Community Resilience     | resilience based on social connectivity                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Environmental Resilience | resilience based on natural resources and conditions                    | score [0 to 1]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |
| Total Resilience         | sum of six resilience scores                    | score [0 to 6]             | infrequent       | U.S.                | [Baseline Resilience Indicators for Communities](https://sc.edu/study/colleges_schools/artsandsciences/centers_and_institutes/hvri/data_and_resources/bric/index.php) |

| Biodiversity             |  priority areas for biodiversity conservation                   | score [0 to 100]           | infrequent       | Global              | [UN Biodiversity Lab](https://unbiodiversitylab.org/en/about/) |
| Earthquake              |  seismic risk                   | peak ground acceleration   | static       | Global              | [Global Earthquake Model](https://www.globalquakemodel.org/product/global-seismic-hazard-map) |
| Subsidence              | subsidence rate                    | mm/year                    | infrequent       | Global              | [Davydzenka et al. 2024, Colorado School of Mines](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL104497) |
| Hail                   | days with severe hail risk                   | days/year                  | annual       | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov) |
| Tornadoes              | days with severe (EF1+) tornado risk                    | days/year                  | annual       | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov) |
| Severe Wind            | days with severe (>33m/s) non-hurricane wind risk                   | days/year                  | annual       | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov) |
| Severe Thunderstorms   | days with severe convective storms risk                    | days/year                  | annual       | U.S.                | [NOAA Storm Prediction Center](https://www.spc.noaa.gov) |
| Landslide              | landslide risk                   | annual frequency           | annual       | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/) |
| Coldwave               | consecutive extreme low temperatures risk                    | annual frequency           | annual       | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/) |
| Volcanic Activity      | volcanic risk                    | annual frequency           | annual       | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/) |
| Tsunami                | tsunami risk                    | annual frequency           | annual       | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/) |
| Avalanche              | avalanche risk                    | annual frequency           | annual       | U.S.                | [FEMA National Risk Index](https://hazards.fema.gov/nri/) |


## Multimodal Model Integration
We support the development of customized [multimodal modeling workflows](https://www.sustglobal.com/insights/populous-unpacking-the-geospatial-dimension-for-multimodal-insights) tailored to your target variable. These workflows integrate the datasets listed above, our core climate modeling suite, and additional proprietary inputs and model architectures. Contact us to learn more.
