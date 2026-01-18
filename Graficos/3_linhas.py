# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('faturamento-limpo', parent_path="./Graficos/data")
print(dados)


# %%

import pandas as pd

dataframe = pd.DataFrame.from_dict(dados)
print(dataframe)


# %%

#* Tratando dados mal tipados:

# Para correta inferência de dados, é necessário converter a coluna de meses de referencias para o tipo datetime
dataframe['mes_referencia'] = pd.to_datetime(dataframe['mes_referencia'])
dataframe.info()

# Antes: carregado como 'object', pois era simplesmente uma string
# Depois: convertido para 'datetime64[ns], para correta análise temporal'

# %%

#* Definindo o índice do DataFrame como a coluna dos meses de referência:

dataframe.set_index('mes_referencia', inplace=True)
print(dataframe)


# %%

#* Gráfico de Linhas

line_kwargs = {
    'title': 'Gráfico de Linhas do Faturamento ao Longo dos Meses',
    'xlabel': 'Mês de Referência',
    'ylabel': 'Faturamento (R$)'
}

dataframe.plot.line(
    y='faturamento_total',
    **line_kwargs
)

# %%
