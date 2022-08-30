import os
import pandas as pd
import plotly.express as px

chart_total = pd.DataFrame()

data_list = os.listdir("C:/Users/Anase/Desktop/workspace/python/01-15 - Curso de Python - Aula 1-/01-15 - Curso de Python - Aula 1/Vendas")

for data in data_list:
    if 'Vendas' in data:
        chart = pd.read_csv(f"C:/Users/Anase/Desktop/workspace/python/01-15 - Curso de Python - Aula 1-/01-15 - Curso de Python - Aula 1/Vendas/{data}")
        chart_total = chart_total.append(chart)
        print(chart_total)

chart_produtos = chart_total.groupby('Produto').sum()
chart_produtos = chart_produtos[["Quantidade Vendida", 'Preco Unitario']].sort_values(by="Quantidade Vendida", ascending=True)
print(chart_produtos)

chart_total['Faturamento'] = chart_total['Quantidade Vendida'] * chart_total['Preco Unitario']

chart_faturamento = chart_total.groupby('Produto').sum()
chart_faturamento = chart_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(chart_faturamento)

chart_stores = chart_total.groupby('Loja').sum()
chart_stores = chart_stores[["Faturamento"]]
print(chart_stores)

fig = px.bar(chart_stores, x=chart_stores.index, y='Faturamento')
fig.show()