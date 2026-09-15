"""
Problem: Vector with dunder methods
Difficulty: Medium | Topic: __len__, __getitem__, __iter__, __eq__, __hash__, __lt__, operators

Implement class Vector(*components) of numbers:

  Vector(1, 2, 3)
  len(v) == 3; v[0] == 1; v[-1] == 3; list(v) == [1, 2, 3]  (iteration via __iter__)
  v + w, v - w        -> component-wise, ValueError if lengths differ
  v * 3, 3 * v        -> scalar multiply (__mul__ and __rmul__)
  v @ w               -> dot product (__matmul__)
  -v                  -> negation (__neg__)
  abs(v)              -> Euclidean length
  v == w              -> same components; hashable so it can go in a set (__hash__)
  v < w               -> compare by abs(), ties by components tuple (__lt__)
  repr(v)             -> "Vector(1, 2, 3)"
  bool(Vector())      -> False (empty), any non-empty vector is truthy (via __len__)

Store components in a tuple so the vector is immutable and hashing is trivial.

Hints:
1. self._c = tuple(components). Hash with hash(self._c).
2. __rmul__ = __mul__ handles 3 * v.
3. __lt__: return (abs(self), self._c) < (abs(other), other._c)
4. Do not forget to return NotImplemented from __eq__ for non-Vector operands.
"""
import math


class Vector:
    def __init__(self, *components: float):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, i: int) -> float:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __sub__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __mul__(self, k: float) -> "Vector":
        raise NotImplementedError

    def __rmul__(self, k: float) -> "Vector":
        raise NotImplementedError

    def __matmul__(self, other: "Vector") -> float:
        raise NotImplementedError

    def __neg__(self) -> "Vector":
        raise NotImplementedError

    def __abs__(self) -> float:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    def __lt__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    v, w = Vector(1, 2, 3), Vector(4, 5, 6)
    assert len(v) == 3 and v[0] == 1 and v[-1] == 3 and list(v) == [1, 2, 3]
    assert v + w == Vector(5, 7, 9) and w - v == Vector(3, 3, 3)
    assert v * 2 == Vector(2, 4, 6) and 2 * v == Vector(2, 4, 6)
    assert v @ w == 32
    assert -v == Vector(-1, -2, -3)
    assert abs(Vector(3, 4)) == 5.0
    assert v != w and v == Vector(1, 2, 3) and v != (1, 2, 3)
    assert len({v, Vector(1, 2, 3), w}) == 2
    assert Vector(1, 1) < Vector(3, 4) and not Vector(3, 4) < Vector(1, 1)
    assert abs(Vector(0, 5)) == abs(Vector(3, 4)) and Vector(0, 5) < Vector(3, 4)  # tie broken by components
    assert sorted([Vector(3, 4), Vector(0, 1), Vector(0, 5)]) == [Vector(0, 1), Vector(0, 5), Vector(3, 4)]
    assert repr(v) == "Vector(1, 2, 3)" and repr(Vector()) == "Vector()"
    assert not Vector() and Vector(0)
    try:
        v + Vector(1, 2)
        assert False
    except ValueError:
        pass
    try:
        v[3]
        assert False
    except IndexError:
        pass
    print("ok")
