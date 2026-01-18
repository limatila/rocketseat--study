# %%

import pandas as pd

from common.utils import DataLoaders, DataPresentation

df_clientes = DataLoaders.load_csv_to_dataframe('churn_contracts', parent_path="./data/datasets/churns/")
df_clientes.info()

DataPresentation.print_sequencially(
    '\n5 primeiros registros:', df_clientes.head(5),
    inicial="\n#---Dataframe dos Contratos---#")


# %%

#* Tratando valores e erros
try:
    df_clientes['TotalCharges'] = df_clientes['TotalCharges'].astype(float, errors='raise')
except ValueError as e:
    #? O 'astype' pode não converter certas strings para float, então usamos 'to_numeric' com 'coerce'
    #? Deixando valores inválidos como NaN para tratamento posterior
    
    if "could not convert" in str(e):
        df_clientes['TotalCharges'] = pd.to_numeric(df_clientes['TotalCharges'], errors='coerce')
        # Outras opções envolvem 'ignore', e 'raise' (padrão)
    else:
        raise e

if df_clientes['TotalCharges'].count() < df_clientes.shape[0]: #Shape vem de Numpy, retorna em 0.Linhas e 1.Colunas
    print(f"Existem {df_clientes['TotalCharges'].isna().sum()} valores NaN em 'TotalCharges'.")


# %%

# Entendendo a resposta para uso de fatura digital no dataset (são 2 flags apenas)
tipos_fatura_digital = df_clientes['PaperlessBilling'].drop_duplicates().values
tipos_fatura_digital = list(tipos_fatura_digital)

# Entendendo os tipos de contratos no dataset (são 3)
tipos_contrato = df_clientes['Contract'].drop_duplicates().values
tipos_contrato = list(tipos_contrato)

# Entendendo os tipos de método de pagamento (são 4)
tipos_metodo_pagamento = df_clientes['PaymentMethod'].drop_duplicates().values
tipos_metodo_pagamento = list(tipos_metodo_pagamento)

DataPresentation.print_sequencially(
    f'\nTipos de Fatura Digital:\n{tipos_fatura_digital}',
    f'\nTipos de Contrato:\n{tipos_contrato}',
    f'\nTipos de Método de Pagamento:\n{tipos_metodo_pagamento}',
    inicial="\n#---Análise dos Tipos de Contratos e Métodos de Pagamento---#"
)


# %%

#* Renomeando colunas

nomes_replace = {
    'customerID': 'ID do Cliente',
    'tenure': 'Tempo de Contrato',
    'Contract': 'Tipo de Contrato',
    'PaperlessBilling': 'Usa Fatura Digital',
    'PaymentMethod': 'Tipo de Método de Pagamento',
    'MonthlyCharges': 'Custo Mensal',
    'TotalCharges': 'Custo Total Cobrado',
    'Churn': 'Cancelou o Serviço'
}

#! Cuidado! Isso renomeia como se deve carregar os nomes de colunas no script
df_clientes.rename(columns=nomes_replace) #inplace=True modifica o DF diretamente, sem redeclaração

print(df_clientes.columns) 


# %%

df_clientes.plot.scatter(
    x='Tempo de Contrato',
    y='Custo Total Cobrado',
    title='Relação entre Tempo de Contrato e Custo Total Cobrado'
)

# %%
