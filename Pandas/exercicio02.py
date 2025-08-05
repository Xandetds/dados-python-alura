import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.columns)

renomear_colunas = {
    'work_year' : 'ano',
    'experience_level': 'nivel_experiencia', 
    'employment_type' : 'tipo_emprego', 
    'job_title' : 'cargo',
    'salary' : 'salario', 
    'salary_currency' : 'moeda_salario',
    'salary_in_usd' : 'salario_em_usd', 
    'employee_residence' : 'residencia_empregado',
    'remote_ratio' : 'taxa_remoto', 
    'company_location' : 'localizacao_empresa', 
    'company_size' : 'tamabnho_empresa'
}

df.rename(columns = renomear_colunas, inplace=True)
print(df.columns)