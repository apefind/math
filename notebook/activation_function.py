"""Numerically stable version of sigmoid::

    def sigmoid(x):
        if x >= 0:
            return 1.0 / (1.0 + math.exp(-x))
        else:
            y = math.exp(x)
            return y / (1 + y)

"""

import math


def heaviside(x):
    return 0 if x < 0.0 else 1


def linear(x, a=1.0):
    return a * x


def dx_linear(_, a=1.0):
    return a


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dx_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))
