
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title='Amazon_alert',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)



col1, col2 = st.columns(2)

# (max_items, cloud_cover,start_date,end_date,area)

with col1:
    cloud_cover = st.slider('Maximum cloud cover',  -9.0, -7.0, -8.0)

with col2:
    max_items = st.slider('Maximum number of images',  -9.0, -7.0, -8.0)

col3, col4 = st.columns(2)

with col3:
    start_date = st.slider("When do you start?",
                        value=date(2020, 1, 1),
                        format="MM/DD/YY")

with col4:
    end_date = st.slider("When do you stop?",
                        value=date(2020, 1, 2),
                        format="MM/DD/YY")
    
    
col5, col6 = st.columns(2)
with col5:
    lat = st.slider('Latitude - Y',  -9.0, -7.0, -8.0)

with col6:
    lon = st.slider('Longitude - X', -74.0, -72.0, -73.0)

st.write(f"You picked a point at Latitude {lat} and Longitude {lon}.")


lat_long_df = pd.DataFrame(data={'lat' : [lat], 'lon': [lon]})


st.map(lat_long_df)


