# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Dispersao/data")
print(dados)


# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)


# %%
#* Estatísticas descritivas básicas do DataFrame.

dataframe.describe()
# Exibe contas básicas, desvios, além da medida conforme gráfico de distribuição de amostra normal.


# %%

from common.utils import DataPresentation

DataPresentation.print_sequencially(
    dataframe['altura'].mean(), # Média Aritmética
    dataframe['idade'].median(), # Mediana
    dataframe['cidade'].mode(), # Moda
)


# %%

from common.utils import DataPresentation

DataPresentation.print_sequencially(
    dataframe.idade.var(), # A Variância, medida quantitativa matemática, indica o quão os dados estão espalhados em relação à média.
    dataframe.idade.std(), # O Desvio Padrão, medida qualitativa real, indica o quão os dados estão dispersos, na unidade de medida original.
    dataframe.idade.std() / dataframe.idade.mean(), # Coeficiente de Variação, medida qualitativa percentual, indica o quão os dados estão dispersos em relação à média em termos percentuais.
)

