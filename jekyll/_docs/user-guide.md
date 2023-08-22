---
layout: doc
title: Climate Explorer User Guide
subtitle: This User Guide will provide you with an overview of the Climate Explorer dashboard, a step-by-step guide of how to upload your assets, and how to interpret the risk data and graphics.
date: 2023-01-01
lastmod: 2023-08-20
author: GE
tags:
- start
- intro
- quickstart
- climate explorer
- walkthrough
---

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

Portfolio information can be uploaded in two formats: CSV and GeoJSON. The sections below provide more details on how to upload portfolio information using any of these formats.

Portfolio size is currently limited to 5000 assets for CSV-based portfolios and 2000 assets for GeoJSON-based portfolios. Additional account-level portfolio size limits may apply. Please contact [sales@sustglobal.com](mailto:sales@sustglobal.com) to increase your portfolio size limits.

#### Portfolios in CSV format

An example of a portfolio CSV file can be found here: [demo portfolio](https://raw.githubusercontent.com/sustglobal/dev-center/master/resources/example_portfolio.csv). This demo portfolio is a useful starting point if you are interested in building your own portfolio for use in Climate Explorer, whether via UI or API. Simply right-click on the demo portfolio link above, select **Save Link As**, and add a .csv extension to the file name (so it becomes example_portfolio.csv) and this will change the file to a CSV. Open the portfolio file and add your assets before uploading the portfolio on the [Portfolio View](https://explorer.sustglobal.io/portfolios/) on Climate Explorer as described above. Each of the supported fields in the portfolio CSV file is documented below:


| Field Name | Description |
| - | - |
| **lat**           | **Required.** Latitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 90 to +90 degrees, at least 2 decimal places
| **lng**           | **Required.** Longitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 180 to +180 degrees, at least 2 decimal places
| **entity_id**     | **Optional.** Meaningful identifier of asset, typically used to map into external systems.
| **entity_name**   | **Optional.** Name of the asset in the portfolio, could also be text string on the name of a city or location
| **label:type**    | **Optional.** Type indicator for the asset. This could be a city or a company name or type of mine
| **label:address** | **Optional.** Address of the asset.
| **label:price**   | **Optional.** Value in USD of asset used to drive the "Value-at-Risk" portion of the Climate Explorer dashboard. Either a native float or USD currency format is accepted (e.g. 12345.00 or $12,345.00). Commas are optional in both cases.
| **label:YOUR_KEY**   | **Optional.** Additional labels (any column header prefixed with `label:`) are preserved in the results, and are not meaningful to Climate Explorer.


Note that the geocodes (lat/lng coordinates) of all the physical assets in your portfolio are the only required fields.

To anonymize the risk graphics that appear on the dashboard views, you can use the **entity_id** field to do so. Simply, **entity_id** field is preferred to the lat and lng field. By doing so, this will effectively "hide" the coordinates in the dashboard views.

#### Portfolios in GeoJSON format

As an alternative to CSV, Climate Explorer also supports uploading portfolios in [GeoJSON](https://geojson.org/) format. The snippet below shows the structure supported by Climate Explorer to upload portfolios in this format. An example of a portfolio in GeoJSON format can be found here: [demo portfolio](https://raw.githubusercontent.com/sustglobal/dev-center/master/resources/example_portfolio.json).

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "entity_id": "YOS",
        "entity_name": "Yosemite National Park",
        "labels": {
          "type": "US National Park",
          "address": "9035 Village Dr, Yosemite Valley, CA 95389"
        }
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [ -119.54, 37.85 ],
            [ -119.52, 37.85 ],
            [ -119.52, 37.87 ],
            [ -119.54, 37.87 ],
            [ -119.54, 37.85 ]
          ]
        ]
      }
    }
  ]
}
```

Note that the *features* list can contain one or more features. Each one of these features contains three important attributes: *type*, *properties*, and *geometry*. From these, only the *type* and *geometry* properties are required whereas the *properties* property is optional.

The *type* attribute is self-explanatory. It simply indicates that this element is a feature.

The *geometry* property contains geospatial information particular to the feature. This property is described by two required properties: *type* and *coordinates*. The former specifies the type of the geospatial information which can be either a *Point*, *Polygon* or *MultiPolygon*. Other geometry types such as *LineString* are **NOT** currently supported. The *coordinates* property specifies the geographic coordinates of said point or polygon. 

There is currently a hard limit on the number of edges and total area described by the uploaded geometries. These limits are 35000 edges and 100000 km<sup>2</sup>.

The *properties* attribute corresponds to specific information related to this point or polygon. This information is expressed in terms of three required properties: *entity_id*, *entity_name*, and *labels*. Each of these properties have the same meaning as those provided in CSV-based portfolios (see section above). 

Finally, Climate Explorer only supports geometry files in GeoJSON format. To upload geometries represented in other formats such as shapefiles, these files should be first converted to GeoJSON using tools such as [ArcGIS](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/features-to-json.htm) or [QGIS](https://qgis.org/en/site/).

### Mapping Physical Addresses to Geocodes

If you only have addresses and not geocodes, you can use the [Mapbox Geocoding Playground](https://docs.mapbox.com/playground/geocoding/) to secure geocodes for a specific address. Alternatively, you can also secure the geocodes from [Google Maps](https://www.google.com/maps) by copying the numbers in the URL. 

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
