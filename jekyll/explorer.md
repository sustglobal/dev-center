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
