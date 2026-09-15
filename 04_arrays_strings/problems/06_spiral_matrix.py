"""
Problem: Spiral Matrix
Difficulty: Medium | Pattern: 2D traversal with shrinking boundaries
Source: LeetCode 54

Given an m x n matrix, return all elements in spiral order (right, down, left, up, repeat).

Example 1:
  [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]           -> [1, 2, 3, 6, 9, 8, 7, 4, 5]
Example 2:
  [[1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12]]     -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Constraints:
  1 <= m, n <= 10
  -100 <= matrix[i][j] <= 100

Hints:
1. Keep four bounds: top, bottom, left, right. Walk one edge, then move that bound inward.
2. After walking the top row and right column, check top <= bottom before walking the bottom
   row and left <= right before walking the left column (avoids double-counting on single rows/cols).
3. Stop when top > bottom or left > right.

Expected: O(m*n) time, O(1) extra space (output not counted)
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1]]) == [1]
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert spiral_order([]) == []
    print("ok")
