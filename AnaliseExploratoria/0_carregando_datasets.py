# %%

from common.utils import DataLoaders, DataPresentation


df_clientes = DataLoaders.load_csv_to_dataframe('churn_customers', parent_path="./data/datasets/churns/")
df_clientes.info()

DataPresentation.print_sequencially(
    '\n5 primeiros registros:', df_clientes.head(5),
    inicial="\n#---Dataframe dos Clientes---#")

