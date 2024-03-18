import streamlit as st
from data_filter import df, df_mensal
from grapichs import receita_mensal_mundial
#------Configuração inicial da página web------
st.set_page_config(
    layout='wide',
    page_title='Dashboard',
    initial_sidebar_state='collapsed'
)

tab1, tab2, tab3 = st.tabs(['World sells', 'Sales per country', 'Sales per model'])

with tab1:
    st.dataframe(df)
    st.write("hello")
with tab2:
    columnOne, columnTwo = st.columns(2)
    with columnOne:
        st.dataframe(df_mensal)
        st.plotly_chart(receita_mensal_mundial, use_container_width=True)