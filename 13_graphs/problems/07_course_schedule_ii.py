"""
Problem: Course Schedule II
Difficulty: Medium | Pattern: topological sort (Kahn)
Source: LeetCode 210

Same setup as Course Schedule: prerequisites[i] = [a, b] means take b before a. Return
any valid order in which to take all courses, or an empty list if impossible.

Example 1:
  numCourses = 2, prerequisites = [[1, 0]] -> [0, 1]
Example 2:
  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] -> [0, 1, 2, 3] or [0, 2, 1, 3]
Example 3:
  numCourses = 1, prerequisites = [] -> [0]

Constraints:
  1 <= numCourses <= 2000
  All pairs are distinct.

Hints:
1. Kahn's algorithm: the order in which nodes leave the queue IS a topological order.
2. If the order has fewer than numCourses entries, return [].

Expected: O(V + E) time, O(V + E) space
"""
from collections import deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    def valid(order, n, prereqs):
        if sorted(order) != list(range(n)):
            return False
        pos = {c: i for i, c in enumerate(order)}
        return all(pos[b] < pos[a] for a, b in prereqs)

    assert find_order(2, [[1, 0]]) == [0, 1]
    p = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert valid(find_order(4, p), 4, p)
    assert find_order(1, []) == [0]
    assert valid(find_order(3, []), 3, [])
    assert find_order(2, [[1, 0], [0, 1]]) == []
    assert find_order(3, [[0, 1], [1, 2], [2, 0]]) == []
    p = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]
    assert find_order(6, p) == [0, 1, 2, 3, 4, 5]
    p = [[4, 0], [4, 1], [5, 2], [5, 3], [6, 4], [6, 5]]
    assert valid(find_order(7, p), 7, p)
    print("ok")
