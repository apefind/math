import unittest
from activation_function import heaviside, linear, dx_linear, sigmoid, dx_sigmoid
from delta_rule import dotprod, delta_rule


def and_(x, y):
    return int(x and y)


def or_(x, y):
    return int(x or y)


def nand(x, y):
    return int(not x and not y)


def xor(x, y):
    return int(x and not y or not x and y)


boolean_domain = (0, 0), (0, 1), (1, 0), (1, 1)
separable_boolean_operators = and_, or_, nand
non_separable_boolean_operators = (xor,)


def one_third(x, s=0.3):
    if abs(x) <= s:
        return 0
    elif abs(1 - x) < s:
        return 1
    return x


class DeltaRuleTestCase(unittest.TestCase):
    def test_separable_boolean_operators(self):
        for f in separable_boolean_operators:
            T = [(x, f(*x)) for x in boolean_domain]
            t, eps, epochs = 0.01, 0.05, 500
            w, b = delta_rule(T, a=linear, da=dx_linear, t=t, eps=eps, epochs=epochs)
            f = lambda x: one_third(dotprod(w, x) + b)
            self.assertTrue(all(f(x) == y for x, y in T))
            t, eps, epochs = 0.01, 0.05, 5000
            w, b = delta_rule(T, a=sigmoid, da=dx_sigmoid, t=t, eps=eps, epochs=epochs)
            f = lambda x: heaviside(dotprod(w, x) + b)
            for x, y in T:
                self.assertEqual(f(x), y)

    def test_non_separable_boolean_operators(self):
        for f in non_separable_boolean_operators:
            t, eps, epochs = 0.01, 0.05, 5000
            T = [(x, f(*x)) for x in boolean_domain]
            w, b = delta_rule(T, a=linear, da=dx_linear, t=t, eps=eps, epochs=epochs)
            f = lambda x: one_third(dotprod(w, x) + b)
            self.assertTrue(any(f(x) != y for x, y in T))
            t, eps, epochs = 0.01, 0.05, 5000
            w, b = delta_rule(T, a=dx_sigmoid, da=dx_sigmoid, t=t, eps=eps, epochs=epochs)
            f = lambda x: heaviside(dotprod(w, x) + b)
            self.assertTrue(any(f(x) != y for x, y in T))


def test_delta_rule(f, X, a, da, evaluate, t=0.01, eps=0.05, epochs=50):
    T = [(x, f(*x)) for x in X]
    w, b = delta_rule(T, a, da, t=t, eps=eps, epochs=epochs)
    p = lambda x: dotprod(w, x) + b
    if all(evaluate(p(x)) == y for x, y in T):
        print(f"{f.__name__}: ok")
    else:
        print(f"{f.__name__}: failed")
    for x, y in T:
        z = evaluate(p(x))
        if z == y:
            print(f"    {f.__name__}{x} = {y}")
        else:
            print(f"    {f.__name__}{x} = {y} <> {z}")


def test_delta_rule1():
    t, eps, epochs = 0.01, 0.05, 5000
    for f in (or_, and_, nand, xor):
        test_delta_rule(f, boolean_domain, a=sigmoid, da=dx_sigmoid, evaluate=heaviside, t=t, eps=eps, epochs=epochs)


if __name__ == "__main__":
    unittest.main()
    # test_delta_rule1()
