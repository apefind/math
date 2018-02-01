
import math


def golden_section_search(f, I, eps=0.00001):
    t = 0.5 * (math.sqrt(5) - 1)
    a, b = I
    while abs(b - a) > eps:
        x, y = b - t * (b - a), a + t * (b - a)
        if f(x) > f(y):
            a = x
        else:
            b = y
    return (a + b) / 2


if __name__ == '__main__':
    p, q, I = 0, 0, (-1, 1)
    p, q, I = 10, 0, (-100, 100)
    p, q, I = -14, 0, (-10000, 10000)
    f = lambda x: (x + p) ** 2 + q
    x0 = golden_section_search(f, I)
    print(f'arg min f on {I}: {x0}')
