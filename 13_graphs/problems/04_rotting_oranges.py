"""
Problem: Rotting Oranges
Difficulty: Medium | Pattern: multi-source BFS
Source: LeetCode 994

In an m x n grid, 0 = empty, 1 = fresh orange, 2 = rotten orange. Every minute, any
fresh orange 4-directionally adjacent to a rotten one becomes rotten. Return the minimum
minutes until no fresh orange remains, or -1 if impossible.

Example 1:
  grid = [[2,1,1],[1,1,0],[0,1,1]] -> 4
Example 2:
  grid = [[2,1,1],[0,1,1],[1,0,1]] -> -1
Example 3:
  grid = [[0,2]] -> 0

Constraints:
  1 <= m, n <= 10

Hints:
1. Put ALL rotten oranges in the queue at time 0. Count fresh ones.
2. BFS layer by layer; each layer is one minute. Rot fresh neighbors, decrement fresh count.
3. Answer = number of layers that rotted something; -1 if fresh > 0 at the end.

Expected: O(m * n) time, O(m * n) space
"""
from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0
    assert oranges_rotting([[2, 1, 1, 1, 2]]) == 2
    assert oranges_rotting([[2, 0, 1], [0, 0, 0], [1, 0, 2]]) == -1
    assert oranges_rotting([[1, 2], [2, 1]]) == 1
    print("ok")
