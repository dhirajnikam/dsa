"""
Problem: Search a 2D Matrix
Difficulty: Medium | Pattern: Binary search on a flattened index
Source: LeetCode 74

You are given an m x n integer matrix with the following properties:
  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return True if target is in the matrix. Must run in O(log(m * n)).

Example 1:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
  Output: True

Example 2:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
  Output: False

Constraints:
  1 <= m, n <= 100
  -10^4 <= matrix[i][j], target <= 10^4

Hints:
1. The whole matrix read row by row is one sorted array of length m * n.
2. Virtual index i maps to matrix[i // n][i % n]. Never actually flatten it (that is O(mn)).
3. Run the standard closed-interval search on indices 0 .. m*n - 1.

Expected: O(log(m * n)) time, O(1) space.
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(m, 3) is True, 'Check: search_matrix(m, 3) is True'
    assert search_matrix(m, 13) is False, 'Check: search_matrix(m, 13) is False'
    assert search_matrix(m, 1) is True and search_matrix(m, 60) is True, 'Check: search_matrix(m, 1) is True and search_matrix(m, 60) is True'
    assert search_matrix(m, 0) is False and search_matrix(m, 61) is False, 'Check: search_matrix(m, 0) is False and search_matrix(m, 61) is False'
    assert search_matrix([[1]], 1) is True, 'Check: search_matrix([[1]], 1) is True'
    assert search_matrix([[1]], 2) is False, 'Check: search_matrix([[1]], 2) is False'
    assert search_matrix([[1], [3], [5]], 3) is True, 'Check: search_matrix([[1], [3], [5]], 3) is True'      # single column
    assert search_matrix([[1, 3, 5]], 4) is False, 'Check: search_matrix([[1, 3, 5]], 4) is False'          # single row
    assert search_matrix([[]], 1) is False, 'Check: search_matrix([[]], 1) is False'                 # empty row
    print("ok")
