import streamlit as st
import os

def present_photos(category_directory_path, width = 300, col_num = 2):

    images = [img for img in os.listdir(category_directory_path)]

    cols = st.columns(col_num)

    for i, image in enumerate(images):
        image_path = f'{category_directory_path}/{image}'
        with cols[i%col_num]:
            st.image(image_path, image.split('.')[0], width = width)

    return None

