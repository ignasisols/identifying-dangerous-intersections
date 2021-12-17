"""
Make sure to install streamlit with `pip install streamlit`.

Run `streamlit hello` to get started!

Streamlit is *V* cool, and it's only going to get cooler (as of February 2021):

https://discuss.streamlit.io/t/override-default-color-palette/9088/2

To run this app:

In the terminal:
1-Load the intersections_app_streamlit environment (conda activate intersections_app_streamlit)
2- cd into this directory: cd Metis_projects/metis_DataEngineering_project/
3. Run `streamlit run streamlit_app.py`
"""

import pandas as pd
import streamlit as st
import plotly.express as px


# Title
st.title('Dangerous intersections in the USA')

# Load data
data = pd.read_csv('dataset_clusters.csv')

# st.dataframe(data)

# search bar input:
state_input = st.text_input('Choose a State') # st.text_input("label goes here", default_value_goes_here)
county_input = st.text_input('Choose a County', '') # st.text_input("label goes here", default_value_goes_here)
city_input = st.text_input('Choose a City', '') # st.text_input("label goes here", default_value_goes_here)

if not state_input: # US level
    data_input = data.copy()
    zoom_map = 2.2

if state_input and city_input and not county_input:
    data_input = data[(data['State'] == state_input) & (data['City'] == city_input)].copy()
    zoom_map = 10

if state_input and county_input:
    data_input = data[(data['State'] == state_input) & (data['County'] == county_input)].copy()
    zoom_map = 8

if state_input and not city_input and not county_input:
    data_input = data[data['State'] == state_input].copy()
    zoom_map = 5

if len(data_input) == 0:
    st.text('This location is not on our database. Please try again')
    data_input = data.copy()
    zoom_map = 2.2

choice = st.radio('Pick one',['All intersections','Only intersections with fatalities'])


colorscale = [
[0, 'rgb(0, 128, 255)'],
[1, 'rgb(255, 0, 0)']
]

# st.secrets["MAPBOX_TOKEN"]
px.set_mapbox_access_token(MAPBOX_TOKEN)

# px.set_mapbox_access_token(open(".streamlit/secrets.toml").read())

# px.set_mapbox_access_token(open(".mapbox_token").read())

if choice == 'Only intersections with fatalities':
    data_input = data_input[data_input['fatalities_ratio'] > 0.0].copy()
    fig = px.scatter_mapbox(data_input, lat="Latitude", lon="Longitude", size="num_accidents_fatalities", size_max=15, zoom=zoom_map) # zoom=2.5
else:
    fig = px.scatter_mapbox(data_input, lat="Latitude", lon="Longitude", color="fatalities_ratio", size="count",
                      color_continuous_scale=colorscale, size_max=15, zoom=zoom_map) # zoom=2.5


st.plotly_chart(fig)
