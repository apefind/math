from perceptron import dotprod


def delta_rule(T, a, da, t=0.01, eps=0.001, epochs=250):
    n = len(T[0])
    w, b = n * (0.0,), 0.0
    for _ in range(epochs):
        err = 0.0
        for x, y in T:
            z = dotprod(w, x) + b
            az, daz = a(z), da(z)
            d = y - az
            w = tuple(w[i] + t * d * daz * x[i] for i in range(n))
            b = b + t * az * daz
            err = err + d * d
        if err < eps:
            break
    return w, b
