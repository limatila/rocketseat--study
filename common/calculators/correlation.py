
import numpy as np


class CalculadoraCorrelacaoBivariada:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def correlacoes_gerais(self, method: str = 'Pearson'):
        """ Cálcula correlações gerais entre todas as colunas do DataFrame, método Pearson por padrão """

        method = method.lower()

        if method not in ['pearson', 'spearman', 'kendall']:
            raise ValueError("Método de correlação inválido. Use 'pearson', 'spearman' ou 'kendall'.")

        return self.dataframe.corr(method=method)

    def correlacao_pearson(self, coluna_x, coluna_y) -> np.float64:
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
            if coluna not in self.dataframe.columns:
                raise KeyError(f"Coluna #'{coluna}' não encontrada no DataFrame")

        return self.dataframe[coluna_x].corr(self.dataframe[coluna_y], method='pearson')
    
    def correlacao_spearman(self, coluna_x, coluna_y) -> np.float64:
        """ Cálcula correlação da coluna X com coluna Y, método Spearman """

        #? Cálculo fórmula de Spearman aplicada:
        # n = len(coluna_x)
        # rank_x = {x: rank for rank, x in enumerate(sorted(set(coluna_x)), start=1)}
        # rank_y = {y: rank for rank, y in enumerate(sorted(set(coluna_y)), start=1)}
        # d_squared_sum = sum((rank_x[x] - rank_y[y]) ** 2 for x, y in zip(coluna_x, coluna_y))
        
        # return 1 - (6 * d_squared_sum) / (n * (n ** 2 - 1))

        for coluna in [coluna_x, coluna_y]:
            if coluna not in self.dataframe.columns:
                raise KeyError(f"Coluna #'{coluna}' não encontrada no DataFrame")

        return self.dataframe[coluna_x].corr(self.dataframe[coluna_y], method='spearman')
    
    def correlacao_kendall(self, coluna_x, coluna_y) -> np.float64:
        """ Cálcula correlação da coluna X com coluna Y, método Kendall """

        #? Cálculo fórmula de Kendall aplicada:
        # n = len(coluna_x)
        # concordant_pairs = sum((1 if (x1 - x2) * (y1 - y2) > 0 else 0) for i, (x1, y1) in enumerate(zip(coluna_x, coluna_y)) for j, (x2, y2) in enumerate(zip(coluna_x, coluna_y)) if i < j)
        # discordant_pairs = sum((1 if (x1 - x2) * (y1 - y2) < 0 else 0) for i, (x1, y1) in enumerate(zip(coluna_x, coluna_y)) for j, (x2, y2) in enumerate(zip(coluna_x, coluna_y)) if i < j)
        
        # return (concordant_pairs - discordant_pairs) / (0.5 * n * (n - 1))

        for coluna in [coluna_x, coluna_y]:
            if coluna not in self.dataframe.columns:
                raise KeyError(f"Coluna #'{coluna}' não encontrada no DataFrame")

        return self.dataframe[coluna_x].corr(self.dataframe[coluna_y], method='kendall')
