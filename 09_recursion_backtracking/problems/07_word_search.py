"""
Problem: Word Search
Difficulty: Medium | Pattern: Grid DFS backtracking
Source: LeetCode 79

Given an m x n grid of characters board and a string word, return True if word exists in
the grid. The word can be constructed from letters of sequentially adjacent cells
(horizontally or vertically). The same cell may not be used more than once.

Example 1:
  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
  Output: True

Example 2:
  Input: same board, word = "SEE"
  Output: True

Example 3:
  Input: same board, word = "ABCB"
  Output: False

Constraints:
  1 <= m, n <= 6
  1 <= len(word) <= 15
  board and word consist of only lowercase and uppercase English letters.

Hints:
1. Try starting a DFS from every cell whose letter matches word[0].
2. dfs(r, c, i): return True if word[i:] can be found starting at (r, c). Base: i == len(word).
3. Mark the cell with a sentinel like '#' before exploring neighbors, restore it after.

Expected: O(m * n * 3^L) time, O(L) recursion space.
"""


def exist(board: list[list[str]], word: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(b, "ABCCED") is True
    assert exist(b, "SEE") is True
    assert exist(b, "ABCB") is False
    assert exist([["a"]], "a") is True
    assert exist([["a"]], "b") is False
    assert exist([["a", "a"]], "aaa") is False   # cannot reuse a cell
    assert exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB") is True
    assert b == [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]  # board restored
    print("ok")
