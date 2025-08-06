import pandas as pd

import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df_limpo = df.dropna()

print(df_limpo.isnull().sum())

print(df_limpo.head())

print(df_limpo.info())

df_limpo = df_limpo.assign(work_year = df_limpo["work_year"].astype("int64"))

print(df_limpo.info())
