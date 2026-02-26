# %%

import pandas as pd
from scipy.stats import chi2_contingency

from common.utils import DataLoaders
from common.calculators.correlation import CalculadoraCorrelacaoBivariada

dados = DataLoaders.load_json_to_dict('pearson-bivariation', parent_path="./Medidas/data")
df_registro_viagem_carro = pd.DataFrame(dados)
df_registro_viagem_carro.info()

calculadora_correlacao = CalculadoraCorrelacaoBivariada(df_registro_viagem_carro)

# %%

calculadora_correlacao.correlacao_kendall('velocidade', 'distancia')
