# Wilfire risk to global forest carbon offset projects

This notebook allows you to explore a collection of 190 global forest carbon projects and their exposure to historical and future wildfire. The analysis is based off of Sust Global's 2023 ICLR paper 'Widespread increases in future wildfire risk to global forest carbon offset projects revealed by explainable AI'. See https://www.climatechange.ai/papers/iclr2023/33 or https://arxiv.org/abs/2305.02397 for the full paper.

The analysis includes both satellite observed wildfires as well as modeled fires using Sust Global's wildfire AI model. The wildfire AI model is trained on 7 million global satellite wildfire observations. Validation results suggest substantial potential for high resolution, enhanced accuracy projections of global wildfire risk, and the model outperforms the U.S. National Center for Atmospheric Research’s leading fire model.

The wildfire AI data provided has been smoothed with a 10-year moving average. If interested in 1) Monthly/annual raw data 2) Precise map views of the results at high (300m-500m) spatial resolution, or 3) Expanded analysis at these projects or new projects, please contact us.

## Requirements

You will need to register with Sust Global to receive an API Key in order to access the wildfire AI data for the 190 projects. Your API Key is unique, and do not share it with others.

## Notebook versions

There are two versions of the analysis, one that calls the API directly 'Wildfire_Risk_Forest_Carbon_SustGlobal_PyClient.ipynb' and one that uses the Sust Global Python client 'Wildfire_Risk_Forest_Carbon_SustGlobal_PyClient.ipynb'. Either are accessible once you have registered and have your unique API key, and the underlying data is the same with either method.