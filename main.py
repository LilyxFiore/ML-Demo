import pandas as pd
import datetime as dt

id=input('introduzca id del cliente:')

df1=pd.read_csv("Datasets/datasetout/customer_out.csv",encoding='mbcs',dtype={"customer_id": str})
df1258=pd.read_csv("Datasets/datasetout/final_out.csv",encoding='mbcs',dtype={"customer_id": str})

a=df1258[df1258["customer_id"]==id].iloc[:,15]
b=df1258[df1258["category"]==a.iloc[0]]
b=b["product_name"].drop_duplicates()

print("Productos recomendados:")
print (b[0:5].to_list())