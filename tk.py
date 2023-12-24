# list comprehension

list = [print(i ** 2) for i in range(10)]

print(list)

nl = ["Odd " if i % 2 == 1 else i for i in range(10)]

print(nl)
