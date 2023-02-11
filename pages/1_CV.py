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


prof_tab, edu_tab, skill_tab, cert_tab = st.tabs(['Professional experience', 'Education', 'Skills', 'Certificates'])

with prof_tab:
    

    
    # Define a custom CSS style for the expander header
    st.set_config(**{
            "expander": {
                "header_expand_icon": '<svg style="color: red;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M8 16l4-4 4 4z"/></svg>',
                "header_collapse_icon": '<svg style="color: red;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M16 8l-4 4-4-4z"/></svg>',
                "header_font_size": "24px",
                "header_font_weight": "bold",
                "header_color": "blue",
                "border_radius": "10px",
                "background_color": "#f0f0f0",
                "padding": "10px",
            }
        }
    )

    with st.expander('Freelance - Data Engineer'):

        st.markdown(''':date: 12/2022 - Current''')
        st.markdown(''':round_pushpin: Berlin, Germany''')
        st.markdown('''
                    * Deforestation alert system : Leveraging of satellite imagery to give an NGO early warning of deforestation activities in the Amazon
                    * Responsible for API building and data infrastructure''')
    # Apply CSS styling to the text
        


    with st.expander('Le Wagon - Teaching Assistant'):

        st.markdown(''':date: 01/2023 - Current''')
        st.markdown(''':round_pushpin: Berlin, Germany''')
        st.markdown('''
                    * One on one work with students to improve their understanding of coding''')


    with st.expander('European Central Bank - Research Analyst'):

        st.markdown(''':date: 02/2017 - 12/2021''')
        st.markdown(''':round_pushpin: Frankfurt am Main, Germany''')
        st.markdown('''
                    * Improving the ETL pipeline for the ECB economic forecast including automation and quality assessment procedures
                    * Providing input to ad-hoc briefings to the governing council
                    * Developing of internal dashboards to clearly present the developments in the public finances of EU member states
                    * Applying diverse time-series methods in debt and wage forecasting
                    ''')


    with st.expander('Católica-Lisbon SBE - Faculty Assistant'):

        st.markdown(''':date: 09/2016 - 02/2017''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Lecturing undergraduates on the basic tools used for data analysis
                    ''')

    with st.expander('TechnipFMC - Engineer'):

        st.markdown(''':date: 08/2013 - 08/2015''')
        st.markdown(''':round_pushpin: Kongsberg, Norway''')
        st.markdown('''
                    * Coordinating the designer team for a complete engineering project
                    * Deploying root cause analysis methods
                    ''')


    with st.expander('Sonae SR - Business Analyst'):

        st.markdown(''':date: 05/2012 - 05/2013''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Developing of a predictive alarm system for delays of big deliveries
                    * Tracking of KPI’s
                    * Methodical analysis of sales to understand market dynamics
                    ''')




with edu_tab:

    with st.expander('Le Wagon - Data Science Bootcamp'):

        st.markdown(''':date: 10/2022 - 12/2022''')
        st.markdown(''':round_pushpin: Berlin, Germany''')
        st.markdown('''
                    * ETL machine learning bootcamp
                    * Final project: Image search through sketch (Convolutional Neural Network with custom triplet loss function to suggest pictures similar to a user’s sketch)''')


    with st.expander('Católica-Lisbon SBE - MSc in Economics'):

        st.markdown(''':date: 04/2015 - 07/2017''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Economic and statistical modelling
                    ''')
        
    
    with st.expander('IST, University of Lisbon - MSc in Mechanical Engineering'):

        st.markdown(''':date: 09/2006 - 09/2012''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Intelligent systems and optimization
                    ''')
        
        
        

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