import streamlit as st


#------Configuração inicial da página web------
st.set_page_config(
    layout='wide',
    page_title='Dashboard',
    initial_sidebar_state='collapsed'
)

tab1, tab2, tab3 = st.tabs(['World sells', 'Sales per country', 'Sales per model', 'Not shipped'])