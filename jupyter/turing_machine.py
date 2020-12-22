from array import array


def int2bin(x):
    return [int(i) for i in bin(x)[2:]]


def bin2int(X):
    return sum(2 ** i if x == 1 else 0 for i, x in enumerate(reversed(X)))


def int2xnbin(X):
    y = []
    for x in X:
        for n in int2bin(x):
            if n == 0:
                y.append(0)
            elif n == 1:
                y.append(1)
                y.append(0)
        y.append(1)
        y.append(1)
        y.append(0)
    return y


def xnbin2int(y):
    i, x, X = 0, [], []
    while i < len(y):
        if y[i] == 0:
            x.append(0)
            i += 1
        elif y[i] == 1:
            i += 1
            if y[i] == 0:
                x.append(1)
                i += 1
            else:
                X.append(bin2int(x))
                i += 2
                x = []
    return X


class Tape:
    LEFT = "L"
    RIGHT = "R"
    STOP = "STOP"

    def __init__(self, values):
        self.values = array("I", values)
        self.pos = 0

    def __repr__(self):
        return "".join([f"{v}" for v in self.values[:self.pos]] +
                       [_blu(self.values[self.pos])] +
                       [f"{v}" for v in self.values[self.pos + 1:]])

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def read(self):
        return self.values[self.pos]

    def write(self, v):
        self.values[self.pos] = v

    def move(self, mv):
        if mv == Tape.LEFT:
            if self.pos == 0:
                self.values.insert(0, 0)
            else:
                self.pos -= 1
        else:
            if self.pos == len(self.values) - 1:
                self.values.append(0)
            self.pos += 1


class TuringMachine:

    def __init__(self, instructions):
        self.instructions = instructions

    def __getitem__(self, i):
        return self.instructions[i]

    def __call__(self, tape, max_iterations=None):
        i, instr, mv = 0, 0, None
        while not mv == Tape.STOP:
            if max_iterations is not None and i > max_iterations:
                raise GeneratorExit(f"max iterations {max_iterations} reached")
            value = tape.read()
            try:
                next_instr, new_value, mv = self.instructions[instr][value]
            except KeyError:
                raise GeneratorExit(f"instruction {instr}. for r={value} not found")
            yield instr, next_instr, value, new_value, mv
            tape.write(new_value)
            tape.move(mv)
            instr = next_instr
            i += 1


def generate_instructions(k):
    def iter_instructions(k):
        i, K = 0, [1, 1, 0] + int2bin(k) + [1, 1, 0]
        values, mv = [], None
        while i < len(K):
            if K[i] == 0:
                values.append(0)
                i += 1
            elif K[i:i + 2] == [1, 0]:
                values.append(1)
                i += 2
            elif K[i:i + 3] == [1, 1, 0]:
                mv = Tape.RIGHT
                i += 3
            elif K[i:i + 4] == [1, 1, 1, 0]:
                mv = Tape.LEFT
                i += 4
            elif K[i:i + 5] == [1, 1, 1, 1, 0]:
                mv = Tape.STOP
                i += 5
            else:
                raise GeneratorExit(f"invalid instruction {K[i:i + 5]}")  # e.g. T_7
            if mv is not None:
                if not values:
                    values = [0, 0]
                elif values == [1]:
                    values = [0, 1]
                yield bin2int(values[:-1]), values[-1], mv
                values, mv = [], None

    I = {}
    for i, instr in enumerate(iter_instructions(k)):
        if i % 2 == 0:
            I[i // 2] = {0: instr}
        else:
            I[i // 2][1] = instr
    return I


class UniversalTuringMachine(TuringMachine):

    def __init__(self, k):
        super().__init__(generate_instructions(k))
        self.k = k

    def __str__(self):
        return f"T_{self.k}"
