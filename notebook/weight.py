from vector import add, dotprod


def weight(x, y):
    w = add(x, y)
    while True:
        if dotprod(w, x) <= 0:
            w = add(w, x)
        elif dotprod(w, y) <= 0:
            w = add(w, y)
        else:
            return w
