# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Medidas/data")
print(dados)


# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)


# %%

#* Gráfico de Dispersão
dispersao_kwargs = {
    'title': 'Gráfico de Dispersão entre Altura e Idade',
    'xlabel': 'Idade (anos)',
    'ylabel': 'Altura (cm)',
    'color': 'black',
    'marker': 'o'
}


dataframe.plot.scatter(
    x='idade',
    y='altura',
    **dispersao_kwargs
)

# Note que na nossa amostra, existem 2 Outliers (pontos fora do padrão). 
# Uma criança muito alta, e um adulto muito baixo.


# %%

#* Box Plot
boxplot_kwargs = {
    'ylabel': 'Valores',
    'grid': True
}

dataframe.boxplot(
    column=['idade'],
    **boxplot_kwargs
)


# %%

dataframe.boxplot(
    column=['altura'],
    **boxplot_kwargs
)

