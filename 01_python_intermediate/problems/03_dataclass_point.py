"""
Problem: Point dataclass
Difficulty: Warm-up | Topic: dataclasses, frozen, order, hashing, methods

1. Complete the Point dataclass: fields x: float, y: float (default 0.0).
   It must be frozen (immutable, hashable) and ordered (compares by (x, y)).
   Add methods:
     .distance_to(other) -> Euclidean distance (float)
     .__add__(other) -> Point(self.x + other.x, self.y + other.y)
     .midpoint(other) -> Point halfway between
2. closest_to_origin(points) -> the Point with the smallest distance to (0, 0).
   Ties: the smaller point by (x, y) ordering.
3. unique_sorted(points) -> list of distinct points in ascending (x, y) order.

Hints:
1. @dataclass(frozen=True, order=True). Frozen means you cannot assign self.x in methods.
2. min(points, key=lambda p: (p.distance_to(Point(0, 0)), p))
3. sorted(set(points)) works only because the class is frozen (hashable) and ordered.
"""
from dataclasses import dataclass
import math


@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float = 0.0

    def distance_to(self, other: "Point") -> float:
        raise NotImplementedError

    def __add__(self, other: "Point") -> "Point":
        raise NotImplementedError

    def midpoint(self, other: "Point") -> "Point":
        raise NotImplementedError


def closest_to_origin(points: list[Point]) -> Point:
    raise NotImplementedError


def unique_sorted(points: list[Point]) -> list[Point]:
    raise NotImplementedError


if __name__ == "__main__":
    p = Point(3, 4)
    assert p.x == 3 and p.y == 4 and Point(1).y == 0.0, 'Check: p.x == 3 and p.y == 4 and Point(1).y == 0.0'
    assert p.distance_to(Point(0, 0)) == 5.0, 'Check: p.distance_to(Point(0, 0)) == 5.0'
    assert p + Point(1, 1) == Point(4, 5), 'Check: p + Point(1, 1) == Point(4, 5)'
    assert Point(0, 0).midpoint(Point(2, 4)) == Point(1, 2), 'Check: Point(0, 0).midpoint(Point(2, 4)) == Point(1, 2)'
    assert repr(Point(1, 2)) == "Point(x=1, y=2)", 'Check: repr(Point(1, 2)) == "Point(x=1, y=2)"'
    assert Point(1, 2) < Point(1, 3) < Point(2, 0), 'Check: Point(1, 2) < Point(1, 3) < Point(2, 0)'
    assert len({Point(1, 1), Point(1, 1), Point(2, 2)}) == 2, 'Check: len({Point(1, 1), Point(1, 1), Point(2, 2)}) == 2'
    try:
        p.x = 10
        assert False, 'Check: False'
    except Exception:
        pass
    assert closest_to_origin([Point(3, 4), Point(1, 1), Point(-1, 1)]) == Point(-1, 1), 'Check: closest_to_origin([Point(3, 4), Point(1, 1), Point(-1, 1)]) == Point(-1, 1)'
    assert closest_to_origin([Point(5, 0)]) == Point(5, 0), 'Check: closest_to_origin([Point(5, 0)]) == Point(5, 0)'
    assert unique_sorted([Point(2, 1), Point(1, 5), Point(2, 1), Point(1, 2)]) == [
        Point(1, 2), Point(1, 5), Point(2, 1)], 'Check: unique_sorted([Point(2, 1), Point(1, 5), Point(2, 1), Point(1, 2)]) == [ Point(1, 2), Point(1, 5), Point(2, 1)]'
    assert unique_sorted([]) == [], 'Check: unique_sorted([]) == []'
    print("ok")
