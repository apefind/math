
import math


def and_(a, b):
    return int(a and b)


def perceptron(f, n, eps=0.00001):
    pass


if __name__ == '__main__':
    p, q, I = 0, 0, (-10, 10)
    p, q, I = -4, 1, (-10, 10)
    f = lambda x: (x + p) ** 2 + q
    x0 = golden_section_search(f, I)
    print(f'arg min f on {I}: {x0}')
