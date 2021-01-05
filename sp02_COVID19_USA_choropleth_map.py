import pandas as pd 
import plotly.express as px 
from urllib.request import urlopen
import json

with urlopen(
    'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

df = pd.read_csv(url, dtype={'fips':str})
df['text'] = df['county'] + ', ' + df['state']


fig = px.choropleth_mapbox(df, locations='fips',
    geojson = counties, color='cases',
    color_continuous_scale=px.colors.sequential.Oryel,
    range_color=[0,250],
    mapbox_style='carto-positron',
    hover_name = 'text',
    hover_data = ['deaths'],
    center = {'lat':37, 'lon':-95},
    zoom = 2.5,
    title = 'USA COVID-19 cases',
    animation_frame = 'date')

fig.update_layout(coloraxis_colorbar = 
    dict(tickvals=[0,100,200,250],
    ticktext=['0','100','200','>250']))

fig.show()