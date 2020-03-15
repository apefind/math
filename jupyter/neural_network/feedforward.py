import random
import np as _np
import numpy as np


def feedforward(a, N, x):
    for W, B in N:
        x = a(np.dot(W, x) + B)
    return x


def get_random_weights_and_biases(k, l, m=None, layers=0):
    N = [(np.random_matrix(l, k), np.random_vector(l))]
    for _ in range(layers):
        N.append((np.random_matrix(l, l), np.random_vector(l)))
    if m is not None:
        N.append((np.random_matrix(m, l), np.random_vector(m)))
    return N


class FeedForward:

    def __init__(self, dim, layers, a):
        self.dim = dim
        self.N = get_random_weights_and_biases(*dim, layers)
        self.a = a

    def __call__(self, x):
        return self.feedforward(x)

    def __repr__(self):
        return repr(self.N)

    def feedforward(self, x):
        return feedforward(self.a, self.N, x)


class FeedForwardSingleLayer(FeedForward):

    def __init__(self, dim, a, da):
        super().__init__(dim=(*dim, None), layers=0, a=a)
        self.da = da

    def train(self, T, s=0.01, epochs=50):
        for _ in range(epochs):
            for x, y in random.sample(T, len(T)):
                z = feedforward(np.linear, self.N, x)
                az, daz = self.a(z), self.da(z)
                d = y - az
                for W, B in self.N:
                    for i, w in enumerate(W):
                        w += s * d[i] * daz[i] * x
                    B += s * d * daz
