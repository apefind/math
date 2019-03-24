from random import randint


def add(v, w):
    return tuple(x + y for x, y in zip(v, w))


def dotproduct(v, w):
    return sum(x * y for x, y in zip(v, w))


def weight(x, y):
    w = add(x, y)
    while True:
        if dotproduct(w, x) < 0:
            w = add(w, x)
        elif dotproduct(w, y) < 0:
            w = add(w, y)
        else:
            return w
        
        
def test_weight(x, y):
    print(f'x = {x}, y = {y}')
    i, w = 0, add(x, y)
    while True:
        a, b = dotproduct(w, x), dotproduct(w, y)
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