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