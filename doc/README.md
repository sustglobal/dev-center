# Sust Global API Documentation

## Overview

Sust Global enables customers in the financial service space with physical risk exposure assessments using our SaaS climate intelligence product offering. Sust Global's API is a RESTful API interface to Sust Global's climate intelligence capabilities. 

Sust Global API is intended to enable users with the following capaibilities:
- Trigger the creation of physical climate risk exposure data for a specific collection of assets (sites) defined by the user
- Enable direct access to climate risk data for download and replication in user's data stores and data warehouses for use in the user's own analysis and application development. 

## How to become a Sust Developer

Using the Sust Global API requires that you have a Sust API key: if you don't already have an account with us, you can [reach out](mailto:sales@sustglobal.com) to us for an API key.

Once you're signed up, you can find your API key in your account settings. 


## API Endpoints


### Retreive collections

```bash
/v1/riskdataset/collections
```

### Required parameters
None

### Response
The response is a list of collections accessible to the user with the specified key. Each item in the list would have the following properties:
- `id` 
- `date_creation`: date of creation of the collection
- `date_validation`: date of validation of the resulting risk data collection
- `collection_name`: user defined name of the collection
- `collection_name_api`: name of the collection for access by API end points
- `status`: status of the risk collection dataset

### Example Usage
`curl -X GET "https://climate-explorer.sustglobal.com/api/v1/riskdataset/collections/?api_key=YOUR_SUST_API_KEY"`






## Citing Sust API

From a concept to adoption by an emerging group of early adopters, many people have invested time and energy in developing and enabling access to Sust Global's capabilities. Please cite Sust Global when using our data and insights.

To cite Sust Global's data in publications, please use the following:

Sust Inc (2021). Sust Global Application Program Interface: Transforming frontier cliamate scicence to actionable intelligence. https://sustglobal.github.io/dev-center/.
@Misc{,
  author =    {Sust Global Team},
  organization = {Sust Inc},
  title =     {Sust Global Application Program Interface: Transforming frontier cliamate scicence to actionable intelligence.},
  year =      {2021--},
  url = "https://sustglobal.github.io/dev-center/"
}