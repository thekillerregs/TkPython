# numpy broadcasting

import numpy as np

X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

w = np.array([10, 20, 30])

print(X), print(' '), print(w)

Z = X + w

print(Z), print(' '), print(Z)

v = np.array([-1, 0, 1, 0], ndmin=2).T

print(X), print(" "), print(X * v)

tk = np.arange(9)

M = np.reshape(tk, (3, 3))

C = np.tile(M, (3, 1))

B = C * np.reshape(tk, (-1, 1))

print(tk), print(M), print(C), print(B)
