import streamlit as st
import os

st.set_page_config(
    page_title='Joao Semeano Portfolio site',
    layout="wide",
    page_icon=':palm_tree:',
    initial_sidebar_state="auto",
    menu_items=None)



width = 120
col_num = 3

# def present_photos(category_directory_path):

#     images = [img for img in os.listdir(category_directory_path)]

#     cols = st.columns(col_num)

#     for i, image in enumerate(images):
#         image_path = f'{category_directory_path}/{image}'
#         with cols[i%col_num]:
#             st.image(image_path, image.split('.')[0], width= width)

#     return None

# st.header('Hi! ')
st.markdown('''
            # Hi! :hatching_chick: 
            ## My name is João Domingues Semeano and I welcome you to my portfolio page
            
            ### After several years working in mechanical engineering and central banking, I decided to refocus on data science. 
            ### I used my sabbatical to complete a data science bootcamp and update my knowldge on cloud data management techniques.
            ### I am looking for a position where I can develop my ETL and machine learning skills to unlock the meaningful stories behind big data.
            
            In this page you find:
            1. My CV with professional experience, education and certifications
            2. Sketch 2 Image: an app that searches for images similar to your sketch
            3. Amazon Rainforest Satellite Monitor: an app built for an NGO to give early warning of deforestation activities in the Amazon

            ''')

# with open("other/resume.pdf", "rb") as pdf_file:
#     resume = pdf_file.read()

# with open("other/cover_letter.pdf", "rb") as pdf_file:
#     cover = pdf_file.read()


# cols = st.columns(2)
# with cols[0]:
#     st.download_button('Download my resume', resume, 'Erez-Tepper-Data-Scientist-Resume.pdf')

# with cols[1]:
#     st.download_button('Download my cover letter', cover, 'Erez-Tepper-Data-Scientist-Cover-Letter.pdf')

# categories = ['Languages', 'Collection, Analysis, Visualization', 'Machine Learning', 'Deployment', 'On My Watchlist']
# tabs = st.tabs(categories)
# for i, category in enumerate(categories):

#     base_path = f'bucket/Tech Stack/{categories[i]}'

#     with tabs[i]:
#         present_photos(base_path)