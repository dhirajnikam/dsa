"""
Problem: Minimum Path Sum
Difficulty: Medium | Pattern: grid DP, minimize
Source: LeetCode 64

Given an m x n grid of non-negative integers, find a path from top-left to bottom-right
moving only right or down that minimizes the sum of the numbers on the path. Return that sum.

Example 1:
  grid = [[1,3,1],
          [1,5,1],
          [4,2,1]] -> 7   (1 -> 3 -> 1 -> 1 -> 1)
Example 2:
  grid = [[1,2,3],[4,5,6]] -> 12

Constraints:
  1 <= m, n <= 200
  0 <= grid[i][j] <= 200

Hints:
1. State: dp[r][c] = min sum to reach (r, c).
2. Recurrence: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]); edges have one option.
3. One row of space, or overwrite the grid in place if allowed.

Expected: O(m * n) time, O(n) space
"""


def min_path_sum(grid: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
    assert min_path_sum([[5]]) == 5
    assert min_path_sum([[1, 2, 3]]) == 6
    assert min_path_sum([[1], [2], [3]]) == 6
    assert min_path_sum([[0, 0], [0, 0]]) == 0
    assert min_path_sum([[9, 1, 1], [1, 9, 1], [1, 1, 1]]) == 13
    assert min_path_sum([[1, 100, 1], [1, 100, 1], [1, 1, 1]]) == 5
    print("ok")
