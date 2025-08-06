import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.isnull())

print("---------------------------------------------------------------------------------------------------")

print(df.head())

print("---------------------------------------------------------------------------------------------------")

print(df.isnull().sum())

print("---------------------------------------------------------------------------------------------------")

print(df["work_year"].unique())

print("---------------------------------------------------------------------------------------------------")

print(df[df.isnull().any(axis=1)])
