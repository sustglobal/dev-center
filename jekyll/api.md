---
title: Climate Explorer API Guide
toc: true
---

Sust Global's Climate Explorer API is a RESTful API interface to Sust Global's climate intelligence capabilities. 
The API currently enables users to access generated physical risk exposure datasets programmatically.
This guide helps users learn how to work with the API directly.

## Quickstart

To quickly get up and going with the Climate Explorer API, you first must retrieve your API key.
Navigate to your [Climate Explorer User Profile](https://explorer.sustglobal.io/account/profile/) and copy the value of `API Key`.
This value will be referenced below as `$APIKEY`.

Open a local terminal, then run the following `curl` command:

```
curl "https://explorer.sustglobal.io/api/portfolios/?api_key=$APIKEY&project=ec-DEMO"
```

A successful response from the portfolios endpoint will contain a set of all portfolios you currently may access.
For example, a single portfolio named "MRTG_demo":

```
{
  "portfolio_id": "f150aac833c2c6c2",
  "portfolio_name": "MRTG_demo",
  "created_at": "2022-02-03T11:47:37Z",
  "updated_at": "2022-02-12T23:28:59Z",
  "status": "Risk data available"
}
```

This response tells us that the `MRTG_demo` portfolio already contains physical risk exposure data.
Before we fetch any risk-related data, we will first retrieve the assets from the portfolio:

```
curl "https://explorer.sustglobal.io/api/portfolios/MRTG_demo/assets?api_key=$APIKEY&project=ec-DEMO"
```

The output below is a single object from the list of assets you will observe:

```
{
  "portfolio_name": "MRTG_demo",
  "portfolio_index": 30,
  "entity_id": "",
  "entity_name": "760",
  "lat": 38.764016,
  "lng": -121.244538,
  "labels": {
    "tag": "56,628 SF",
    "type": "Office",
  }
}
```

Now, we can fetch a summary of the risk exposure data pertaining to this portfolio with the following command:

```
curl "https://explorer.sustglobal.io/api/portfolios/MRTG_demo/datasets/physical/summary?api_key=$APIKEY&project=ec-DEMO"
```

A single object from the response is displayed below:

```
{
  "portfolio_name": "MRTG_demo",
  "portfolio_index": 228,
  "entity_name": "302",
  "entity_id": "",
  "window": 15,
  "window_start_year": 2022,
  "scenario": "ssp126",
  "risk_summaries": [
    {
      "hazard": "cyclone",
      "risk_class": "LOW",
      "risk_score": 0
    },
    {
      "hazard": "flood_potential",
      "risk_class": "LOW",
      "risk_score": 0
    },
    {
      "hazard": "heatwave",
      "risk_class": "LOW",
      "risk_score": 0.11072656322738
    },
    {
      "hazard": "sea_level_rise",
      "risk_class": "LOW",
      "risk_score": 0
    },
    {
      "hazard": "water_stress",
      "risk_class": "LOW",
      "risk_score": 0.472303866057673
    },
    {
      "hazard": "wildfire",
      "risk_class": "LOW",
      "risk_score": 0
    }
  ]
}
```

To fetch the more granular timeseries data, we can use the "items" endpoint.
We can also apply some filters this time around: `hazard=wildfire`, `scenario=ssp585`, and `start_date=2022`

```
curl "https://explorer.sustglobal.io/api/portfolios/MRTG_demo/datasets/physical/items?api_key=$APIKEY&project=ec-DEMO&hazard=wildfire&scenario=ssp585&start_date=2022"
```

Below is a truncated object from the response:

```
{
  "portfolio_name": "MRTG_demo",
  "portfolio_index": 49,
  "entity_id": "",
  "entity_name": "167",
  "scenario": "ssp585",
  "hazard": "wildfire",
  "indicator": "burned_area_norm",
  "measure": "mid",
  "risk_exposure": {
    "2022": 1.530678391456604,
    "2023": 5.00434160232544,
    "2024": 1.4145750999450684,
    "2025": 1.45624041557312,
    "2026": 2.020421028137207,
    "2027": 2.387681722640991,
    "2028": 2.2932016849517822,
    "2029": 2.7874271869659424,
    "2030": 2.900757312774658,
    "2031": 1.892580509185791,
    ...
```

Read through the remainder of this document from here to learn about other aspects of the API.

## API Mechanics

### Authentication

All API requests must be authenticated using an API key.
Find your own API key at in your [Climate Explorer User Profile](https://explorer.sustglobal.io/account/profile/).

To authenticate an API request, simply pass your API key as a query parameter named `api_key`.
For example, if your API key were `FOOBAR` then you would authenticate your request like so:

```
curl "https://explorer.sustglobal.io/api/portfolios/?api_key=FOOBAR"
```

### Projects

Note that a project must typically be indicated via a `project` query parameter.
You can programmatically identify which projects you may access via the `/api/projects/` endpoint:

```
% curl "https://explorer.sustglobal.io/api/projects/?api_key=$APIKEY"
[
  {
    "project_id": "a19b6282de313211",
    "project_name": "ec-DEMO"
  }
]
```

You may use either the `project_id` or `project_name` value in the query parameter.
For example, using the project name:

```
curl "https://explorer.sustglobal.io/api/portfolios/?api_key=$APIKEY&project=ec-DEMO"
```

...or the project ID:

```
curl "https://explorer.sustglobal.io/api/portfolios/?api_key=$APIKEY&project=a19b6282de313211"
```

### Pagination

Many API endpoints support paginated requests. This allows a consumer of the API to make a series of API requests, each
time reading a subset of the total result set.

Users control pagination with the `page` and `rows` query parameters. The value of `rows` sets the maximum number of results
that the API should return for a given `page`.

The default `rows` value is 50, meaning that a client is forced to paginate their requests if more than 50 items exist in a given list.

An example of pagination over a set of 120 items might work like so:

1. Request one sets `page=1` and `rows=50`, receiving 50 items
2. Request two sets `page=2` and `rows=50`, receiving 50 items
3. Request two sets `page=3` and `rows=50`, receiving 20 items

Note that once a set of items smaller in number than the value of `rows` is received from a paginated request, the client should
halt any further requests.

## Error Responses

When an API request fails, clients should always consider the HTTP status code.
Status codes are used as accurately as possible. For example, when an invalid
request is made, a `400 Bad Request` code will be returned.

In addition to the status code, clients should also attempt to parse a
JSON-encoded error response available in the HTTP response body.
The JSON object contains one of more human-readable errors, represented
as an array of strings. For example:

```
{
    "errors": [
        "lat: coordinate out of bounds"
    ]
}
```

It is inadvisable to attempt to parse meaningful data from error strings, as they
will evolve over time as Sust Global capabilities expand. In other words, there
is no contract established in the content of error strings.

## API Examples

This section contains a set of example commands you can run on your machine to interact with the API.

Note that many of the examples refer to environment variables that must be set manually:
* Your API key, must be set in the `$APIKEY` environment variable. See [Authentication](#authentication) to learn more about this.
* The `$PORTFOLIO` environment variable refers to the name of the portfolio you wish to work with. You determine this value.

### Create a Portfolio

To create a new portfolio, simply run the following cURL command:

```
curl -i -X POST "https://explorer.sustglobal.io/api/portfolios/?api_key=$APIKEY&project=$PROJECT&portfolio=$PORTFOLIO"
```

### Upload Assets to a Portfolio

Once you have created a portfolio, you may upload a CSV file containing your assets using the following command.
The value of `$ASSET_FILE` must be the location of a local CSV file containing assets.
Please see the [Climate Explorer Guide](/explorer.html) for more information about assets and CSV file requirements.

```
curl -i -F asset=@$ASSET_FILE "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/assets/import?api_key=$APIKEY&project=$PROJECT"
```

### Export Portfolio Assets

It may be useful to download all assets in a given portfolio to a local CSV file.
This is primarily useful when you intend to re-upload a modified set of assets to a portfolio.

```
curl -OJ "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/assets/export?api_key=$APIKEY&project=$PROJECT"
```

A CSV file will be written to the filesystem.

### Fetch Physical Risk Exposure Timeseries Data

After physical risk exposure data has been generated, one may interact with it natively via the API:

```
curl -i "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/datasets/physical/items?api_key=$APIKEY&project=$PROJECT"
```

Note that this endpoint will contain a lot of data, so you should be familiar with pagination controls. Documentation is
available earlier in this guide.

Additional query parameters that may be useful include `scenario`, `hazard`, `indicator` and `measure.
An example of filtering the risk exposure dataset to SSP2-4.5 for a specific wildfire-related indicator:

```
curl -i "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/datasets/physical/items?api_key=$APIKEY&project=$PROJECT&scenario=ssp245&hazard=wildfire&indicator=burned_area_norm&measure=mid"
```

Please review the API Reference for documentation of all supported query parameters.

### Summarize Physical Risk Exposure

A summary of physical risk exposure data with an optional `scenario` filter is available via API:

```
curl -i "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/datasets/physical/summary?api_key=$APIKEY&project=PROJECT"
```

### Export Physical Risk Exposure

Download a ZIP archive containing the physical risk exposure data for a specific portfolio using the following command:

```
curl -OJ "https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/datasets/physical/export?api_key=$APIKEY&project=$PROJECT"
```

A ZIP file will be written to the filesystem.

## API Endpoint Reference

You may access the [Climate Explorer API Reference](https://explorer.sustglobal.io/redoc/), which describes every REST endpoint, parameter, request and response.

## OpenAPI / Swagger

The Climate Explorer API is documented using OpenAPI (Swagger).
You may access the document at the following URI:

```
https://explorer.sustglobal.io/swagger.json
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
