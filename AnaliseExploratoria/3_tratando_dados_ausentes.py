# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_unificado.out', parent_path='./data/output/')

df_unificado = pd.DataFrame.from_dict(dados)
df_unificado.info()


# %%

#* Tratando dados para o tipo float e booleano

colunas_numericas = [
    'MonthlyCharges',
    'TotalCharges',
]

for coluna_a_corrigir in colunas_numericas:
        df_unificado[coluna_a_corrigir] = (
            pd.to_numeric(
                df_unificado[coluna_a_corrigir],
                errors='coerce'
            )
        )

colunas_booleanas = [
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'PaperlessBilling',
    'Churn',
    'PhoneService',
]

for coluna_a_corrigir in colunas_booleanas:
    df_unificado[coluna_a_corrigir] = (
        df_unificado[coluna_a_corrigir]
        .map({'Yes': True, 'No': False, 1: True, 0: False})
    )

# %%

#* Verificando dados ausentes

# dados ausentes por coluna
print('\nDados Ausentes em cada Index:')
df_unificado[df_unificado.isna().any(axis=1)]['TotalCharges']


# %%
