
import streamlit as st
import pandas as pd
from datetime import date
# from amazon_functions.gee import authentication
import numpy as np
# import geemap
# import tensorflow as tf
# import tensorflow_hub as hub
# import matplotlib.pyplot as plt
import time
import PIL 
# import cv2
# from google.cloud import storage
import io
# import pystac
# import pystac_client
from pystac_client import Client
from shapely import geometry 

#import Point#, Polygon
# from shapely.geometry import Point
import rioxarray
# from rioxarray.merge import merge_arrays
import rasterio



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
    
    # calculate the distance of top left corners
    x_step = int((1-overlap)*dist)
    y_step = int((1-overlap)*dist)
    
    # calculate longitudes of top left corner    
    vec_x = x_step*np.arange(0,int(mosaic.shape[0]//x_step),1)
    
    # calculate latitudes of top left corner
    vec_y = y_step*np.arange(0,int(mosaic.shape[1]//y_step),1)    
    
    # generate matrix of top left corners llongitude and latitude
    top_left_M = np.array(np.meshgrid(vec_x,vec_y)).T.reshape(len(vec_x)*len(vec_y),2)
    
    print(f'List contains {len(top_left_M)} chips')
    
    # create the data frame with longitude and latitude of both corners of the chip
    chip_df = pd.DataFrame(data=top_left_M, columns=['x_top_left', 'y_top_left'])
    
    chip_df['x_bottom_right'] = chip_df.apply(lambda x: x['x_top_left']+dist , axis=1)
    chip_df['y_bottom_right'] = chip_df.apply(lambda x: x['y_top_left']+dist , axis=1)
    
    chip_df['rgb'] = chip_df.apply(lambda x: mosaic[x['x_top_left']:x['x_bottom_right'],x['y_top_left']:x['y_bottom_right'],:]  , axis=1)
    

    # chip_df['thumbnail'] = chip_df.apply(lambda x: f"{ x['x_top_left'] }_{ x['y_top_left'] }.jpg", axis=1)
    
    def create_thumbnail(img_array,name,dist):
        # Create an Image object from the numpy array
        img_jpg = PIL.Image.fromarray(img_array, mode = 'RGB')
        # plt.imshow(img_jpg)
        img_jpg.save(f"pics/{name}")

    
    # for  ind, chip in chip_df.iterrows():
    #     create_thumbnail(chip['rgb'],chip['thumbnail'],dist)
    
    
    return chip_df




def aws_sentinel_retrieve_item(max_items, cloud_cover,start_date,end_date,area):
    

    ## source

    api_url = "https://earth-search.aws.element84.com/v0"
    client = Client.open(api_url)
    
    # define area of interest

    # areas_list = [[-73.434884,-8.811260,-72.683737,-9.205097]]

    # 3578.46 sqkm close to the point William mentioned (I think)

    # area = areas_list[0]
    # coords =((area[0],area[1]),(area[0],area[3]),(area[2],area[3]),(area[2],area[1]), (area[0],area[1]))
    # point = Polygon(coords)

    point = geometry.Point(area[0],area[1])
    # download images from S2 AWS bucket

    collection = "sentinel-s2-l2a-cogs"  # Sentinel-2, Level 2A, COGs

    search = client.search(
        collections=[collection],
        intersects=point,
        max_items=max_items,
        datetime=f"{start_date}/{end_date}",
        query=[f"eo:cloud_cover<{cloud_cover}"]
        # resolution  =10
    )

    print(search.matched())


    # create dataframe with main metadata and thumbnails
    
    if search.matched() < 1:
        return 'failed'
    
    items = search.get_all_items()
    
    return items

        


def aws_sentinel_chip(items):

    # Merge each colour band independently and group them into a RGB array

    start_mos = time.time()

    mosaic_red = rioxarray.open_rasterio(items[0].assets["B04"].href)
    
    
    # rasterio.open(items[0].assets['B04'].href) #for item in items]
    # mosaic_red, out_trans_red = merge(item_B04)

    # mosaic_green = rasterio.open(items[0].assets['B03'].href) #for item in items]
    # # mosaic_green, out_trans_green = merge(item_B03)

    # mosaic_blue = rasterio.open(items[0].assets['B02'].href) #for item in items]
    # # mosaic_blue, out_trans_blue = merge(item_B02)

    # print(f'time to complete mosaics : {time.time()-start_mos} (s)')
        
    # mosaic_red = scale_values(mosaic_red.reshape((mosaic_red.shape[1],mosaic_red.shape[2])))
    # mosaic_green = scale_values(mosaic_green.reshape((mosaic_green.shape[1],mosaic_green.shape[2])))
    # mosaic_blue = scale_values(mosaic_blue.reshape((mosaic_blue.shape[1],mosaic_blue.shape[2])))
    
    # mosaic_rgb = [mosaic_red, mosaic_green, mosaic_blue]
    
    # print(f'{time.time() - start_mos} seconds to prepare chips.' )
    
    # chip_df = chipping(mosaic_rgb, 256, 0.3)

    return mosaic_red #chip_df

st.set_page_config(
    page_title='Amazon_alert',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)



col1, col2 = st.columns(2)

# (max_items, cloud_cover,start_date,end_date,area)

with col1:
    cloud_cover = st.slider('Maximum cloud cover (%)',  50, 100, 75)

with col2:
    max_items = st.slider('Maximum number of images',  5,100,(5))

col3, col4 = st.columns(2)

with col3:
    start_date = st.slider("When do you start?",
                        value=date(2020, 1, 1),
                        format="DD/MM/YY")

with col4:
    end_date = st.slider("When do you stop?",
                        value=date(2020, 1, 2),
                        format="DD/MM/YY")
    
    
col5, col6 = st.columns(2)
with col5:
    lat = st.slider('Latitude - Y',  -9.0, -7.0, -8.0)

with col6:
    lon = st.slider('Longitude - X', -74.0, -72.0, -73.0)


html_str = f"""
<p class="a">You picked a point at Latitude {lat} and Longitude {lon}. <br />
Up to {max_items} images collected between {start_date} and {end_date} and with less than {cloud_cover}% of cloud cover will be considered.</p>
"""

st.markdown(html_str, unsafe_allow_html=True)


lat_long_df = pd.DataFrame(data={'lat' : [lat], 'lon': [lon]})

col7, col8, col9 = st.columns(3)
show_mosaic = 0
with col8:
    st.map(lat_long_df)
    if st.button('Get mosaic df'):
        items =  aws_sentinel_retrieve_item(max_items, cloud_cover,start_date,end_date,[lat,lon])
        
        if items == 'failed':
            st.write('No image returned. Please increase the considered period (start and end dates) or allow for more clouds (Maximum cloud cover).')
        else:
            mosaic_rgb  = aws_sentinel_chip(items)
            show_mosaic = 1
            
            
if show_mosaic == 1:
    st.write(mosaic_rgb.values)

        


    
    

    