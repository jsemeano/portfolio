import streamlit as st
import os
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title='Certificates and references',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


base_path = f'bucket/'

prof_tab, edu_tab, tech_skill_tab, lang = st.tabs(['Professional experience', 'Education', 'Online technical certifications', 'Languages'])


with prof_tab:
    
    subfolder = 'work_life/'

    with st.expander('European Central Bank'):
        
        st.image(f'{base_path}{subfolder}Domingues Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg')



with edu_tab:
    
    subfolder = 'academic_life'

    with st.expander('European Central Bank'):
        
        st.image(f'{base_path}{subfolder}Domingues Semeano_HR_EMPLOYMENT_LETTER_EN_V3-0001.jpg')



with tech_skill_tab:
    
    subfolder = 'academic_life'


with lang:
    
    subfolder = 'academic_life'

