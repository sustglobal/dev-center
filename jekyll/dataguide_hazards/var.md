---
title: Climate Data Guide - Financial Risk Analysis
toc: true
permalink: /var.html
---


**Data Description**

Physical perils produce damage that can be quantified using historical data.  The purpose of Financial Risk Analysis (sometimes referred to as Value-at-Risk or VaR) is to estimate the annual damage to a structure using the full suite of hazard exposure data, in conjunction with structure type and purpose.  Financial Risk Analysis calculates a probabilistic estimate of annual damage for acute hazards:
- Wildfires
- Floods
- Cyclones

Using hazard exposure data on the frequency of different event intensities, we translate each event into an estimate of damage from that intensity using well-established and peer-reviewed damage functions.  We then integrate across all of these expected events, weighted by their likelihood, to come to a single annual value of percentage loss.

## Methodologies
### Floods
To calculate financial risk from flooding, we start with flood risk exposure data in the form of <i>annual exceedance probabilities</i> (also known as Return Periods).  This data essentially describes the annual likelihood of flooding of a given depth.  We combine this data with <i>Depth-Damage-Functions</i> from the US Army Corps of Engineers.  These functions (also known as <i>impact functions</i> or <i>vulnerability curves</i>) describe the expected damage to a given structure type for a given flood depth.  For example, a flood of depth 1m may damage 30% of a structure's total value, for the typical single family wooden home.

The curves provided by the Army Corps were designed specifically for the United States.  In order to adapt them for global use cases, we apply regional calibrations using data from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework.  These calibrations account for large-scale differences in building standards around the world.  For example, these calibrations allow us to more accurately describe the impact of 1m of flooding in Japan (where building standards are very high) and other places of the world where standards may be lower.

### Cyclones
To calculate financial risk for cyclones, we start with wind speed exposure data in the form of <i>annual exceedance probabilities</i> (also known as Return Periods).  This data essentially describes the annual likelihood of a given wind speed.  We combine this data with regionally specific vulnerability curves from the [CLIMADA](https://nhess.copernicus.org/articles/21/393/2021/) risk analysis framework.  These functions (also known as <i>impact functions</i> or <i>vulnerability curves</i>) describe the expected damage to a given structure type for a given wind speed.  For example, a wind speed of 60 meters per second may damage 50% of a structure's total value, for the typical single family wooden home.

### Wildfires
For wildfire, we take a different approach to measuring damage.  In the event of exposure to wildfire within 1km of an asset, we assume that there is a 10% change that the asset is affected by the fire, and if affected, a fire would destroy 75% of an assets value.  These values are derived from research on historic impacts from wildfires in California.  

## Asset Type Specific Damages
In order to more accurately calculate financial risk, it is possible to upload asset types, via the `label:type` column.  This allows us to apply specialized impact functions based on the uploaded asset type, accounting for industry-specific characteristics.

## Available Asset Types

The available asset types are given in the table below.  For Climate Explorer to recognize an asset type, you must include a column named `label:type` that matches exactly the label given below in **bold**.

| *Category* | *Label for use in CE* | *Examples of this type of asset* | 
| ---------- | -------- | ------- |
| _Agriculture_ | **Agriculture** | Agricultural areas, horse stalls, veterinary offices | 
| _Commercial_ | **Retail Trade** | Appliances, Auto Dealer, Auto Dealership, Bait Stand, Bait Stand, Bakery, Bakery, Boat Sales/Service, Book Store, Book Store, Camera Store, Candy Store, Carpet and Paint Shop, Clothing, Clothing Store, Clothing-Mens, Convenience Store, Crafts, Department Store, Department Store, Drive thru market, Drug, Drug Store, Fabric Store, Feed Store, Flea Market, Florist, Fruit Stand, Furniture, Furniture Store, Gas Station, Gas/Butane Supply, Gift Shop, Greenhouse, Gun Shop, Hardware, Hardware, Hobby Shop, Home Repair Store, Large Furniture, Large Grocery, Lawnmower, Liquor, Liquor Store, Liquor Store, Meat Market, Medium Grocery, Motorcycle Dealer, Music Center, Neighborhood Grocery, Nursery, Paint Store, Pawn Shop, Remnant Shop, Service Station, Service Station, Shoe Repair, Shoe Store, Small Grocery, Supermarket, Toy Store, Tractor Sales, Trophy Shop, Upholstery Shop, Used Appliances/Cloth, Used Furniture, Vacuum Cleaner Sales, Variety Store, Video Games, Wine Store.
| | **Parking** | Garage |
| | **Wholesale Trade** | Auto Junk Yard, Auto Parts/Mufflers, Beer Warehouse, Bottled Gases Warehouse, Food Warehouse, Heavy Equipment Storage, Jewelry, Lumber Yard, Lumber, Machine Parts Storage, Medical Supplies, Municipal Storage Warehouse, Paper Products Warehouse, Private Storage, Quonset Hut Storage, Safety Equipment, Sporting Goods Warehouse, T.V. Repair, T.V. Station, Trailer Parts, Warehouse |
| | **Personal and Repair Services** | Auto Repair, Barber Shop, Beauty Salon, Boat Service, Car Wash, Cemetery, Cleaners substation, Funeral Home, Laundry, Photo Studio, Private Day Care, Re-Upholstery, Truck Mfg & Sales, Washateria, Watch Repair |
| | **Professional/Technical Services** | Accounting Firm, Airport, Big Office Commercial, Boat Storage, Business, Filtering Plant, Import Sales, Legal Office, Office Building, Piers, Professional, Real Estate Office, Sewage Treatment, Transport Company, Utility Company |
| | **Banks** | Bank | 
| | **Hospital** | Hospital |
| | **Medical Office/Clinic** | Chiropractic Clinic, Dentist's Office, Doctor's Office, Medical Office, X-Ray Service |
| | **Entertainment & Recreation** | Bowling Alley, Cafeteria Restaurant, Country Club, Drive-In Restaurant, Fast Food Restaurant, Fishing Party Boat, Full-Service Restaurant, Lounge, Physical Fitness, Private Club, Private Golf Course, Private Pool, Recreation Facilities, Restaurant, T.V. Station, Tavern, Telephone Exchange |
| | **Theaters** | Private Hall, Indoor Theater, Movie Theater, Organization Hall, Drive-In Theater |
| | **Commercial** | Generic grouping for items in _Commercial_ category |
| _Education_ | **Grade Schools** | Commercial School, Library, School, Elementary School | 
| | **Colleges/Universities** | College, University |
| | **Education** | Generic grouping for items in _Education_ category | 
| Government | **General Services** | City Hall, Post Office, Government facility |
| | **Emergency Response** | Fire Station, Police Station |
| | **Government** | Generic grouping for items in _Government_ category | 
| _Industrial_ | **Heavy** | Boiler Building, Cabinet Shop Mfg, Concrete Mfg, Door Mfg, Fabrication Shop, Heat Exchanger Mfg, Heavy Machine Shop, Lumber Mill, Metal Coatings Services, Metal Recycling, Pipe Threader Facility, Research Lab-Machine, Welding-Machine |
| | **Light** | Battery Mfg, Commercial Printing, Cooling Tower, Electronic Equip Mfg, Frame Shop, Furniture Mfg, Industrial Loading Dock, Instrument Mfg, Leather Goods Mfg, Locker Bldg, Maint Bldg-Mfg Facility, Newspaper Print Plant, Newspaper Sales Office, Office-Manuf Facility |
| | **Food/Drugs/Chemicals** | Chemical Laboratory, Chemical Plant Bonding, Chemical Plant, Chemical refinery, Detergent Manuf. Facility, Feed Mill, Food Processor, Meat Packing, Oil Storage Tanks, Plastic Mfg |
| | **Metals/Minerals Processing** | Foundry, Refinery-Lead, Sand & Gravel, Sheet Metal |
| | **High Technology** | Data Center, Microchip Manuf. |
| | **Construction** | Carpet Tile Flooring, Carpeting Service, Construction Co, Contractor Roofing, Contractor-Electric, Heating & Air Conditioning Service, Pier Drilling Co, Plumbing Co, Plumbing Services, Sandblasting Co, Water Well Service |
| | **Industrial** | Generic grouping for items in _Industrial_ category | 
| Religion | **Churches and Other Non-profit Org.** | Church, Civic Association |
| Single Family	| **Single Family Dwelling** | One, two, or three story, with or without basement |
| _Residential_ | **Manuf.  Housing** | Mobile Home, Manufacture Home |
| | **Multifamily Dwelling** | Apartments, Condominium |
| | **Temporary Lodging** | Hotel, Motel |
| | **Institutional Dormitory** | Institutional Dormitory |
| | **Nursing Home** | Nursing Home, Rest Home |
| | **Residential** | Generic grouping for items in _Residential_ category | 

