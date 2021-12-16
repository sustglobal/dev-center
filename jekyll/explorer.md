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
An example of a portfolio CSV file can be found in the Developer Center: [demo portfolio](https://github.com/sustglobal/dev-center/blob/master/resources/DEMO_combined_locations.csv).
This demo portfolio is a useful starting point for anyone interested in building their own portfolio for use in Climate Explorer, whether via UI or API.

Each of the required fields in the portfolio CSV file are documented below. All fields must be populated unless otherwise noted:

| Field Name | Description |
| - | - |
| `Entity Name` | Name of the asset in the portfolio, could also be text string on the name of a city or location
| `Type`        | Type indicator for the asset. This could be a city or a company name or type of mine
| `lat`         | Latitude of the asset in [WGS84 coordinates](https://spatialreference.org/ref/epsg/wgs84/), range within 90 to +90 degrees, at least 2 decimal places
| `lng`         | Longitude of the asset in [WGS84 coordinates](https://spatialreference.org/ref/epsg/wgs84/), range within 180 to +180 degrees, at least 2 decimal places
| `Tag`         | Any metadata. Can be left null if no relevant metadata.
| `Address`     | Address of the location. Can be left null if there is no address.

Please note that portfolios are currently limited to 1000 assets in size.
