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

**Available Asset Types**

| Entertainment & Recreation | 
| Retail Trade | 
| Emergency Response | 
| Churches and Other Non-profit Org. | 
| Banks | 
| Construction | 
| Parking | 
| Grade Schools | 
| Personal and Repair Services | 
| Agriculture | 
| Single Family | 
| Institutional Dormitory | 
| Education | 
| General Services | 
| Government | 
| Food/Drugs/Chemicals | 
| High Technology | 
| Residential | 
| Medical Office/Clinic | 
| Theaters | 
| General | 
| Industrial | 
| Religion | 
| Manuf.  Housing | 
| Multifamily Dwelling | 
| Temporary Lodging | 
| Hospital | 
| Single Family Dwelling | 
| Nursing Home | 
| Colleges/Universities | 
| Professional/Technical Services | 
| Commercial | 
| Metals/Minerals Processing | 
| Wholesale Trade | 
| Heavy | 
| Light | 