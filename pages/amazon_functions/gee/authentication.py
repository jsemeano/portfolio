

import ee
# import folium
# import geehydro
import numpy as np
# import geemap
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import time
import PIL 
import cv2
from google.cloud import storage
import pandas as pd
import io
from pystac_client import Client
from shapely.geometry import Point, Polygon
# from shapely.geometry import Point
import rioxarray
from rioxarray.merge import merge_arrays
import rasterio
from rasterio.merge import merge
from IPython.display import Image, display
from IPython.core.display import HTML 
import requests
from io import BytesIO


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


def chipping_grid_px(mosaic, dist, overlap):
    
    """
    Creates the grid for the chips
    Inputs: - initial longitude (top left)
            - initial latitude (top left)
            - distance (in pixel size) each pixel is then turned into 0.0001 degrees
            
    Outputs:- final longitude (bottom right)
            - final latitude (bottom right)
    """
    
    start_lon = outer_area[0]
    start_lat = outer_area[1]
    end_lon = outer_area[2]
    end_lat = outer_area[3]
    
    # calculate the step in degrees for the top left corners
    lon_step =  int((1-overlap)*dist)
    lat_step = int((1-overlap)*dist)

    # calculate the step in degrees for the top left corners
    lon_side =  dist*0.0001
    lat_side = dist*0.0001
    
    # calculate longitudes of top left corner    
    vec_lon = start_lon + lon_step*np.arange(0,(end_lon-start_lon)//lon_step,1)
    
    # calculate latitudes of top left corner
    vec_lat = start_lat - lat_step*np.arange(0,-(end_lat-start_lat)//lat_step,1)
    
    # generate matrix of top left corners llongitude and latitude
    top_left_M = np.array(np.meshgrid(vec_lon,vec_lat)).T.reshape(len(vec_lon)*len(vec_lat),2)
    
    print(f'List contains {len(top_left_M)} chips')
    
    
    # create the data frame with longitude and latitude of both corners of the chip
    chip_df = pd.DataFrame(data=top_left_M, columns=['lon_top_left', 'lat_top_left'])
    
    chip_df['lon_bottom_right'] = chip_df.apply(lambda x: x['lon_top_left']+lon_side , axis=1)
    chip_df['lat_bottom_right'] = chip_df.apply(lambda x: x['lat_top_left']-lat_side , axis=1)
    
    return chip_df





# try:
#     ee.Initialize()
# except Exception as e:
def aws_sentinel(max_items, cloud_cover,start_date,end_date,area):
    
    start = time.time()

    ## source

    api_url = "https://earth-search.aws.element84.com/v0"
    client = Client.open(api_url)
    
    # define area of interest

    # areas_list = [[-73.434884,-8.811260,-72.683737,-9.205097]]

    # 3578.46 sqkm close to the point William mentioned (I think)

    # area = areas_list[0]
    coords =((area[0],area[1]),(area[0],area[3]),(area[2],area[3]),(area[2],area[1]), (area[0],area[1]))
    point = Polygon(coords)


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

    items = search.get_all_items()

        
    # Merge each colour band independently and group them into a RGB array

    start_mos = time.time()

    item_B04 = [rasterio.open(item.assets['B04'].href) for item in items]
    mosaic_red, out_trans_red = merge(item_B04)

    item_B03 = [rasterio.open(item.assets['B03'].href) for item in items]
    mosaic_green, out_trans_green = merge(item_B03)

    item_B02 = [rasterio.open(item.assets['B02'].href) for item in items]
    mosaic_blue, out_trans_blue = merge(item_B02)

    print(f'time to complete mosaics : {time.time()-start_mos} (s)')
        
    mosaic_red = scale_values(mosaic_red.reshape((mosaic_red.shape[1],mosaic_red.shape[2])))
    mosaic_green = scale_values(mosaic_green.reshape((mosaic_green.shape[1],mosaic_green.shape[2])))
    mosaic_blue = scale_values(mosaic_blue.reshape((mosaic_blue.shape[1],mosaic_blue.shape[2])))
    
    mosaic_rgb = [mosaic_red, mosaic_green, mosaic_blue]
    
    print(f'{time.time() - start} seconds to prepare chips.' )
    
    chipping_grid_px(mosaic_rgb, 256, 0.3)

    return mosaic_rgb



# # function to display images in grid

# def print_images(item_df,x_num):
 
#     x_n = 0
#     y_n = 0
    
#     if item_df.shape[0] == 2:
#         fig, axs = plt.subplots(2, x_num, figsize=(8,8))
#     else:
#         fig, axs = plt.subplots(int(item_df.shape[0]/x_num), x_num, figsize=(8,8))
    
#     for index, item in item_df.iterrows():
#         response = requests.get(item['thumbnail'])
#         img = PIL.Image.open(BytesIO(response.content))
#         axs[y_n,x_n].imshow(img)
#         axs[y_n,x_n].set_title(item['datetime'].to_datetime64().astype('datetime64[s]'))
        
#         x_n += 1
        
#         if x_n == x_num:
#             x_n = 0
#             y_n +=1
        
#     plt.show()
        












# aws_sentinel()



# for item in items:

#     # item = items[pos]
#     print(item.datetime)
#     # print(item.geometry)
#     # print(item.properties)    
    
#     assets = item.assets  # first item's asset dictionary
#     # print(assets.keys())

#     # for key, asset in assets.items():
#     #     print(f"{key}: {asset.title}")

#     print(assets["thumbnail"].href)


# b02_href = assets["B02"].href



# start_open_rasterio = time.time()

# b02 = rioxarray.open_rasterio(b02_href)


# print(b02.rio.crs)
# print(b02.rio.nodata)
# print(b02.rio.bounds())
# print(b02.rio.width)
# print(b02.rio.height)




# start_to_raster = time.time()

# # b02.rio.to_raster("B02.tif")  VERY TIME CONSUMING STEP


# print(f'This took {time.time() - start_to_raster} seconds' )

# print(f'This took {time.time() - start} seconds' )

