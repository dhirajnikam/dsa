# What a strong candidate says:
# "Is the board always 9x9 with '.' for empty, and does valid mean 'no rule broken so far'
#  rather than 'solvable'? Then it is one pass: every filled digit must be unique in its
#  row, its column and its 3x3 box. I'll tag each occurrence as (row, d), (col, d) and
#  (box, d) and put them in a set; a repeat means invalid. O(81) time, O(81) space."


def is_valid_sudoku(board):
    # O(n^2) time, O(n^2) space for a 9x9 board (constant here)
    # One seen-set with tagged tuples covers all three constraints in a single pass.
    seen = set()
    for r in range(9):
        for c in range(9):
            d = board[r][c]
            if d == ".":
                continue
            tags = (("row", r, d), ("col", c, d), ("box", r // 3, c // 3, d))
            if any(t in seen for t in tags):
                return False
            seen.update(tags)
    return True
