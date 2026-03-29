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

#* Removendo dados ausentes por linha, limpando registro quebrados

df_limpo = df_unificado.dropna(axis=0) # 'inplace=True' pode ser usado para modificar o DataFrame na memória.
df_limpo.shape

# Personalizações do argumento 'how':
# 'any' - Remove linhas onde qualquer valor é ausente (padrão).
# 'all' - Remove linhas onde todos os valores são ausentes.


# %%

from common.utils.DataPresentation import print_sequencially

#* Imputação de dados ausentes - Substituição de valores nulos por específicos

df_imputado = df_unificado.fillna('TESTE_VALOR', inplace=False) # 'inplace=True' pode ser usado também.

# Especificando colunas individualmente
df_imputado_colunas = df_unificado.fillna(
      { #ou value={}
        'TotalCharges': 'ABSTRATO',
        'MonthlyCharges': 'MENSALIDADE',
    }
)

query_colunas_modificadas = df_imputado.query(
    "TotalCharges == 'TESTE_VALOR'"
)['TotalCharges']
query_coluna_especificas_modificadas = df_imputado_colunas.query(
    "TotalCharges == 'ABSTRATO' or MonthlyCharges == 'MENSALIDADE'"
)[
    ['TotalCharges', 'MonthlyCharges']  #? Selecionando múltiplas colunas
]

print_sequencially(
    f"DataFrame com imputação geral de dados ausentes: \n{query_colunas_modificadas}",
    f"DataFrame com imputação específica por coluna: \n{query_coluna_especificas_modificadas}",
)


# %%

#* Tratando dados ausentes substituindo pela sua média

df_unificado.fillna(
    value={
        'TotalCharges': df_unificado['TotalCharges'].mean()
    },
    inplace=True
)
# pode ser tratado por coluna (Series) também, onde não se pode especificar outras colunas.

df_unificado.info() # TotalCharges -> 4043 non null


# %%

#* Salvando em novo JSON

from common.utils.DataSavers import save_dict_to_json

dict_from_df = df_unificado.to_dict(orient='records')

save_dict_to_json(
    dict_from_df, 'churn_tratado', overwrite=True
)

# %%
