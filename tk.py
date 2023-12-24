# plots

import matplotlib.pyplot as plt
import numpy as np

plt.plot(3, 4, 'c^')
plt.plot(2, 4.2, 'bo')
plt.legend(['cyan', 'blue'])

x = np.linspace(0, 3 * np.pi, 101)
y = np.sin(x)

plt.plot(x, y, 'm:')
plt.show()
