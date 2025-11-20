import streamlit as st

import warnings
warnings.filterwarnings("ignore")


st.title('Dashboard')
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Overview','Heatmaps']) # Future development: 'Glossary', 'Suggestions'

#************************************************************
#*SETTING UP TAB 1 - OVERVIEW
#************************************************************

st.divider()
st.caption("© 2025 - EikosApp.com. All Rights Reserved")
