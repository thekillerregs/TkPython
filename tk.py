# resolution

import matplotlib.pyplot as plt
import numpy as np
from IPython import display
#deprecated :skull:
display.set_matplotlib_formats('svg')

x = np.linspace(.5,5,10)
y1 = np.log(x)
y2 = 2-np.sqrt(x)

plt.plot(x,y1,'bo-', label='log')
plt.plot(x,y2,'rs-',label='sqrt')
plt.legend()

plt.show()