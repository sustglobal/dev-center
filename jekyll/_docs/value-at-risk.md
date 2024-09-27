---
layout: doc
title: Financial Risk Analysis
subtitle: Physical hazards can cause direct damage to the built environment. The resulting financial risks can be quantified by leveraging publicly available relationships that map hazard exposure values (e.g., 1 meter flood depth) to asset-level impacts (e.g., 30% damage to structure). These relationships are called <i>damage functions</i> and are discussed in greater detail in the Methodology section. 
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

Currently, Sust Global provides two metrics of financial risk: (1) <i>Structural Damage</i> and (2) <i>Business Interruption</i>. A brief description of each is provided below with a deeper discussion of hazard-specific calculations found in the Methodologies section:

1. <i>Structural Damage</i> - Direct damage to structures, including homes, warehouses, businesses, etc., calculated as the percentage of a structure’s value expected to be destroyed. Because structural damage is defined as a percentage of overall value, the financial loss can only be computed when an asset’s value is known. Structural damage estimates are available for wildfires, floods (both coastal and inland), and tropical cyclones.

2. <i>Business Interruption</i> - Days per year in which business cannot be conducted due to a variety of direct (e.g., damage to asset structure) and indirect (e.g., damage to nearby energy grid or transportation networks) impacts. Direct impacts (i.e., Tier 1) are available through the API and dashboard. Indirect impacts (i.e., Tier 2) are only made available upon request as a .csv file. Business interruption estimates are available for wildfires, floods (both coastal and inland), tropical cyclones, and heatwaves. 

**Data Availability**

Financial risk is calculated across a range of warming scenarios, time horizons, spatial scales, and hazards. The following cuts of data are readily available:

* <i>Warming Scenarios</i> - SSP1, SSP2, SSP5
* <i>Time Horizons</i> - Baseline, 2030, 2050, 2080
* <i>Spatial Scales</i> - Asset, Portfolio (i.e., asset sum), Polygon (e.g., county)
* <i>Hazards</i> - Wildfire, flooding, tropical cyclones, heatwaves

## Methodologies
For each asset within a portfolio, physical risk exposure is evaluated under a variety of warming scenarios (e.g., SSP5) throughout the 21st century across multiple hazards. To estimate the resulting financial impacts, we use <i>damage functions</i> to translate hazard exposure (e.g,. 1 meter of flooding) to impacts like asset damage (e.g., 10% of structure value) and business interruption (e.g., 10 days). Our damage functions are empirically derived and based on publicly available and peer-reviewed research. Greater detail on hazard-specific damage functions are provided in the following sections.

By combining physical hazard exposure with damage functions, we can estimate the financial impacts of climate hazards in several meaningful ways. One such method is to examine the financial loss in response to a particular hazard event (e.g., 1-in-100 year flood). Additionally, we can look beyond a specific hazard event and estimate the average annual expected loss by integrating financial risk across multiple hazard return periods (e.g., 1-in-10 year, 1-in-50 year, 1-in-100 year, etc.). While the former approach can estimate the financial loss in a year where an asset was 'hit' by a large event, the latter represents the expected financial loss per year, averaged over many years.

Financial impacts are estimated under a particular warming scenario (e.g., SSP5) and at a particular period of time (e.g., 2050). Beyond calculating losses for a single hazard, we aggregate financial impacts across hazards to give a more holistic perspective on climate-induced financial risk. Lastly, in addition to estimating finacial losses at each asset, we calculate the imapact across portfolio by aggregating projected loss across all hazards and all assets. 



### Floods
Flood losses are based on flood depths associated with particular <i>return period</i> events (e.g., 1-in-100 year flood). We use damage functions based on data from the US Army Corps of Engineers. Given a flood depth, these empirically-derived functions describe the resulting damage to a structure. Because flood damage varies across structure types (e.g., single family wooden home, reinforced concrete 5-story building), we use a variety of structure-specific damage curves. Although we provide a default damage curve, more precise estimates of flood-driven financial risk require building-type information for each asset. 


The US Army Corps of Engineers damage functions were designed based on building standards in the United States. However, building standards vary across the globe and are directly tied to a structure’s vulnerability to flooding. For example, one meter of flooding is likely to cause less damage to a structure in Japan, where the building standards are high, than it is to the same structure in the Philippines, where the building standards are lower. To enable more accurate estimates global risk, we apply corrections based on regional differences in building standards, following the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework.

### Cyclones
Wind-driven losses associated with tropical cyclones are based on 1-minute sustained wind speed measured  at 10m for particular <i>return period</i> events (e.g., 1-in-100 year cyclone). We use damage functions from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework. Given a wind speed, these empirically-derived functions describe the resulting damage to a structure. Because wind-related damage varies across structure types (e.g., single family wooden home, reinforced concrete 5-story building), we use a variety of structure-specific damage curves.

Although we provide a default damage curve, more precise estimates of wind-driven financial risk require building-type information for each asset. Similar to the flood damage curves, regional differences in building standards are accounted for to provide more accurate estimates of global risk.

### Wildfires
Financial impacts from wildfire are based on the percent chance of a wildfire event within 1km of an asset in a given year. Unlike wind speed and flood depth, damage functions for wildfire are not publicly available. One reason for this lack of data is that, unlike wind and flooding, wildfire damage does not scale with hazard intensity. Rather, wildfire damage can be thought of as binary - meaning a structure either catches fire, or does not. We derive a binary wildfire damage curve based on historic impacts from California wildfires. When a wildfire is located within 1km of an asset, we assume a 10% chance of the asset being impacted. If impacted, a fire would destroy 75% of an asset’s value. 


### Heatwaves
Losses due to heatwaves are based on the number of days per year when temperature exceeds the 98th percentile. Here, the 98th percentile is calculated using the previous 30 years of data for each particular location. We use a relative measure of heat - specific to a location and time - because impacts often depend on whether the local population and environment is affected. For example, a 40°C day in Phoenix, Arizona is unremarkable whereas a 40°C in London, England may result in significant disruption. 

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

