import pandas as pd

import numpy as np

df_salarios = pd.DataFrame({  #cria uma base de para testar numeros nulos e organização
    "nome" : ["Alexandre", "Isabela", "Rafael", "Daniela", "Suele", "Elvio"],
    "salario" : [2550, 2000, np.nan, 5000, np.nan, 5000]
     })

df_salarios["salario_media"] = df_salarios["salario"].fillna(df_salarios["salario"].mean().round(2)) #calcula a media e substitui salarios null


print(df_salarios)