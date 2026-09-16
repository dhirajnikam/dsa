"""09 · Recursion & Backtracking — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        out.append(path[:])                    # every node of the tree is a subset; copy it
        for i in range(start, len(nums)):
            path.append(nums[i])               # choose
            backtrack(i + 1, path)             # explore only forward: no reordering duplicates
            path.pop()                         # un-choose

    backtrack(0, [])
    return out
    # O(n * 2^n) time (2^n subsets, O(n) to copy each), O(n) stack. Iterative: out += [s+[x] for s in out].


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)                        # equal values adjacent, so the skip below works
    out: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        out.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue                       # same value already started a branch at this level
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return out
    # O(n * 2^n) worst case.


def permutations(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    used = [False] * len(nums)

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return out
    # O(n * n!) time, O(n) stack.


def permutations_unique(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    out: list[list[int]] = []
    used = [False] * len(nums)

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue                       # place equal values left to right only
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return out
    # O(n * n!) worst case; far fewer leaves with many duplicates.


def combinations(n: int, k: int) -> list[list[int]]:
    out: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        if len(path) == k:
            out.append(path[:])
            return
        need = k - len(path)
        for i in range(start, n - need + 2):   # prune: enough numbers must remain to fill k
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return out
    # O(k * C(n, k)) time.


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    out: list[list[int]] = []

    def backtrack(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            out.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                continue                       # prune
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)   # i, not i + 1: reuse allowed
            path.pop()

    backtrack(0, target, [])
    return out
    # Exponential in target / min(candidates); output-sized.


def combination_sum_ii(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    out: list[list[int]] = []

    def backtrack(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            out.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break                          # sorted: everything after is bigger too
            if i > start and candidates[i] == candidates[i - 1]:
                continue                       # duplicate value at this level
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)   # each position once
            path.pop()

    backtrack(0, target, [])
    return out
    # O(2^n) worst case.


KEYPAD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
          "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    out: list[str] = []

    def backtrack(i: int, path: list[str]) -> None:
        if i == len(digits):
            out.append("".join(path))
            return
        for ch in KEYPAD[digits[i]]:           # one digit per level; its letters are the choices
            path.append(ch)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return out
    # O(4^n * n) time.


def generate_parentheses(n: int) -> list[str]:
    out: list[str] = []

    def backtrack(path: list[str], open_: int, close: int) -> None:
        if len(path) == 2 * n:
            out.append("".join(path))
            return
        if open_ < n:                          # can still open
            path.append("(")
            backtrack(path, open_ + 1, close)
            path.pop()
        if close < open_:                      # can only close what is open
            path.append(")")
            backtrack(path, open_, close + 1)
            path.pop()

    backtrack([], 0, 0)
    return out
    # Output is the n-th Catalan number, ~ 4^n / n^1.5; only valid prefixes are ever built.


def word_search(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, k: int) -> bool:
        if k == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[k]:
            return False
        saved = board[r][c]
        board[r][c] = "#"                      # mark: the board is the visited set
        found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1)
                 or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
        board[r][c] = saved                    # unmark
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
    # O(R * C * 3^L) time, O(L) stack.


def palindrome_partition(s: str) -> list[list[str]]:
    out: list[list[str]] = []

    def is_pal(a: int, b: int) -> bool:        # s[a:b] a palindrome?
        b -= 1
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True

    def backtrack(start: int, path: list[str]) -> None:
        if start == len(s):
            out.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):   # choose where the next piece ends
            if is_pal(start, end):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return out
    # O(n * 2^n) worst case (all same letter). A DP table of palindromes makes is_pal O(1).


def n_queens(n: int) -> list[list[str]]:
    out: list[list[str]] = []
    cols: set[int] = set()
    diag: set[int] = set()                     # r - c
    anti: set[int] = set()                     # r + c
    placement: list[int] = []                  # placement[r] = column of the queen in row r

    def backtrack(r: int) -> None:
        if r == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in placement])
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue                       # attacked: prune
            cols.add(c); diag.add(r - c); anti.add(r + c); placement.append(c)
            backtrack(r + 1)
            cols.discard(c); diag.discard(r - c); anti.discard(r + c); placement.pop()

    backtrack(0)
    return out
    # O(n!) time bound, O(n) space beyond the output. O(1) validity check via three sets.


def restore_ip_addresses(s: str) -> list[str]:
    out: list[str] = []

    def valid(part: str) -> bool:
        return (len(part) == 1 or part[0] != "0") and int(part) <= 255

    def backtrack(start: int, parts: list[str]) -> None:
        if len(parts) == 4:
            if start == len(s):
                out.append(".".join(parts))
            return
        remaining_parts = 4 - len(parts)
        remaining_chars = len(s) - start
        if not remaining_parts <= remaining_chars <= 3 * remaining_parts:
            return                             # prune: cannot split what is left into the parts needed
        for end in range(start + 1, min(start + 3, len(s)) + 1):
            part = s[start:end]
            if valid(part):
                parts.append(part)
                backtrack(end, parts)
                parts.pop()

    backtrack(0, [])
    return out
    # At most 3^4 = 81 leaves: effectively constant time for a valid-length input.


def sudoku_solver(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties: list[tuple[int, int]] = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r // 3) * 3 + c // 3].add(v)

    def solve(i: int) -> bool:
        if i == len(empties):
            return True                        # every empty cell filled
        r, c = empties[i]
        b = (r // 3) * 3 + c // 3
        for v in "123456789":
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                continue
            board[r][c] = v                    # choose
            rows[r].add(v); cols[c].add(v); boxes[b].add(v)
            if solve(i + 1):
                return True                    # propagate success; do not undo
            board[r][c] = "."                  # un-choose
            rows[r].discard(v); cols[c].discard(v); boxes[b].discard(v)
        return False

    solve(0)
    # Exponential worst case (9^empties), O(1) per validity check via the three set arrays.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
