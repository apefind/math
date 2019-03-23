import math
from random import randint


def add(v, w):
    return tuple(x + y for x, y in zip(v, w))


def crossprod(v, w):
    return sum(x * y for x, y in zip(v, w))


def norm(v):
    return math.sqrt(crossprod(v, v))


def angle(v, w):
    return math.degrees(math.acos(crossprod(v, w) / (norm(v) * norm(w))))
    
    
def weight(x, y):
    w = add(x, y)
    while True:
        if crossprod(w, x) < 0:
            w = add(w, x)
        elif crossprod(w, y) < 0:
            w = add(w, y)
        else:
            return w
        
        
def test_weight(x, y):
    print(f'x = {x}, y = {y}')
    i, w = 0, add(x, y)
    while True:
        a, b = crossprod(w, x), crossprod(w, y)
        print(f'    w{i} = {w}, w{i} * x = {a}, w{i} * y = {b}')
        if a < 0:
            w = add(w, x)
        elif b < 0:
            w = add(w, y)
        else:
            break
        i = i + 1


if __name__ == '__main__':
    n = 10
    for _ in range(3):
        x, y = (randint(-n, n), randint(-n, n)), (randint(-n, n), randint(-n, n))
        test_weight(x, y)