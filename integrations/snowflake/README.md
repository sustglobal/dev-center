# Sust Global – Climate Risk Analytics with Streamlit

This project provides an interactive Streamlit dashboard for visualizing climate risk analytics data (e.g., wildfire, sea level rise, cyclone, flood, heatwave, and water stress).

It connects to Snowflake using Snowpark, enriches geospatial hazard datasets, and displays them with geospatial overlays.

## Prereqs

Install the following python packages:
```
pip install snowflake-snowpark-python shapely geopandas pandas streamlit
```

Note: geopandas requires system-level dependencies (e.g., gdal, fiona). Follow the GeoPandas installation guide for your OS.


## Environment Variables

Before running, set the following Snowflake connection parameters in your shell or .env file:

```
export SP_ACCOUNT="<your_account>"
export SP_USER="<your_username>"
export SP_PASSWORD="<your_password>"
export SP_ROLE="<your_role>"
export SP_DB="<your_database>"
export SP_WAREHOUSE="<your_warehouse>"
```

## Running the Dashboard
1.	Clone this repository:

```
git clone https://github.com/sustglobal/dev-center.git
cd dev-center
```

2.	Install dependencies (if not already installed):

```
pip install -r requirements.txt
```

3.	Run the Streamlit app:

```
streamlit run example.py
```

4.	Open your browser at `http://localhost:8501`
