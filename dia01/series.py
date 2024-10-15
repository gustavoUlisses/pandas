# %%
import pandas as pd

# %%
idades = [10, 20, 30]
idades
# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media -i)**2
variancia = total / (len(idades) - 1)
variancia
# %%
series_idades = pd.Series(idades)
series_idades
# %%
series_idades.mean()
# %%
series_idades.var()

# %%
idades[0]

# %%
series_idades.index = ['t','e','o','c']
# %%
series_idades['t']

# %%
series_idades.iloc[0]
# %%
