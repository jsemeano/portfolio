from fastapi import FastAPI
import requests
import base64
import sys
sys.path.append("..")
from gee import authentication


# UVICORN START TERMINAL COMMAND
# uvicorn fast:api --reload

# WEBPAGE 
# http://localhost:8000/

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'not ok': True}



@app.get('/classify')
async def classify():
    
    # aws_sentinel(max_items, cloud_cover,start_date,end_date)
    
    # big 2x2 area: [-73.434884,-8.811260,-72.683737,-9.205097]
    # smaller 2x1 area: [-73.434884,-8.811260,-72.683737,-8.911260]

    resp = authentication.aws_sentinel(30,90,'2020-08-30','2020-08-30',[-73.434884,-8.811260,-72.683737,-8.911260])
     
    return resp







# @app.post("/image/")
# async def post_image(url: str):
#     # Send a request to the URL and retrieve the image data
#     response = requests.get(url)
#     image_data = base64.b64encode(response.content).decode("utf-8")

#     # Return the image data as a response
#     return {
#         "image_url": url,
#         "image_data": image_data
#     }