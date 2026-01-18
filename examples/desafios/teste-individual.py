# %%
#* Setup

import pandas as pd

from common.config.core import PROJECT_ROOT


# %% 
#* Definições

df_faturamentos = pd.read_csv(PROJECT_ROOT / 'data/datasets/churns/churn_customers.csv')
df_faturamentos.info()


# %%

#* Questão 1., Q. 2., Q. 3...
