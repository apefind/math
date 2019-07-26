from random import random
from perceptron import dotprod


def delta_rule(T, a, da, t=0.01, eps=0.05, epochs=50):
    n = len(T[0])
    w, b = n * (random(),), random()
    for _ in range(epochs):
        err = 0.0
        for x, y in T:
            z = dotprod(w, x) + b
            az, daz = a(z), da(z)
            d = y - az
            w = tuple(w[i] + t * d * daz * x[i] for i in range(n))
            b = b + t * d * daz
            err = err + d * d
        if 0.5 * err < eps:
            break
    return w, b
