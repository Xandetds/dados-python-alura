import pandas as pd

import numpy as np

import matplotlib.pyplot as plt 

import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())

#df_limpo["experience_level"].value_counts().plot(kind= "bar", title="Distribuiçao de senioridade")                  #Comentando graficos pois somente um abre por vez pelo vscode
                                                                                                       

ordem_crescente = df_limpo.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending= True).index


plt.figure(figsize=(8, 5))
sns.barplot(data= df_limpo, x= "experience_level", y= "salary_in_usd", order= ordem_crescente)
plt.title("salario medio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salario médio anual (USD)")



plt.show() #abre outra janela com o grafico



