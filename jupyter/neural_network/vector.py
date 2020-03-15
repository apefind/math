import math


def neg(v):
    return tuple(-x for x in v)


def norm(v):
    return math.sqrt(dotprod(v, v))


def normed(v):
    n = norm(v)
    return tuple(x / n for x in v)


def add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def dotprod(u, v):
    return sum(x * y for x, y in zip(u, v))


def angle(u, v):
    return math.acos(dotprod(u, v) / (norm(u) * norm(v)))
