# %%
from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Dispersao/data")
print(dados)

# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)

# %%

dataframe.describe()

# %%
from common.utils import DataPresentation

DataPresentation.print_sequencially(
    dataframe['altura'].mean(),
    dataframe['idade'].median(),
    dataframe['cidade'].mode(),
)


# %%
from common.utils import DataPresentation

DataPresentation.print_sequencially(
    dataframe['idade'].var(),
    dataframe['altura'].std(),
)

