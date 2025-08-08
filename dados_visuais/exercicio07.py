import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())

df_data_engineer = df_limpo[df_limpo['job_title'] == 'Data Engineer']

salario_por_pais_data_engineer = df_limpo["remote_ratio"].value_counts().reset_index()
salario_por_pais_data_engineer.columns = ["remote_ratio", "job_title"]

fig = px.pie(salario_por_pais_data_engineer,
            names= "job_title",
            values= "remote_ratio",
            title= "Proporção dos engenheiros de dados trabalhando remotamente",
            )

fig.update_traces(textinfo= "percent+label")

fig.write_html("salario_por_pais_data_engineer.html") # Salva o gráfico em um arquivo HTML
import webbrowser # Importa a biblioteca para abrir o navegador
webbrowser.open("salario_por_pais_data_engineer.html")