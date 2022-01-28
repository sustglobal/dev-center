---
title: Climate Explorer Quickstart Guide
---

Climate Explorer is available at [https://explorer.sustglobal.io](https://explorer.sustglobal.io).
This UI enables Sust Global customers to manage their physical asset portfolios and gain insights regarding climate risk exposure.

Developers are encouraged to integrate with Climate Explorer through the API.
Please read the [Climate Explorer API Guide](./api.html) to learn about these capabilities.

Climate Explorer is currently in beta and will be generally available in mid 2022.
If you do not yet have a Climate Explorer account, please contact [sales@sustglobal.com](mailto:sales@sustglobal.com).


# Create New Portfolios

As a user of Climate Explorer, you can manage collections of physical assets as "portfolios", each of which can be represented as a CSV file. 

To create a new portfoilio go to the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer and click on the button labelled `New Portfolio`. When creating a new portfolio, make sure that the name has no gaps in it. Having given the portfolio a name, you can upload information on the phyical assets. 

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

| Hazard | Description | Unit | Range of Possible Values | Spatial Resolution |
| - | - | - | - | - |
| Fire Exposure | Monthly active fire severity based on satellite observations. We transform the [NASA Active Fire Data](https://firms2.modaps.eosdis.nasa.gov/) to report on active fires. Note that because these values are based on satellite observations and we cannot discern wildfires from human generated fires. | Unit interval with 1.0 indicating maximum active fires recorded in a month (30 in 2020) | 0.0 to 1.0 | 10km |
| Flooding Exposure | Monthly exposure of assets to floods. We transform data from multiple flood observatories to report on active floods at the points of interest. The severity classes are based on the recurrence interval: (class 1) Large flood events: recurrence < 20 year; (class 2) Very large events: 20 year < recurrence < 100 year; (class 3) Extreme events: recurrence > 100 years. Values are set based on severity*0.333. | Unit interval with 1.0 indicating maximum severity extreme flooding (recurrence exceeding 100 years) | 0.0 to 1.0 | 1km |
| Cyclone Exposure | Monthly asset level exposure to cyclones/hurricanes. We source cyclone tracks from the [NOAA IBTRACs](https://www.ncdc.noaa.gov/ibtracs/). Cyclones are tagged based on severity to a scale of 1 to 5 which is used to assign the value in the unit interval. Values are set based on severity*0.2. | Unit interval with 1.0 indicating maximum cyclone severity level 5 (example: Katrina-2005, Irma-2017, Dorian-2019). | 0.0 to 1.0 | 1km |

## Forward Looking Reporting Outcomes

All reports and supported risk projections are at annual cadence. Some of our datasets allow for higher cadence reporting, please contact us for custom requests.

For creating standard heatmaps, we assess the physical risk over the 30 year window between 2021 and 2050 and look at the maximum risk exposure to a specific hazard for an asset. We use the maximum risk exposure value to color code the asset to LOW (Green), MEDIUM (Yellow), HIGH (Red) risk categories.

| Fundamental Variable / Hazard | Description | Unit | Range of Possible Values | Spatial Resolution | Heat Map Coding Range | Max Risk Value |
| - | - | - | - | - | - |
| Annual Temperature | Annual mean annual temperature at the asset location | °C | -5 to 45 | 100km | N/A | N/A |
| Annual Precipitation | Annual total precipitation at the asset location | mm | 0 to 5000 | 100km | N/A | N/A |
| Extreme Precipitation | Annual probabilistic projections of number of days in a year where precipitation exceeds 51mm | Number of days | 0 to 365 | 100km | N/A | N/A |
| Wildfire Risk | Annual Percentage of exposed land within 14km radius of the asset to wildfire | Percentage | 0 to 100 | 14km | LOW: 0.0-0.007; MEDIUM: 0.007-1.0; HIGH: >1.0 | 10.0 |
| Inland Flooding | Annual exposure of asset to floods | Probability score | 0.0 to 1.0 | 4km | Based on number of years with probability of flood >5%; LOW: 0-0.5; MEDIUM: 0.3; HIGH: >0.3 | 1.0 |
| Heatwaves | Annual heatwave days per year where temperature at asset is projected to exceed 98th percentile of historic recordings | Number of days | 0 to 365 | 100km | LOW: 0-30; MEDIUM: 30-50; HIGH: >50 | 200 |
| Sea Level Rise | Annual projection of sea level rise relative to average sea level at the asset over 1980-2010 | Rise in meters | 0.0 to 2.0 | 100km | LOW: <0.1; MEDIUM:0.1 to 0.3; HIGH: >0.3 | 0.75 |
| Drought (SPEI) | Annual projection of standard precipitation evapo-transipiration index | Index score | -3.0 to 3.0 | 100km | LOW: >-1.5; MEDIUM: -1.5 to -2.0; HIGH: <-2.0 | 3.0 |
| Tropical Cyclones | Annual projection of probability of cyclone exposure | Probability score | 0.0 to 1.0 | 50km | LOW: < 0.5; MEDIUM: 0.5 to 0.7; HIGH: > 0.7 | 1.0 |

