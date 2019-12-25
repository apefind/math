# %load activation_function.py
"""Numerically stable version of sigmoid::

    def sigmoid(x):
        if x >= 0:
            return 1.0 / (1.0 + math.exp(-x))
        y = math.exp(x)
        return y / (1 + y)

"""

import math


def heaviside(x, offset=0.0):
    return 0 if x < offset else 1


def relu(x, r=1.0):
    return max(0.0, r * x)


def dx_relu(x, r=1.0):
    return 0.0 if x < 0.0 else r


def linear(x, r=1.0):
    return r * x


def dx_linear(_, r=1.0):
    return r


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dx_sigmoid(x):
    return sigmoid(x) * (1.0 - sigmoid(x))


tanh = math.tanh


def dx_tanh(x):
    return 1.0 - tanh(x) ** 2

