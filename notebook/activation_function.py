"""Numerically stable version of sigmoid::

    def sigmoid(x):
        if x >= 0:
            return 1.0 / (1.0 + math.exp(-x))
        y = math.exp(x)
        return y / (1 + y)

"""

import math


def heaviside(x):
    return 0 if x < 0.0 else 1


def step(x, d=0.5):
    return 0 if x < d else 1


def relu(x):
    return max(0.0, x)


def linear(x, r=1.0):
    return r * x


def dx_linear(_, r=1.0):
    return r


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dx_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


tanh = math.tanh


def dx_tanh(x):
    return 1 - tanh(x) ** 2
