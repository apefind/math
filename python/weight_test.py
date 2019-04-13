import math
from random import randint
from weight import add, dotproduct


def invert(v):
    return tuple(-x for x in v)


def norm(v):
    return math.sqrt(dotproduct(v, v))


def angle(v, w):
    return math.acos(dotproduct(v, w) / (norm(v) * norm(w)))


def test_weight(x, y):
    print(f'x = {x}, y = {y}')
    print(f'|x| = {norm(x)}, |y| = {norm(y)}, |y|/|x| = {norm(y) / norm(x)}')
    i, w = 0, x + y
    while True:
        a, b = dotproduct(w, x), dotproduct(w, y)
        print(f'    w{i} = {w}, w{i} * x = {a}, w{i} * y = {b}')
        # print(f'wx = {dotproduct(w, x)}, b = {math.degrees(angle(w, x))} deg')
        # print(f'wy = {dotproduct(w, y)}, a = {math.degrees(angle(w, y))} deg')
        if a < 0:
            w = add(w, x)
        elif b < 0:
            w = add(w, y)
        else:
            break
        i = i + 1


def get_test_data():
    #return [((-1, 1), (6, 1))]
    return [((4, -6), (-10, 5))]
    n = 10
    return [((randint(-n, n), randint(-n, n)),
             (randint(-n, n), randint(-n, n))) for _ in range(3)]


if __name__ == '__main__':
    for x, y in get_test_data():
        test_weight(x, y)