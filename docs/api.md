---
title: Sust Global API Introduction
---

# Sust Global API Introduction

Sust Global enables customers in the financial service space with physical risk exposure assessments using our climate intelligence product offering. Sust Global's API is a RESTful API interface to Sust Global's climate intelligence capabilities. 

Sust Global API is intended to enable users with the following capaibilities:
* Trigger the creation of physical climate risk exposure data for a specific collection of assets (sites) defined by the user
* Enable direct access to climate risk data for download and replication in user's data stores and data warehouses for use in the user's own analysis and application development.

The topics covered in this document include:
* Table of Contents
{:toc}

## How to become a Sust Developer

Using the Sust Global API requires that you have a Sust API key: if you don't already have an account with us, you can [reach out](mailto:sales@sustglobal.com) to us for an API key.

Once you're signed up, you can find your API key in your account settings. 

## API Endpoints

The `/create` endpoint allows users to trigger and create a risk data collection based on a single asset or an input csv file where each row corresponds to an asset in an asset collection. 

The `/collections` end point list the collections that a user has access to. The user can query the API for the assets, risk datasets and risk summaries associated with any specific collection in the list of collections.

## Retrieve collections

```bash
/v1/riskdataset/collections
```

### Required parameters
None

### Response
The response is a list of collections accessible to the user with the specified key. Each item in the list would have the following properties:
- `id`: id of the collection
- `date_creation`: date of creation of the collection
- `date_validation`: date of validation of the resulting risk data collection
- `collection_name`: user defined name of the collection
- `collection_name_api`: name of the collection for access by API end points
- `status`: status of the risk collection dataset

### Example Usage
`curl -X GET "https://sustglobal.io/api/v1/riskdataset/collections/?api_key=YOUR_SUST_API_KEY"`


## Retrieve assets in a collection

```bash
/v1/riskdataset/{selected_collection}/assets/sync
```

### Required parameters
Requires the user the specify the asset collection for which the assets are retrived
- `selected_collection`
- `rows`: number of items retrieved (max:250)
- `page`: number of the page retrieved 

### Response
The response is a list of assets in a collection accessible to the user with the specified key. Each item in the list would have the following properties:
- `id`: id of the asset 
- `entity_name`: name of the asset
- `lat`: latitude of the asset
- `lng`: longitude of the asset
- `address`: address of the asset (could be blank)
- `type`: user defined type of the asset
- `tag`: user assigned tag to the asset (could be blank)
- `price`: user assigned price to the asset (could be blank)

### Example Usage
`curl -X GET "https://sustglobal.io/api/v1/riskdataset/{selected_collection}/assets/sync?api_key="YOUR_SUST_API_KEY"`


## Retrieve items in a risk dataset for a specific collection

```bash
/v1/riskdataset/{selected_collection}/items
```

### Required parameters
Requires the user the specify the asset collection for which the assets are retrived
- `selected_collection`
- `risk_type`: risk type of interest [fire/flood/SPEI/SLR/heatwaves]
- `scenario`: define the climate scenario [ssp126/ssp245/ssp585]
- `start_date`: define the start date from which the collection is filtered
- `end_date`: define the end date to which the collection is filtered
- `rows`: number of items retrieved (max:250)
- `page`: number of the page retrieved 

### Response
The response is a list of items in a risk dataset for a specific collection accessible to the user with the specified key. Each item in the list would have the following properties:
- `id`: id of the risk dataset item 
- `collection`: name of the collection
- `risk_type`: risk type
- `scenario`: climate scenario 
- `date_validated`: date when the assigned risk dataset has been validated
- `asset_id`: id of the asset to which this risk dataset item belongs
- `risk_exposure`: annual or monthly risk exposure as floating point values

### Example Usage
`curl -X GET "https://sustglobal.io/api/v1/riskdataset/{selected_collection}/items&risk_type={risk_type}&scenario={scenario}?api_key="YOUR_SUST_API_KEY"`

## Retrieve risk data summary for a specific collection

```bash
/v1/riskdataset/{selected_collection}/summary
```

### Required parameters
Requires the user the specify the asset collection for which the assets are retrived
- `selected_collection`
- `rows`: number of items retrieved (max:250)
- `page`: number of the page retrieved 

### Response
The response is a list of summary items in a risk dataset for a specific collection accessible to the user with the specified key. Each item in the list would have the following properties:
- `id`: id of the risk dataset item 
- `collection`: name of the collection
- `risk_type`: risk type
- `scenario`: climate scenario 
- `date_validated`: date when the assigned risk dataset has been validated
- `asset_id`: id of the asset to which this risk dataset item belongs
- `risk_summary`: a summary label for each of the risk types [fire/flood/SPEI/SLR]

### Example Usage
`curl -X GET "https://sustglobal.io/api/v1/riskdataset/{selected_collection}/summary?api_key="YOUR_SUST_API_KEY"`


## Post collection for creation of risk dataset
```bash
/v1/create
```

### Required parameters
Requires the user the specify the asset collection for which the assets are retrived
- `collection_name`: name of the collection
- `file_name`: name of the file with asset data based on Sust intake template

### Response
The response is status code. `200` indicates successful post of new asset collection.

### Example Usage
`curl -X POST "https://sustglobal.io/api/v1/create/{collection_name}/assets?api_key="YOUR_SUST_API_KEY" -F "asset=@{file_name};type=text/csv"`

## Post asset for creation of risk dataset

```bash
/v1/riskdataset/create
```

### Required parameters
Requires the user the specify the asset collection for which the assets are retrived
- `collection_name`: name of the collection assigned to the asset
- `lat`: latitude of the asset
- `lng`: longitude of the asset
- `type`: type of the asset 

### Response
The response is a list of summary items in a risk dataset for a specific collection accessible to the user with the specified key. Each item in the list would have the following properties:
- `id`: id of creation request 
- `collection`: name of the collection

### Example Usage
`curl -X GET "https://sustglobal.io/api/v1/riskdataset/create&lat={lat}&lng={lng}&collection={collection_name}&type={type}?api_key="YOUR_SUST_API_KEY"`


## Citing Sust Global API

From a concept to adoption by an emerging group of early adopters, many people have invested time and energy in developing and enabling access to Sust Global's capabilities. Please cite Sust Global when using our data and insights. To cite Sust Global's data in publications, please use the following:

Sust Inc (2021). Sust Global Application Programming Interface: Transforming frontier climate science to actionable data. https://sustglobal.github.io/dev-center/.
```
@Misc{,
  author       = {Sust Global Team},
  organization = {Sust Inc},
  title        = {Sust Global Application Programming Interface: Transforming frontier climate science to actionable data},
  year         = {2021--},
  url          = "https://sustglobal.github.io/dev-center/"
}
```
