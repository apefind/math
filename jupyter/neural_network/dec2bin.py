import numpy as np


def int2dec(n):
    return np.array(tuple(0.99 if i == n else 0.01 for i in range(10)))


def dec2int(X):
    for i, x in enumerate(X):
        if x > 0.5:
            return i


def int2bin(n):
    b = []
    while n > 0:
        n, x = divmod(n, 2)
        b.append(x)
    return np.array(b + [0] * (4 - len(b)))


def bin2int(X):
    return sum(2 ** i if x > 0.5 else 0 for i, x in enumerate(X))
