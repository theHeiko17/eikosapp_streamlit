import streamlit as st

import warnings
warnings.filterwarnings("ignore")


st.title('Dashboard')
tab1, tab2 = st.tabs(['Overview','Heatmaps']) # Future development: 'Glossary', 'Suggestions'

#************************************************************
#*SETTING UP TAB 1 - OVERVIEW
#************************************************************
with tab1:
    st.header("Majors")
    prices_maj = st.empty()
    st.header("Minors")
    prices_min = st.empty()

with tab2:
    heatmap_cont = st.empty()



st.divider()
st.caption("© 2025 - EikosApp.com. All Rights Reserved")


