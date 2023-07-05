---
title: Climate Data Guide - Financial Risk Analysis
toc: true
permalink: /var.html
---


**Data Description**

Physical perils produce damage that can be quantified using historical data.  Incorporating data on an assets economic function and structural function, we can get even more precise financial risk estimates.  Currently, Sust Global focuses on two forms of financial risk analysis (sometimes referred to as Value-at-Risk or VaR):

1. Structural Damage - Direct damage to structures, including homes, warehouses, businesses, etc., due to climate hazards, defined in terms of percentage of the structures value expected to be destroyed.  For structural damage, we estimate impacts from wildfires, floods (both coastal and inland), and tropical cyclones.

2. Business Interruption - Processes that make it impossible to conduct business for a certain period of time, either by destroying business assets, including structures; by making business impossible to conduct; or by impacting transportation or energy grid networks in the nearby vicinity of the business.  We define business interruption in terms of days per year in which business cannot be conducted.  For business interruption, we estimate impacts from wildfires, floods (both coastal and inland), tropical cyclones, and heatwaves.  We use two tiers of business interruption: tier 1 involves impacts to structure itself, while tier 2 involves impacts to an asset's surrounding road network and powerlines.  Tier 1 is available through the API and dashboard, while tier 2 is available as a csv dataset on request.  We estimate days of interruption using a combination of empirical damage functions and models of future weather so severe business could not be conducted.

The methodology involves determining an assets exposure to a given hazard under different scenarios of climate change throughout the 21st century.  This hazard exposure is then translated into expected losses, in terms of either structural damage or business interruption, via a damage function, also known as a vulnerability curve.  These damage functions are based on observational data and allow us to estimate how much damage a given hazard, at a given intensity would be expected to do to a specific type of asset, structure, or business.  Combining hazard exposure data with a damage function yields expected losses at a given hazard intensity.  Then, for hazards for which different levels of intensity exist, we integrate over the intensity values to derive a single annual value of expected loss.

## Methodologies
### Floods
To calculate financial risk from flooding, we start with flood risk exposure data in the form of <i>annual exceedance probabilities</i> (also known as Return Periods).  This data essentially describes the annual likelihood of flooding of a given depth.  We combine this data with <i>Depth-Damage-Functions</i> from the US Army Corps of Engineers.  These functions (also known as <i>impact functions</i> or <i>vulnerability curves</i>) describe the expected damage to a given structure type for a given flood depth.  For example, a flood of depth 1m may damage 30% of a structure's total value, for the typical single family wooden home.

The curves provided by the Army Corps were designed specifically for the United States.  In order to adapt them for global use cases, we apply regional calibrations using data from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework.  These calibrations account for large-scale differences in building standards around the world.  For example, these calibrations allow us to more accurately describe the impact of 1m of flooding in Japan (where building standards are very high) and other places of the world where standards may be lower.

### Cyclones
To calculate financial risk for cyclones, we start with wind speed exposure data in the form of <i>annual exceedance probabilities</i> (also known as Return Periods).  This data essentially describes the annual likelihood of a given wind speed.  We combine this data with regionally specific vulnerability curves from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework.  These functions (also known as <i>impact functions</i> or <i>vulnerability curves</i>) describe the expected damage to a given structure type for a given wind speed.  For example, a wind speed of 60 meters per second may damage 50% of a structure's total value, for the typical single family wooden home.

### Wildfires
For wildfire, we take a different approach to measuring damage.  In the event of exposure to wildfire within 1km of an asset, we assume that there is a 10% change that the asset is affected by the fire, and if affected, a fire would destroy 75% of an assets value.  These values are derived from research on historic impacts from wildfires in California.  

### Heatwaves
We use heatwaves in the business interruption analysis, which we define as days per year above the 98th percentile for temperature of the previous 30 years.  The 98th percentile value is location- and time period-specific due to the fact that whether a heatwave disrupts business depends in part on normal temperature ranges in a given location, as well as whether those normal ranges encourage the use of adaptive technology, such as air conditioners.

## Asset Type Specific Damages
In order to more accurately calculate financial risk, it is possible to upload asset types, via the `label:type` column.  This allows us to apply specialized impact functions based on the uploaded asset type, accounting for industry- and structure-specific characteristics.

## Available Asset Types

The available asset types are given in the table below.  For Climate Explorer to recognize an asset type, you must include a column named `label:type` that matches exactly the label given below in **bold**.

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
      <td style="border: 1px solid black; padding: 5px;">Battery Mfg, Commercial Printing, Cooling Tower, Electronic Equip Mfg, Frame Shop, Furniture Mfg, Industrial Loading Dock, Instrument Mfg, Leather Goods Mfg, Locker Bldg, Maint Bldg-Mfg Facility, Newspaper Print Plant, Newspaper Sales Office, Office-Manuf Facility</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Food/Drugs/Chemicals</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Chemical Laboratory, Chemical Plant Bonding, Chemical Plant, Chemical refinery, Detergent Manuf. Facility, Feed Mill, Food Processor, Meat Packing, Oil Storage Tanks, Plastic Mfg</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>Metals/Minerals Processing</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Foundry, Refinery-Lead, Sand &amp; Gravel, Sheet Metal</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td style="border: 1px solid black; padding: 5px;"><strong>High Technology</strong></td>
      <td style="border: 1px solid black; padding: 5px;">Data Center, Microchip Manuf.</td>
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
      <td style="border: 1px solid black; padding: 5px;">Mobile Home, Manufacture Home</td>
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

