# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)
df_tratado.info()


# %%

#* Querys: analisando registros com determinadas condições

#? Base: 3. - Clientes com múltiplos serviços (internet, telefone, TV a cabo) têm uma taxa de churn menor.
# Clientes filtrados que possuem os 3 serviços:
clientes_multiplos_servicos = df_tratado[
    (df_tratado.PhoneService == True) &
    (df_tratado.InternetService != 'No') &
    (df_tratado.StreamingTV == 'Yes')
]
# query nativa

registros_diferentes_servicos = clientes_multiplos_servicos[
    ['PhoneService', 'InternetService', 'StreamingTV', 'Churn']
]
registros_diferentes_servicos.value_counts()


# %%

#* Mostrando dados

churn_multiplos_servicos = clientes_multiplos_servicos['Churn']

(churn_multiplos_servicos.value_counts(normalize=True) * 100).plot.bar(
    title='Gráfico de Barras do Churn de Clientes com Múltiplos Serviços',
    xlabel='Churn',
    ylabel='Porcentagem (%)'
)

#* Resultado: 30% dos clientes que possuem multiplos serviços (os 3 ao mesmo tempo) cancelaram contrato


# %%

clientes_sem_multiplos_servicos = df_tratado[~(df_tratado.index.isin(clientes_multiplos_servicos.index))]

churn_sem_multiplos_servicos = clientes_sem_multiplos_servicos['Churn']
(churn_sem_multiplos_servicos.value_counts(normalize=True) * 100).plot.bar(
    title='Gráfico de Barras do Churn de Clientes sem Múltiplos Serviços',
    xlabel='Churn',
    ylabel='Porcentagem (%)'
)

#* Resultado do inverso: 25% dos clientes que não possuem multiplos serviços (os 3 ao mesmo tempo) cancelaram contrato


# %%
