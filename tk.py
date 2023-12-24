# for loop

import numpy as np

numbers = np.linspace(3, 17.1, 25)

for n in range(18):
    if n % 2 == 0:
        print(str(n) + " is even")
