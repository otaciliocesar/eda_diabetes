# %%
import pandas as pd
# %%
import numpy as np
# %%

#Acessando a base de dados
# %%
diabetes = pd.read_csv('diabetes.csv')
# %%
#Verificando as informações dos dados.
# %%
print(diabetes.info())
# %%
#Validando se as informações contidas na tabela estão com a tipagemm correta
print(diabetes.head(10))
# %%
#Verificando as colunas como solicitado no exercicio 3. How many columns (features) does the data contain?
print(diabetes.columns)
# %%
# print number of rows
print(len(diabetes))
# %%
# find whether columns contain null values
diabetes_null = diabetes['Pregnancies'].isnull().any()
print(diabetes_null)
# %%
diabetes_num_null = diabetes['Pregnancies'].isnull().sum()
print(diabetes_num_null)
# %%
diabetes_columns_null = diabetes.isnull().sum()
print(diabetes_columns_null)
# %%
# perform summary statistics
print(diabetes.describe())
# %%%
# replace instances of 0 with NaN
diabetes[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)
print(diabetes.describe())
# %%%
#Revendo as informações da tabela após substituir os valores nulos
print(diabetes.info())
# %%%
#Verificando quais colunas estão com valores faltando
diabetes2_columns_null = diabetes.columns[diabetes.isnull().any()]
print(diabetes2_columns_null)
#%%
#Verificando a quantidade de valores nulos em cada coluna
diabetes_missing = diabetes.isnull().sum()
print(diabetes_missing)
#%%
#Validando se o valores nulos foramm atualizados
print(diabetes.info())
#%%
#Verificando a coluna Outcome column
print(diabetes['Outcome'].unique())
#%%
# Trocando o valor "O" para "0" e transforando o tipo da coluna para int
diabetes['Outcome'] = diabetes['Outcome'].astype(int)
diabetes['Outcome'] = diabetes['Outcome'].replace('O', '0')
print(diabetes['Outcome'].unique())
#%%
print(diabetes['Outcome'])
#%%
print(diabetes.value_counts)
#%%

# Substitui 0 por NaN em todas as colunas, exceto na coluna 'coluna_ignorada'
diabetes.loc[:, diabetes.columns != 'Outcome'] = diabetes.loc[:, diabetes.columns != 'Outcome'].replace(0, np.nan)

#%%
print(diabetes.value_counts)
# %%
