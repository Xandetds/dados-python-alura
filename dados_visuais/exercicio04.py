import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

df_limpo.isnull().sum()

print(df_limpo.head())

ordem_senioridade = ["EN", "MI", "SE", "EX"]
sns.boxplot(x="experience_level", y="salary_in_usd", data= df_limpo, order = ordem_senioridade, palette= "Set2", hue= "experience_level")
plt.title("Salario por senioridade")
plt.xlabel("Salario (USD)")
plt.show()