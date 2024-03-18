from data_filter import df, df_mensal
import plotly.express as px

receita_mensal_mundial = px.line(
    df_mensal,
    x='ORDERDATE',
    y='SALES',
    markers=True,
    range_y=(0, df_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Vendas mensal - mundo'
)
receita_mensal_mundial.update_layout(yaxis_title = 'Receita')