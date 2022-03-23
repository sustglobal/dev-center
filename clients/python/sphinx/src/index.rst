Sust Global Python API Client
=============================

This document details how to use the ``sust-api-client`` python package to interact with Sust Global's Climate Explorer API.

Much of this client is generated using OpenAPI:

* Current OpenAPI spec: https://explorer.sustglobal.io/swagger.json
* OpenAPI spec documenation: https://explorer.sustglobal.io/redoc/

Quickstart
----------

Initialize a client, providing your Climate Explorer API key and project name:

.. code-block:: python

    client = ClimateExplorerClient(API_KEY, project=PROJECT)


Access physical risk exposure summary data with filters:

.. code-block:: python

    client.physical_risk_summary(
        window=Windows.YEAR_30,
        hazard=Hazards.WILDFIRE,
        scenario=Scenarios.SSP585)


Python API Reference
--------------------

.. automodule:: sust.api.climate_explorer
   :members:
   :undoc-members:
