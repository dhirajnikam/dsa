"""
Problem: N-Queens
Difficulty: Hard | Pattern: Backtracking with constraint sets
Source: LeetCode 51

The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no
two queens attack each other (same row, column, or diagonal). Return all distinct solutions
in any order. Each solution is a list of n strings, where 'Q' is a queen and '.' is empty.

Example 1:
  Input: n = 4
  Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Example 2:
  Input: n = 1
  Output: [["Q"]]

Constraints:
  1 <= n <= 9

Hints:
1. Place one queen per row. The choice at row r is which column c to use.
2. A column is attacked if c is used. Diagonals are attacked if (r - c) or (r + c) is used.
   Keep three sets: cols, diag (r - c), anti (r + c).
3. When r == n, convert the column list into board strings and record.

Expected: O(n!) time, O(n) extra space (excluding output).
"""


def solve_n_queens(n: int) -> list[list[str]]:
    raise NotImplementedError


def _no_attacks(board: list[str]) -> bool:
    cols = [row.index("Q") for row in board]
    n = len(board)
    if any(row.count("Q") != 1 or len(row) != n for row in board):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if cols[i] == cols[j] or abs(cols[i] - cols[j]) == j - i:
                return False
    return True


if __name__ == "__main__":
    assert sorted(solve_n_queens(4)) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert solve_n_queens(1) == [["Q"]]
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
    out = solve_n_queens(6)
    assert len(out) == 4 and all(_no_attacks(b) for b in out)
    assert len(set(map(tuple, out))) == 4
    assert len(solve_n_queens(8)) == 92
    print("ok")
