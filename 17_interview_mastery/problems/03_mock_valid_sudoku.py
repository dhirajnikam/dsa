"""
Problem: Mock interview 3 - Valid Sudoku
Difficulty: Medium | Pattern: Hashing (sets keyed by row / column / box)
Source: LeetCode 36

Interviewer says:
  "Here is a Sudoku board that is partly filled in. Tell me whether it's valid."

Ask about: the exact input format (9x9 list of lists? strings?), how empty cells are
represented, whether "valid" means "no rule broken so far" or "solvable", what characters
can appear, whether the board is always 9x9.

Hints (constraints you should have asked about):
1. board is a 9x9 list of lists of one-character strings: digits "1"-"9" or "." for empty.
   Valid means: no digit repeats in any row, any column, or any of the nine 3x3 boxes.
   It does NOT need to be solvable. Only filled cells matter.
2. One pass over 81 cells. For each digit d at (r, c), record (r, d), (c, d), and
   (r // 3, c // 3, d) in a seen set; a repeat means invalid. Three separate sets, or one
   set with tagged tuples, both fine.
3. The box index is (r // 3) * 3 + c // 3 if you want a single int.
4. Follow-up: how would you validate an n^2 x n^2 board? Same code with n in place of 3.

Expected: O(81) = O(1) time for the fixed board (O(n^2) general), O(1) space (O(n^2) general)
"""


def is_valid_sudoku(board: list[list[str]]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    def grid(rows):
        return [list(r) for r in rows]

    valid = grid([
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ])
    assert is_valid_sudoku(valid) is True, 'Check: is_valid_sudoku(valid) is True'

    col0_dup = grid(["83..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"])
    assert is_valid_sudoku(col0_dup) is False, 'Check: is_valid_sudoku(col0_dup) is False'          # 8 appears twice in column 0

    empty = grid(["........."] * 9)
    assert is_valid_sudoku(empty) is True, 'Check: is_valid_sudoku(empty) is True'

    col_dup = grid(["1........", "1........", ".........", ".........", ".........", ".........", ".........", ".........", "........."])
    assert is_valid_sudoku(col_dup) is False, 'Check: is_valid_sudoku(col_dup) is False'

    box_dup = grid(["1........", ".1.......", ".........", ".........", ".........", ".........", ".........", ".........", "........."])
    assert is_valid_sudoku(box_dup) is False, 'Check: is_valid_sudoku(box_dup) is False'           # same 3x3 box, different row and column

    box_ok = grid(["1........", "...1.....", ".........", ".........", ".........", ".........", ".........", ".........", "........."])
    assert is_valid_sudoku(box_ok) is True, 'Check: is_valid_sudoku(box_ok) is True'             # different row, column and box

    row_dup = grid(["1.......1", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."])
    assert is_valid_sudoku(row_dup) is False, 'Check: is_valid_sudoku(row_dup) is False'

    corner = grid(["........."] * 8 + ["........9"])
    assert is_valid_sudoku(corner) is True, 'Check: is_valid_sudoku(corner) is True'
    print("ok")
