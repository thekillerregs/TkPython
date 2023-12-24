# seaborn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

n = 200
D = np.zeros((n, 2))

D[:, 0] = np.linspace(0, 10, n) + np.random.randn(n)
D[:, 1] = D[:, 0] ** 2 + np.random.randn(n) * 10

sns.jointplot(x=D[:, 0], y=D[:, 1])
plt.show()

df = pd.DataFrame(data=D, columns=['var1', 'var2'])

sns.jointplot(x=df.columns[0], y=df.columns[1], data=df, kind='kde')

plt.show()

x = np.linspace(-1, 1, n)
y1 = x ** 2
y2 = np.sin(3 * x)
y3 = np.exp(-10 * x ** 2)

sns.scatterplot(x=y1, y=y2, hue=y3, palette='Spectral', legend=False)

plt.show()
