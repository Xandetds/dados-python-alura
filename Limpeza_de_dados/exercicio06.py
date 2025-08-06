import pandas as pd

import numpy as np

df_cidades = pd.DataFrame({
    "nome" : ["Alexandre", "carlos", "joao", "maria", "Gabriel"],
    "Cidade" : ["Urussanga", np.nan, "Criciuma", np.nan, "Cocal"]
})

df_cidades["Cidade"] = df_cidades["Cidade"].fillna("Não informado!") #da tambem para substituir direto e nao criar uma coluna nova

print(df_cidades)