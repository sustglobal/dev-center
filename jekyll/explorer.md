---
title: Climate Explorer User Guide
---

Climate Explorer is available at [https://explorer.sustglobal.io](https://explorer.sustglobal.io).
This UI enables Sust Global customers to manage their physical asset portfolios and gain insights regarding risk exposure.

Developers are encouraged to integrate with Climate Explorer through an API.
Please read the [Climate Explorer API Guide](./api.html) to learn about these capabilities.

Climate Explorer is currently in beta and will be generally available in mid 2022.
If you do not yet have a Climate Explorer account, please contact [sales@sustglobal.com](mailto:sales@sustglobal.com).

## Building Portfolios

Users of Climate Explorer manage collections of physical assets as "portfolios", each of which can be represented as a CSV file.
An example of a portfolio CSV file can be found in the Developer Center: [demo portfolio](https://github.com/sustglobal/dev-center/blob/master/resources/example_portfolio.csv).
This demo portfolio is a useful starting point for anyone interested in building their own portfolio for use in Climate Explorer, whether via UI or API.

Each of the supported fields in the portfolio CSV file are documented below:

| Field Name | Description |
| - | - |
| `lat`           | **Required.** Latitude of the asset in [WGS84 coordinates](https://spatialreference.org/ref/epsg/wgs84/), range within 90 to +90 degrees, at least 2 decimal places
| `lng`           | **Required.** Longitude of the asset in [WGS84 coordinates](https://spatialreference.org/ref/epsg/wgs84/), range within 180 to +180 degrees, at least 2 decimal places
| `entity_id`     | Meaningful identifier of asset, typically used to map into external systems.
| `entity_name`   | Name of the asset in the portfolio, could also be text string on the name of a city or location
| `label:type`    | Type indicator for the asset. This could be a city or a company name or type of mine
| `label:address` | Address of the asset.
| `label:price`   | Value in USD of asset.
| `label:<KEY>`   | Additional labels (any column header prefixed with `label:`) are preserved, and are not meaningful to Climate Explorer.

Please note that portfolios are currently limited to 1000 assets in size.

## Historic Reporting Outcomes

All reports are at a monthly cadence based on observations and historic catalogs
covering the months from Jan 2010 to Dec 2020. Some of our datasets allow for
higher cadence reporting, please contact us for custom requests.

| Fundamental Variable / Hazard | Description | Unit | Range of Possible Values | Spatial Resolution |
| - | - | - | - | - |
| Fire Exposure | MoM active fire severity based on satellite observations. We transform the [NASA Active Fire Data](https://firms2.modaps.eosdis.nasa.gov/) to report on active fires. Note that because these values are based on satellite observations and we cannot discern wildfires from human generated fires. | Unit interval with 1.0 indicating maximum active fires recorded in a month (30 in 2020) | 0.0 to 1.0 | 10km |
| Flooding Exposure | MoM exposure of assets to floods. We transform data from the [Dartmouth Flood Observatory](https://floodobservatory.colorado.edu/Archives/index.html) to report on active floods at the points of interest. The severity classes are based on the recurrence interval: (class 1) Large flood events: recurrence < 20 year; (class 2) Very large events: 20 year < recurrence < 100 year; (class 3) Extreme events: recurrence > 100 years. Values are set based on severity*0.333. | Unit interval with 1.0 indicating maximum severity extreme flooding (recurrence exceeding 100 years) | 0.0 to 1.0 | 1km |
| Cyclone Exposure | MoM asset level exposure to cyclones/hurricanes. We source cyclone tracks from the NOAA IBTRACs data source. Cyclones are tagged based on severity to a scale of 1 to 5 which is used to assign the value in the unit interval. Values are set based on severity*0.2. | Unit interval with 1.0 indicating maximum cyclone severity level 5 (example: Atlantic Cyclone Katrina-2005, Irma-2017, Dorian-2019). | 0.0 to 1.0 | 1km |

## Forward Looking Reporting Outcomes

All reports are at an annual cadence and our risk projects are a Year-over-Year (YoY) cadence. Some of our datasets allow for higher cadence reporting, please contact us for custom requests.

For creating heatmaps, we assess the physical risk over the 30 year window between 2021 and 2050 and look at the maximum risk exposure to a specific hazard for an asset. We use the maximum risk exposure value to color code the asset to LOW (Green), MEDIUM (Yellow), HIGH (Red) risk categories.

| Fundamental Variable / Hazard | Description | Unit | Range of Possible Values | Spatial Resolution | Heat Map Coding Range |
| - | - | - | - | - | - |
| Annual Temperature | YoY mean annual temperature at the asset location | °C | -5 to 45 | 100km | N/A |
| Annual Precipitation | YoY total precipitation at the asset location | mm | 0 to 5000 | 100km | N/A |
| Extreme Precipitation | YoY probabilistic projections of number of days in a year where precipitation exceeds 51mm | Number of days | 0 to 365 | 100km | N/A |
| Wildfire Risk | YoY Percentage of exposed land within 50km radius of the asset to wildfire | Percentage | 0 to 100 | 14km | LOW: 0.0-0.1; MEDIUM: 0.1-1.0; HIGH: >1.0 |
| Inland Flooding | YoY exposure of asset to floods | Probability score | 0.0 to 1.0 | 4km | Based on number of years with probability of flood >5%; LOW: 0; MEDIUM: 1-2; HIGH: >=3 |
| Heatwaves | YoY heatwave days per year where temperature at asset is projected to exceed 98th percentile of historic recordings | Number of days | 0 to 365 | 100km | LOW: 0-30; MEDIUM: 30-50; HIGH: >50 |
| Sea Level Rise | YoY projection of sea level rise relative to 1980-2010 average sea level | Rise in meters | 0.0 to 2.0 | 100km | LOW: <0.1; MEDIUM:0.1 to 0.3; HIGH: >0.3 |
| Drought (SPEI) | YoY projection of standard precipitation evapo-transipiration index | Index score | -3.0 to 3.0 | 100km | LOW: >-1.5; MEDIUM: -1.5 to -2.0; HIGH: <-2.0 |
