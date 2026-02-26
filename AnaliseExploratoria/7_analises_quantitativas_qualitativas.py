# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)


# %%

import numpy as np

#? Base: 5. - Clientes com contratos anuais são menos propensos ao churn.
# Interpretando coluna nova no dataframe com base numa condição sobre Contratos Anuais:

df_tratado['isAnualContract'] = np.where(df_tratado.tenure < 6, True, False)
df_tratado.info()


# %%

#Criando tabela de contingência

df_crosstab_churn_anual_condition = pd.crosstab(
    df_tratado.Churn, df_tratado.isAnualContract
)
df_crosstab_churn_anual_condition


# %%

from scipy.stats import chi2_contingency

#Calculando p-valor e outros scores

chi_scores_churn_anual_condition = chi2_contingency(df_crosstab_churn_anual_condition)
chi_scores_churn_anual_condition

p_valor_churn_anual_condition = chi_scores_churn_anual_condition[1]
scores_churn_anual_condition = chi_scores_churn_anual_condition[0]

# * Resultado:
p_valor_churn_anual_condition 
#* p-valor muito menor que 0.05, 1^-147, variáveis não são independentes, ou seja, existe uma associação entre as variáveis.

scores_churn_anual_condition
#* Qui2 de +- 669.72, indicando uma associação forte entre as variáveis, ou seja, clientes com contratos anuais são menos propensos ao churn.

#* A hipótese nula (H0) é rejeitada, indicando que existe uma associação significativa entre as variáveis analisadas.
#* A hipótese alternativa (H1) é aceita, sugerindo que clientes com contratos anuais são menos propensos ao churn.


# %%
