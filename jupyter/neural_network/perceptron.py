from vector import dotprod


def perceptron(T, s=0.01, epochs=50):
    n = len(T[0][0])
    w, b = n * (0.0,), 0.0
    for _ in range(epochs):
        done = True
        for x, y in T:
            if dotprod(w, x) + b >= 0:
                z = 1
            else:
                z = 0
            w = tuple(w[i] - s * (z - y) * x[i] for i in range(n))
            b = b - s * (z - y)
            if not y == z:
                done = False
        if done:
            break
    return w, b
