# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)
df_tratado.info()


# %%

#? Base: 1. - A faixa etária do cliente tem uma forte associacão com a taxa de churn.
# Tabela de contingência entre faixa etária e churn:

cross_senior_costumer_churn = round(pd.crosstab(
    df_tratado['SeniorCitizen'], df_tratado['Churn'],
    normalize='index',
) * 100, 2)


# Renomear colunas (Churn)
cross_senior_costumer_churn.rename(
    columns={0: 'Cancelou', 1: 'Não Cancelou'},
    inplace=True
)

#Renomear índices (Senioridade)
cross_senior_costumer_churn.index = cross_senior_costumer_churn.index.map(
    {False: 'Não', True: 'Sim'}
)

 
# %%

#* Visualização

cross_senior_costumer_churn.plot.bar(
    title='Gráfico de Barras do Churn por Senioridade',
    xlabel='Possui idade Senior',
    ylabel='Porcentagem (%)',
)

"""
* Analisando:
* Seniors tem uma taxa menor de churn (60% cancelaram, comparando a 75% dos não Seniors que cancelaram).
* E a medida de não churn (clientes que não cancelaram) se inverte, onde houveram mais cancelamentos que
* os clientes mais novos.
"""


# %%
