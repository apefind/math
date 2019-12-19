import random
from vector import dotprod


def delta_rule(T, a, da, s=0.01, epochs=50):
    n = len(T[0])
    w, b = n * (random.random(),), random.random()
    for _ in range(epochs):
        for x, y in T:
            z = dotprod(w, x) + b
            az, daz = a(z), da(z)
            d = y - az
            w = tuple(w[i] + s * d * daz * x[i] for i in range(n))
            b = b + s * d * daz
    return w, b
