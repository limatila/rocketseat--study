# %%

from common.utils import DataLoaders

dados = DataLoaders.load_json_to_dict('test-dataframe', parent_path="./Medidas/data")
print(dados)


# %%

from pandas import DataFrame

dataframe = DataFrame.from_dict(dados)
print(dataframe)


# %%

#* Simetria
# representa distribuição dos dados em torno da média.

skew_altura = dataframe.altura.skew()
skew_idade = dataframe.idade.skew()

print(
    f"Idade: {skew_idade} está indicando que é {
        ('assimétrica à direita' if skew_idade > 0 else 'assimétrica à esquerda') if skew_idade != 0 else 'simétrica'                               # type: ignore
    }"
)
print(
    f"Altura: {skew_altura} está indicando que é {
        ('assimétrica à direita' if skew_altura > 0 else 'assimétrica à esquerda') if skew_altura != 0 else 'simétrica'                             # type: ignore
    }"
)

# Valores próximos de 0 indicam simetria perfeita. Valores positivos indicam assimetria à direita, e valores negativos indicam assimetria à esquerda.


# %%

#* Curtose
# representa o quão "pontuda" ou "achatada" é a distribuição dos dados, ou seja, o quão está espalhado os dados em torno da média.
#Curtose Leptocúrtica: valores maiores que 3, indicando uma distribuição mais pontuda.
#Curtose Platicúrtica: valores menores que 3, indicando uma distribuição mais achatada.
#Curtose Mesocúrtica: valor igual a 3, indicando uma distribuição normal, completamente gaussiana.

kurtosis_idade = dataframe.idade.kurt()

print(
    f"Idade: {kurtosis_idade} está indicando que é {
        ('leptocúrtica' if kurtosis_idade > 3 else 'platicúrtica') if kurtosis_idade != 3 else 'mesocúrtica'                                                    # type: ignore
    }"
)


# %%
