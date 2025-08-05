import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.columns)



print("---------------------------------------------------------------------------------------------------")



renomear_colunas = {
    'work_year' : 'ano',
    'experience_level': 'senioridade', 
    'employment_type' : 'contrato', 
    'job_title' : 'cargo',
    'salary' : 'salario', 
    'salary_currency' : 'moeda',
    'salary_in_usd' : 'salario_em_dolar', 
    'employee_residence' : 'residencia',
    'remote_ratio' : 'remoto', 
    'company_location' : 'empresa', 
    'company_size' : 'tamanho_empresa'
}

df.rename(columns = renomear_colunas, inplace=True)
print(df.columns)



print("---------------------------------------------------------------------------------------------------")



print(df["senioridade"].value_counts())

print("---------------------------------------------------------------------------------------------------")

print(df["contrato"].value_counts())

print("---------------------------------------------------------------------------------------------------")

print(df['remoto'].value_counts())

print("---------------------------------------------------------------------------------------------------")

print(df['tamanho_empresa'].value_counts())


print("---------------------------------------------------------------------------------------------------")


senioridade = {
    'SE' : 'senior',
    'MI' : 'pleno',
    'EN' : 'junior' ,
    'EX' : 'executivo'
}

df['senioridade'] = df['senioridade'].replace(senioridade)
print(df["senioridade"].value_counts())


print("---------------------------------------------------------------------------------------------------")



contrato = {
    'FT' : 'integral',
    'PT' : 'meio periodo',
    'FL' : 'freelancer' ,
    'CT' : 'contrato temporario'
}

df['contrato'] = df['contrato'].replace(contrato)
print(df["contrato"].value_counts())


print("---------------------------------------------------------------------------------------------------")



tamanho_empresa = {
    'S' : 'pequena',
    'M' : 'media',
    'L' : 'grande' 
    }

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df["tamanho_empresa"].value_counts())


print("---------------------------------------------------------------------------------------------------")


remoto = {
    0 : 'presencial',
    50 : 'hibrido',
    100 : 'remoto'
}

df['remoto'] = df['remoto'].replace(remoto)
print(df["remoto"].value_counts())

print("---------------------------------------------------------------------------------------------------")

print(df.head())


print("---------------------------------------------------------------------------------------------------")


print(df.describe(include = "object"))


print("---------------------------------------------------------------------------------------------------")


print(df.describe())


