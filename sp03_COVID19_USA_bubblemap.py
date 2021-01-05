import pandas as pd 
import plotly.express as px 
from datetime import datetime, timedelta, date 
import sys
import os

if not os.path.exists('./figure'):
    os.mkdir('./figure')


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'


# load the data
df = pd.read_csv(url)


df_statenames = pd.read_csv('./USA_states_twoletter_code.csv')


df['state code'] = df['state']
for i in range(len(df_statenames)):
    df['state code'].replace(df_statenames.loc[i]['state name'],
        df_statenames.loc[i]['two letter'], inplace=True)

max_cases_allday = df['cases'].max()
size_ref = 80

dt_start = datetime(2020,1,21) 
dt_end = datetime.combine( date.today(), datetime.min.time() )
delta_t = timedelta(days=1)

dt = dt_start 
# while dt<dt_end:
dt = dt_end - 3* delta_t
time_str = dt.strftime('%Y-%m-%d')
print('Plotting ' + time_str)

#pick out one day data
df1 = df[ df['date']==time_str  ]
max_cases_today = df1['cases'].max()
size_max = size_ref * max_cases_today/max_cases_allday

fig = px.scatter_geo(df1, locations='state code',
    locationmode = 'USA-states', color='cases',
    color_continuous_scale=px.colors.sequential.Agsunset,
    range_color=(0, max_cases_allday),
    hover_name='state', size='cases', size_max = size_max,
    hover_data=['deaths'], scope='usa',
    title='USA COVID-19 cases as on ' + time_str)

fig.update_layout(width=800, height=450, 
    paper_bgcolor='rgb(188, 201, 245)',
    plot_bgcolor='rgb(188, 201, 245)')

fig.write_image('./figure/COVID-19_states_' + 
    time_str + '.png', scale=5)

dt = dt + delta_t 