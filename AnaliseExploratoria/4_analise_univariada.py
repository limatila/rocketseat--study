# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)
df_tratado.info()


# %%

from common.utils.DataPresentation import print_sequencially

#* Com base nas propostas descritas no .md do módulo, analisamos univariadamente:

# Contar quantidade de clientes por uso de:
qtd_clientes_servico_telefone = df_tratado.PhoneService.value_counts() # normalize = True exibe porcentagens referentes à amostra
qtd_clientes_servico_internet = df_tratado.InternetService.value_counts()
qtd_clientes_servico_streaming = df_tratado.StreamingTV.value_counts()
#? Usa por dentro df_tratado.NomeColuna.unique(), que retorna a lista de valores enumerados

print_sequencially(
    ('Quantidade de clientes por uso de serviço de telefone:', qtd_clientes_servico_telefone),
    ('Quantidade de clientes por uso de serviço de internet:', qtd_clientes_servico_internet),
    ('Quantidade de clientes por uso de serviço de streaming de TV:', qtd_clientes_servico_streaming),
)


# %%

#* Plot de barras da quantidade de clientes que usam serviço de telefone:

# Serviço de telefone
clientes_telefone_porcentagem = (
    (qtd_clientes_servico_telefone / qtd_clientes_servico_telefone.sum()) * 100
)

bar_plot_telefone = clientes_telefone_porcentagem.plot.bar(
    title='Gráfico de Barras do Uso de Serviço de Telefone',
    xlabel='Uso de Serviço de Telefone',
    ylabel='Porcentagem (%)'
)

bar_plot_telefone.bar_label(bar_plot_telefone.containers[0])


# %%

#* Plot de barras da quantidade de clientes por tipo cobrança de contrato:

colunas_traduzir = {
    'Month-to-month': 'Mês a Mês',
    'One year': 'Um Ano',
    'Two year': 'Dois Anos'
}

df_contratos_traduzido = df_tratado.Contract.replace(colunas_traduzir)

clientes_pagamento_mensal_porcentagem = df_contratos_traduzido.value_counts(normalize=True) * 100

clientes_pagamento_mensal_porcentagem = clientes_pagamento_mensal_porcentagem.reindex(
    ['Mês a Mês', 'Um Ano', 'Dois Anos']
)

bar_plot_contratos = clientes_pagamento_mensal_porcentagem.round(2).plot.bar(
    title='Gráfico de Barras do Tipo de Cobrança Mensal',
    xlabel='Tipo de Cobrança Mensal',
    ylabel='Porcentagem (%)'
)

bar_plot_contratos.bar_label(bar_plot_contratos.containers[0])


# %%
