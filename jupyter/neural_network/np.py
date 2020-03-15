"""Alternative implementations for dx_relu::

    np.where(x > 0.0, 1.0, 0.0)
    np.heaviside(x, 0.0)
    np.vector(*(0.0 if t < 0.0 else 1.0 for t in x))

"""

import numpy as np


def _sigmoid(x):
    return 1 / (1 + np.exp(-x))


def _dx_sigmoid(x):
    return _sigmoid(x) * (1.0 - _sigmoid(x))


def _relu(x):
    return np.maximum(0.0, x)


def _dx_relu(x):
    return (x > 0.0).astype(x.dtype)


def _linear(x, r=1.0):
    return np.multiply(x, r)


def _dx_linear(x, r=1.0):
    return r * np.ones(len(x))


def _dx_tanh(x):
    return 1.0 - np.tanh(x)**2


np.sigmoid = _sigmoid
np.dx_sigmoid = _dx_sigmoid
np.relu = _relu
np.dx_relu = _dx_relu
np.linear = _linear
np.dx_linear = _dx_linear
np.dx_tanh = _dx_tanh


def _vector(*args):
    return np.array(list(args))


def _matrix(*args):
    return np.array(list(args))


def _random_vector(n):
    return np.random.random_sample((n,))


def _random_matrix(n, m):
    return np.random.random_sample((n, m))


np.vector = _vector
np.matrix = _matrix
np.random_vector = _random_vector
np.random_matrix = _random_matrix
