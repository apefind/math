def AND(x, y):
    return int(x and y)


def OR(x, y):
    return int(x or y)


def NAND(x, y):
    return int(not x and not y)


def XOR(x, y):
    return int(x and not y or not x and y)


BOOLEAN_OPERATORS = AND, OR, NAND, XOR
BOOLEAN_OPERATOR_DOMAIN = (0, 0), (0, 1), (1, 0), (1, 1)
BOOLEAN_TESTDATA = {f: [(x, f(*x)) for x in BOOLEAN_OPERATOR_DOMAIN] for f in BOOLEAN_OPERATORS}
SEPARABLE_BOOLEAN_OPERATORS = AND, OR, NAND
NON_SEPARABLE_BOOLEAN_OPERATORS = XOR
