# exceptions

def funfun(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise Exception('Only numbers!')

    z = x * y
    return z


print(funfun(2, 2.5))
