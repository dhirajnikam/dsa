"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium | Pattern: reverse DFS from borders, intersect
Source: LeetCode 417

heights is an m x n grid. The Pacific touches the top and left edges, the Atlantic the
bottom and right edges. Water flows from a cell to a 4-neighbor whose height is less than
or equal to its own. Return all cells [r, c] from which water can reach BOTH oceans, in
any order.

Example 1:
  heights = [[1,2,2,3,5],
             [3,2,3,4,4],
             [2,4,5,3,1],
             [6,7,1,4,5],
             [5,1,1,2,4]]
  -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:
  heights = [[1]] -> [[0,0]]

Constraints:
  1 <= m, n <= 200

Hints:
1. Simulating flow from every cell is O((mn)^2). Reverse it: start at the ocean and climb.
2. From every Pacific border cell, DFS to neighbors with height >= current. Collect the
   reachable set. Do the same for the Atlantic. Answer = intersection.

Expected: O(m * n) time, O(m * n) space
"""


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    norm = lambda cells: sorted(map(tuple, cells))
    h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert norm(pacific_atlantic(h)) == [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
    assert norm(pacific_atlantic([[1]])) == [(0, 0)]
    assert norm(pacific_atlantic([[1, 1], [1, 1]])) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert norm(pacific_atlantic([[1, 2, 3]])) == [(0, 0), (0, 1), (0, 2)]
    assert norm(pacific_atlantic([[3], [2], [1]])) == [(0, 0), (1, 0), (2, 0)]
    assert norm(pacific_atlantic([[1, 2], [4, 3]])) == [(0, 1), (1, 0), (1, 1)]
    assert norm(pacific_atlantic([[5, 1], [1, 5]])) == [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("ok")
