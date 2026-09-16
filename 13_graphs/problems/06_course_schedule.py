"""
Problem: Course Schedule
Difficulty: Medium | Pattern: directed cycle detection (Kahn / 3-color)
Source: LeetCode 207

There are numCourses courses labeled 0..numCourses-1. prerequisites[i] = [a, b] means you
must take course b before course a. Return True if you can finish all courses.

Example 1:
  numCourses = 2, prerequisites = [[1, 0]] -> True
Example 2:
  numCourses = 2, prerequisites = [[1, 0], [0, 1]] -> False

Constraints:
  1 <= numCourses <= 2000
  0 <= len(prerequisites) <= 5000
  All pairs are distinct.

Hints:
1. "Can finish" = the directed graph has no cycle.
2. Kahn's: repeatedly remove nodes with in-degree 0. If you removed all n, no cycle.
3. Or DFS with 3 colors: a GRAY (on-path) node reached again means a cycle.

Expected: O(V + E) time, O(V + E) space
"""
from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True, 'Check: can_finish(2, [[1, 0]]) is True'
    assert can_finish(2, [[1, 0], [0, 1]]) is False, 'Check: can_finish(2, [[1, 0], [0, 1]]) is False'
    assert can_finish(1, []) is True, 'Check: can_finish(1, []) is True'
    assert can_finish(3, []) is True, 'Check: can_finish(3, []) is True'
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True, 'Check: can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True'
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False, 'Check: can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False'
    assert can_finish(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) is True, 'Check: can_finish(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) is True'
    assert can_finish(4, [[0, 1], [2, 3], [3, 2]]) is False, 'Check: can_finish(4, [[0, 1], [2, 3], [3, 2]]) is False'
    print("ok")
