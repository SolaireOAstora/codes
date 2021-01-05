import numpy as np 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 

df = pd.read_csv('./COVID-19.csv')

# sort by case number
df = df.sort_values(by=['cases'], ascending=False)
df.index = np.arange(0,len(df))

# generate a plotly figure object
fig = px.scatter_geo(df, locations='country',
    locationmode = 'country names',color='country',
    color_discrete_sequence=px.colors.qualitative.Dark24,
    size='cases',size_max=30,hover_data=['death'],
    hover_name='country',scope='world',
    title=dict(text='COVID-19 cases as on April 1st, 2020',
        font=dict(size=20)))

# fig.update_layout(geo=go.layout.Geo(showcountries=True,
#     countrycolor='grey'))

fig.show()

# fig.write_image('./COVID-19_map.png', scale=10)
