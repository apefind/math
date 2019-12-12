import math


def neg(v):
    return tuple(-x for x in v)


def norm(v):
    return math.sqrt(dotprod(v, v))


def normed(v):
    n = norm(v)
    return tuple(x / n for x in v)


def add(v, w):
    return tuple(x + y for x, y in zip(v, w))


def dotprod(v, w):
    return sum(x * y for x, y in zip(v, w))


def angle(v, w):
    return math.acos(dotprod(v, w) / (norm(v) * norm(w)))
