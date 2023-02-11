import streamlit as st
import os

st.set_page_config(
    page_title='Erez Tepper Portfolio Site',
    layout="wide",
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

st.header('I am not a front-end developer or a designer, but I still hope that this website will show you who I am.')
st.markdown('''
            ### I am excited to start my data science path.
            I chose to be in data science because for a tech profession with never-ending iner-disciplinary learning.
            A Flexible, cross-industries possibilities.
            And an ability to make a real impact, and possibilites in impact-tech.
            ### I believe I am the right person for the job.
            Agile, versitile and independent when it comes to learning new skills and abilities.
            Proactive team member with the ability to walk the extra mile, lead and be led.
            Data Science, cross-functionality teams and versitile learning are my passion.
            Modesty and will to learn.
            ### You will find here:
            1. My current project- Amazon rainforest illegal activity monitor, that will actually be deployed in cooparation with NGOs from Peru, in order to assist them.
            2. The final project in a machine learning program- A UI that allows you to sketch, and transform your sketch into an image, build with my amazing team at "Le Wagon".
            3. A tool that I built for my self, based on GPT3, for optimizing job applications.
            4. Just a short description of my current contract in NLP, because it is protected with an NDA.                5. Summary of my social enterprenaurship national projects.
            6. Certifications, courses and University honors.
            7. References.
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