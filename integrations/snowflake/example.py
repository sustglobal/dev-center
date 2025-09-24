import os
from snowflake.snowpark import Session
from shapely.geometry import shape
import json
import pandas as pd
import geopandas as gpd
import streamlit as st

# ----------------------------
# Snowflake connection details
# ----------------------------
# Load connection parameters from environment variables
CONNECTION_PARAMETERS = {
    "account": os.environ['SP_ACCOUNT'],
    "user": os.environ['SP_USER'],
    "password": os.environ['SP_PASSWORD'],
    "role": os.environ['SP_ROLE'],
    "database": os.environ['SP_DB'],
    "warehouse": os.environ['SP_WAREHOUSE'],
}

# Open a Snowflake session
with Session.builder.configs(CONNECTION_PARAMETERS).create() as session:
    # Define the database tables to be used
    zip_codes_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.US_STATES_ZIP_CODES'
    reit_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.REIT_DATA'
    srs_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.SRS_DATA'


    def enrich_hazard_data(to_enrich, hazards):
        """
        Enrich a GeoDataFrame with hazard risk labels and colors.

        Args:
            to_enrich (GeoDataFrame): Input data containing SCENARIO_ANALYTICS JSON.
            hazards (list[str]): List of hazard types (e.g., wildfire, flood).

        Returns:
            DataFrame: DataFrame with added hazard label and color columns.
        """
        # Keep only lat, lon, and asset info
        df = to_enrich[['lat', 'lon', 'Info']].copy()

        # For each hazard, parse SCENARIO_ANALYTICS JSON and assign risk levels
        for hazard in hazards:
            df[f'{hazard}_label'] = to_enrich['SCENARIO_ANALYTICS'].apply(
                lambda x: json.loads(x)['ssp585'][hazard]['summary_label']
            )
            # Assign a color for mapping based on risk level
            df[f'{hazard}_color'] = df[f'{hazard}_label'].apply(
                lambda x: '#d82526' if x == 'HIGH' 
                          else '#ffc156' if x == 'MEDIUM' 
                          else '#69b764'
            )

        return df


    def join_data_with_us_zips(to_join):
        """
        Spatially join assets with U.S. ZIP code boundaries.

        Args:
            to_join (GeoDataFrame): Asset data with geometry.

        Returns:
            GeoDataFrame: Assets joined with ZIP code geometries.
        """
        # Load U.S. ZIP codes from Snowflake
        raw_zips = session.table(zip_codes_db).to_pandas()

        # Convert stored geometry JSON into Shapely geometries
        geom = [shape(json.loads(i)) for i in raw_zips['GEOMETRY']]

        # Create a GeoDataFrame for ZIPs with a geographic CRS (WGS84)
        us_zips = gpd.GeoDataFrame(raw_zips, geometry=geom)
        us_zips = us_zips.set_crs("epsg:4326", inplace=True)

        # Spatial join: find which ZIP each asset point falls within
        gdf = gpd.sjoin(to_join, us_zips, predicate='within')

        # Extract latitude/longitude values from join result
        gdf['lat'] = pd.to_numeric(gdf['LAT_left'])
        gdf['lon'] = pd.to_numeric(gdf['LNG_left'])

        return gdf
        

    @st.cache_data()
    def get_srs_data():
        """
        Fetch, process, and enrich SRS (sustainability risk) data.

        Returns:
            DataFrame: Enriched data ready for visualization.
        """
        # Pull SRS data from Snowflake
        df = session.table(srs_db).to_pandas()

        # Ensure numeric types for coordinates
        df['LNG'] = pd.to_numeric(df['LONGITUDE'])
        df['LAT'] = pd.to_numeric(df['LATITUDE'])

        # Rename asset name to 'Info' for clarity
        df.rename(columns={'ASSETNAME': 'Info'}, inplace=True)

        # Create a GeoDataFrame with asset point geometries
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.LNG, df.LAT))
        gdf = gdf.set_crs("epsg:4326", inplace=True)

        # Join with ZIP codes and enrich with hazard labels/colors
        joined = join_data_with_us_zips(gdf)
        enriched = enrich_hazard_data(
            joined,
            ['sea_level_rise', 'wildfire', 'cyclone', 'flood', 'heatwave', 'water_stress']
        )

        # Add company (issuer) info to dataset
        enriched['company'] = gdf['ISSUERNAME']
        
        return enriched


    def srs():
        """
        Streamlit app entrypoint:
        - Lets user select a hazard and company.
        - Displays asset locations on a map with hazard risk coloring.
        """
        st.title("Sust Global - Climate Risk Analytics")

        # Load enriched SRS data
        df = get_srs_data()

        # Dropdown to choose hazard
        hazard = st.selectbox(
            'Hazard:',
            ('Wildfire', 'Sea Level Rise', 'Cyclone', 'Flood', 'Heatwave', 'Water Stress'),
            index=0
        )
        hazard = hazard.lower()

        # Normalize hazard naming to match column names
        if hazard == 'sea level rise':
            hazard = 'sea_level_rise'
        if hazard == 'water stress':
            hazard = 'water_stress' 

        # Dropdown to choose issuer/company
        companies = df['company'].unique()
        companies.sort()
        issuer = st.selectbox('Issuer:', tuple(companies), index=0)

        # Display selected company assets on map, colored by hazard risk
        st.map(
            df[df['company'] == issuer],
            latitude='lat',
            longitude='lon',
            color=f'{hazard}_color'
        )

    # Run the Streamlit app
    srs()