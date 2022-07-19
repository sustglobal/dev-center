import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def display_fwd_timeseries_data(df, asset_index, risk_label):

    START_YEAR = 2022
    END_YEAR = 2100
    
    colors = {
    'background': '#FFFFFF',
    'text': '#AAAAAA'
    }
    
    trace_collection = []

    risk_colnames = [str(i) for i in list(range(START_YEAR, END_YEAR+1))]
    df_selected = df[df['portfolio_index']==asset_index]
    #df_selected = df[asset_index:asset_index+1]
    df_filtered = df_selected[risk_colnames].copy()

    year_labels = [x for x in df_filtered.columns.values]
    year_val = pd.to_numeric(year_labels)

    risk_val = df_filtered.values[0]
    trace_color = {'asset':'rgb(255, 0, 0)'}

    trace = go.Scatter(
        name=risk_label,
        x=year_val,
        y=risk_val,
        mode='lines',
        line=dict(width=3.0, color=trace_color['asset']))

    data = [trace]

    
    layout = go.Layout(
        title='Normalized Multi-Hazard Predictive Risk Exposure : ',
        yaxis=dict(title=risk_label,
                   showline=True,
                   showgrid=False,
                   showticklabels=True,
                   linecolor='rgb(82, 82, 82)',
                   linewidth=2,
                   ticks='outside',
                   range=[0,0.5],
                   tickfont=dict(
                         family='Arial',
                         size=12,
                         color='rgb(82, 82, 82)')
                   ),
        xaxis=dict(title='Year of Assessment',
                   showline=True,
                   showgrid=False,
                   showticklabels=True,
                   linecolor='rgb(82, 82, 82)',
                   linewidth=2,
                   ticks='outside',
                   tickfont=dict(
                         family='Arial',
                         size=12,
                         color='rgb(82, 82, 82)'),
                   rangeselector=dict(
                       buttons=list([
                           dict(count=1,
                                label='1y',
                                step='year',
                                stepmode='backward'),
                           dict(count=3,
                                label='3y',
                                step='year',
                                stepmode='backward'),
                           dict(count=6,
                                label='10y',
                                step='year',
                                stepmode='backward'),
                           dict(step='all')
                       ])
                   ),
                   rangeslider=dict(
                       visible=True
                   ),
                   type='date'),
        showlegend=True,
        legend=dict(x=0, y=1.0),
        transition_duration=50,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'])

    fig = go.Figure(data=data, layout=layout)
    return fig

def estimated_heatmap(df):

    START_YEAR = 2022
    END_YEAR = 2072
    LOW_BP = 0.05
    HIGH_BP = 0.075
    HEATMAP_MAX_MARKER_SIZE = 16
    MAP_ZOOM_LEVEL = 2
    margin_params = {"r": 0, "l": 0, "b": 0}
    legend_params = dict(x=1, y=1.02, orientation="h", yanchor="bottom", xanchor="right")
    
    risk_colnames = [str(i) for i in list(range(START_YEAR, END_YEAR+1))]
    df_selected = df[risk_colnames]
    df_risk = pd.DataFrame({'A': []})
    df_risk['max_risk'] = df_selected.max(axis=1)
    df_risk['loss_marker'] = df_risk['max_risk']*(HEATMAP_MAX_MARKER_SIZE - 1)/0.1
    df_risk['loss_marker'] = df_risk['loss_marker'].astype(int) + 1
    df_risk['loss_marker'] = df_risk['loss_marker'].abs()
    df_risk['lat'] = df.geometry.y.values
    df_risk['lng'] = df.geometry.x.values
    df_risk['entity_name'] = df['entity_name']
#     df_risk['visitation_count'] = df['visitation_count'].values
    
    for index, row in df_risk.iterrows():
        val = row['max_risk']

        if val <= LOW_BP:
            df_risk.loc[index, 'risk_class'] = 'LOW'
        elif val > LOW_BP and val <= HIGH_BP:
            df_risk.loc[index, 'risk_class'] = 'MEDIUM'
        else:
            df_risk.loc[index, 'risk_class'] = 'HIGH'
    df_risk.drop(['A'], axis=1, inplace=True)
    
    # map_fig = px.scatter_mapbox(df_risk, lon="lng", lat="lat", hover_name="Address", color="risk_class", color_discrete_sequence=['#00FF00', '#FFFF00', '#FF0000'], size_max=1, hover_data=[df_risk.index, "max_risk", "risk_class"], zoom=2, height=400) #size='Price', size_max=6,
    map_fig = px.scatter_mapbox(df_risk, lon="lng", lat="lat", hover_name="entity_name", color="risk_class", color_discrete_sequence=['#008CFF', '#0000FF', '#00DFFF', '#FF00FF', '#00FFFF', '#8C00FF', '#8C8C8C', '#8C008C', '#008C8C'], 
                                color_discrete_map={'LOW': '#00FF00', 'MEDIUM': '#FFFF00', 'HIGH': '#FF0000'}, size='loss_marker', size_max=HEATMAP_MAX_MARKER_SIZE, hover_data=["max_risk", "risk_class"], zoom=MAP_ZOOM_LEVEL, height=1000)  # size_max=1 size='Price', size_max=6,

    map_fig.update_layout(clickmode='event+select', mapbox_style="white-bg", margin=margin_params, legend=legend_params,
        mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])

    return map_fig, df_risk