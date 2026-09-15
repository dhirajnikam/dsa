"""
Problem: Set Matrix Zeroes
Difficulty: Medium | Pattern: in-place marking using first row/column as flags
Source: LeetCode 73

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.
Do it IN PLACE.

Example 1:
  [[1, 1, 1],          [[1, 0, 1],
   [1, 0, 1],    ->     [0, 0, 0],
   [1, 1, 1]]           [1, 0, 1]]
Example 2:
  [[0, 1, 2, 0],       [[0, 0, 0, 0],
   [3, 4, 5, 2],  ->    [0, 4, 5, 0],
   [1, 3, 1, 5]]        [0, 3, 1, 0]]

Constraints:
  1 <= m, n <= 200
  -2^31 <= matrix[i][j] <= 2^31 - 1

Hints:
1. O(m + n) space: collect zero rows and zero cols in two sets, then wipe. Get this working first.
2. O(1) space: use row 0 and column 0 as the flag arrays. Record separately whether row 0
   and column 0 themselves need zeroing.
3. Process the inner cells (r >= 1, c >= 1) first, then row 0 and column 0 last.

Expected: O(m*n) time, O(1) space (O(m + n) accepted as a first pass)
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    m = [[1]]
    set_zeroes(m)
    assert m == [[1]]
    m = [[0]]
    set_zeroes(m)
    assert m == [[0]]
    m = [[1, 2, 3]]
    set_zeroes(m)
    assert m == [[1, 2, 3]]
    m = [[1, 0, 3]]
    set_zeroes(m)
    assert m == [[0, 0, 0]]
    m = [[1, 2], [3, 4], [5, 0]]
    set_zeroes(m)
    assert m == [[1, 0], [3, 0], [0, 0]]
    m = [[0, 1], [1, 1]]
    set_zeroes(m)
    assert m == [[0, 0], [0, 1]]
    print("ok")
