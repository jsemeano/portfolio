import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title='Joao Semeano CV',
    page_icon=':palm_tree:',
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)


st.markdown('''
            # Curriculum Vitae
            In the sections below I share the detailed stages of my professional and education life
            ''')


prof_tab, edu_tab, tech_skill_tab, tech_cert_tab, soft_skill_tab, lang = st.tabs(['Professional experience', 'Education', 'Technical skills', 'Online technical certifications', 'Soft skills', 'Languages'])
# prof_tab, edu_tab, tech_skill_tab, lang = st.tabs(['Professional experience', 'Education', 'Online technical certifications', 'Languages'])



def bar_chart(skill_num):
    
    if skill_num == 100:
        skill_num = 99.9

    fig, ax = plt.subplots( figsize=(10, 0.1))
        
    b1 = ax.barh(1, skill_num, color="red")
    b2 = ax.barh(1, 100-skill_num, left=skill_num, color="gainsboro")
    ax.set_axis_off()
    
    return fig


base_path = 'bucket/'

with prof_tab:
    
    subfolder = 'work_life/'

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
        if st.checkbox('Certification', key = 'Certification ECB'):
            # subfolder = 'work_file/'
            # img = Image.open(f'{base_path}{subfolder}ECB.jpg')
            st.image(Image.open(f'{base_path}{subfolder}ECB.jpg').resize((400,500)))


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

    subfolder = 'academic_life/'

    with st.expander('Le Wagon - Data Science Bootcamp'):

        st.markdown(''':date: 10/2022 - 12/2022''')
        st.markdown(''':round_pushpin: Berlin, Germany''')
        st.markdown('''
                    * ETL machine learning bootcamp
                        * Deep dive on SKLearn and TensorFlow
                        * Introduction to cloud environments with Google Cloud Platform
                        * Deployment of apps with Docker and Streamlit
                    * Final project: Image search through sketch (Convolutional Neural Network with custom triplet loss function to suggest pictures similar to a user’s sketch)
                    
                    ''')
        if st.checkbox('Certification', key = 'Certification LeWagon'):
            st.image(Image.open(f'{base_path}{subfolder}lewagon.jpg').resize((400,500)).rotate(-180))
        


    with st.expander('Católica-Lisbon SBE - MSc in Economics'):

        st.markdown(''':date: 04/2015 - 07/2017''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Economic and statistical modelling
                    ''')
        
        if st.checkbox('Certification', key = 'Certification Católica'):
            st.image(Image.open(f'{base_path}{subfolder}catolica1.jpg').resize((400,500)).rotate(-90))
            st.image(Image.open(f'{base_path}{subfolder}catolica2.jpg').resize((400,500)).rotate(-90))
                
        
    
    with st.expander('IST, University of Lisbon - Bsc and MSc in Mechanical Engineering'):

        st.markdown(''':date: 09/2006 - 09/2012''')
        st.markdown(''':round_pushpin: Lisbon, Portugal''')
        st.markdown('''
                    * Intelligent systems and optimization
                    ''')
        
        if st.checkbox('Certification', key = 'Certification MSc'):
            st.image(Image.open(f'{base_path}{subfolder}ist_msc_1.jpg').resize((400,500)).rotate(-90))
            st.image(Image.open(f'{base_path}{subfolder}ist_msc_2.jpg').resize((400,500)).rotate(-90))
                   
        if st.checkbox('Certification', key = 'Certification BSc'):
            st.image(Image.open(f'{base_path}{subfolder}ist_bsc_1.jpg').resize((400,500)).rotate(-90))
            st.image(Image.open(f'{base_path}{subfolder}ist_bsc_2.jpg').resize((400,500)).rotate(-90))
            st.image(Image.open(f'{base_path}{subfolder}ist_bsc_3.jpg').resize((400,500)).rotate(-90))
                   
        



with tech_skill_tab:
    st.markdown('''
                ### Technical skills
                '''
                )
    
    
    
    # # Option with points
    # cols = st.columns([9, 1, 1, 1, 1, 1, 20])
    
    # cols[0].markdown('Data Analysis')
    # cols[1].markdown(':red_circle:')
    # cols[2].markdown(':red_circle:')
    # cols[3].markdown(':red_circle:')
    # cols[4].markdown(':red_circle:')
    # cols[5].markdown(':red_circle:')
    
    # option with bars
    # cols = st.columns([9, 1, 1, 1, 1, 1, 20])
    cols = st.columns([9,20])
    
    cols[0].markdown('Data analysis')
    with cols[1]:
       
        st.pyplot(bar_chart(100))
            
    cols = st.columns([9,20])
            
    cols[0].markdown('ETL pipelines')
    with cols[1]:
       
        st.pyplot(bar_chart(100))        
            
    cols = st.columns([9,20])           
    cols[0].markdown('Statistical modelling')
    with cols[1]:
       
        st.pyplot(bar_chart(100))
        
            
    cols = st.columns([9,20])                    
    cols[0].markdown('Bayesian analysis')
    with cols[1]:
       
        st.pyplot(bar_chart(75))
            
    cols = st.columns([9,20])                    
    cols[0].markdown('Machine learning')
    with cols[1]:
       
        st.pyplot(bar_chart(50))
            
    cols = st.columns([9,20])        
    cols[0].markdown('GIS')
    with cols[1]:
       
        st.pyplot(bar_chart(50))
        
    st.markdown('''
                ### Software
                '''
                )
    
    cols = st.columns([9,20])
    
    cols[0].markdown('Python')
    with cols[1]:
       
        st.pyplot(bar_chart(100))
            
    cols = st.columns([9,20])        
    cols[0].markdown('Excel/VBA')
    with cols[1]:
       
        st.pyplot(bar_chart(100))
            
    cols = st.columns([9,20])        
    cols[0].markdown('SQL')
    with cols[1]:
       
        st.pyplot(bar_chart(75))
            
    cols = st.columns([9,20])        
    cols[0].markdown('Git')
    with cols[1]:
       
        st.pyplot(bar_chart(75))
            
    cols = st.columns([9,20])        
    cols[0].markdown('Google cloud platform')
    with cols[1]:
       
        st.pyplot(bar_chart(50))
            
    cols = st.columns([9,20])
    cols[0].markdown('Amazon Warehouse Services')
    with cols[1]:
       
        st.pyplot(bar_chart(50))
            
    cols = st.columns([9,20])        
    cols[0].markdown('Docker')
    with cols[1]:
       
        st.pyplot(bar_chart(25))
            
    cols = st.columns([9,20])
    cols[0].markdown('dbt')
    with cols[1]:
       
        st.pyplot(bar_chart(25))        
            
    cols = st.columns([9,20])
    cols[0].markdown('Snowflake')
    with cols[1]:
       
        st.pyplot(bar_chart(25))
            
    cols = st.columns([9,20])
    cols[0].markdown('Looker')
    with cols[1]:
       
        st.pyplot(bar_chart(25))
 
            
    cols = st.columns([9,20])
    cols[0].markdown('MLFlow')
    with cols[1]:
       
        st.pyplot(bar_chart(25))        
            
    cols = st.columns([9,20])
    cols[0].markdown('Uvicorn')
    with cols[1]:
       
        st.pyplot(bar_chart(25))
            
    cols = st.columns([9,20])
    cols[0].markdown('R')
    with cols[1]:
       
        st.pyplot(bar_chart(25))           
 
    st.markdown('''
            ### Python packages
            '''
            )
    
    cols = st.columns([9,20])

    cols[0].markdown('Pandas')
    with cols[1]:
       
        st.pyplot(bar_chart(100))
            
    cols = st.columns([9,20]) 
    cols[0].markdown('Numpy')
    with cols[1]:

        st.pyplot(bar_chart(100))
            
    cols = st.columns([9,20])        
    cols[0].markdown('Matplotlib/Seaborn')
    with cols[1]:
       
        st.pyplot(bar_chart(75))
            
    cols = st.columns([9,20])
    cols[0].markdown('TensorFlow/Keras')
    with cols[1]:
       
        st.pyplot(bar_chart(75))         
            
    cols = st.columns([9,20]) 
    cols[0].markdown('SKLearn')
    with cols[1]:

        st.pyplot(bar_chart(75))    
            
    cols = st.columns([9,20])    
    cols[0].markdown('FastApi')
    with cols[1]:
       
        st.pyplot(bar_chart(50))
            
    cols = st.columns([9,20])
    cols[0].markdown('Geopandas')
    with cols[1]:
       
        st.pyplot(bar_chart(25))     
            
    cols = st.columns([9,20])
    cols[0].markdown('Rasterio')
    with cols[1]:
       
        st.pyplot(bar_chart(25))     



with tech_cert_tab:
    subfolder = 'academic_life/'
    
    col5, col6 = st.columns(2)
    
    with col5:
    
        st.markdown("[![Foo](https://new.inform-datalab.com/wp-content/uploads/snowflake-logo.png)](https://www.credly.com/badges/36c8d90d-894d-4006-80db-d9546b08c224/linked_in_profile)")
    
        st.markdown("[![Foo](https://awsmp-logos.s3.amazonaws.com/70b90c19-ed12-4fe9-a99e-28dcea832219/f36486226e4d0430922cb95a55a1edfb.png)](https://www.credential.net/ab3f6a44-df0e-46d1-a7ae-11f8c544f642)")
    
    
    st.image(Image.open(f'{base_path}{subfolder}SQL_UC_DAVIS.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}scrum_methoddologies.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}scaling_agile.JPG'))
    st.image(Image.open(f'{base_path}{subfolder}applied_machine_learning_michigan.JPG'))
  
    

with soft_skill_tab:
 
    st.markdown('''
            ### Working style
            
            * Curious
            * Proactive
            * Team player 
            * Pragmatic}
            '''
            )   
    
 
    st.markdown('''
            ### Languages
            
            * Portuguese (Native)
            * English (C2)
            * German (B2)
            * Spanish (B2)
            '''
            )   

with lang:
    pass



