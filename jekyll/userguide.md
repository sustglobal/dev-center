---
title: Climate Explorer User Guide
toc: true
---

## Introduction

This User Guide will provide you with an overview of the Climate Explorer dashboard, a step-by-step guide of how to upload your assets, and how to interpret the risk data and graphics.

## Contents

- For a guide on how to upload your portfolios and use the dashboard graph controls, look at `How to use Climate Explorer` below
- Take a look at the [Dashboard Guide](./dashboardguide.html) for a description and methodology behind each of the dashboard views and a guide to interpreting the numbers.
- Take a look at the [CSV Dataset Guide](./csvdatasetguide.html) for a description and methodology behind each of the CSV datasets and a guide to interpreting the numbers.
- Take a look at the [Data Guide](./dataguide.html) if you want to develop a deeper understanding of the underlying climate data behind the dashboard and the datasets.
- Take a look at the [API Guide](./api.html) if you want to develop a deeper understanding of the Sust Global API.

## What can you do with Climate Explorer?

Our Climate Explorer dashboard product provides you with physical climate risk analysis information, which can be used for reporting, risk management and strategic planning needs.

Our data on annualized hazard exposure is derived from multiple climate models. These models generate midterm (15 year) and long term (30 year) projections. While we provide annualized exposure data across all indicators, across all supported scenarios, this data can be most reliably used as 5, 15 or 30 year aggregates to cover near term, midterm and long term risk exposure. We provide asset level hazard exposure summaries over these three time windows as well.

## How to use Climate Explorer

### Walkthrough video

Please watch the below video to learn how to log into Climate Explorer and how to create a portfolio, upload assets and use the dashboard.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q1OsUfyojMk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### Uploading a portfolio

To create a new portfolio, go to the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer and click on the button labeled New Portfolio. When creating a new portfolio, make sure that the name has no spaces in it. Having given the portfolio a name, you can upload information on the physical assets.

An example of a portfolio CSV file can be found here: [demo portfolio](https://raw.githubusercontent.com/sustglobal/dev-center/master/resources/example_portfolio.csv). This demo portfolio is a useful starting point if you are interested in building your own portfolio for use in Climate Explorer, whether via UI or API. Simply right click on the demo portfolio link above, select ‘Save Link As’, and add a .csv extension to the file name (so it becomes example_portfolio.csv) and this will change the file to a CSV. Open the portfolio file and add your assets before uploading the portfolio on the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer as described above. Each of the supported fields in the portfolio CSV file is documented below:


| Field Name | Description |
| - | - |
| `lat`           | **Required.** Latitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 90 to +90 degrees, at least 2 decimal places
| `lng`           | **Required.** Longitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 180 to +180 degrees, at least 2 decimal places
| `entity_id`     | **Optional.** Meaningful identifier of asset, typically used to map into external systems.
| `entity_name`   | **Optional.** Name of the asset in the portfolio, could also be text string on the name of a city or location
| `label:type`    | **Optional.** Type indicator for the asset. This could be a city or a company name or type of mine
| `label:address` | **Optional.** Address of the asset.
| `label:price`   | **Optional.** Value of asset. Expected to in the same denomination across the portfolio
| `label:<KEY>`   | **Optional.** Additional labels (any column header prefixed with `label:`) are preserved in the results, and are not meaningful to Climate Explorer.


Note that the geocodes (lat/lng coordinates) of all the physical assets in your portfolio are the only required fields. If you only have addresses and not the geocodes, you can use the Mapbox Geocoding Playground to secure geocodes for a specific address. Alternatively, you can also secure the geocodes from Google Maps by copying the numbers in the URL. 
If you would like to 'anonymise' the risk graphics that appear on the dashboard views, you can use the entity_id field to do so. Simply, entity_id field is preferred to the lat and lng field. By doing so, this will effectively ‘hide’ the coordinates in the dashboard views.

Portfolios are currently limited to 5000 assets in size. Additional account-level portfolio size limits may apply. Please contact sales@sustglobal.com to increase your portfolio size limits.

### Using the graph controls

Within Climate Explorer, each graph allows for real-time configuration and analysis. On the top right of each graph, you can zoom-in and out, pan, and hover to configure your data in real-time.

Please refer to this [guide](https://plotly.com/chart-studio-help/getting-to-know-the-plotly-modebar/) on how to use the graph controls, including zoom, pan, hover and reset. [Here](https://plotly.com/chart-studio-help/zoom-pan-hover-controls/) is a more interactive version where you can practice using the graph controls yourself.

## Disclaimer and Liability

1. **Disclaimer.** While Sust Global endeavors to ensure that the information, analysis and forecasts in the dataset and Climate Explorer Dashboard are correct, Sust Global will not be liable for any errors, inaccuracies or delays in content or for any actions taken in reliance thereon. 

2. Sust Global does not guarantee the accuracy of or endorse the views or opinions given by any third party content provider.

3. The information contained in the User Guide and Climate Explorer Dashboard and Sust Global API is provided without any conditions, warranties or other terms of any kind. Accordingly, and to the maximum extent permitted by law, the User Guide and Climate Explorer Dashboard is provided on the basis that Sust Global excludes all representations, warranties, conditions and other terms (including, without limitation, the conditions implied by law of satisfactory quality, fitness for purpose and the use of reasonable care and skill) which but for this legal notice might have effect in relation to this service.

4. **Liability.** Sust Global excludes all liability and responsibility for any amount or kind of loss or damage that may result to users (whether a paid subscriber or not) or third parties (including without limitation, any direct, indirect, punitive or consequential loss or damages, or any loss of income, profits, goodwill, data, contracts, use of money, or loss or damages arising from or connected in any way to business interruption, and whether in tort (including without limitation negligence), contract or otherwise) in connection with the User Guide and any derivative pages in any way or in connection with the use, inability to use or the results of use of the Brochure, any websites linked to the Brochure or the materials on such websites.

5. This exclusion of liability will include but not be limited to loss or damage due to viruses that may infect your computer equipment, software, data or other property on account of your access to or use of the Brochure or your downloading of any material from any websites linked to the Brochure.

6. **Governing Law and Jurisdiction.** The validity, interpretation, construction and performance of these documents shall be governed by the laws of the United States, where applicable, and otherwise by the laws of the State of California, without regard to its principles of conflicts of laws. Any dispute arising out of this legal notice shall be heard in a court of competent jurisdiction over cases and controversies arising in San Francisco, California. 
