import pandas as pd 
import plotly.express as px 
from urllib.request import urlopen
import json
from datetime import datetime,timedelta,date
import os

if not os.path.exists('./figure'):
    os.mkdir('./figure')

with urlopen(
    'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

df = pd.read_csv(url, dtype={'fips':str})
df['text'] = df['county'] + ', ' + df['state']

dt_start = datetime(2020,1,21)
dt_end = datetime.combine(date.today(), datetime.min.time())
delta_t = timedelta(days=1)

dt = dt_start
while dt<=dt_end:
    time_str = dt.strftime('%Y-%m-%d')
    print('Plotting ' + time_str)

    df1 = df[df['date']==time_str]

    fig = px.choropleth_mapbox(df1, locations='fips',
        geojson = counties, color='cases',
        color_continuous_scale=px.colors.sequential.Oryel,
        range_color=[0,250],
        mapbox_style='carto-positron',
        hover_name = 'text',
        hover_data = ['deaths'],
        center = {'lat':37, 'lon':-95},
        zoom = 2.5,
        title = 'USA COVID-19 cases as on ' + time_str)

    fig.update_layout(coloraxis_colorbar = 
        dict(tickvals=[0,100,200,250],
        ticktext=['0','100','200','>250']),
        width=800,height=450)

    fig.write_image('./figure/COVID-19_counties_'+
        time_str+'.png', scale=5)
    
    dt = dt + delta_t