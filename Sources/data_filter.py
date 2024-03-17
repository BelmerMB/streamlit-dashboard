import pandas as pd

df = pd.read_csv('./Data/sales_data.csv', sep=',', encoding='Windows-1252')
df.drop_duplicates(inplace=True)

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])


#agrupamento por mês e ano de vendas
df_mensal = df.set_index('ORDERDATE').groupby(pd.Grouper(freq='M')).sum().reset_index()
print(df_mensal["SALES"])
# irar colunas não essenciais a principio
# df.drop(columns=["ORDERNUMBER","MSRP","ORDERNUMBER","CUSTOMERNAME","PHONE","ADDRESSLINE1","ADDRESSLINE2", "POSTALCODE", "TERRITORY" ,"CONTACTLASTNAME","CONTACTFIRSTNAME"], inplace=True)
# df.to_csv('sales_data_small.csv')
