---
layout: blocks
title: FAQ
tags:
- faq
- wildfire
- flood
- questions

blocks:
- block: faq
  heading: General
  faqs: 
  - title: What time period does your historic observation dataset cover?
    content: Our historic observation datasets cover the period from Jan 2010 to Dec 2020.
  - title: What time period does your forward looking projected outcome dataset cover?
    content: Our forward looking projected outcomes assess the period from 2023 to 2100.
  - title: What geographies does your dataset include?
    content: Our capabilities are global. We provide climate scenario analysis over the entirety of the earth’s landmass.
  - title: How does your dataset enable for climate change adaptation?
    content: Our dataset and analytics enable scenario driven analysis for climate change adaptation. Using our API product or the Climate Explorer dashboard, our customers and partners are enabled with asset-level assessments of climate risk exposure from acute and chronic climate related hazards.
  - title: How are are the Low, Medium, and High risk ranges determined for each hazard?
    content: The ranges are determined based on typical ranges of exposures in areas where our customers assets are typically located.  Based on sampling from within these locations, we arrive at threshold values by giving consideration to what would be considered low, medium and high risk for the specific hazard in question.
- block: faq
  heading: Wildfire
  faqs:
  - title: Why do I see active fires within the dataset, but no projected scenario based fire hazards?
    content: 'There are occasionally sites where we see observed active fires and no projected scenario based fire hazard. This could be due to: Human generated fires that are not controlled fires and not wildfires; Limitations of the wildfire projection models; Changing risk exposure. 


    For more detail:

    1. This could be due to erroneous historic data. The MODIS satellites use temperature to estimate fire prevalence, so other activities that generate fire/heat can appear as wildfire. This includes power plants, gas flares, or prescribed burns.

    2. It could be flaws in CMIP6 models, especially when fires are driven by processes too small-scale for coarse models to capture. Our product should deal with that in most cases, but not all.

    3. Your probability of future risk exposure may also appear as 0 due to shifting land use patterns in the future. Changing vegetation cover due to drying or expanding urbanization can decrease future risk in areas with high historic risk.'
  - title: Which values are relevant when the historic fire data and future projections disagree?
    content: The historic data will be a better indicator of near-term fire risk but the climate models will be a better indicator of long-term, decadal and multi-decadal fire risk.
  - title: How do you determine the severity of wildfire risk?
    content: Historic fire severity is represented by the number of active fires within 10km radius of the asset, scaled to a value between 0 and 1.0.
  - title: How are controlled burns determined?
    content: We use satellite derived observations, which means that we cannot determine which fires are human generated vs natural fire. However, controlled burns surface as observed fires in the historic exposure. The forward looking fire exposure across scenarios accounts for controlled burns on agricultural land.
  - title: Why is the probability of future risk exposure 0 if my asset has historic wildfire risk?
    content: Your probability of future risk exposure may appear as 0 due to shifting land use patterns in the future.  Changing vegetation cover due to drying or expanding urbanization can decrease future risk in areas with high historic risk. Alternatively, it could be erroneous historic data.  The MODIS satellite dataset, that we use for our historic fire exposure estimates uses temperature to estimate fire prevalence, so other activities that generate fire/heat can appear as wildfire.  This includes power plants, gas flares, or prescribed burns. There could be flaws in CMIP6 models, especially when fires are driven by processes too small-scale for coarse models to capture. Our SuperResolution capability deals with this in most cases, but not always.
- block: faq
  heading: Flooding
  faqs:
  - title: Does historic and projected flooding include both coastal and inland flooding?
    content: Historic flooding covers inland and coastal flooding. Projected flooding data only covers inland flooding. You can look at the cyclone projections and sea level rise projections as indicators of forward looking coastal flooding.
  - title: In the user guide, it stated that all climate models for flooding and tropical cyclones run under the High Emissions (SSP5-RCP8.5) pathway scenario, thus all values shown for the Strong Mitigation (SSP1-RCP2.6) and Middle of the Road (SSP2-RCP4.5) scenarios are identical to those of the High Emissions scenario. Can you explain why this is the case?
    content: We have yet to find reliable representations of inland flooding and cyclone projections for SSP1-RCP26 and SSP2-RCP45 and will update when we have them.
  - title: The flooding data reports the probability of flooding exceeding 0.5 m - where does the 0.5 meters come from?
    content: It is common for flood models to add a "doorstep" value below which flooding does no damage.  This is to account for the fact that buildings are sometimes raised a small distance above the ground, especially in flood-prone areas, and to account for the fact that a small amount of flooding can normally be contained using simple ad-hoc flood prevention measures like sandbags.  While there is no universally agreed upon value for this "doorstep" threshold, 0.5 meters is commonly used.
- block: faq
  heading: Dashboard
  faqs:
  - title: Why is my hazard HIGH-risk on the risk heat map view, but LOW-risk on the multi-hazard view?
    content: We take risk values, re-normalize them according to a maximum value, and then apply new thresholds. Therefore,  the risk heat map classifications are not necessarily indicative of multi-hazard classifications. Assets on the risk heat map are labeled (colored) based on the categories of LOW/MEDIUM/HIGH as outlined in our documentation on our developer center. The multihazard heatmap is based on a combined score derived from risk exposure to the asset across all the different hazards.
  - title: Is the overall severity coloring based on the highest category risk or is it based on the normalization method mentioned in the user guide?
    content: Overall severity is based on the maximum risk across all hazards, determined by the normalization method described in the user guide.
  - title: Is asset level loss associated with the highest risk category used for severity coloring, or does it represent overall asset loss estimates for all hazards?
    content: Asset level risk is based on the estimate of the loss from a specific hazard. The heatmap color indicates the level of exposure across all the assets in the portofolio. The value of the asset is scaled by the level of exposure to determine the estimated loss in the estimated value at risk summary.
  - title: What does the “distribution by type” option for Estimated Value at Risk Summary mean?
    content: Distribution by type is a grouping of all assets of the same type to create one slice (category). This is based on the aggregated value of estimated loss, determined by the type of assets.
  - title: Why does the cyclone projection tend to be a flat line beyond the year 2050?
    content: We provide annual cyclone projections over the years 1980-2050. Beyond the year 2050, we use the mean probability of cyclone projections over the 2030-2050 window for that specific asset location.
- block: faq
  heading: Dataset (CSV)
  faqs:
  - title: What does the risk exposure file nomenclature mean (e.g., ubd vs lbd)?
    content: No postfix represents the midpoint value. ubd and lbd represent upper and lower bound values (usually mapped to the 16th and 84th percentiles from the distribution of simulation runs for climate models for the specific hazard), and are indicative of the values for the gray bars in the time series plot.
  - title: Why do the historic values of a hazard change with each scenario?
    content: The historic values of a hazard beginning in 2015 are derived from simulation runs across multiple scenarios. There will be minor variability for the historic years (2015-present) across scenarios.

---