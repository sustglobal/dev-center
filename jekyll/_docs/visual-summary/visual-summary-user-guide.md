---
layout: doc
title: Visual Summary User Guide
subtitle: This User Guide will provide you with an overview of the Visual Summary dashboard, a step-by-step guide of how to upload your assets, and how to interpret the visualization of the data.
date: 2024-11-15
lastmod: 2024-11-18
author: TA
tags:
- start
- intro
- quickstart
- visual summary
- walkthrough
---


## What can you do with Visual Summary?

Our Visual Summary dashboard product provides you with financial impact metrics and physical climate risk analysis information, which can be used for strategic planning needs.

Currently, Sust Global provides two metrics of financial risk: (1) <i>Structural Damage</i> and (2) <i>Business Interruption</i>. A brief description of each is provided below:

1. <i>Structural Damage</i> - Direct damage to structures, including homes, warehouses, businesses, etc., calculated as the percentage of a structure’s value expected to be destroyed. Because structural damage is defined as a percentage of overall value, the financial loss can only be computed when an asset’s value is known. Structural damage estimates are available for wildfires, floods (both coastal and inland), and tropical cyclones.

2. <i>Business Interruption</i> - Days per year in which business cannot be conducted due to a variety of direct (e.g., damage to asset structure) and indirect (e.g., damage to nearby energy grid or transportation networks) impacts. Business interruption estimates are available for wildfires, floods (both coastal and inland), tropical cyclones, and heatwaves.

## How to use Visual Summary

### Uploading a portfolio

To create a new portfolio, go to the [Portfolio View](https://finance.sustglobal.io/portfolios) on Visual Summary and click on the button labeled New Portfolio. When creating a new portfolio, make sure that the name has no spaces in it. Having given the portfolio a name, you can upload information on the physical assets.

Portfolio information must be uploaded according to the Sust Institutional Data Template. The section below provides more details on this format.

Portfolio size is currently limited to 5000 assets for CSV-based portfolios and 2000 assets for GeoJSON-based portfolios. Additional account-level portfolio size limits may apply. Please contact [sales@sustglobal.com](mailto:sales@sustglobal.com) to increase your portfolio size limits.

#### The Sust Institutional Data Template

The Sust Institutional Data Template file can be found here: [example csv](https://docs.google.com/spreadsheets/d/1JKOk85TFckIgRuvdljzXZLV2pf-ZOj0NNoKYmqdkWBk/edit?usp=sharing). The example sheet is a useful starting point if you are interested in building your own portfolio for use in Visual Summary, whether via UI or API. Simply left-click on the example CSV link above, select **File** -> **Download** -> **Comma Separated Values**. Open the portfolio file and add your assets (if desired) before uploading the portfolio on the [Portfolio View](https://finance.sustglobal.io/portfolios) on Visual Summary as described above. Each of the supported fields in the portfolio CSV file is documented below:


| Field Name | Description |
| - | - |
| **lat**           | **Required.** Latitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 90 to +90 degrees, at least 2 decimal places
| **lng**           | **Required.** Longitude of the asset in degrees [WGS84 coordinates](https://spatialreference.org/ref/epsg/4326/), range within 180 to +180 degrees, at least 2 decimal places
| **entity_id**     | **Optional.** Meaningful identifier of asset, typically used to map into external systems.
| **entity_name**   | **Optional.** Name of the asset in the portfolio, could also be text string on the name of a city or location
| **type**          | **Optional.** Type indicator for the asset. See [Value at Risk](/value-at-risk#available-asset-types) for more types
| **label:Address** | **Optional.** Address of the asset.
| **label:company_name**| **Optional.** Company attached to this particular asset.
| **label:financial_exposure_weight**   | **Optional.** The decimal percent value of the proportion of this portfolio tied to this asset (e.g. 0.10)
| **label:YOUR_KEY**   | **Optional.** Additional labels (any column header prefixed with `label:`) are preserved in the results, and are not meaningful to Visual Summary.

Note that the geocodes (lat/lng coordinates) of all the physical assets in your portfolio are the only required fields.

### Mapping Physical Addresses to Geocodes

If you only have addresses and not geocodes, you can use the [Mapbox Geocoding Playground](https://docs.mapbox.com/playground/geocoding/) to secure geocodes for a specific address. Alternatively, you can also secure the geocodes from [Google Maps](https://www.google.com/maps) by copying the numbers in the URL. 

## Disclaimer and Liability

1. **Disclaimer.** While Sust Global endeavors to ensure that the information, analysis and forecasts in the dataset and Visual Summary Dashboard are correct, Sust Global will not be liable for any errors, inaccuracies or delays in content or for any actions taken in reliance thereon. 

2. Sust Global does not guarantee the accuracy of or endorse the views or opinions given by any third party content provider.

3. The information contained in the User Guide and Visual Summary Dashboard and Sust Global API is provided without any conditions, warranties or other terms of any kind. Accordingly, and to the maximum extent permitted by law, the User Guide and Visual Summary Dashboard is provided on the basis that Sust Global excludes all representations, warranties, conditions and other terms (including, without limitation, the conditions implied by law of satisfactory quality, fitness for purpose and the use of reasonable care and skill) which but for this legal notice might have effect in relation to this service.

4. **Liability.** Sust Global excludes all liability and responsibility for any amount or kind of loss or damage that may result to users (whether a paid subscriber or not) or third parties (including without limitation, any direct, indirect, punitive or consequential loss or damages, or any loss of income, profits, goodwill, data, contracts, use of money, or loss or damages arising from or connected in any way to business interruption, and whether in tort (including without limitation negligence), contract or otherwise) in connection with the User Guide and any derivative pages in any way or in connection with the use, inability to use or the results of use of the Brochure, any websites linked to the Brochure or the materials on such websites.

5. This exclusion of liability will include but not be limited to loss or damage due to viruses that may infect your computer equipment, software, data or other property on account of your access to or use of the Brochure or your downloading of any material from any websites linked to the Brochure.

6. **Governing Law and Jurisdiction.** The validity, interpretation, construction and performance of these documents shall be governed by the laws of the United States, where applicable, and otherwise by the laws of the State of California, without regard to its principles of conflicts of laws. Any dispute arising out of this legal notice shall be heard in a court of competent jurisdiction over cases and controversies arising in San Francisco, California.  -->
