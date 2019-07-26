from activation_function import heaviside
from boolean import boolean_domain, boolean_operators
from perceptron import dotprod, perceptron


def test_perceptron(f, X, t=0.01, epochs=50):
    T = [(x, f(*x)) for x in X]
    w, b = perceptron(T, t=t, epochs=epochs)
    p = lambda x: heaviside(dotprod(w, x) + b)
    for x, y in T:
        if p(x) == y:
            print(f"{f.__name__}{x} = {y}")
        else:
            print(f"{f.__name__}{x} = {y} <> {p(x)}")
    if all(p(x) == y for x, y in T):
        print(f"{f.__name__}: ok")
    else:
        print(f"{f.__name__}: failed")


if __name__ == "__main__":
    t, epochs = 0.01, 50
    for f in boolean_operators:
        test_perceptron(f, boolean_domain, t=t, epochs=epochs)
