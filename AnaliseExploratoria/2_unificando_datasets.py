# %%
#* Utilizando vários dataframes de CSVs diferentes para realizar a análise exploratória
#* com o máximo de dados possíveis.

import pandas as pd

from common.utils import DataPresentation
from common.utils.DataLoaders import load_csv_to_dataframe

PARENT_CHURNS_PATH: str = "./data/datasets/churns/"

df_clientes = load_csv_to_dataframe('churn_customers', parent_path=PARENT_CHURNS_PATH)
df_contratos = load_csv_to_dataframe('churn_contracts', parent_path=PARENT_CHURNS_PATH)
df_servicos = load_csv_to_dataframe('churn_services', parent_path=PARENT_CHURNS_PATH)

DataPresentation.print_sequencially(
    f'Clientes {df_clientes.columns.tolist()}',
    f'Contratos {df_contratos.columns.tolist()}',
    f'Serviços {df_servicos.columns.tolist()}',
    inicial='Dataframes carregados:\n'
)

DataPresentation.print_sequencially(
    f'Clientes: {df_clientes.shape}',
    f'Contratos: {df_contratos.shape}',
    f'Serviços: {df_servicos.shape}',
    inicial='Shapes dos Dataframes:\n',
    early_breakline=True
)


# %%

#* Unificando datasets

df_unificado = df_clientes.merge(
    df_contratos,
    on=['customerID'],
    how='left'
)

df_unificado = df_unificado.merge(
    df_servicos,
    left_on=['customerID'],
    right_on=['Customer_ID'],
    how='left'
)

# Removendo coluna discrepante
df_unificado = df_unificado.drop(columns=['Customer_ID'])

df_unificado.info()

print('\nDataframe Unificado - Primeiras 5 linhas:\n')
df_unificado.head(5)
        

# %%

#* Salvando em novo JSON

from common.utils.DataSavers import save_dict_to_json

dict_from_df = df_unificado.to_dict(orient='records')

save_dict_to_json(
    dict_from_df, 'churn_unificado', overwrite=True
)


# %%
