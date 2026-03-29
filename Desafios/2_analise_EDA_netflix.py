# %%

from common.utils.DataLoaders import load_csv_to_dataframe

#* Carregando dataset com método padronizado do repositório
df_netflix = load_csv_to_dataframe(
    file_name="netflix_daily_top_10",
    parent_path="./data/datasets/desafios/"
)


# %%

import pandas as pd

#* Primeiramente, tratando os dados do dataframe

#Tratando dado em data, como datetime nativo
df_netflix['As of'] = df_netflix['As of'].astype('datetime64[ns]')
df_netflix.sort_values('As of', inplace=True)

#Tratando dados numéricos, como int
for col_name in ['Year to Date Rank', 'Last Week Rank']:
    df_netflix[col_name] = pd.to_numeric(df_netflix[col_name], errors='coerce')

# Tratando dados booleanos
df_netflix['Netflix Exclusive'] = df_netflix['Netflix Exclusive'].astype('boolean', errors='ignore')


# %%

from common.utils.DataPresentation import print_sequencially

#* 1. Tipos de dados disponíveis
print_sequencially(
    df_netflix.dtypes,
    inicial="1. - Tipos de dados disponíveis:\n\n---\n",
)
# informado na segunda coluna.


# %%

#* 2. Período da análise feita

print_sequencially(
    f"Data inicial: {df_netflix['As of'].min().date()}",
    f"Data final: {df_netflix['As of'].max().date()}",
    inicial="2. - Período da análise feita:\n\n---\n",
)


# %%

#* 3. Tamanho da base de dados

print_sequencially(
    f"Número de linhas: {df_netflix.shape[0]}",
    f"Número de colunas: {df_netflix.shape[1]}",
    inicial="3. - Tamanho da base de dados:\n\n---\n",
)


# %%

#* 4. Verificar dados nulos

print("4. - Verificar dados nulos:\n\n---")

# Quantidade de dados nulos por coluna
print(df_netflix.isnull().sum())

#* vários valores nulos encontrados em Year to Date Rank, Last Week Rank e Netflix Exclusive, 
#* o que pode indicar que nem todos os títulos estavam presentes em todas as semanas,
#* além de que nem todos eram exclusivos da Netflix.

#? Meios para tratar alguns dados nulos:

#tratando nulos booleanos:
df_netflix['Netflix Exclusive'] = df_netflix['Netflix Exclusive'].fillna(False)


# %%

#* 5. Outliers

print_sequencially(
    f"Assimetria: {df_netflix['Viewership Score'].skew()}",
    f"Curtose: {df_netflix['Viewership Score'].kurt()}",
    inicial="5. - Outliers:\n\n---\n",
)

df_netflix.plot.box(y='Viewership Score', title='Boxplot - Viewership Score')
df_netflix['Viewership Score'].describe()

#* Outliers no score de visualização são esperados, visto que poucos títulos 
#* podem ter scores mais favoritos, sendo melhores em qualidade ou favoritismo do público.


# %%

#* Analisando um pouco mais esses Outliers

# Contagem de títulos com Viewership Score acima de 600
títulos_com_score_alto = df_netflix[df_netflix['Viewership Score'] > 600].shape[0]
# 246 outliers grandes.

print(f"Número de títulos com Viewership Score acima de 600: {títulos_com_score_alto}")

#* Devido a alta kurtose (leptocúrtica), a distribuição não é normal,
#* Logo, é esperado que poucos títulos tenham os maiores scores de views de conteúdo.

hist_kwargs = {
    'bins': 15,
    'figsize': (5, 6),
    'title': 'Histograma - Viewership Score'
}

df_netflix['Viewership Score'].plot.hist(**hist_kwargs).invert_xaxis()
#* Pequena concetração no meio do plot, mas considerável concentração de títulos com scores pequenos.
#* Pequena concetração considerável de títulos com scores pequenos.

# %%
