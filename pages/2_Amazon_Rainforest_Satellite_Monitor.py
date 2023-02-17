
import streamlit as st
import pandas as pd
from datetime import date
import numpy as np
# import time
from pystac_client import Client
from shapely import geometry 
import rioxarray
import requests


st.set_page_config(
    page_title='Amazon_alert',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)



api_url = 'https://deforestation-2f7jkaqqnq-ew.a.run.app'
prediction_url = api_url + '/classify'
requests.get(api_url) #to activate container

# def scale_values(values):
#     # # Get the minimum and maximum values
#     max_value_allowed = 5000
#     # min_value = np.min(values)
#     # max_value = np.max(values)
#     # # Calculate the range of the values
#     # value_range = max_value - min_value
#     if max_value_allowed-np.min(values) == 0:
#         print(np.max(values)-np.min(values))
#         return None
    
#     # Scale the values to a range of 0 to 1
#     scaled_values = np.rint(255*((values - np.min(values)) / (np.max(values)-np.min(values))))
#     scaled_values = np.where(scaled_values >= 255, 255, scaled_values)
    
#     return  scaled_values 
#     # return  (min_value, max_value, value_range) # scaled_values_int 

def scale_values(values):
    # Get the minimum and maximum values
    max_value_allowed = 5000
    min_value = np.min(values)
    max_value = np.max(values)
    # Calculate the range of the values
    value_range = max_value_allowed - min_value
    # Scale the values to a range of 0 to 1
    scaled_values = np.array([255*((value - min_value) / value_range) for value in values]).astype(int)
    scaled_values = np.where(scaled_values >= 255, 255, scaled_values)

    return  scaled_values

def chipping(mosaic,dist,overlap):

    # calculate longitudes of top left corner    
    vec_x = int((1-overlap)*dist)*np.arange(0,int(mosaic.shape[0]//int((1-overlap)*dist)),1)
    vec_x[-1] = mosaic.shape[0]-dist

    # calculate latitudes of top left corner
    vec_y = int((1-overlap)*dist)*np.arange(0,int(mosaic.shape[1]//int((1-overlap)*dist)),1)    
    vec_y[-1] = mosaic.shape[1]-dist

    # create the data frame with longitude and latitude of both corners of the chip
    chip_df = pd.DataFrame(data=np.array(np.meshgrid(vec_x,vec_y)).T.reshape(len(vec_x)*len(vec_y),2), columns=['x_top_left', 'y_top_left'])

    chip_df['x_bottom_right'] = chip_df.apply(lambda x: x['x_top_left']+dist , axis=1)
    chip_df['y_bottom_right'] = chip_df.apply(lambda x: x['y_top_left']+dist , axis=1)

    chip_df['rgb'] = chip_df.apply(lambda x: mosaic[x['x_top_left']:x['x_bottom_right'],x['y_top_left']:x['y_bottom_right'],:]  , axis=1)

    return chip_df

def aws_sentinel_retrieve_item(max_items, cloud_cover,start_date,end_date,area):
    
    search = Client.open("https://earth-search.aws.element84.com/v0").search(
        collections=["sentinel-s2-l2a-cogs"],
        intersects=geometry.Point(area[0],area[1]),
        max_items=max_items,
        datetime=f"{start_date}/{end_date}",
        query=[f"eo:cloud_cover<{cloud_cover}"]
        # resolution  =10
    )

    # create dataframe with main metadata and thumbnails

    if search.matched() < 1:
        return 'failed'
    
    items = search.get_all_items()
    
    item = items[pd.DataFrame(data = {'cloud_cover' : [item.properties['eo:cloud_cover'] for item in items]}).sort_values(by='cloud_cover').index[0]]
    
    del items

    return item

def aws_sentinel_chip(item,area):
    
    geom = item.geometry['coordinates'][0]
    
    lon_geom = [i[0] for i in geom]
    lat_geom = [i[1] for i in geom]

    max_lon = max(lon_geom)
    min_lon = min(lon_geom)
    max_lat = max(lat_geom)
    min_lat = min(lat_geom)
    
    ind_item = (-min_lon+area[0])//((-min_lon+max_lon)/61)*61 + (-min_lat+area[1])//((-min_lat+max_lat)/61)

    # Merge each colour band independently and group them into a RGB array

    mosaic_red = rioxarray.open_rasterio(item.assets["B04"].href).values
    mosaic_green = rioxarray.open_rasterio(item.assets["B03"].href).values
    mosaic_blue = rioxarray.open_rasterio(item.assets["B02"].href).values  

    mosaic_rgb = np.stack([mosaic_red.reshape((mosaic_red.shape[1],mosaic_red.shape[2])), 
                           mosaic_green.reshape((mosaic_green.shape[1],mosaic_green.shape[2])), 
                           mosaic_blue.reshape((mosaic_blue.shape[1],mosaic_blue.shape[2]))], 
                          axis=2)
    
    print(f'red : max - {np.max(mosaic_red)} , min - {np.min(mosaic_red)} ')
    print(f'green : max - {np.max(mosaic_green)} , min - {np.min(mosaic_green)} ')
    print(f'blue : max - {np.max(mosaic_blue)} , min - {np.min(mosaic_blue)} ')
    
    del mosaic_blue
    del mosaic_green
    del mosaic_red
   
    mosaic_rgb = chipping(mosaic_rgb,256,0.3)

    mosaic_rgb = mosaic_rgb.iloc[int(ind_item)]['rgb']
    
    # print(mosaic_rgb)
    
    for i in range(3):
        print(i)
        mosaic_rgb[:,:,i] = scale_values(mosaic_rgb[:,:,i])
    
    return   mosaic_rgb 


############### Streamlit page ####################

col3, col4 = st.columns(2)

with col3:
    start_date = st.slider("When do you start?",
                        value=date(2022, 1, 1),
                        format="DD/MM/YY")

with col4:
    end_date = st.slider("When do you stop?",
                        value=date(2023, 2, 10),
                        format="DD/MM/YY")
    
    
col5, col6 = st.columns(2)
with col5:
    lat = st.slider('Latitude - Y',  -9.0, -7.0, -8.0)

with col6:
    lon = st.slider('Longitude - X', -74.0, -72.0, -73.0)


html_str = f"""
<p class="a">You picked a point at Latitude {lat} and Longitude {lon}. <br />
Images collected between {start_date} and {end_date}.</p>
"""

st.markdown(html_str, unsafe_allow_html=True)

lat_long_df = pd.DataFrame(data={'lat' : [lat], 'lon': [lon]})

col7, col8, col9 = st.columns(3)

show_mosaic = 100

with col8:
    st.map(lat_long_df)
    if st.button('Get chip'):
        items =  aws_sentinel_retrieve_item(15, 70,start_date,end_date,[lon,lat])
        
        if items == 'failed':
            show_mosaic = 0
            
        else:
            print(items)
            mosaic_rgb  = aws_sentinel_chip(items,[lon,lat])
            show_mosaic = 1

    if show_mosaic == 1:
        # st.write(mosaic_rgb)
        st.image(mosaic_rgb, clamp=True, channels='RGB')
        
        sketch_byte = mosaic_rgb.tobytes()
        response_classes = requests.post(prediction_url, files={'sketch': sketch_byte}).json()

        prediction = np.array(response_classes)
        
        st.write(prediction)
        
    elif show_mosaic == 0:
        st.write('No image returned. Please increase the considered period (start and end dates) or allow for more clouds (Maximum cloud cover).')
        
