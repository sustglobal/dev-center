---
layout: doc
title: Nature API User Guide
subtitle: Sust Global's Nature API is a RESTful API interface to Sust Global's nature and carbon intelligence capabilities. This guide helps users learn how to work with the API directly.
date: 2023-11-17
lastmod: 2023-11-17
author: TA
tags:
- api
- quickstart
---

## Quickstart

To quickly get up and going with the Nature API, you first must retrieve your API key.
Navigate to your [Nature User Profile](https://nature.sustglobal-dev.io/account/profile) and copy the value of **API Key**.
This value will be referenced below as **$APIKEY**.

Open a local terminal, then run the following **curl** command:

```bash
curl "https://api.nature.sustglobal.io/projects" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: nc-demo"
```

If you have **jq** installed, you may prefer to pipe the result through for better viewing:

```bash
curl "https://api.nature.sustglobal.io/projects" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: nc-demo" | jq .
```

A successful response from the projects endpoint will contain a set of all sub-projects you currently may access.
For example, a single sub-project named "VCS1378 - ARR Chinchina River":

```
[
  {
    "id":"5e547b14-93cb-11ee-bb5b-3fac1250342e",
    "project":"nc-demo",
    "name":"VCS1378 - ARR Chinchina River",
    "status":"Processing Completed",
    "type":"Forest Carbon"
  }
]
```

This response status ("Processing Completed") tells us that the **VCS1378 - ARR Chinchina River** sub-project already contains summary data. We can fetch this data with the following command, where the ID in the URL corresponds to the ID of the sub-project:

```bash
curl "https://api.nature.sustglobal.io/projects/5e547b14-93cb-11ee-bb5b-3fac1250342e/export" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: nc-demo"
```

Likewise with **jq** included:
```bash
curl "https://api.nature.sustglobal.io/projects/5e547b14-93cb-11ee-bb5b-3fac1250342e/export" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: nc-demo" | jq .
```

A truncated version of the response is displayed below:

```
{
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [ ... ]
    },
    "metadata": {
        "Entity Name": "VCS1378",
        "label:project_name_sqkm": "Forestry Project for the Basin of the Chinchina River, an Environmental and Productive Alternative for the City and the Region",
        "label:country": "Colombia",
        "Type": "Forestry and Land Use",
        "label:continent": "South America",
        "label:poly_area": 1196.7751479009767
    },
    "summary": {
        "pest_disease_baseline_mean": 4,
        "seismic_baseline_mean": 2.7344253333333333,
        "wildfire_carbon_loss_baseline_mean": 0.9609010907672909,
        "wildfire_observed_baseline_mean": 0,
        "wildfire_ssp585_baseline_mean": 0.0005720844798136863,
        "wildfire_ssp585_2050_mean": 0.0006717108151462417,
        "water_balance_ssp585_2050_mean": 1135.5001212914913
    }
}
```

Read through the remainder of this document from here to learn about other aspects of the API.

## API Mechanics

### Authentication

All API requests must be authenticated using an API key.
Find your own API key at in your [Nature User Profile](https://nature.sustglobal.io/account/profile).

To authenticate an API request, simply pass your API key as an HTTP header named **X-SustGlobal-APIKey**.
For example, if your API key were **MY_API_KEY** then you would authenticate your request like so:

```
curl "https://api.nature.sustglobal.io/projects" --header "X-SustGlobal-APIKey: MY_API_KEY"
```

### Projects

Note that a project must typically be indicated via a **project** HTTP header.
You can programmatically identify which projects you may access via the **/superprojects/** endpoint:

```bash
curl "https://api.nature.sustglobal.io/superprojects" --header "X-SustGlobal-APIKey: $APIKEY"
```

Results will look like:
```
[
    "nc-demo"
]
```

Then for subsequence API calls, use the **project_name** value in the HTTP headers.
For example:

```
curl "https://api.nature.sustglobal.io/projects" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: nc-demo"
```

## API Examples

This section contains a set of example commands you can run on your machine to interact with the API.

Note that many of the examples refer to environment variables that must be set manually:
* Your API key, must be set in the **$APIKEY** environment variable. See [Authentication](#authentication) to learn more about this.
* The **$PROJECT** environment variable refers to the name of the project you wish to work with. You determine this value.

### Upload a new Sub-Project From a File

To upload a new sub-project from a file, you will need to have access to a file with the geojson representation of the project area, 
and [jq](https://jqlang.github.io/jq/) installed.

See the following example for a file named **MYGEOJSONFILE.geojson** uploading to a sub-project named **My Project**:

```bash
jq -n --slurpfile geojson MYGEOJSONFILE.geojson '{"projectName": "My Project","geojson": $geojson[],"type": "NCS"}' \
 | curl "https://api.nature.sustglobal.io/projects" \
   --header "X-SustGlobal-Project: $PROJECT" \
   --header "X-SustGlobal-APIKey: $APIKEY" \
   --header "Content-Type: application/json" \
   --data @-
```

### Upload a new Sub-Project Directly From Command Line

To upload a new sub-project directly from the command line, you will need to include a geojson representation of the project area. See the following example:

```bash
curl -i -X POST "https://api.nature.sustglobal.io/projects" \
--header "X-SustGlobal-APIKey: $APIKEY" \
--header "X-SustGlobal-Project: $PROJECT" \
--header 'Content-Type: application/json' \
--data '{
    "projectName": "cURL Test",
    "geojson": {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "Entity Name": "PLAN_VIVO-160821804314941641368371873322842545572",
                    "label:project_name_sqkm": "Babatana Rainforest Conservation Project (Sirebe)",
                    "label:country": "Solomon Islands",
                    "Type": "Forestry and Land Use",
                    "label:continent": "Oceania",
                    "label:poly_area": 8.1214649910303081
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                156.80579365893459,
                                -6.969562860514157
                            ],
                            [
                                156.794210750667588,
                                -6.994757321999014
                            ],
                            [
                                156.773269899563275,
                                -6.982389131815538
                            ],
                            [
                                156.796501156257051,
                                -6.966945254126119
                            ],
                            [
                                156.80579365893459,
                                -6.969562860514157
                            ]
                        ]
                    ]
                }
            }
        ]
    },
    "type": "NCS"
}'
```

### Export Sub-Project Summary as File

To export the sub-project summary results as a file (make sure to set the **$PROJECTID**):

```
curl -OJ "https://api.nature.sustglobal.io/projects/$PROJECTID/export" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: $PROJECT"
```

This will write a json file to the filesystem.


## API Endpoint Reference

You may access the [Nature API Reference](https://api.nature.sustglobal.io/docs), which describes every REST endpoint, parameter, request and response.

## OpenAPI / Swagger

The Nature API is documented using OpenAPI (Swagger).
You may access the document at the following URI:

```
https://api.nature.sustglobal.io/openapi.json
```

This URL is publicly-accessible and is automatically updated as the API evolves.

## Citing Sust Global API

From a concept to adoption by an emerging group of early adopters, many people have invested time and energy in developing and enabling access to Sust Global's capabilities. Please cite Sust Global when using our data and insights. To cite Sust Global's data in publications, please use the following:

```
Sust Inc (2021). Sust Global Application Programming Interface: Transforming frontier climate science to actionable data. https://developers.sustglobal.com.
```

```
@Misc{,
  author       = {Sust Global Team},
  organization = {Sust Inc},
  title        = {Sust Global Application Programming Interface: Transforming frontier climate science to actionable data},
  year         = {2021--},
  url          = "https://developers.sustglobal.com"
}
```
