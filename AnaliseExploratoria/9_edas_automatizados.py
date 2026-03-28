# %%

import pandas as pd

from common.utils.DataLoaders import load_json_to_dict

#! Carregue a partir dos dados unificados do script anterior
dados = load_json_to_dict('churn_tratado.out', parent_path='./data/output/')

df_tratado = pd.DataFrame.from_dict(dados)

# %%

#* Várias bibliotecas já fazem EDA de forma automatizada e configurável, aumento a produtividade 
#* e a qualidade da análise exploratória, com métodos refinados e visualizações avançadas.


#* Algumas bibliotecas populares para EDA automatizado incluem:
#* - **Pandas Profiling**: Gera um relatório detalhado com estatísticas descritivas, gráficos e insights sobre o DataFrame.
#* - **Sweetviz**: Cria relatórios interativos e visuais para análise de dados, comparando conjuntos de dados e destacando diferenças.
#* - **Autoviz**: Gera visualizações automáticas para explorar os dados, identificando padrões e relações entre variáveis.


# %%

#* Exemplo de uso do Sweetviz para análise exploratória automatizada:
import sweetviz as sv

report = sv.analyze(df_tratado, target_feat='Churn')
report.show_html('./AnaliseExploratoria/out/sweetviz_report.html', open_browser=False)

# %%
