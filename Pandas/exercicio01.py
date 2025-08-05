import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head(7))

print("---------------------------------------------------------------------------------------")

print(df.info())

print("---------------------------------------------------------------------------------------")

print(df.describe())

print("---------------------------------------------------------------------------------------")

print(df.shape)

print("---------------------------------------------------------------------------------------")

linhas, colunas = df.shape[0], df.shape[1]

print("linhas: ", linhas)
print("colunas: ", colunas)
