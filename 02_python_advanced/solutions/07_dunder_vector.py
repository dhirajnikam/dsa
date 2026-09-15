import math


class Vector:
    def __init__(self, *components):
        self._c = tuple(components)

    def __len__(self):
        return len(self._c)

    def __getitem__(self, i):
        return self._c[i]

    def __iter__(self):
        return iter(self._c)

    def _check(self, other):
        if len(self) != len(other):
            raise ValueError("dimension mismatch")

    def __add__(self, other):
        self._check(other)
        return Vector(*(a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        self._check(other)
        return Vector(*(a - b for a, b in zip(self, other)))

    def __mul__(self, k):
        return Vector(*(a * k for a in self))

    __rmul__ = __mul__

    def __matmul__(self, other):
        self._check(other)
        return sum(a * b for a, b in zip(self, other))

    def __neg__(self):
        return Vector(*(-a for a in self))

    def __abs__(self):
        return math.sqrt(sum(a * a for a in self))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self._c == other._c

    def __hash__(self):
        return hash(self._c)

    def __lt__(self, other):
        return (abs(self), self._c) < (abs(other), other._c)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self._c))})"
