---
layout: doc
title: Financial Risk Analysis
subtitle: Sust Global is dedicated to providing asset managers with tools that assess and mitigate the financial risks associated with climate change. As climate-related hazards such as floods, wildfires, cyclones, and heatwaves increase in frequency and severity, it becomes crucial to quantify the potential losses for businesses and assets. Sust Global's financial impact and business interruption models are designed to address this need, quantifying the potential losses from these hazards through a framework that integrates hazard, exposure, and vulnerability.
date: 2023-01-01
lastmod: 2024-09-09
author: MC
tags:
- data
- financial risk
- var
- value at risk
---


**Financial Risk Metrics**

We utilize two key metrics—structural damage and business interruption—to assess the financial risks posed by climate hazards, providing asset managers with a detailed understanding of potential economic losses from physical and operational impacts. 

1. <i>Structural Damage</i> - Expressed as a percentage of the asset’s total value, this metric reflects the expected annual proportion of the asset that is likely to be damaged by a specific hazard event. The calculation considers the intensity of the climate hazard, the vulnerability of the asset, and utilizes empirically derived damage functions. Estimates are available for wildfires, floods (both coastal and inland), and tropical cyclones.

2. <i>Business Interruption</i> - Annual downtime (in days) when operations are halted due to climate hazards. It accounts for both direct impacts (e.g., structural damage) and indirect disruptions (e.g., power outages, road closures). Applicable to floods, wildfires, cyclones, and heatwaves, this metric helps businesses assess operational risk and plan for resilience across supply chains and infrastructure.

By combining structural damage and business interruption metrics, Sust Global provides asset managers with a more complete picture of the financial risks associated with climate change and consistent with IPCC [methodologies](https://www.ipcc.ch/report/ar6/wg2/). While the structural damage metric offers a clear assessment of the physical harm to assets, the business interruption metric highlights the operational vulnerabilities that can cause prolonged financial losses. Together, these metrics allow for a comprehensive evaluation of risk across different warming scenarios, time horizons, and spatial scales, from individual assets to entire portfolios.

For instance, in assessing flood risks, asset managers can determine not only the expected physical damage to their properties but also how long operations might be disrupted due to road closures or power outages. In wildfire-prone regions, understanding the likelihood of prolonged business shutdowns due to evacuations and damaged infrastructure can help guide decisions on where to allocate resources for fire prevention or insurance.

Moreover, these metrics support scenario-based planning by providing insights into how risks might evolve over time, under different climate change scenarios. Asset managers can assess risks not just for the present but for future timeframes like 2030, 2050, or 2080, enabling long-term financial planning that considers potential increases in hazard frequency and intensity.

Ultimately, our financial risk metrics equip asset managers with the tools needed to make informed decisions about protecting their assets and minimizing financial losses in an era of increasing climate uncertainty. Whether through improved structural resilience or operational continuity strategies, these insights help businesses safeguard their future in a changing climate.


**Data Availability**

Sust Global's models offer a variety of financial risk assessments, which are customizable across several dimensions:

* <i>Warming Scenarios</i> - Scenarios include SSP1-2.6, SSP2-4.5, and SSP5-8.5, representing various levels of greenhouse gas emissions and socioeconomic developments.
* <i>Time Horizons</i> - Projections are available for different time periods, including Baseline, 2030, 2050, and 2080, allowing both short-term and long-term risk analysis.
* <i>Spatial Scales</i> - Risk calculations are available at the asset level, portfolio level (aggregated across multiple assets), and polygon level (e.g., counties), ensuring flexibility for various use cases.
* <i>Hazards</i> - Models cover a broad range of climate-related hazards, including wildfire, flooding, tropical cyclones, and heatwaves.

## Methodologies
For each asset within a portfolio, physical risk exposure is evaluated under a variety of warming scenarios (e.g., SSP5) throughout the 21st century across multiple hazards. To estimate the resulting financial impacts, we use <i>damage functions</i> to translate hazard exposure (e.g,. 1 meter of flooding) to impacts like asset damage (e.g., 10% of structure value) and business interruption (e.g., 10 days). Our damage functions are empirically derived and based on publicly available and peer-reviewed research.

By combining physical hazard exposure with damage functions, we can estimate the financial impacts of climate hazards in several meaningful ways. One such method is to examine the financial loss in response to a particular hazard event (e.g., 1-in-100 year flood). Additionally, we can look beyond a specific hazard event and estimate the average annual expected loss by integrating financial risk across multiple hazard return periods (e.g., 1-in-10 year, 1-in-50 year, 1-in-100 year, etc.). While the former approach can estimate the financial loss in a year where an asset was 'hit' by a large event, the latter represents the expected financial loss per year, averaged over many years.

Financial impacts are estimated under a particular warming scenario (e.g., SSP5) and at a particular period of time (e.g., 2050). Beyond calculating losses for a single hazard, we aggregate financial impacts across hazards to give a more holistic perspective on climate-induced financial risk. Lastly, in addition to estimating finacial losses at each asset, we calculate the impact across the portfolio by aggregating projected loss across all hazards and all assets. 


### Floods
Flood losses are based on flood depths associated with specific *return period* events (e.g., a 1-in-100-year flood). Sust Global uses empirically derived damage functions from the [US Army Corps of Engineers](https://usace.contentdm.oclc.org/digital/collection/p16021coll2/id/6789/) and the European Commission Joint Research Center [ECJRC](https://publications.jrc.ec.europa.eu/repository/handle/JRC105688) to estimate structural damage. These [functions](https://link.springer.com/article/10.1007/s40710-014-0038-2) map flood depth to expected damage and vary by building type and region.

The model includes 240 damage functions across 39 asset categories (e.g., residential, commercial, industrial), allowing for asset-specific assessments. Where detailed asset data is unavailable, a default curve is applied.

Because flood vulnerability depends heavily on local building standards, we apply regional corrections using the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) framework. For example, one meter of flooding may cause significantly less damage to a structure in Japan than in the Philippines, due to differences in construction quality and codes.

### Cyclones
Wind-driven losses associated with tropical cyclones are based on 1-minute sustained wind speed measured  at 10m for particular <i>return period</i> events (e.g., 1-in-100 year cyclone). We use damage functions from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework. Given a wind speed, these empirically-derived functions describe the resulting damage to a structure. Because wind-related damage [varies](https://www.nhc.noaa.gov/pdf/NormalizedHurricane2008.pdf) across structure types (e.g., single family wooden home, reinforced concrete 5-story building), we use a variety of structure-specific damage curves.

Although we provide a default damage curve, more precise estimates of wind-driven financial risk require building-type information for each asset. Similar to the flood damage curves, regional differences in building standards are accounted for to provide more accurate estimates of global risk.

### Wildfires
Sust Global’s wildfire structural damage model provides a robust approach to assessing the financial risks posed by wildfires to assets. Unlike flood or cyclone wind damage, wildfire damage typically operates on a binary scale—either a structure is impacted by fire or it escapes entirely. This characteristic shapes how wildfire risk is quantified and modeled.

The wildfire model begins by estimating the probability of a wildfire occurring at an asset in a given year. The wildfire damage functions differ significantly from those used for other hazards. We developed our damage function based on historical data, particularly property damage from the 2018 [Camp Fire](https://fireecology.springeropen.com/articles/10.1186/s42408-021-00117-0) in California, which destroyed 18,000 structures and caused an estimated $16.5 billion in damage. From this analysis, we estimate that if a wildfire occurs at an asset, there is a 10% chance the asset will be directly impacted. If impacted, the model assumes that 75% of the asset's total value will be lost. This binary approach reflects the nature of wildfire damage, where partial damage is rare, and total destruction is more common.


### Heatwaves
For heatwaves, business interruption days are calculated based on the estimated annual number of heatwave days for the asset scaled by the fraction of outdoor labor associated with the asset type. This approach accounts for the varying vulnerability of different asset types to heatwaves, providing a tailored estimate of business interruption risk based on their reliance on outdoor labor. We currently do not assess structural damage from heatwaves, as their impacts primarily affect cooling costs and worker productivity rather than causing physical damage.


## Asset Type Specific Damages
As mentioned above, an asset’s vulnerability to hazard exposure (i.e., susceptibility to damage if exposed) is strongly governed by the structure type (e.g., reinforced concrete building). Although a default structure type can be used if asset-level structure type information is unknown, financial risk outputs will be more accurate if structure type is uploaded for each asset. Asset type can be included using the **label:type** column. Doing so will enable us to quantify financial impacts using specialized damage functions based on each asset type while accounting for industry- and structure-specific characteristics.

## Available Asset Types

The available asset types are given in the table below.  For Climate Explorer to recognize an asset type, you must include a column named **label:type** that matches exactly the label given below in **bold**.

<table>
  <thead>
    <tr>
      <th style="border-bottom: 2px solid black; border-right: 2px solid black;padding: 5px;"><em>CATEGORY</em></th>
      <th style="border-bottom: 2px solid black; padding: 5px;"><em>LABEL FOR USE IN CE</em></th>
      <th style="border-bottom: 2px solid black; border-left: 2px solid black;padding: 5px;"><em>EXAMPLES OF THIS TYPE OF ASSET</em></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Agriculture</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Agriculture</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Agricultural areas, horse stalls, veterinary offices</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Commercial</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Retail Trade</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Appliances, Auto Dealer, Auto Dealership, Bait Stand, Bait Stand, Bakery, Bakery, Boat Sales/Service, Book Store, Book Store, Camera Store, Candy Store, Carpet and Paint Shop, Clothing, Clothing Store, Clothing-Mens, Convenience Store, Crafts, Department Store, Department Store, Drive thru market, Drug, Drug Store, Fabric Store, Feed Store, Flea Market, Florist, Fruit Stand, Furniture, Furniture Store, Gas Station, Gas/Butane Supply, Gift Shop, Greenhouse, Gun Shop, Hardware, Hardware, Hobby Shop, Home Repair Store, Large Furniture, Large Grocery, Lawnmower, Liquor, Liquor Store, Liquor Store, Meat Market, Medium Grocery, Motorcycle Dealer, Music Center, Neighborhood Grocery, Nursery, Paint Store, Pawn Shop, Remnant Shop, Service Station, Service Station, Shoe Repair, Shoe Store, Small Grocery, Supermarket, Toy Store, Tractor Sales, Trophy Shop, Upholstery Shop, Used Appliances/Cloth, Used Furniture, Vacuum Cleaner Sales, Variety Store, Video Games, Wine Store.</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Parking</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Garage</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Wholesale Trade</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Auto Junk Yard, Auto Parts/Mufflers, Beer Warehouse, Bottled Gases Warehouse, Food Warehouse, Heavy Equipment Storage, Jewelry, Lumber Yard, Lumber, Machine Parts Storage, Medical Supplies, Municipal Storage Warehouse, Paper Products Warehouse, Private Storage, Quonset Hut Storage, Safety Equipment, Sporting Goods Warehouse, T.V. Repair, T.V. Station, Trailer Parts, Warehouse</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Personal and Repair Services</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Auto Repair, Barber Shop, Beauty Salon, Boat Service, Car Wash, Cemetery, Cleaners substation, Funeral Home, Laundry, Photo Studio, Private Day Care, Re-Upholstery, Truck Mfg &amp; Sales, Washateria, Watch Repair</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Professional/Technical Services</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Accounting Firm, Airport, Big Office Commercial, Boat Storage, Business, Filtering Plant, Import Sales, Legal Office, Office Building, Piers, Professional, Real Estate Office, Sewage Treatment, Transport Company, Utility Company</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Banks</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Bank</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Hospital</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Hospital</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Medical Office/Clinic</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Chiropractic Clinic, Dentist’s Office, Doctor’s Office, Medical Office, X-Ray Service</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Entertainment &amp; Recreation</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Bowling Alley, Cafeteria Restaurant, Country Club, Drive-In Restaurant, Fast Food Restaurant, Fishing Party Boat, Full-Service Restaurant, Lounge, Physical Fitness, Private Club, Private Golf Course, Private Pool, Recreation Facilities, Restaurant, T.V. Station, Tavern, Telephone Exchange</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Theaters</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Private Hall, Indoor Theater, Movie Theater, Organization Hall, Drive-In Theater</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Commercial</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Generic grouping for items in <em>Commercial</em> category</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Education</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Grade Schools</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Commercial School, Library, School, Elementary School</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Colleges/Universities</strong></td>
      <td style="border: 1px solid black; padding: 5px;">College, University</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Education</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Generic grouping for items in <em>Education</em> category</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;">Government</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>General Services</strong></td>
      <td style="border: 1px solid black; padding: 5px;">City Hall, Post Office, Government facility</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Emergency Response</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Fire Station, Police Station</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Government</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Generic grouping for items in <em>Government</em> category</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Industrial</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Heavy</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Boiler Building, Cabinet Shop Mfg, Concrete Mfg, Door Mfg, Fabrication Shop, Heat Exchanger Mfg, Heavy Machine Shop, Lumber Mill, Metal Coatings Services, Metal Recycling, Pipe Threader Facility, Research Lab-Machine, Welding-Machine</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Light</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Battery Mfg, Commercial Printing, Cooling Tower, Electronic Equip Mfg, Frame Shop, Furniture Mfg, Industrial Loading Dock, Instrument Mfg, Leather Goods Mfg, Locker Bldg, Maint Bldg-Mfg Facility, Newspaper Print Plant, Newspaper Sales Office, Office-Mfg Facility</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Food/Drugs/Chemicals</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Chemical Laboratory, Chemical Plant Bonding, Chemical Plant, Chemical refinery, Detergent Mfg Facility, Feed Mill, Food Processor, Meat Packing, Oil Storage Tanks, Plastic Mfg</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Metals/Minerals Processing</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Foundry, Refinery-Lead, Sand &amp; Gravel, Sheet Metal</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>High Technology</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Data Center, Microchip Mfg</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Construction</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Carpet Tile Flooring, Carpeting Service, Construction Co, Contractor Roofing, Contractor-Electric, Heating &amp; Air Conditioning Service, Pier Drilling Co, Plumbing Co, Plumbing Services, Sandblasting Co, Water Well Service</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Industrial</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Generic grouping for items in <em>Industrial</em> category</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Religion</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Churches and Other Non-profit Org.</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Church, Civic Association</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Single Family</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Single Family Dwelling</strong></td>
      <td style="border: 1px solid black; padding: 5px;">One, two, or three story, with or without basement</td>
    </tr>
    <tr>
      <td style="border-top: 1px solid black; padding: 5px;"><em>Residential</em></td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Manuf.  Housing</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Mobile Home, Manufactured Home</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Multifamily Dwelling</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Apartments, Condominium</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Temporary Lodging</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Hotel, Motel</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Institutional Dormitory</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Institutional Dormitory</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Nursing Home</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Nursing Home, Rest Home</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Residential</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Generic grouping for items in <em>Residential</em> category</td>
    </tr>
  </tbody>
</table>

