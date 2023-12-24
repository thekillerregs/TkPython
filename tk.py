# variables

import numpy as np

N = 10

r = np.zeros(N)

for i in range(N):
    r[i] = i ** 2

print(r)

del r

print(r)

