Sust Global Python API Client
=============================

This document details how to use the ``sust-api-client`` python package to interact with Sust Global's Climate Explorer API.

Much of this client is generated using OpenAPI:

* Current OpenAPI spec: https://explorer.sustglobal.io/swagger.json
* OpenAPI spec documenation: https://explorer.sustglobal.io/redoc/

More on our developer documentation can be found at:

* Sust Global developer center: https://developers.sustglobal.com/

Install the client
------------------

You can install the client using ``pip``:

.. code-block:: python

    pip install sust-api-client

Introduction
------------

Initialize a client, providing your Climate Explorer API key and project name (``API_KEY`` and ``PROJECT``, respectively):

.. code-block:: python

    from sust.api import ClimateExplorerClient
    cl = ClimateExplorerClient(API_KEY, PROJECT)

You can scan through the list of available portfolios in the specified project and associated status using the following:

.. code-block:: python

    for pf in cl.portfolios():
        print(pf.name, pf['status'])

The status could be one of ``No data available``, ``Waiting on risk data generation`` or ``Risk data available``. To submit a new portfolio for risk data generation, you need to assign it a name and provide asset locations associated with the portfolio as a CSV file. Kindly use the `intake template <https://developers.sustglobal.com/explorer.html>`_ format for this purpose, see the `Quick Start Guide <https://developers.sustglobal.com/explorer.html>`_ for a demo portfolio as well: 

.. code-block:: python

    pf = cl.create_portfolio(PORTFOLIO_NAME)
    with open('path_to_intake_portfolio_asset.csv', 'rb') as af:
        pf.import_assets_csv(af)

Once asset level risk data is generated for your portfolio, the portfolio's status changes to ``Risk data available``. This process can take up to 24 hours depending on the size of the portfolio.

The following demonstrates how to access the physical risk exposure timeseries data filtered to a specific scenario, hazard and indicator, then load it into a pandas dataframe for further analysis. Each row in the dataframe maps to an asset from the previously-uploaded CSV: 

.. code-block:: python

    import pandas as pd
    from sust.api import (ScenarioFilters, HazardFilters, IndicatorFilters)

    ts = pf.physical_risk_timeseries(ScenarioFilters.SSP585, HazardFilters.WILDFIRE, IndicatorFilters.BURNED_AREA)
    df = pd.DataFrame(ts.to_dicts())

The Sust Global API supports several of the `IPCC CMIP6 climate scenarios <https://www.carbonbrief.org/cmip6-the-next-generation-of-climate-models-explained>`_, each of which are documented in the ScenarioFilters enum (e.g. ``SSP126``, ``SSP245`` and ``SSP585``).

You can also filter responses based on hazards. Hazards could be one of ``CYCLONE``, ``WILDFIRE``, ``FLOOD_POTENTIAL``, ``WATER_STRESS``, ``SEA_LEVEL_RISE``, ``HEATWAVE`` or ``FUNDAMENTAL``. See ``HazardFilters`` for the complete list.

You could optionally also filter the risk exposure dataset based on the indicators. Indicator filters are hazard specific. You could use the ``PROBABILITY`` or the ``OBSERVED_FREQUENCY`` indicators with the ``CYCLONE`` hazard, ``BURNED_AREA``, ``FIRE_KBDI_SUSCEPTIBILITY`` or ``OBSERVED_SCORE`` with the ``WILDFIRE`` hazard, ``PROBABILITY`` or ``OBSERVED_SCORE`` with the ``FLOOD_POTENTIAL`` hazard, ``SCORE`` or ``SPEI`` for the ``WATER_STRESS`` hazard, ``CHANGE`` for the ``SEA_LEVEL_RISE`` hazard, ``FREQUENCY`` for the ``HEATWAVE`` hazard and ``TEMPERATURE``, ``PRECIPITATION`` or ``EXTREME_PRECIPITATION`` for the ``FUNDAMENTAL`` hazard for the fundamental climate indicators. 

Physical risk summary datasets can be accessed and optionally filtered by hazard type or by window. Sust Global provides summaries over the 5, 15 and 30 year windows. Provided by ``WindowFilters`` are ``YEARS_5``, ``YEARS_15`` or ``YEARS_30``. Here is an example:

.. code-block:: python

    from sust.api import WindowFilters

    sm = pf.physical_risk_summary(ScenarioFilters.SSP585, WindowFilters.YEARS_5, HazardFilters.WILDFIRE)
    df = pd.DataFrame(sm.to_dicts())

These examples showcase how you can access risk exposure datasets and load them to dataframes as an entry point for exploration data analysis.
Additional information is available in the `Sust Global Dev Center <https://developers.sustglobal.com>`_.


Python API Reference
--------------------

.. autoclass:: sust.api.climate_explorer.ClimateExplorerClient
   :members:

.. autoclass:: sust.api.climate_explorer.Portfolio
   :members:

.. autoclass:: sust.api.climate_explorer.AssetList
   :members:

.. autoclass:: sust.api.climate_explorer.PhysicalRiskTimeseriesList
   :members:

.. autoclass:: sust.api.climate_explorer.PhysicalRiskSummaryList
   :members:

.. autoclass:: sust.api.climate_explorer.LabelFilter
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.ScenarioFilters
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.HazardFilters
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.IndicatorFilters
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.WindowFilters
   :members:
   :undoc-members:

.. autoclass:: sust.api.climate_explorer.MeasureFilters
   :members:
   :undoc-members:
