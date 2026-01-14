# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Medidas/data", exclude_keys=['nome', 'cidade'])
print(dados)


# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)


# %%
from common.utils import DataPresentation


#* Correlação
# Mede a relação entre duas variáveis, indicando se elas tendem a aumentar ou diminuir juntas (ou não são relacionadas).


#* Coeficiente de Correlação de Pearson
# Pearson mede a relação linear entre duas variáveis contínuas
corr_pearson = dataframe.corr(method='pearson')

# colunas iguais terão correlação 1, porque são idênticas
# colunas não iguais serão mais correlacionadas conforme valores se aproximam de 1
# colunas inversamente correlacionadas terão valores próximos de -1

#* Coeficiente de Correlação de Spearman
# Spearman é usado para dados ordinais ou quando a relação não é linear
corr_spearman = dataframe.corr(method='spearman')


#* Coeficiente de Correlação de Kendall
# Kendall é outra medida para dados ordinais, focando na concordância entre pares de observações
corr_kendall = dataframe.corr(method='kendall')

DataPresentation.print_sequencially(
    f'Pearson: \n{corr_pearson}',
    f'Spearman: \n{corr_spearman}',
    f'Kendall: \n{corr_kendall}'
)

# %%


#* Correlações específicas
# mede a coluna específica desejada, ao inves de mostrar todas as correlaçÕes de colunas
print(dataframe['idade'].corr(dataframe['altura'], method='pearson'))  # Correlação entre idade e salário


# %%
