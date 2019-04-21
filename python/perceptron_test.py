from perceptron import dotprod, perceptron


def heaviside(x):
    return 0 if x < 0.0 else 1


def and_(x, y):
    return int(x and y)


def or_(x, y):
    return int(x or y)


def xor(x, y):
    return int(x and not y or not x and y)


def nand(x, y):
    return int(not x and not y)


def test_perceptron(f, X):
    M = [(x, f(*x)) for x in X]
    w, b = perceptron(M)
    p = lambda x: heaviside(dotprod(w, x) + b)
    for x, y in M:
        print(f"{f.__name__}{x} -> {p(x)}: {y}")
    print(f"{f.__name__}: {all(p(x) == y for x, y in M)}")


if __name__ == "__main__":
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for f in (or_, and_, nand, xor):
        test_perceptron(f, X)
