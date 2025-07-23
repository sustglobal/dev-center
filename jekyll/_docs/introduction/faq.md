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
    content: Our historic observation datasets cover the period from Jan 2010 to Dec 2024 for Cyclone, Heatwave, Water Stress, and Wildfire exposure. For historical Sea-Level Rise, the data spans Jan 2010 to Dec 2022. For historical flood risk, the data spans Jan 2012 to April 2022.
  - title: What time period does your forward looking projected outcome dataset cover?
    content: Our forward looking projected outcomes assess the period from 2025 to 2100.
  - title: What geographies does your dataset include?
    content: Our capabilities are global. We provide climate scenario analysis over the entirety of the earth’s landmass.
  - title: How does your dataset enable for climate change adaptation?
    content: Our dataset and analytics enable scenario driven analysis for climate change adaptation. Using our API product or the Climate Explorer dashboard, our customers and partners are enabled with asset-level assessments of climate risk exposure from acute and chronic climate related hazards.
  - title: How are are the Low, Medium, and High risk ranges determined for each hazard?
    content: The ranges, defined in the Climate Data Guide, are determined based on typical ranges of exposures in areas where our customers assets are typically located.  Based on sampling from within these locations, we arrive at threshold values by giving consideration to what would be considered low, medium and high risk for the specific hazard in question.
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
    content: Both historic and projected flooding cover inland and coastal flooding. Coastal flooding accounts for storm surge as well as sea-level rise.
  - title: Do you include fluvial (riverine) and pluvial flood risk?
    content: The inland component of our flood risk model covers only riverine flood risk. We are exploring pluvial flood risk models, so contact us if this is critical.
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
  - title: What do the upper and lower bounds represent?
    content: Upper and lower bounds reflect the 16th and 84th confidence interval bands, which corresponds approximately to +/- 1 standard deviation. Occasionally, risk data skews towards either bound for a particular hazard type based on the hazard model. Generally, the probability bounds can never go below 0 or above 1. In the case of flood probability, values are capped at 0.5.
  - title: Why are some hazards and subsequent financial risks constant with time?
    content: If projected exposure and risk values are similar to present day, it suggests a weak or non-existent relationship between climate change and a given hazard at a particular location. Climate change will impact hazard severity and frequency in unique ways. Further, any changes will not be uniform across the globe. For another hazards like flooding and tropical cyclones, the absence of increasing risk likely reflects a weak or non-existent relationship between a hazard event and rising global temperatures. However, concerning wildfire, our hazard model considers not only weather conditions condusive to wildfires (i.e., fire weather), but variables such as historical burn scars and other metrics that increase ignition potential. While fire weather generally incerases with climate change, constant wildfire risk over time can reflect the lack of a detectable relationship between fire weather and fire risk at a given location.
- block: faq
  heading: Dataset (CSV)
  faqs:
  - title: What does the risk exposure file nomenclature mean (e.g., ubd vs lbd)?
    content: No postfix represents the midpoint value. ubd and lbd represent upper and lower bound values (usually mapped to the 16th and 84th percentiles from the distribution of simulation runs for climate models for the specific hazard), and are indicative of the values for the gray bars in the time series plot.

---
