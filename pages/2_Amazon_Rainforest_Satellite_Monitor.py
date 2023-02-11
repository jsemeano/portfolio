
import streamlit as st

st.set_page_config(
    page_title='Amazon_alert',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


long = st.slider('Longitude - X', -72.0, -74.0, -73.0)


lat = st.slider('Latitude - Y',  -9.0, -7.0, -8.0)

st.write(f"You picked a point at Longitude {long} and Latitude {lat}")





