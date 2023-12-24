# enumerate and zip

import numpy as np

ns = np.linspace(-5, 5, 7)

for i, n in enumerate(ns):
    print("Index: " + str(i) + " has a value of " + str(n))

listA = [3, 4, 5, 6, 3, -17]
listB = ['q', 'w', 'e', 'r', 't', 'y']

for a, b in zip(listA, listB):
    print(str(a) + ' ' + b)
