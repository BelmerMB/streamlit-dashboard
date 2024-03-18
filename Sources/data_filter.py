import pandas as pd

try:
    df = pd.read_csv('./Data/sales_data.csv', sep=',', encoding='Windows-1252')
except FileNotFoundError as fn:
    print(f'File not found or doesnot exist, check the path and the name\nExiting...')
    exit(0)



df.drop_duplicates(inplace=True)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])


#agrupamento por mês e ano de vendas
df_mensal = df.set_index('ORDERDATE').groupby(pd.Grouper(freq='M')).sum().reset_index()
df_mensal['Ano'] = df_mensal['ORDERDATE'].dt.year
df_mensal['mes'] = df_mensal['ORDERDATE'].dt.month_name(locale='Portuguese')
# df.drop(columns=["ORDERNUMBER","MSRP","ORDERNUMBER","CUSTOMERNAME","PHONE","ADDRESSLINE1","ADDRESSLINE2", "POSTALCODE", "TERRITORY" ,"CONTACTLASTNAME","CONTACTFIRSTNAME"], inplace=True)
# df.to_csv('sales_data_small.csv')
