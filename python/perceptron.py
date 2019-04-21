def dotprod(v, w):
    return sum(x * y for x, y in zip(v, w))


def perceptron(M, t=0.1, max_iterations=50):
    n = len(M[0])
    w, b = n * (0.0, ), 0.0
    for _ in range(max_iterations):
        done = True
        for x, y in M:
            if dotprod(w, x) + b >= 0:
                z = 1
            else:
                z = 0
            w = tuple(w[i] - t * (z - y) * x[i] for i in range(n))
            b = b - t * (z - y)
            if not y == z:
                done = False
        if done:
            break
    return w, b
