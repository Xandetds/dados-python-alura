import pandas as pd

import numpy as np

df_temperaturas = pd.DataFrame({   #cria uma base de para testar numeros nulos e organização
    "Dia" : ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], 
    "Temperatura" : [30, np.nan, 24.4, np.nan, 15.5]
}) 

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()

print(df_temperaturas)
