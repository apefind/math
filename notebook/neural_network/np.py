import numpy as np


def _sigmoid(x):
    return 1 / (1 + np.exp(-x))


def _dx_sigmoid(x):
    return _sigmoid(x) * (1.0 - _sigmoid(x))


def _relu(x):
    return np.maximum(0.0, x)


# def dx_relu(x, r=1.0):
#     return 0.0 if x < 0.0 else r


def _linear(x, r=1.0):
    return np.multiply(x, r)


# def _dx_linear(x, r=1.0):
#     return

np.sigmoid = _sigmoid
np.dx_sigmoid = _dx_sigmoid
np.relu = _relu
np.linear = _linear


def _vector(*args):
    return np.array(list(args))


def _matrix(*args):
    return np.array(list(args))


def _random_vector(n):
    return np.random.random_sample((n))


def _random_matrix(n, m):
    return np.random.random_sample((n, m))


np.vector = _vector
np.matrix = _matrix
np.random_vector = _random_vector
np.random_matrix = _random_matrix