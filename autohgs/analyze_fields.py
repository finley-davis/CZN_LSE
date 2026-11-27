import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#check out one of the fields data files
df_000 = pd.read_csv('/Users/finleydavis/Desktop/CZN Project/HGS/_repo/autohgs/fields/case_018.csv')

lse = df_000['land_surface_elevation'].values

x = np.linspace(0, len(lse), len(lse))

plt.plot(x, lse)
plt.xlim(0, 50)
plt.show()