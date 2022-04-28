---
title: Climate Explorer Quickstart Guide
toc: true
---

Climate Explorer is available at [https://explorer.sustglobal.io](https://explorer.sustglobal.io).
This UI enables Sust Global customers to manage their physical asset portfolios and gain insights regarding climate risk exposure.

Developers are encouraged to integrate with Climate Explorer through the API.
Please read the [Climate Explorer API Guide](./api.html) to learn about these capabilities.

Climate Explorer is currently in beta and will be generally available in mid 2022.
If you do not yet have a Climate Explorer account, please contact [sales@sustglobal.com](mailto:sales@sustglobal.com).

# Introductory Video

Welcome to Climate Explorer - this video will provide a walkthrough of how to upload your assets, autogenerate the risk exposure report and populate a dashboard with the results of that analysis. We will then go over how to derive climate scenario analysis outcomes from the dashboard view for your analysis, assessment and reporting needs.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q1OsUfyojMk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>


# Climate Scenarios

This tool covers the following three distinct climate scenarios:

1. **Strong Mitigation:** This scenario covers the optimal sustainable path, also referred to as the Green Road (SSP1-RCP2.6). It encompasses socioeconomics and representative emissions pathways for a graduate and pervasive global shift towards a more sustainable future.

2. **Middle of the Road:** This scenario covers a middle path, with challenges to climate mitigation (SSP2-RCP4.5). In this scenario, environmental systems experience degradation, and although there are some improvements. overall the intensity of resource and energy use declines. This is a likely scenario if governments and policy reflect a strong sense of urgency towards climate adaptation.

3. **High Emissions:** This scenario covers a future where the world continues on its current trajectory (SSP5-RCP8.5). There is continued reliance on competitive markets to produce rapid technological progress. Global markets are increasingly integrated.

# Projects in Climate Explorer

As a user of Climate Explorer, you can manage collections of physical assets as "portfolios", each of which can be represented as a CSV file. Projects act as logical groupings of portfolios, and users are assigned permissions at the scope of a project: either `viewer` (read only) or `editor` (ability to create new portfolios). As a user, you will typically have access to multiple projects. For example, Sust Global will provide you with viewer access to a demo project containing demo portfolios, as well as editor access to one or more projects where you can create your own portfolios.

# Create New Portfolios

To create a new portfolio go to the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer and click on the button labelled `New Portfolio`. When creating a new portfolio, make sure that the name has no gaps in it. Having given the portfolio a name, you can upload information on the phyical assets.

An example of a portfolio CSV file can be found in the Developer Center: [demo portfolio](https://raw.githubusercontent.com/sustglobal/dev-center/master/resources/example_portfolio.csv). This demo portfolio is a useful starting point if you are  interested in building their own portfolio for use in Climate Explorer, whether via UI or API. Simply save the link to the demo portfolio as a CSV file and edit it before `uploading assets` on the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer.

Each of the supported fields in the portfolio CSV file are documented below:

| Field Name | Description |
| - | - |
| `lat`           | **Required.** Latitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 90 to +90 degrees, at least 2 decimal places
| `lng`           | **Required.** Longitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 180 to +180 degrees, at least 2 decimal places
| `entity_id`     | **Optional.** Meaningful identifier of asset, typically used to map into external systems.
| `entity_name`   | **Optional.** Name of the asset in the portfolio, could also be text string on the name of a city or location
| `label:type`    | **Optional.** Type indicator for the asset. This could be a city or a company name or type of mine
| `label:address` | **Optional.** Address of the asset.
| `label:price`   | **Optional.** Value in USD of asset.
| `label:<KEY>`   | **Optional.** Additional labels (any column header prefixed with `label:`) are preserved in the results, and are not meaningful to Climate Explorer.

Note that the geocodes (lat/lng coordinates) of all the physical assets in your portfolio are required. If you only have addresses and not the geocodes, you can use the [Mapbox Geocoding Playground](https://docs.mapbox.com/playground/geocoding/) to secure geocodes for a specific address. Alternately, you can also secure the geocodes from [Google Maps](https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop).
Please note that portfolios are currently limited to 5000 assets in size. Additionally account level portfolio size limits might apply. Please contact [sales@sustglobal.com](mailto:sales@sustglobal.com) if you would like to increase your portfolio size limits.

# Interpret results

As a user of Climate Explorer, you can download physical risk exposure projection results on their portfolio. Once you have created a new portfolio and uploaded assets, wait for the status to update to `Risk data available`. Once data is available, you can bulk download the risk exposure dataset as a zip file using `Download Risk Exposure` option. You can also switch over to the [Dashboard View](https://explorer.sustglobal.io/), select the specific portfolio you created and view the results on the interactive dashboard.

## Historic Reporting Outcomes

All reports are generated at a monthly cadence based on observations and historic catalogs covering the months from Jan 2010 to Dec 2020. Some of our datasets allow for
higher cadence reporting, please contact us for custom requests.

## Forward Looking Reporting Outcomes

All reports and supported risk projections are at annual cadence. Some of our datasets allow for higher cadence reporting, please contact us for custom requests.

For creating standard heatmaps, we assess the physical risk over the 30 year window between 2021 and 2050 and look at the maximum risk exposure to a specific hazard for an asset. We use the maximum risk exposure value to color code the asset to LOW (Green), MEDIUM (Yellow), HIGH (Red) risk categories.

| hazard    |  description  |   indicator   |  unit   |   value_min  |  value_max  |  value_norm  |  spatial_resolution |
| - | - | - | - | - | - |- |- |
| cyclone |  Monthly asset level exposure to cyclones/hurricanes. We source cyclone tracks from the [NOAA IBTRACs](https://www.ncdc.noaa.gov/ibtracs/). Frequency of category 3/4/5 cyclones. | obs_freq | frequency | 0.0 | 3.0 | 2.00 | 1000.0 |
| cyclone | Annual projection of probability of at least one hit by a category 3/4/5 cyclone  | prob | probability | 0.0 | 1.0 | 0.50 | 50000.0 |
| flood_potential | Monthly exposure of assets to floods. We transform data from multiple flood observatories to report on active floods at the points of interest. The severity classes are based on the recurrence interval: (class 1) Large flood events: recurrence < 20 year; (class 2) Very large events: 20 year < recurrence < 100 year; (class 3) Extreme events: recurrence > 100 years. Values are set based on severity*0.333. | obs_score | score | 0.0 | 1.0 | 1.00 | 1000.0 |
| flood_potential | Annual exposure of asset to floods  | inland_flood_prob | probability | 0.0 | 1.0 |  1.00 | 4000.0 |
| fundamental | Annual mean annual temperature at the asset location | temp | degree_celsius | -5.0 | 45.0 | 45.00 | 100000.0 |
| fundamental | Annual total precipitation at the asset location | precip | millimeter | 0.0 | 5000.00 | 5000.0 | 100000.0 |
| fundamental | Annual days per year where precipitation exceeds 51mm | extreme_precip | day | 0.0 | 365.0 | 365.0 | 100000.0 |
| heatwave | Annual heatwave days per year where temperature at asset is projected to exceed 98th percentile of historic recordings | freq | day | 0.0 | 365.0 | 200.0 | 100000.0 |
| sea_level_rise | Annual projection of sea level rise relative to average sea level at the asset over 1980-2010 | change | meter | -0.2 | 2.0 | 0.75 | 100000.0 |
| water_stress | Annual projection of standard precipitation evapo-transipiration index | spei_norm |  score |  -3.0 |  3.0 |  3.00 |  100000.0 |
| water_stress | Annual ratio of water demand to renewable water availability | score | score | 0.0 | 4.0 | 4.00 | 500.0 |
| wildfire | Monthly active fire severity based on satellite observations. We transform the [NASA Active Fire Data](https://firms2.modaps.eosdis.nasa.gov/) to report on active fires. Note that because these values are based on satellite observations and we cannot discern wildfires from human generated fires. | obs_score  | score | 0.0 | 1.0 | 1.00 | 300.0 |
| wildfire | Annual fraction of land exposed to wildfire within 300km radius of the asset   | burned_area_norm  | score | 0.0 | 1.0 | 0.1 | 300.0 |
| wildfire | Average annual probability of a wildfire occurring across all land areas within 1km of the asset | fire_kbdi_susceptability  |  score | 0.0 | 1.0 | 1.00 | 300.0 |

*To create the normalized multi-hazard projected risk exposure view in Climate Explorer, we divide each indicator by its corresponding normalization factor [or other name choice] in the table below and threshold values between 0 and 1.
*The heat map coding range for floods indicates a flood exceedance frequency (i.e. the number of floods exceeding 5% probability in the 30-year period.
