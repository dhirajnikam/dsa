"""
Problem: Asteroid Collision
Difficulty: Medium | Pattern: stack simulation with collision resolution
Source: LeetCode 735

Each asteroid has a size (absolute value) and direction (positive = right, negative = left).
All move at the same speed. When two collide, the smaller explodes; equal sizes both explode.
Two asteroids moving the same direction never meet. Return the state after all collisions.

Example 1:
  asteroids = [5, 10, -5] -> [5, 10]      (10 destroys -5)
Example 2:
  asteroids = [8, -8] -> []
Example 3:
  asteroids = [10, 2, -5] -> [10]         (2 dies, then 10 beats -5)
Example 4:
  asteroids = [-2, -1, 1, 2] -> [-2, -1, 1, 2]   (never meet)

Constraints:
  2 <= len(asteroids) <= 10^4
  -1000 <= asteroids[i] <= 1000, asteroids[i] != 0

Hints:
1. Only a right-mover on the stack top followed by a left-mover can collide.
2. For each left-mover, keep popping right-movers smaller than it. Stop if the top is larger
   (left-mover dies) or equal (both die).
3. If the stack is empty or its top is a left-mover, push the current asteroid.

Expected: O(n) time, O(n) space
"""


def asteroid_collision(asteroids: list[int]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert asteroid_collision([5, 10, -5]) == [5, 10], 'Check: asteroid_collision([5, 10, -5]) == [5, 10]'
    assert asteroid_collision([8, -8]) == [], 'Check: asteroid_collision([8, -8]) == []'
    assert asteroid_collision([10, 2, -5]) == [10], 'Check: asteroid_collision([10, 2, -5]) == [10]'
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2], 'Check: asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]'
    assert asteroid_collision([1, -1, -2, -2]) == [-2, -2], 'Check: asteroid_collision([1, -1, -2, -2]) == [-2, -2]'
    assert asteroid_collision([1, 2, 3]) == [1, 2, 3], 'Check: asteroid_collision([1, 2, 3]) == [1, 2, 3]'
    assert asteroid_collision([-1, -2, -3]) == [-1, -2, -3], 'Check: asteroid_collision([-1, -2, -3]) == [-1, -2, -3]'
    assert asteroid_collision([1, -2, -2, -2]) == [-2, -2, -2], 'Check: asteroid_collision([1, -2, -2, -2]) == [-2, -2, -2]'
    assert asteroid_collision([5, 5, -5]) == [5], 'Check: asteroid_collision([5, 5, -5]) == [5]'
    assert asteroid_collision([1, 2, -3, 4]) == [-3, 4], 'Check: asteroid_collision([1, 2, -3, 4]) == [-3, 4]'
    print("ok")
