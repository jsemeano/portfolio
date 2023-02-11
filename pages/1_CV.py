import streamlit as st
import os

st.set_page_config(
    page_title='Joao Semeano CV',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


st.markdown('''
            # Curriculum Vitae
            In the sections below I share the detailed stages of my professional and education life
            ''')



st.header('My NLP Job Hunt Tool')

intro_tab, prof_tab, edu_tab, skill_tab, cert_tab = st.tabs(['Introduction', 'Professional experience', 'Education', 'Skills', 'Certificates'])

with intro_tab:
    st.markdown('''
                #### This section is my inner tool for optimizing job applications.
                * Upload your resume, and/or cover letter, and job description, and get back:
                    * Gaps between requirements and candidate experience
                    * Soft skills, hard skills and tools that were not mentioned in the documents
                    * Ideas how to improve the douments to better apply for the job
                    * General conclusion
                * Upload the logo of the company, and extract main color palette from it to improve design.
                * Use your openAI token or the password provided by me.
                ''')

with prof_tab:

    with st.expander('Sketch to Image Transformer UI'):
    st.markdown("""## Let's transform your sketches with our AI! :cat:""")
    st.write('description bellow- streamlit canvas is not supported inside tabs')


    # #image_choice = st.radio('I want to see similar:', ('photo', 'sketch'), horizontal = True)
    # image_choice = 'photo'


    # col1, col2 = st.columns(2)

    # with col1:
    #     uploaded_resume = st.file_uploader('Upload your resume')
    #     if uploaded_resume != None:
    #         resume_text = extract_content(uploaded_resume)

    # with col2:
    #     uploaded_cover = st.file_uploader('Upload your cover letter')
    #     if uploaded_cover != None:
    #         cover_text = extract_content(uploaded_cover)

    # text = resume_text + cover_text



    # job_description = st.text_area('Enter job description')

    # if (job_description != '') & ((resume_text != '') | (cover_text != '')) & (token is not None):

    #     openai.api_key = token

    #     if st.button('What am I missing?'):

    #         summary = gpt_job(job_description)['choices'][0]['text']
    #         time.sleep(30)
    #         missing, summary = super_gpt(summary = summary, resume = resume_text, cover = cover_text)

with edu_tab:

    st.markdown('''
                education
                '''
                )

with skill_tab:
    st.header('These are my future plans:')
    st.markdown('''
                skills
                '''
                )
with cert_tab:
    st.header('These are my future plans:')
    st.markdown('''
                * Web scraping feature for job description extraction with a link
                * Company homepage design for a color palette feature with a link
                * Fonts extraction feature
                * Documents modifier feature
                '''
                )