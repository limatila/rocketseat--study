# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Medidas/data")
print(dados)


# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)


# %%

#* Histogramas

dataframe.idade.plot.hist(title='Histograma de Idade', xlabel='Idade', ylabel='Frequência dos Dados')


# %%

import matplotlib.pyplot as plt

#* Barras

bars_altura_kwargs = {
    'title': 'Gráfico de Barras de cada Altura',
    'xlabel': 'Participante',
    'ylabel': 'Altura (cm)'
}

#Ordenando decrescentemente o gráfico de barras por altura
ASC = False
dataframe_ordenado_altura = dataframe.sort_values(by='altura', ascending=ASC)

dataframe_ordenado_altura['altura'].plot.bar( x='nome', y='altura', **bars_altura_kwargs) #especificando o que representa cada eixo

# Mostra nome de cada participante
plt.xticks(
    ticks=range(len(dataframe_ordenado_altura)),
    labels=dataframe_ordenado_altura['nome'],
    rotation=35)
plt.show()


# %%

import matplotlib.pyplot as plt

#* Barras Horizontais

bars_idade_kwargs = {
    'title': 'Gráfico de Barras Horizontais de Idade',
    'xlabel': 'Idade',
    'ylabel': 'Participante'
}

ASC = True
dataframe_ordenado_idade = dataframe.sort_values(by='idade', ascending=ASC)

dataframe_ordenado_idade.plot.barh(
    x='nome',
    y=['idade', 'altura'], #Mostrando duas colunas no mesmo gráfico
    **bars_idade_kwargs
)

# Mostrando labels, em y
plt.yticks(
    ticks=range(len(dataframe_ordenado_idade)),
    labels=dataframe_ordenado_idade['nome'],
    rotation=10)
plt.show()

# %%
