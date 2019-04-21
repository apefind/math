def add(v, w):
    return tuple(x + y for x, y in zip(v, w))


def dotprod(v, w):
    return sum(x * y for x, y in zip(v, w))


def weight(x, y):
    w = add(x, y)
    while True:
        if dotprod(w, x) < 0:
            w = add(w, x)
        elif dotprod(w, y) < 0:
            w = add(w, y)
        else:
            return w
