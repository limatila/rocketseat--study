# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)

if __name__ == "__main__":
    df_tratado.info()


# %%

#? Base: 2. - Clientes com planos mais caros tendem a ter uma taxa de churn maior.
# Lista de valores mensais dos clientes:

valores_mensais = df_tratado['MonthlyCharges']


# %%
#* Agrupando os clientes por faixa de valor mensal

intervalos = [0, 20, 40, 60, 80, 100, 120]

labels = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120']

faixas_mensais_agrupadas = pd.cut(valores_mensais, bins=intervalos, labels=labels)

if __name__ == "__main__":
    print(faixas_mensais_agrupadas.value_counts())


# %%

#* Visualizando a distribuição dos clientes por faixa de valor mensal, em ordem crescente
faixas_mensais_ordenadas = (
    pd.Categorical(faixas_mensais_agrupadas, categories=reversed(labels), ordered=True)
)

kwargs_barh = {
    'color': 'skyblue',
    'edgecolor': 'black',
    'title': 'Distribuição de Clientes por Faixa de Valor Mensal',
    'xlabel': 'Número de Clientes',
    'ylabel': 'Faixa de Valor Mensal',
}

if __name__ == "__main__":
    faixas_mensais_ordenadas.value_counts().sort_index().plot.barh(**kwargs_barh)


#
# * Resultado: os clientes estão bem distribuidos em torno de valores médios, 
# * sendo que os 2 maiores grupos estão na faixa de 60-80 e 80-100 reais mensais,
# * o que pode indicar que a maioria dos clientes tem planos de preço intermediário - alto.
#

# %%

#* Considerando essa distribuição podemos inferir uma alta assimetria a direita:

print(f"Valor de Assimetria dos valores mensais: {valores_mensais.skew()}")


# %%

valores_mensais.plot.box(
    title="Distribuição dos Valores Mensais",
    xlabel="Valores Mensais",
    ylabel="Clientes"
)

# %%
