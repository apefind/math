
def heaviside(x):
    return 0 if x < 0.0 else 1


def crossprod(v, w):
    return sum(x * y for x, y in zip(v, w))


def perceptron(f, M, t=0.1, max_iterations=50):
    n = len(M[0])
    w, b = n * [0.0], 0.0
    for _ in range(max_iterations):
        done = True
        for x, y in M:
            z = heaviside(crossprod(w, x) + b)
            w = [w[i] - t*(z - y)*x[i] for i in range(n)]
            b = b - t*(z -y)
            if not y == z:
                done = False
        if done:
            break
    return lambda x: heaviside(crossprod(w, x) + b)
    

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
    p = perceptron(f, M)
    for x, y in M:
        print(f'{x} -> {p(x)}: {y}')
    print(f'{f.__name__}: {all(p(x) == y for x, y in M)}')


if __name__ == '__main__':
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    test_perceptron(or_, X)
    test_perceptron(and_, X)
    test_perceptron(nand, X)
    test_perceptron(xor, X)
