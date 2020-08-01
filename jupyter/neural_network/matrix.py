class matrix(tuple):
    def __new__(self, *rows):
        return tuple.__new__(matrix, rows)

    def __init__(self, *rows):
        self.num_rows = len(self)
        self.num_cols = len(self[0])

    def __rmul__(self, s):
        if isinstance(s, tuple):
            assert self.num_rows == len(s)
            return tuple(sum(x * y for x, y in zip(col, s)) for col in self.t)
        return matrix(*(tuple(s * x for x in row) for row in self))

    def __mul__(self, M):
        if isinstance(M, matrix):
            assert self.num_cols == M.num_rows
            return matrix(*(tuple(sum(x * y for x, y in zip(row, col)) for row in self) for col in M.t))
        elif isinstance(M, tuple):
            assert self.num_cols == len(M)
            return tuple(sum(x * y for x, y in zip(row, M)) for row in self)

    def __neg__(self):
        return matrix(*(tuple(-x for x in row) for row in self))

    def __add__(self, M):
        return matrix(*(tuple(x + y for x, y in zip(row0, row1)) for row0, row1 in zip(self, M)))

    def __sub__(self, M):
        return matrix(*(tuple(x - y for x, y in zip(row0, row1)) for row0, row1 in zip(self, M)))

    #     def __str__(self):
    #         return "\n".join(["	".join(str(_rnd(x)) for x in row) for row in self])

    @property
    def dim(self):
        return self.num_rows, self.num_cols

    @property
    def t(self):
        return matrix(*(tuple(row[j] for row in self) for j in range(self.num_cols)))
