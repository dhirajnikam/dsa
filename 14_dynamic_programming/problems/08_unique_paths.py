"""
Problem: Unique Paths
Difficulty: Medium | Pattern: grid DP, count paths
Source: LeetCode 62

A robot starts at the top-left of an m x n grid and can only move right or down. How many
unique paths reach the bottom-right?

Example 1:
  m = 3, n = 7 -> 28
Example 2:
  m = 3, n = 2 -> 3

Constraints:
  1 <= m, n <= 100

Hints:
1. State: dp[r][c] = paths to reach (r, c). First row and column are all 1.
2. Recurrence: dp[r][c] = dp[r-1][c] + dp[r][c-1].
3. One row suffices: row[c] += row[c-1]. Also equals C(m+n-2, m-1).

Expected: O(m * n) time, O(n) space
"""


def unique_paths(m: int, n: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1
    assert unique_paths(10, 1) == 1
    assert unique_paths(2, 2) == 2
    assert unique_paths(10, 10) == 48620
    assert unique_paths(23, 12) == 193536720
    print("ok")
