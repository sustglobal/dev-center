---
layout: doc
title: Search User Guide
subtitle: Sust Global's Search API is a RESTful API interface to Sust Global's rapid retrieval of a single data point. The API currently allows users to supply a lat/lon pair, and instantly get a result on the risk at that location and in the nearby area, for both the near and medium term.
date: 2022-12-14
lastmod: 2023-12-05
author: JPC
tags:
- search
- api
- quickstart
---

## Search UI Quickstart

In the Climate Explorer dashboard, go to the Account menu and click on the `Search` option. On the screen presented, type in the address or the coordinates of the location you want to check.

<p align="center">
<img height="400" src="assets/images/userguide/Search_dashboard.png">
</p>

<p align="center">
<img height="400" src="assets/images/userguide/search_dashboard_coords.png">
</p>

<p align="center">
Search functionality in the Climate Explorer dashboard
</p>

## Search API Quickstart

To quickly get up and going with the Climate Explorer Search API, you first must retrieve your API key. Navigate to your [Climate Explorer User Profile](https://explorer.sustglobal.io/account/profile/) and copy the value of **API Key**. This value will be referenced below as **$APIKEY**.

Open a local terminal, then run the following `curl` command (make sure to replace the `APIKEY`, `PROJECT`, `LAT`, and `LONG` with their corresponding values):

```
curl "https://explorer.sustglobal.io/api/search?lat=$LAT&lng=$LONG" --header "X-SustGlobal-APIKey: $APIKEY" --header "X-SustGlobal-Project: $PROJECT"
```

A successful response from the portfolios endpoint will contain the risk information associated with the location (coordinates) provided. For example:

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "physical_risk_exposure": {
          "background": {
            "15yr": [
              {
                "hazard": "floods",
                "score": 0.10615108185447752,
                "label": "HIGH"
              },
              {
                "hazard": "cyclones",
                "score": 0,
                "label": "LOW"
              },
              {
                "hazard": "drought",
                "score": 0.07531279841012768,
                "label": "LOW"
              },
              {
                "hazard": "heatwaves",
                "score": 13.536979079246521,
                "label": "LOW"
              },
              {
                "hazard": "sea_level_rise",
                "score": 0.026802367565812456,
                "label": "LOW"
              },
              {
                "hazard": "wildfire",
                "score": 0,
                "label": "LOW"
              }
            ],
            "30yr": [
              {
                "hazard": "floods",
                "score": 0.11163490801118314,
                "label": "HIGH"
              },
              {
                "hazard": "cyclones",
                "score": 0,
                "label": "LOW"
              },
              {
                "hazard": "drought",
                "score": 0.0987541839030649,
                "label": "LOW"
              },
              {
                "hazard": "heatwaves",
                "score": 16.12977159023285,
                "label": "LOW"
              },
              {
                "hazard": "sea_level_rise",
                "score": 0.04028329250311741,
                "label": "LOW"
              },
              {
                "hazard": "wildfire",
                "score": 0,
                "label": "LOW"
              }
            ]
          },
          "local": {
            "15yr": [
              {
                "hazard": "cyclones",
                "score": 0,
                "label": "LOW"
              },
              {
                "hazard": "drought",
                "score": 0.07122914524118835,
                "label": "LOW"
              },
              {
                "hazard": "heatwaves",
                "score": 13.53125,
                "label": "LOW"
              },
              {
                "hazard": "sea_level_rise",
                "score": 0.03152499967951014,
                "label": "LOW"
              },
              {
                "hazard": "floods",
                "score": 0.2212430238723755,
                "label": "HIGH"
              },
              {
                "hazard": "wildfire",
                "score": 0,
                "label": "LOW"
              }
            ],
            "30yr": [
              {
                "hazard": "cyclones",
                "score": 0,
                "label": "LOW"
              },
              {
                "hazard": "drought",
                "score": 0.09704220998046496,
                "label": "LOW"
              },
              {
                "hazard": "heatwaves",
                "score": 16.00806427001953,
                "label": "LOW"
              },
              {
                "hazard": "sea_level_rise",
                "score": 0.047384368968447506,
                "label": "LOW"
              },
              {
                "hazard": "floods",
                "score": 0.23287193477153778,
                "label": "HIGH"
              },
              {
                "hazard": "wildfire",
                "score": 0,
                "label": "LOW"
              }
            ]
          }
        }
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -122.8242285597761,
          47.09764797110564
        ]
      }
    }
  ]
}
```

## API Mechanics

The Search API mechanics follow the same guidelines as the ones presented in the [Climate Explorer API Guide](https://developers.sustglobal.com/api-guide#api-mechanics).

## Error Responses

When an API request fails, clients should always consider the HTTP status code. Status codes are used as accurately as possible. For example, when an invalid request is made, a **400 Bad Request** code will be returned.

In addition to the status code, clients should also attempt to parse a JSON-encoded error response available in the HTTP response body. The JSON object contains one of more human-readable errors, represented as an array of strings. For example:

```
{
  "errors": [
    "project nonexistent or lacking authorization"
  ]
}
```

It is inadvisable to attempt to parse meaningful data from error strings, as they will evolve over time as Sust Global capabilities expand. In other words, there is no contract established in the content of error strings.

## API Endpoint Reference

You may access the [Climate Explorer Search API Reference](https://explorer.sustglobal.io/redoc/#operation/search_list), which describes every REST endpoint, parameters, request and responses.

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
