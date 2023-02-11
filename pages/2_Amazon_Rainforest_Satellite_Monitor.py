
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Amazon_alert',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)




lat = st.slider('Latitude - Y',  -9.0, -7.0, -8.0)


long = st.slider('Longitude - X', -74.0, -72.0, -73.0)

st.write(f"You picked a point at Latitude {lat} and Longitude {long}.")


lat_long_df = pd.DataFrame(ata = [lat,long], columns =['lat','long'])


st.map(lat_long_df)


