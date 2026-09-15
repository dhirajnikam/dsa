"""
Problem: Max Area of Island
Difficulty: Medium | Pattern: grid DFS returning size
Source: LeetCode 695

Given an m x n binary grid, return the area (number of cells) of the largest island of
1s connected 4-directionally. Return 0 if there is no island.

Example 1:
  grid = [[0,0,1,0],
          [1,1,0,0],
          [0,1,0,1]] -> 3
Example 2:
  grid = [[0,0,0]] -> 0

Constraints:
  1 <= m, n <= 50

Hints:
1. Same scan as Number of Islands, but the DFS returns how many cells it consumed.
2. dfs(r, c) = 0 if out of bounds or water, else 1 + sum of dfs on 4 neighbors (after marking).

Expected: O(m * n) time, O(m * n) space
"""


def max_area_of_island(grid: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_area_of_island([[0, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1]]) == 3
    assert max_area_of_island([[0, 0, 0]]) == 0
    assert max_area_of_island([[1]]) == 1
    assert max_area_of_island([[1, 1], [1, 1]]) == 4
    assert max_area_of_island([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 1
    assert max_area_of_island([[0, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1]]) == 3
    assert max_area_of_island([[1] * 10 for _ in range(10)]) == 100
    print("ok")
