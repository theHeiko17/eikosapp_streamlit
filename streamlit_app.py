import streamlit as st
import pandas as pd


def renderPage():
    dashboard_page = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/table:")
    about_page =  st.Page("pages/about.py", title="About", icon=":material/contact_page:")
    pg = st.navigation(
                {
                    "My Eikos": [dashboard_page],
                    "About": [about_page],
                    
                },position="sidebar"
            )
    
    st.set_page_config(layout="wide",initial_sidebar_state="auto", page_title="EIKOS - Probabalistic Market Insights") #, 

    pg.run()