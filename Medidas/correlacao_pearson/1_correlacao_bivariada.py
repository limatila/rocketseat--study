# %%

import pandas as pd
import numpy as np

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('pearson-bivariation', parent_path="./Medidas/data")
df_registro_viagem_carro = pd.DataFrame(dados)
df_registro_viagem_carro.info()


def correlacao_pearson(coluna_x, coluna_y, dataframe) -> np.float64:
    """ Cálcula correlação da coluna X com coluna Y, método Pearson """

    #? Cálculo fórmula de Pearson aplicada:
    # n = len(coluna_x)
    # sum_x = sum(coluna_x)
    # sum_y = sum(coluna_y)
    # sum_x_squared = sum(x ** 2 for x in coluna_x)
    # sum_y_squared = sum(y ** 2 for y in coluna_y)
    # sum_xy = sum(x * y for x, y in zip(coluna_x, coluna_y))

    # numerator = n * sum_xy - sum_x * sum_y
    # denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5

    # if denominator == 0:
    #     return 0  # Evita divisão por zero

    # return numerator / denominator

    for coluna in [coluna_x, coluna_y]:
        if coluna not in dataframe.columns:
            raise KeyError(f"Coluna #'{coluna}' não encontrada no DataFrame")

    return dataframe[coluna_x].corr(dataframe[coluna_y], method='pearson')


# %%

from common.utils import DataPresentation

#* Examinando correlações e suas interpretações:

corr_velocidade_distancia = correlacao_pearson('velocidade', 'distancia', df_registro_viagem_carro)
corr_velocidade_tempo = correlacao_pearson('velocidade', 'tempo', df_registro_viagem_carro)
corr_tempo_gasolina = correlacao_pearson('tempo', 'gasolina', df_registro_viagem_carro)
corr_velocidade_horas = correlacao_pearson('velocidade', 'horas_para_chegar', df_registro_viagem_carro)

DataPresentation.print_sequencially(
    f"Correlação entre velocidade e distância percorrida: \n{corr_velocidade_distancia}",
    f"Correlação entre velocidade e tempo: \n{corr_velocidade_tempo}",
    f"Correlação entre tempo e gasolina: \n{corr_tempo_gasolina}",
    f"Correlação entre velocidade e horas_para_chegar: \n{corr_velocidade_horas}"
)

#
# ? Se observa que, nos registros completamente proporcionais que configurei, 
# ? (a cada 10 de velocidade, 100 de distancia aumentam proporcionalmente)
# ? a correlação de Pearson é 1, indicando uma correlação linear perfeita entre velocidade e distância.

# ? A correlação perfeita negativa entre tempo e gasolina (-1) indica que, à medida que o tempo aumenta, 
# ? a gasolina diminui de forma perfeitamente linear.

# ? Correlações não perfeitas tendem a apenas se distanciar de 1 ou -1, indicando que a relação entre as variáveis é 
# ? mais fraca (no meu caso estou apontando isso para a velocidade e horas_para_chegar, com -0.83).
#

corr_velocidade_fome = correlacao_pearson('velocidade', 'fome', df_registro_viagem_carro)

DataPresentation.print_sequencially(
    f"Correlação entre velocidade e fome: \n{corr_velocidade_fome}", early_breakline=True
)

#
# ? Já uma correlação aleatória, como a velocidade e a fome do passageiro é simplesmente muito fraca em comparação,
# ? medindo até -0.52, indicando que não há uma correlação tão forte (e não deveria existir de forma alguma)
#

# %%

#* Visualizando scatter em comparação

import matplotlib.pyplot as plt

plt.scatter(df_registro_viagem_carro['velocidade'], df_registro_viagem_carro['tempo'])
plt.title('Velocidade vs Tempo')
plt.xlabel('Velocidade')
plt.ylabel('Tempo')

#* Linha de correlação (desenhada com regressão linear):
m, b = np.polyfit(df_registro_viagem_carro['velocidade'], df_registro_viagem_carro['tempo'], 1)
plt.plot(df_registro_viagem_carro['velocidade'], m * df_registro_viagem_carro['velocidade'] + b, color='green')

plt.show()

print('Correlação específica: ', corr_velocidade_tempo)

# %%

import matplotlib.pyplot as plt

plt.scatter(df_registro_viagem_carro['velocidade'], df_registro_viagem_carro['horas_para_chegar'])
plt.title('Velocidade vs Horas para Chegar')
plt.xlabel('Velocidade')
plt.ylabel('Horas para Chegar')

#* Linha de correlação (desenhada com regressão linear):
m, b = np.polyfit(df_registro_viagem_carro['velocidade'], df_registro_viagem_carro['horas_para_chegar'], 1)
plt.plot(df_registro_viagem_carro['velocidade'], m * df_registro_viagem_carro['velocidade'] + b, color='red')

plt.show()

print('Correlação específica: ', corr_velocidade_horas)

# %%
