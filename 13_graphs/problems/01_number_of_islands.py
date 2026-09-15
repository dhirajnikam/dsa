"""
Problem: Number of Islands
Difficulty: Medium | Pattern: grid DFS / flood fill
Source: LeetCode 200

Given an m x n grid of "1" (land) and "0" (water), return the number of islands. An
island is a group of "1"s connected horizontally or vertically (not diagonally). The
grid is surrounded by water.

Example 1:
  grid = [["1","1","0"],
          ["1","0","0"],
          ["0","0","1"]] -> 2
Example 2:
  grid = [["0"]] -> 0

Constraints:
  1 <= m, n <= 300
  You may mutate the grid.

Hints:
1. Every unvisited "1" you meet while scanning is a new island. Increment, then flood fill it.
2. Flood fill = DFS/BFS that turns every connected "1" into "0" so it is never counted again.
3. Watch the recursion limit on 300x300; an explicit stack avoids it.

Expected: O(m * n) time, O(m * n) space worst case (stack)
"""


def num_islands(grid: list[list[str]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    g = lambda rows: [list(r) for r in rows]
    assert num_islands(g(["110", "100", "001"])) == 2
    assert num_islands(g(["0"])) == 0
    assert num_islands(g(["1"])) == 1
    assert num_islands(g(["11110", "11010", "11000", "00000"])) == 1
    assert num_islands(g(["11000", "11000", "00100", "00011"])) == 3
    assert num_islands(g(["101", "010", "101"])) == 5
    assert num_islands(g(["000", "000"])) == 0
    assert num_islands([["1"] * 50 for _ in range(50)]) == 1
    print("ok")
