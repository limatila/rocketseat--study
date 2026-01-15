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

#* Barras

bar_kwargs = {
    'title': 'Gráfico de Barras de cada Altura',
    'xlabel': 'Participante',
    'ylabel': 'Altura (cm)'
}

dataframe['altura'].plot.bar( x='nome', y='altura', **bar_kwargs) #especificando o que representa cada eixo
import matplotlib.pyplot as plt


# Mostra nome de cada participante
plt.xticks(
    ticks=range(len(dataframe)),
    labels=dataframe['nome'],
    rotation=35)
plt.show()


# %%
