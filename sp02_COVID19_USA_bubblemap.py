import pandas as pd 
import plotly.express as px 


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'


# load the data
df = pd.read_csv(url)


df_statenames = pd.read_csv('./USA_states_twoletter_code.csv')


df['state code'] = df['state']
for i in range(len(df_statenames)):
    df['state code'].replace(df_statenames.loc[i]['state name'],
        df_statenames.loc[i]['two letter'], inplace=True)

fig = px.scatter_geo(df, locations='state code',
    locationmode = 'USA-states', color='cases',
    color_continuous_scale=px.colors.sequential.Agsunset,
    hover_name='state', size='cases', size_max = 80,
    hover_data=['deaths'], scope='usa',
    title='USA COVID-19 cases',
    animation_frame='date')

fig.show()