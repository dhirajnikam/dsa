from dataclasses import dataclass
import math


@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float = 0.0

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)


def closest_to_origin(points):
    origin = Point(0, 0)
    return min(points, key=lambda p: (p.distance_to(origin), p))


def unique_sorted(points):
    return sorted(set(points))
