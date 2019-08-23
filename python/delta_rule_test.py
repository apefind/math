import unittest
from activation_function import heaviside, linear, dx_linear, sigmoid, dx_sigmoid
from vector import dotprod
from delta_rule import delta_rule


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


def get_boolean_approx(T, a, da, fire, t=0.01, eps=0.05, epochs=50):
    w, b = delta_rule(T, a=a, da=da, t=t, eps=eps, epochs=epochs)
    return lambda x: fire(dotprod(w, x) + b)


class DeltaRuleTestCase(unittest.TestCase):
    def test_separable_boolean_operators(self):
        for f in separable_boolean_operators:
            T = [(x, f(*x)) for x in boolean_domain]
            t, eps, epochs = 0.01, 0.05, 1000
            f = get_boolean_approx(T, a=linear, da=dx_linear, fire=one_third, t=t, eps=eps, epochs=epochs)
            for x, y in T:
                self.assertEqual(f(x), y)
            t, eps, epochs = 0.01, 0.05, 5000
            f = get_boolean_approx(T, a=sigmoid, da=dx_sigmoid, fire=heaviside, t=t, eps=eps, epochs=epochs)
            for x, y in T:
                self.assertEqual(f(x), y)

    def test_non_separable_boolean_operators(self):
        for f in non_separable_boolean_operators:
            t, eps, epochs = 0.01, 0.05, 5000
            T = [(x, f(*x)) for x in boolean_domain]
            f = get_boolean_approx(T, a=linear, da=dx_linear, fire=one_third, t=t, eps=eps, epochs=epochs)
            self.assertTrue(any(f(x) != y for x, y in T))
            t, eps, epochs = 0.01, 0.05, 5000
            f = get_boolean_approx(T, a=sigmoid, da=dx_sigmoid, fire=heaviside, t=t, eps=eps, epochs=epochs)
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
