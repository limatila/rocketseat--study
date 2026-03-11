# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)


# %%

#* Analisando Contratos diferentes e seus valores cobrados no período total.

df_tratado.plot.box(
    column='TotalCharges', by='Contract', 
    figsize=(7, 5), title='Boxplot de TotalCharges por Tipo de Contrato'
)


# %%

#* analisando os contratos mensais, há uma alta quantidade de Outliers, 
#* o que pode indicar que há clientes com cobranças muito altas em relação à média dos contratos mensais. 

df_tratado_contratos_mensais = df_tratado.query("Contract == 'Month-to-month'")
df_tratado_contratos_mensais.TotalCharges.hist(
    bins=15, figsize=(7, 5)
)
#* Verificando no histograma, validamos que a distribuição não é normal, MUITO pendente à esquerda.


# %%

#* Analisando Outliers: método de Tukey
#* Técnica capaz de analisar e indentificar os outliers de forma primária em distribuições não normais.

#* IQR = Quartil 3 - Quartil 1 dos dados (1Q = 25% dos dados, 3Q = 75% dos dados)
#* Limite inferior = Q1 - 1.5 * IQR
#* Limite superior = Q3 + 1.5 * IQR

quartil_1_contratos_mensais = df_tratado_contratos_mensais.TotalCharges.quantile(0.25)
quartil_3_contratos_mensais = df_tratado_contratos_mensais.TotalCharges.quantile(0.75)
iqr_contratos_mensais = quartil_3_contratos_mensais - quartil_1_contratos_mensais

limite_inferior_contratos_mensais = ( quartil_1_contratos_mensais - (iqr_contratos_mensais * 1.5) )
limite_superior_contratos_mensais = ( quartil_3_contratos_mensais + (iqr_contratos_mensais * 1.5) )


# %%

from common.utils import DataPresentation

#* Limpando outliers do dataframe de contratos mensais, utilizando os limites calculados pelo método de Tukey.

# Antes de tratar o DF:
shape_df_antes = df_tratado_contratos_mensais.shape

df_outliers_tratados_contratos_mensais = df_tratado_contratos_mensais.query(
    f"TotalCharges >= {limite_inferior_contratos_mensais} and TotalCharges <= {limite_superior_contratos_mensais}"
)

# Depois de tratar o DF:
shape_df_depois = df_outliers_tratados_contratos_mensais.shape

DataPresentation.print_sequencially(
    f"Shape do DataFrame antes de tratar os outliers: {shape_df_antes}",
    f"Shape do DataFrame depois de tratar os outliers: {shape_df_depois}",
    inicial="=== Análise de Outliers - Método de Tukey ===\n"
)

#* Resultado: 200 outliers foram identificados e tratados sobre a diferença do dataframe original e o tratado.


# %%

from scipy.stats import zscore

# * Limpando outliers com o método Z-Score, mais capaz de identificar outliers em distribuições normais, 
#? também pode ser utilizado em distribuições não normais, desde que haja uma quantidade suficiente de dados.
# Mede o quanto cada ponto de dados está distante da média em termos de desvio padrão.

#* Zscore = (Valor - Média) / Desvio Padrão [executado em cada amostra do espaço amostral (dataframe)]

shape_df_depois = df_outliers_tratados_contratos_mensais

# Calcula o Z-Score para a coluna TotalCharges
z_scores = zscore(df_tratado_contratos_mensais['TotalCharges'])

# Identifica outliers (Z-Score absoluto > 3)
treshold_zscore = 3 # limite para análise, convenção
outliers_zscore = df_tratado_contratos_mensais[abs(z_scores) > treshold_zscore] #abs para unificar desvios, positivos e negativos

# Exibe quantidade de outliers encontrados
print(f"Quantidade de outliers pelo método Z-Score: {len(outliers_zscore)}")

# %%
