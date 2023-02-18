import streamlit as st
import os
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import urllib.request

st.set_page_config(
    page_title='Certificates',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


base_path = 'bucket/'

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
    
    subfolder = 'academic_life/'
    
    
    with st.expander('MSc in Economics - Católica-Lisbon SBE'):
        st.image(Image.open(f'{base_path}{subfolder}catolica1.jpg').rotate(-90))
        st.image(Image.open(f'{base_path}{subfolder}catolica2.jpg').rotate(-90))
    

    with st.expander('MSc in Mechanical Engineering - Instituto Superior Técnico/Universidade de Lisboa'): 
        st.image(Image.open(f'{base_path}{subfolder}ist_msc_1.jpg').rotate(-90))
        st.image(Image.open(f'{base_path}{subfolder}ist_msc_2.jpg').rotate(-90))

    with st.expander('BSc in Mechanical Engineering - Instituto Superior Técnico/Universidade de Lisboa'): 
        st.image(Image.open(f'{base_path}{subfolder}ist_bsc_1.jpg').rotate(-90))
        st.image(Image.open(f'{base_path}{subfolder}ist_bsc_2.jpg').rotate(-90))
        st.image(Image.open(f'{base_path}{subfolder}ist_bsc_3.jpg').rotate(-90))
   
    
with tech_skill_tab:
    
    subfolder = 'academic_life/'
    
    col5, col6 = st.columns(2)
    
    with col5:
    
        st.markdown("[![Foo](https://new.inform-datalab.com/wp-content/uploads/snowflake-logo.png)](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)")
    
        st.markdown("[![Foo](https://awsmp-logos.s3.amazonaws.com/70b90c19-ed12-4fe9-a99e-28dcea832219/f36486226e4d0430922cb95a55a1edfb.png)](https://www.credential.net/ab3f6a44-df0e-46d1-a7ae-11f8c544f642)")
    
    
    st.image(Image.open(f'{base_path}{subfolder}SQL_UC_DAVIS.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}scrum_methoddologies.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}scaling_agile.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}applied_machine_learning_michigan.JPG'))
    # img.show()
    
    
    # st.markdown("[![Foo](https://www.stickersdevs.com.br/wp-content/uploads/2022/01/postgresql-adesivo-sticker.png)](https://www.coursera.org/account/accomplishments/certificate/98G4DCYDUSTM)")
  
    # st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)](https://www.coursera.org/account/accomplishments/certificate/DNYVPE9B4XJD)")
  
  
  
    
    # st.markdown('''
                
    #     st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
        
    #     [Snowflake : Hands On Essentials - Data Warehouse](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)
        
    #     [dbt](https://www.credential.net/ab3f6a44-df0e-46d1-a7ae-11f8c544f642)
        
    #     [SQL for Data Science](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)
        
    #     [Snowflake : Hands On Essentials - Data Warehouse](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)
        
    #     [Snowflake : Hands On Essentials - Data Warehouse](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)
        
    #     [Snowflake : Hands On Essentials - Data Warehouse](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)
        
    # ''')


with lang:
    
    subfolder = 'academic_life'

