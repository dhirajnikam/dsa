"""09 · Recursion & Backtracking — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """All subsets of distinct integers, in any order.
    [1, 2, 3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]] ; [] -> [[]]
    """
    raise NotImplementedError


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """All UNIQUE subsets when nums may contain duplicates. Any order.
    [1, 2, 2] -> [[], [1], [1,2], [1,2,2], [2], [2,2]] ; [0] -> [[], [0]]
    """
    raise NotImplementedError


def permutations(nums: list[int]) -> list[list[int]]:
    """All orderings of distinct integers. Any order.
    [1, 2, 3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] ; [1] -> [[1]]
    """
    raise NotImplementedError


def permutations_unique(nums: list[int]) -> list[list[int]]:
    """All UNIQUE orderings when nums may contain duplicates. Any order.
    [1, 1, 2] -> [[1,1,2],[1,2,1],[2,1,1]] ; [1, 2, 3] -> all 6
    """
    raise NotImplementedError


def combinations(n: int, k: int) -> list[list[int]]:
    """All k-element subsets of 1..n. Any order.
    4, 2 -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] ; 1, 1 -> [[1]]
    """
    raise NotImplementedError


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Distinct positive candidates; each may be used any number of times. Return every
    unique combination summing to target. Any order.
    [2, 3, 6, 7], 7 -> [[2,2,3],[7]] ; [2, 3, 5], 8 -> [[2,2,2,2],[2,3,3],[3,5]] ; [2], 1 -> []
    """
    raise NotImplementedError


def combination_sum_ii(candidates: list[int], target: int) -> list[list[int]]:
    """Candidates may repeat; each POSITION may be used at most once. Return every unique
    combination summing to target (no duplicate combinations). Any order.
    [10,1,2,7,6,1,5], 8 -> [[1,1,6],[1,2,5],[1,7],[2,6]] ; [2,5,2,1,2], 5 -> [[1,2,2],[5]]
    """
    raise NotImplementedError


def letter_combinations(digits: str) -> list[str]:
    """Phone keypad: 2=abc 3=def 4=ghi 5=jkl 6=mno 7=pqrs 8=tuv 9=wxyz. Return every string
    the digits could spell. Any order. Empty input -> [].
    "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"] ; "" -> [] ; "2" -> ["a","b","c"]
    """
    raise NotImplementedError


def generate_parentheses(n: int) -> list[str]:
    """All well-formed strings of n pairs of parentheses. Any order.
    3 -> ["((()))","(()())","(())()","()(())","()()()"] ; 1 -> ["()"]
    """
    raise NotImplementedError


def word_search(board: list[list[str]], word: str) -> bool:
    """Can word be traced through 4-directionally adjacent cells, each cell used at most once?
    The board must be unchanged when you return.
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED" -> True ; same, "ABCB" -> False
    """
    raise NotImplementedError


def palindrome_partition(s: str) -> list[list[str]]:
    """Every way to split s into consecutive pieces that are each palindromes. Any order.
    "aab" -> [["a","a","b"],["aa","b"]] ; "a" -> [["a"]]
    """
    raise NotImplementedError


def n_queens(n: int) -> list[list[str]]:
    """All placements of n queens on an n x n board so none attack another. Each board is a
    list of n strings of "." and "Q". Any order.
    4 -> [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]] ; 1 -> [["Q"]] ; 2 -> []
    """
    raise NotImplementedError


def restore_ip_addresses(s: str) -> list[str]:
    """Every valid IPv4 address formed by inserting three dots into s (digits only). Each part
    is 0..255 with no leading zero (except "0" itself). Any order.
    "25525511135" -> ["255.255.11.135","255.255.111.35"] ; "0000" -> ["0.0.0.0"] ; "1111" -> ["1.1.1.1"]
    """
    raise NotImplementedError


def sudoku_solver(board: list[list[str]]) -> None:
    """Fill the 9x9 board IN PLACE. Cells hold "1".."9" or "." for empty. Exactly one solution
    exists. Every row, column, and 3x3 box must contain each digit exactly once.
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _norm(groups):
    """Sort inside each list and across lists, for order-free comparison of subsets."""
    return sorted(sorted(g) for g in groups)


def _t_01_subsets():
    got = subsets([1, 2, 3])
    assert len(got) == 8
    assert _norm(got) == _norm([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]), got
    assert subsets([]) == [[]]
    assert _norm(subsets([0])) == [[], [0]]
    assert len(subsets(list(range(10)))) == 1024


def _t_02_subsets_with_dup():
    got = subsets_with_dup([1, 2, 2])
    assert _norm(got) == _norm([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]), got
    assert _norm(subsets_with_dup([0])) == [[], [0]]
    got = subsets_with_dup([4, 4, 4, 1, 4])
    assert _norm(got) == _norm([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4],
                                [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]), got
    assert subsets_with_dup([]) == [[]]


def _t_03_permutations():
    got = permutations([1, 2, 3])
    assert sorted(got) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], got
    assert permutations([1]) == [[1]]
    assert sorted(permutations([0, 1])) == [[0, 1], [1, 0]]
    assert len(permutations([1, 2, 3, 4, 5])) == 120


def _t_04_permutations_unique():
    got = permutations_unique([1, 1, 2])
    assert sorted(got) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]], got
    assert len(permutations_unique([1, 2, 3])) == 6
    assert permutations_unique([2, 2, 2]) == [[2, 2, 2]]
    got = permutations_unique([1, 1, 2, 2])
    assert len(got) == 6 and len({tuple(p) for p in got}) == 6, got


def _t_05_combinations():
    got = combinations(4, 2)
    assert _norm(got) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], got
    assert combinations(1, 1) == [[1]]
    assert _norm(combinations(3, 3)) == [[1, 2, 3]]
    assert len(combinations(10, 5)) == 252
    assert _norm(combinations(3, 1)) == [[1], [2], [3]]


def _t_06_combination_sum():
    assert _norm(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert _norm(combination_sum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([2], 1) == []
    assert _norm(combination_sum([1], 2)) == [[1, 1]]
    assert _norm(combination_sum([7, 3, 2], 7)) == [[2, 2, 3], [7]]


def _t_07_combination_sum_ii():
    got = combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
    assert _norm(got) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], got
    assert _norm(combination_sum_ii([2, 5, 2, 1, 2], 5)) == [[1, 2, 2], [5]]
    assert combination_sum_ii([2], 1) == []
    assert _norm(combination_sum_ii([1, 1, 1, 1], 2)) == [[1, 1]]


def _t_08_letter_combinations():
    got = letter_combinations("23")
    assert sorted(got) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], got
    assert letter_combinations("") == []
    assert sorted(letter_combinations("2")) == ["a", "b", "c"]
    assert len(letter_combinations("79")) == 16
    assert len(letter_combinations("2345")) == 81


def _t_09_generate_parentheses():
    got = generate_parentheses(3)
    assert sorted(got) == ["((()))", "(()())", "(())()", "()(())", "()()()"], got
    assert generate_parentheses(1) == ["()"]
    assert sorted(generate_parentheses(2)) == ["(())", "()()"]
    assert len(generate_parentheses(5)) == 42
    assert generate_parentheses(0) == [""]


def _t_10_word_search():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    snapshot = [row[:] for row in board]
    assert word_search(board, "ABCCED") is True
    assert word_search(board, "SEE") is True
    assert word_search(board, "ABCB") is False        # would need to reuse B
    assert board == snapshot, "board must be restored"
    board2 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    assert word_search(board2, "ABCESEEEFS") is True    # snakes through every cell but one
    assert word_search([["a"]], "a") is True
    assert word_search([["a"]], "ab") is False
    assert word_search([["a", "a"]], "aaa") is False


def _t_11_palindrome_partition():
    got = palindrome_partition("aab")
    assert sorted(got) == [["a", "a", "b"], ["aa", "b"]], got
    assert palindrome_partition("a") == [["a"]]
    got = palindrome_partition("aaa")
    assert sorted(got) == [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]], got
    assert sorted(palindrome_partition("ab")) == [["a", "b"]]
    assert len(palindrome_partition("abba")) == 3     # a,b,b,a / a,bb,a / abba


def _valid_queens(board, n):
    if len(board) != n or any(len(row) != n for row in board):
        return False
    cols = [row.index("Q") for row in board if row.count("Q") == 1]
    if len(cols) != n or len(set(cols)) != n:
        return False
    return (len({r + c for r, c in enumerate(cols)}) == n
            and len({r - c for r, c in enumerate(cols)}) == n)


def _t_12_n_queens():
    got = n_queens(4)
    assert sorted(got) == [["..Q.", "Q...", "...Q", ".Q.."], [".Q..", "...Q", "Q...", "..Q."]], got
    assert n_queens(1) == [["Q"]]
    assert n_queens(2) == []
    assert n_queens(3) == []
    got = n_queens(6)
    assert len(got) == 4 and all(_valid_queens(b, 6) for b in got), got
    got = n_queens(8)
    assert len(got) == 92 and all(_valid_queens(b, 8) for b in got)
    assert len({tuple(b) for b in got}) == 92


def _t_13_restore_ip_addresses():
    assert sorted(restore_ip_addresses("25525511135")) == ["255.255.11.135", "255.255.111.35"]
    assert restore_ip_addresses("0000") == ["0.0.0.0"]
    assert restore_ip_addresses("1111") == ["1.1.1.1"]
    got = restore_ip_addresses("101023")
    assert sorted(got) == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"], got
    assert restore_ip_addresses("") == []
    assert restore_ip_addresses("1234567890123") == []   # too long for 4 parts


def _valid_sudoku(board):
    digits = set("123456789")
    for i in range(9):
        if set(board[i]) != digits:
            return False
        if {board[r][i] for r in range(9)} != digits:
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = {board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)}
            if box != digits:
                return False
    return True


def _t_14_sudoku_solver():
    puzzle = [list(r) for r in ["53..7....", "6..195...", ".98....6.",
                                "8...6...3", "4..8.3..1", "7...2...6",
                                ".6....28.", "...419..5", "....8..79"]]
    clues = [row[:] for row in puzzle]
    sudoku_solver(puzzle)
    assert _valid_sudoku(puzzle), puzzle
    for r in range(9):
        for c in range(9):
            if clues[r][c] != ".":
                assert puzzle[r][c] == clues[r][c], "a clue was overwritten"
    assert puzzle[0] == list("534678912")
    solved = [row[:] for row in puzzle]
    sudoku_solver(solved)                      # already solved: must stay valid and unchanged
    assert solved == puzzle


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
