# subplots

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
plt.plot(np.random.randn(10))

plt.subplot(1, 2, 2)
plt.plot(np.random.randn(10))

plt.show()


fig, ax = plt.subplots(1,2, figsize=(10,4))

x = np.arange(10)

ax[0].plot(x,x**2, 'b')
ax[1].plot(x,np.sqrt(x),'r')

plt.show()