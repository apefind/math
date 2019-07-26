from activation_function import heaviside, linear, dx_linear, sigmoid, dx_sigmoid
from boolean import and_, or_, xor, nand, boolean_domain
from delta_rule import dotprod, delta_rule


def test_delta_rule(f, X, a, da, ev, t=0.01, eps=0.05, epochs=50):
    T = [(x, f(*x)) for x in X]
    w, b = delta_rule(T, a, da, t=t, eps=eps, epochs=epochs)
    p = lambda x: dotprod(w, x) + b
    if all(ev(p(x)) == y for x, y in T):
        print(f"{f.__name__}: ok")
    else:
        print(f"{f.__name__}: failed")
    for x, y in T:
        z = ev(p(x))
        if z == y:
            print(f"    {f.__name__}{x} = {y}")
        else:
            print(f"    {f.__name__}{x} = {y} <> {z}")


def test_delta_rule0():
    def ev(x, s=0.3):
        if abs(x) <= s:
            return 0
        elif abs(1 - x) < s:
            return 1
        return x

    t, eps, epochs = 0.01, 0.05, 50
    for f in (or_, and_, nand, xor):
        test_delta_rule(f, boolean_domain, a=linear, da=dx_linear, t=t, eps=eps, epochs=epochs)


def test_delta_rule1():
    t, eps, epochs = 0.01, 0.05, 5000
    for f in (or_, and_, nand, xor):
        test_delta_rule(f, boolean_domain, a=sigmoid, da=dx_sigmoid, ev=heaviside, t=t, eps=eps, epochs=epochs)


if __name__ == "__main__":
    test_delta_rule1()
