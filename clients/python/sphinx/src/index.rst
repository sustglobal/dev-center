Sust Global Python API Client
=============================

This document details how to use the `sust-api-client <https://pypi.org/project/sust-api-client/>`_ python package to interact with Sust Global's Climate Explorer API.

Much of this client is generated using OpenAPI:

* `Current OpenAPI Spec <https://explorer.sustglobal.io/swagger.json>`_
* `OpenAPI Spec Documentation <https://explorer.sustglobal.io/redoc/>`_

More on our developer documentation can be found at:

* `Sust Global Developer Center <https://developers.sustglobal.com/>`_

Install the client
------------------

You can install the client using ``pip``:

.. code-block:: python

    pip install sust-api-client

The current version of the client is `0.0.22 <https://pypi.org/project/sust-api-client/>`_.

Introduction
------------

Initialize a client, providing your Climate Explorer API key and project name (``API_KEY`` and ``PROJECT``, respectively):

.. code-block:: python

    from sust.api import ClimateExplorerClient
    cl = ClimateExplorerClient(API_KEY, PROJECT)

You can scan through the list of available portfolios in the specified project and associated status using the following:

.. code-block:: python

    for pf in cl.portfolios():
        print(pf['portfolio_name'], pf['status'])

The status could be one of ``No data available``, ``Waiting on risk data generation`` or ``Risk data available``. To submit a new portfolio for risk data generation, you need to assign it a name and provide asset locations associated with the portfolio as a CSV file. Kindly use the `intake template <https://developers.sustglobal.com/explorer.html>`_ format for this purpose, see the `Quick Start Guide <https://developers.sustglobal.com/explorer.html>`_ for a demo portfolio as well: 

.. code-block:: python

    pf = cl.create_portfolio(PORTFOLIO_NAME)
    with open('path_to_intake_portfolio_asset.csv', 'rb') as af:
        pf.import_assets_csv(af)

Once asset level risk data is generated for your portfolio, the portfolio's status changes to ``Risk data available``. This process can take up to 24 hours depending on the size of the portfolio.

Accessing Physical Risk Exposure
--------------------------------

The following demonstrates how to access the physical risk exposure timeseries data filtered to a specific scenario, hazard and indicator, then load it into a pandas dataframe for further analysis. Each row in the dataframe maps to an asset from the previously-uploaded CSV: 

.. code-block:: python

    import pandas as pd

    ds = pf.physical_risk_exposure()
    ts = ds.timeseries(ds.scenarios.get('ssp585'), ds.indicators.get('wildfire', 'unified_prob'))
    df = pd.DataFrame(ts.to_dicts())

The Sust Global API supports several of the `IPCC CMIP6 climate scenarios <https://www.carbonbrief.org/cmip6-the-next-generation-of-climate-models-explained>`_, including ``ssp126``, ``ssp245`` and ``ssp585``).

It is common practice to filter timeseries data to specific indicators. The following table documents the
available values. When filtering to a specific indicator, it is important to provide the corresponding hazard value as
well. An example of this is available just above.

+-----------------+--------------------------+
| Hazard          | Indicator                |
+=================+==========================+
| cyclone         | prob                     |
+-----------------+--------------------------+
| cyclone         | obs_freq                 |
+-----------------+--------------------------+
| wildfire        | unified_prob             |
+-----------------+--------------------------+
| wildfire        | obs_score                |
+-----------------+--------------------------+
| flood_potential | inland_flood_prob        |
+-----------------+--------------------------+
| flood_potential | obs_score                |
+-----------------+--------------------------+
| water_stress    | spei_norm                |
+-----------------+--------------------------+
| water_stress    | score                    |
+-----------------+--------------------------+
| water_stress    | unified_score            |
+-----------------+--------------------------+
| water_stress    | obs_score                |
+-----------------+--------------------------+
| sea_level_rise  | change                   |
+-----------------+--------------------------+
| heatwave        | freq                     |
+-----------------+--------------------------+
| fundamental     | precip                   |
+-----------------+--------------------------+
| fundamental     | extreme_precip           |
+-----------------+--------------------------+
| fundamental     | temp                     |
+-----------------+--------------------------+

Summary and timeseries data may be filtered to a hazard. To accomplish this, simply provide a hazard name to the
``PhysicalRiskExposureDataset.hazards.get`` method.

Summary datasets can also be filtered by summary window. Sust Global provides summaries over the 5, 15 and 30 year windows. An example follows:

.. code-block:: python

    ds = pf.physical_risk_exposure()
    sm = ds.summary(ds.windows.get(5), ds.hazards.get('wildfire'))
    df = pd.DataFrame(sm.to_dicts())

These examples showcase how you can access risk exposure datasets and load them to dataframes as an entry point for exploration data analysis.

Additional information is available in the `Sust Global Dev Center <https://developers.sustglobal.com>`_.

Exporting Physical Risk Exposure
--------------------------------

The Physical Risk Exposure information retrieved with the client can be exported to a ZIP file by using the method below:

.. code-block:: python

    ds = portfolio.physical_risk_exposure()
    ds.export_zip(file_name='AGE1.zip') #save to local directory
    ds.export_zip(file_name='/foo/bar/AGE1.zip') #save to /foo/bar

Using the Search Method with Coordinates
----------------------------------------

Retrieving Physical Risk Exposure information can also be retrieved by passing geographic coordinates to the Search method.

.. code-block:: python

    geo_risk = client.search(latitude=47.09764797110564, longitude=-122.8242285597761)

For a detailed description of the output returned by the search method, visit the OpenAPI spec documentation.

Python API Reference
--------------------

.. autoclass:: sust.api.climate_explorer.ClimateExplorerClient
   :members:

.. autoclass:: sust.api.climate_explorer.Portfolio
   :members:

.. autoclass:: sust.api.climate_explorer.AssetList
   :members:

.. autoclass:: sust.api.climate_explorer.PhysicalRiskExposureDataset
   :members:

.. autoclass:: sust.api.climate_explorer.PhysicalRiskExposureTimeseries
   :members:

.. autoclass:: sust.api.climate_explorer.PhysicalRiskExposureSummary
   :members:

.. autoclass:: sust.api.climate_explorer.Scenario
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.ScenarioList
   :members:
   :inherited-members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.Hazard
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.HazardList
   :members:
   :inherited-members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.Indicator
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.IndicatorList
   :members:
   :inherited-members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.Window
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.WindowList
   :members:
   :inherited-members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.Measure
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.MeasureList
   :members:
   :inherited-members:
   :undoc-members:
