# copies and references
import copy

a = [4, 3]

b = a[:]

b[0] = 5

c = copy.deepcopy(b)

c[0] = 27

print(a)
print(b)
print(c)
