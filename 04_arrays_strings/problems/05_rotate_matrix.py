"""
Problem: Rotate Image
Difficulty: Medium | Pattern: in-place 2D transform (transpose + reverse)
Source: LeetCode 48

You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees
clockwise, IN PLACE (modify the input; do not allocate another 2D matrix).

Example 1:
  [[1, 2, 3],          [[7, 4, 1],
   [4, 5, 6],    ->     [8, 5, 2],
   [7, 8, 9]]           [9, 6, 3]]
Example 2:
  [[1, 2], [3, 4]] -> [[3, 1], [4, 2]]

Constraints:
  1 <= n <= 20
  -1000 <= matrix[i][j] <= 1000

Hints:
1. Write out where (r, c) goes after rotation: (c, n - 1 - r).
2. Clockwise 90 = transpose (swap m[r][c] with m[c][r] for c > r) then reverse each row.
3. Counter-clockwise would be transpose then reverse each column.

Expected: O(n^2) time, O(1) space
"""


def rotate(matrix: list[list[int]]) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], 'Check: m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]'
    m = [[1, 2], [3, 4]]
    rotate(m)
    assert m == [[3, 1], [4, 2]], 'Check: m == [[3, 1], [4, 2]]'
    m = [[1]]
    rotate(m)
    assert m == [[1]], 'Check: m == [[1]]'
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(m)
    assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], 'Check: m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]'
    m = [[0, 0], [0, 0]]
    rotate(m)
    assert m == [[0, 0], [0, 0]], 'Check: m == [[0, 0], [0, 0]]'
    m = [[1, 2], [3, 4]]
    rotate(m); rotate(m); rotate(m); rotate(m)
    assert m == [[1, 2], [3, 4]], 'Check: m == [[1, 2], [3, 4]]'
    print("ok")
