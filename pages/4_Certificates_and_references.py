import streamlit as st
import os
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(
    page_title='Certificates and references',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


base_path = 'bucket/'

base_url = 'https://github.com/jsemeano/portfolio/blob/main/bucket/'
suffix = '?raw=true'


prof_tab, edu_tab, tech_skill_tab, lang = st.tabs(['Professional experience', 'Education', 'Online technical certifications', 'Languages'])


with prof_tab:
    
    subfolder = 'work_life/'

    with st.expander('European Central Bank'):
        pass
        # st.image(f'{base_path}{subfolder}Domingues Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg')
        # img = Image.open(BytesIO(requests.get(f'{base_url}{subfolder}Domingues_Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001{suffix}').content))
        
        # response = requests.get(f'{base_url}{subfolder}Domingues Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg{suffix}')
        # img = Image.open(BytesIO(response.content))
        
        # st.image(f'{base_path}{subfolder}Domingues_Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg', width=300, output_format='JPEG')



with edu_tab:
    
    subfolder = 'academic_life'
    print(f'{base_path}{subfolder}catolica1.jpg')

    # with st.expander('European Central Bank'):
        
    #     st.image(f'{base_path}{subfolder}Domingues Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg')
    st.image(f'{base_path}{subfolder}catolica1.jpg', 'catolica1', width=300, output_format='JPEG')



with tech_skill_tab:
    
    subfolder = 'academic_life'


with lang:
    
    subfolder = 'academic_life'

