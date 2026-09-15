"""
Problem: K Closest Points to Origin
Difficulty: Medium | Pattern: size-k max-heap
Source: LeetCode 973

Given an array of points [[x, y], ...] on a plane and an integer k, return the k points
closest to the origin (0, 0) using Euclidean distance. Return them in any order. The
answer is guaranteed to be unique except for the order.

Example 1:
  points = [[1, 3], [-2, 2]], k = 1 -> [[-2, 2]]
Example 2:
  points = [[3, 3], [5, -1], [-2, 4]], k = 2 -> [[3, 3], [-2, 4]]

Constraints:
  1 <= k <= len(points) <= 10^4
  -10^4 <= x, y <= 10^4

Hints:
1. Compare squared distances x*x + y*y; no sqrt needed.
2. Keep a max-heap of size k (push negative distance). When it exceeds k, pop the farthest.
3. heapq.nsmallest(k, points, key=...) is the one-liner. Know both.

Expected: O(n log k) time, O(k) space
"""
import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    norm = lambda pts: sorted(map(tuple, pts))
    assert norm(k_closest([[1, 3], [-2, 2]], 1)) == [(-2, 2)]
    assert norm(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == [(-2, 4), (3, 3)]
    assert norm(k_closest([[0, 0]], 1)) == [(0, 0)]
    assert norm(k_closest([[1, 1], [2, 2], [3, 3]], 3)) == [(1, 1), (2, 2), (3, 3)]
    assert norm(k_closest([[5, 5], [1, 0], [0, -1], [10, 10]], 2)) == [(0, -1), (1, 0)]
    assert len(k_closest([[i, i] for i in range(50)], 7)) == 7
    print("ok")
