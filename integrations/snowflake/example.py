import os
from snowflake.snowpark import Session
from shapely.geometry import shape
import json
import pandas as pd
import geopandas as gpd
import streamlit as st

CONNECTION_PARAMETERS = {
    "account": os.environ['SP_ACCOUNT'],
    "user": os.environ['SP_USER'],
    "password": os.environ['SP_PASSWORD'],
    "role": os.environ['SP_ROLE'],
    "database": os.environ['SP_DB'],
    "warehouse": os.environ['SP_WAREHOUSE'],
}

with Session.builder.configs(CONNECTION_PARAMETERS).create() as session:
    zip_codes_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.US_STATES_ZIP_CODES'
    reit_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.REIT_DATA'
    srs_db = 'SUST_GLOBAL_PRIVATE.CLIMATE_RISK.SRS_DATA'


    def enrich_hazard_data(to_enrich, hazards):
        df = to_enrich[['lat', 'lon', 'Info']].copy()
        for hazard in hazards:
            df[f'{hazard}_label'] = to_enrich['SCENARIO_ANALYTICS'].apply(lambda x: json.loads(x)['ssp585'][hazard]['summary_label'])
            df[f'{hazard}_color'] = df[f'{hazard}_label'].apply(lambda x: '#d82526' if x == 'HIGH' else '#ffc156' if x == 'MEDIUM' else '#69b764')

        return df


    def join_data_with_us_zips(to_join):
        raw_zips = session.table(zip_codes_db).to_pandas()    
        geom = [shape(json.loads(i)) for i in raw_zips['GEOMETRY']]
        us_zips = gpd.GeoDataFrame(raw_zips, geometry=geom)
        us_zips = us_zips.set_crs("epsg:4326", inplace = True)

        gdf = gpd.sjoin(to_join, us_zips, predicate='within')    
        
        gdf['lat'] = pd.to_numeric(gdf['LAT_left'])
        gdf['lon'] = pd.to_numeric(gdf['LNG_left'])
        
        return gdf
        

    @st.cache_data()
    def get_srs_data():
        df = session.table(srs_db).to_pandas()
        df['LNG'] = pd.to_numeric(df['LONGITUDE'])
        df['LAT'] = pd.to_numeric(df['LATITUDE'])
        df.rename(columns={'ASSETNAME': 'Info'}, inplace=True)
        
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.LNG, df.LAT))
        gdf = gdf.set_crs("epsg:4326", inplace = True)

        joined = join_data_with_us_zips(gdf)
        enriched = enrich_hazard_data(joined, ['sea_level_rise','wildfire','cyclone','flood','heatwave','water_stress'])
        enriched['company'] = gdf['ISSUERNAME']
        
        return enriched


    def srs():
        st.title("Sust Global - Climate Risk Analytics")

        df = get_srs_data()

        hazard = st.selectbox('Hazard:',('Wildfire','Sea Level Rise','Cyclone','Flood','Heatwave','Water Stress'), index=0)
        hazard = hazard.lower()
        if hazard == 'sea level rise':
            hazard = 'sea_level_rise'
        if hazard == 'water stress':
            hazard = 'water_stress' 
        companies = df['company'].unique()
        companies.sort()
        issuer = st.selectbox('Issuer:',tuple(companies), index=0)
        st.map(df[df['company'] == issuer], latitude='lat', longitude='lon', color=f'{hazard}_color')

    srs()

