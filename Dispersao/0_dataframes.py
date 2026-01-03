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

