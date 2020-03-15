import random
from vector import dotprod


def delta_rule(T, a, da, s=0.01, epochs=50):
    n = len(T[0][0])
    w, b = tuple(random.random() for _ in range(n)), random.random()
    for _ in range(epochs):
        for x, y in T:
            z = dotprod(w, x) + b
            az, daz = a(z), da(z)
            d = y - az
            t = s * d * daz
            w = tuple(w[i] + t * x[i] for i in range(n))
            b = b + t
    return w, b
