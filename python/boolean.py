def and_(x, y):
    return int(x and y)


def or_(x, y):
    return int(x or y)


def nand(x, y):
    return int(not x and not y)


def xor(x, y):
    return int(x and not y or not x and y)


boolean_domain = (0, 0), (0, 1), (1, 0), (1, 1)
boolean_operators = and_, or_, nand, xor
separable_boolean_operators = and_, or_, nand
non_separable_boolean_operators = xor
