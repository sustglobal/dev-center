---
title: Climate Explorer API Guide
toc: true
---

Sust Global's Climate Explorer API is a RESTful API interface to to Sust Global's climate intelligence capabilities. 
The API is currently enables users to access generated physical risk exposure datasets programmatically.
This guide helps users learn how to work with the API directly.

## Quickstart

To quickly get up and going with the Climate Explorer API, you first must retrieve your API key.
Navigate to your [Climate Explorer User Profile](https://explorer.sustglobal.io/account/profile/) and copy the value of `API Key`.
This value will be referenced below as `$APIKEY`.

Open a local terminal, then run the following `curl` command:

```
curl https://explorer.sustglobal.io/api/portfolios/?api_key=$APIKEY
```

The output will contain a set of all portfolios you currently may access. For example, a single portfolio named "DEMO":

```
[
  {
    "portfolio_id": "95f83d71cd9de1bb",
    "portfolio_name": "DEMO",
    "created_at": "2021-12-03T17:46:17Z",
    "status": "Risk data available"
  }
]
```

This response tells us that the "DEMO" portfolio already has physical risk exposure data.
Before we fetch any risk-related data, we will first retrieve the assets from the portfolio.
Be sure to substitute `$PORTFOLIO` with the name of your own portfolio:

```
curl https://explorer.sustglobal.io/api/portfolios/DEMO/assets?api_key=$APIKEY
```

This portfolio happens to contain a single asset:

```
[
  {
    "id": 9064,
    "entity_name": "Half Dome",
    "lat": 37.74586759398789,
    "lng": -119.53319929681618,
    "address": "Yosemite Valley, CA",
    "type": "Mountain",
    "tag": "Yosemite",
    "price": ""
  }
]
```

We can fetch a summary of this data with the following command.

```
curl https://explorer.sustglobal.io/api/portfolios/$PORTFOLIO/datasets/physical/risk?api_key=$APIKEY
```

The result summarizes the physical risk exposure of the asset.
Note that the output below has been truncated.

```
[
  {
    "asset_id": 9064,
    "entity_name": "Half Dome",
    "date_validation": "2021-12-03T21:00:53Z",
    "risk_summary": {
      "ssp126": {
        "fire_label": "LOW",
        "flood_label": "LOW",
        "heatwave_label": "LOW",
        "drought_label": "MEDIUM",
        "sealevelrise_label": "LOW",
        "cyclone_label": "LOW",
        "fire_score": 0.000709628453478217,
        "flood_score": 0,
	...
```

Read through the remainder of this document from here to learn about other aspects of the API.

## API Mechanics

### Authentication

All API requests must be authenticated using an API key.
Find your own API key at in your [Climate Explorer User Profile](https://explorer.sustglobal.io/account/profile/).

To authenticate an API request, simply pass your API key as a query parameter named `api_key`.
For example, if your API key were "FOOBAR" then you would authenticate your request like so:

```
curl https://explorer.sustglobal.io/api/portfolios/?api_key=FOOBAR
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
