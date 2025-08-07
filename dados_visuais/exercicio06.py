import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())


remoto_contagem = df_limpo["remote_ratio"].value_counts().reset_index()
remoto_contagem.columns = ["tipo_tabalho", "quantidade"]

fig = px.pie(remoto_contagem,
            names= "tipo_trabalho",
            values= "quantidade",
            title= "Proporção dos tipos de trabalho",
            hole= 0.5 #vai de pizza pra rosca
            )

fig.update_traces(textinfo= "percent+label")
fig.show()

