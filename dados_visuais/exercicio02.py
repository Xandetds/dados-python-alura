import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())

plt.figure(figsize=(8,4))
sns.histplot(df_limpo["salary_in_usd"], bins = 50, kde= True)
plt.title("Distribuição de salarios anuais")
plt.xlabel("Salario (USD)")
plt.ylabel("Frequencia")

plt.show()


