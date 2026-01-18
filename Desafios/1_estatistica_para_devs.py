# %%
#* Setup

import pandas as pd

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

# %%

#* Definições

df_faturamentos = pd.DataFrame.from_dict(dict_faturamento)
df_faturamentos.info()

def normalizar_labels_grafico(grafico):
    # Formatando eixo X para mostrar meses
    grafico.set_xticklabels(
        [data_ref.strftime('%b/%Y') for data_ref in df_faturamentos_ordenado['data_ref']],
        rotation=30,
        ha='right'
        )

    # Formatando eixo Y para mostrar valores inteiros
    grafico.yaxis.set_major_formatter(
        FuncFormatter(lambda x, p: f'R$ {int(x):,}'.replace(',', '.'))
    )


# %%

#* Normalizando dados
df_faturamentos['data_ref'] = pd.to_datetime(df_faturamentos['data_ref'])
df_faturamentos.info()


# %%

#* 1. Média de vendas
media_vendas = df_faturamentos['valor'].mean()
print(f'Média de vendas: ${media_vendas:.2f}')


# %%

#* 2. Gráfico de Barras

from matplotlib.ticker import FuncFormatter

# Ordenando dados por data
df_faturamentos_ordenado = df_faturamentos.sort_values('data_ref')

bar_kwargs = {
    'x': 'data_ref',
    'y': 'valor',
    'title': 'Faturamento Mensal',
    'xlabel': 'Data de Referência',
    'ylabel': 'Faturamento (R$)',
}

graficos_barras = df_faturamentos_ordenado.plot.bar(
    **bar_kwargs
)

normalizar_labels_grafico(graficos_barras)


# %%

#* 3. Gráfico de linhas

df_faturamentos_ordenado = df_faturamentos.sort_values('data_ref')

line_kwargs = {
    'x': 'data_ref',
    'y': 'valor',
    'title': 'Faturamento Mensal',
    'xlabel': 'Data de Referência',
    'ylabel': 'Faturamento (R$)',
}

graficos_linhas = df_faturamentos_ordenado.plot.line(
    **line_kwargs
)

normalizar_labels_grafico(graficos_linhas)


# %%
