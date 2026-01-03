# %%
from pandas import DataFrame, Series

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Medidas/data")
print(dados)

# %%


