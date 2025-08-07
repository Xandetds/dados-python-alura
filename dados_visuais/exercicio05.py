import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())


senioridade_media_salario = df_limpo.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending= False).reset_index()

fig = px.bar(senioridade_media_salario, x= "experience_level", y= "salary_in_usd", title= "Media salarial por senioridade", labels= {"experience_level": "Nivel de senioridade", "salary_in_usd": "Media salarial anual (USD)"})

fig.show()

