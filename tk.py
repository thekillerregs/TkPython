# grafs

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])

plt.xlabel('fuck around')
plt.ylabel('find out')

plt.plot(x, x)

plt.show()

x = np.linspace(-3, 3, 101)

plt.plot(x, x, label='y=x')
plt.plot(x, x ** 2, label='y=x**2')
plt.plot(x, x ** 3, label='y=x**3')

plt.legend()
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.title('Mitada...')

plt.xlim(x[0], x[-1])
plt.ylim(-10, 10)

plt.gca().set_aspect(.3)

plt.show()

fig, ax = plt.subplots(1)

ax.plot(x, x, label='y=x')
ax.plot(x, x ** 2, label='y=x**2')
ax.plot(x, x ** 3, label='y=x**3')

ax.set_xlabel('x')
ax.set_ylabel('y=f(x)')
ax.set_title('Mitada²')


plt.show()