---
layout: doc
title: Nature Capital User Guide
subtitle: Sust Global's Nature Capital Dashboard exposes Sust Global's durability (non-permanence) indicators for nature based carbon projects. This guide helps users understand the indicators and corresponding datasets.
date: 2025-05-29
lastmod: 2025-05-29
author: CS
tags:
- nature
- guide
- user
---

## Nature Capital User Guide
This page will provide users of Sust Global’s Nature Capital dashboard with instructions for uploading and analyzing **Forest Carbon** and **Blue Carbon** sequestration projects.

### Nature Capital Overview
Sust Global enables users to assess durability risks to nature-based carbon projects across multiple perils on historic and forward-looking time horizons. Sust Global’s durability analytics support carbon project developers, investors, and evaluators by providing insight into project permanence risk. This tool can aid teams in project site selection, valuation processes, adaptation strategy development, regional screening, and other nature-based carbon project analysis workflows. 


## Uploading a project
To create a new project, click on the button labeled “Create” at the top of the dashboard. 

Projects uploaded to the Nature Capital dashboard are required to be in [GeoJSON](https://geojson.org/) format. The snippet below shows the structure supported by Climate Explorer to upload portfolios in this format. An example of a portfolio in GeoJSON format can be found here: [demo portfolio](https://raw.githubusercontent.com/sustglobal/dev-center/master/resources/example_portfolio.json).

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
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

Both the _type_ and _geometry_ features are required to upload a project. The _type_ attribute is self-explanatory. It simply indicates that this element is a feature.

The __geometry_ property contains geospatial information particular to the feature. This property is described by two required properties: _type_ and _coordinates_. The former specifies the type of the geospatial information which can be either a _Polygon_ or _MultiPolygon_. Other geometry types such as _Point_ and _LineString_ are **NOT** currently supported. The coordinates property specifies the geographic coordinates of said point or polygon.

There is currently a hard limit on the number of edges and total area described by the uploaded geometries. These limits are 35000 edges and 100000 km2.

Please note, the Nature Capital app only supports geometry files in GeoJSON format. To upload geometries represented in other formats such as shapefiles, these files should be first converted to GeoJSON using tools such as [ArcGIS](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/features-to-json.htm) or [QGIS](https://qgis.org/en/site/).

Finally, select whether the project being evaluated is a **Forest Carbon** and **Blue Carbon** project.

## Disclaimer and Liability

1. Disclaimer. While Sust Global endeavors to ensure that the information, analysis and forecasts in the dataset and Nature Capital Dashboard are correct, Sust Global will not be liable for any errors, inaccuracies or delays in content or for any actions taken in reliance thereon.
2. Sust Global does not guarantee the accuracy of or endorse the views or opinions given by any third party content provider.
3. The information contained in the User Guide and Nature Capital Dashboard and Sust Global API is provided without any conditions, warranties or other terms of any kind. Accordingly, and to the maximum extent permitted by law, the User Guide and Climate Explorer Dashboard is provided on the basis that Sust Global excludes all representations, warranties, conditions and other terms (including, without limitation, the conditions implied by law of satisfactory quality, fitness for purpose and the use of reasonable care and skill) which but for this legal notice might have effect in relation to this service.
4. **Liability**. Sust Global excludes all liability and responsibility for any amount or kind of loss or damage that may result to users (whether a paid subscriber or not) or third parties (including without limitation, any direct, indirect, punitive or consequential loss or damages, or any loss of income, profits, goodwill, data, contracts, use of money, or loss or damages arising from or connected in any way to business interruption, and whether in tort (including without limitation negligence), contract or otherwise) in connection with the User Guide and any derivative pages in any way or in connection with the use, inability to use or the results of use of the Brochure, any websites linked to the Brochure or the materials on such websites.
5. This exclusion of liability will include but not be limited to loss or damage due to viruses that may infect your computer equipment, software, data or other property on account of your access to or use of the Brochure or your downloading of any material from any websites linked to the Brochure.
6. **Governing Law and Jurisdiction**. The validity, interpretation, construction and performance of these documents shall be governed by the laws of the United States, where applicable, and otherwise by the laws of the State of California, without regard to its principles of conflicts of laws. Any dispute arising out of this legal notice shall be heard in a court of competent jurisdiction over cases and controversies arising in San Francisco, California.


