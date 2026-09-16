"""00 · Foundations — reference solutions.

Honor rule: open this only after 40 minutes on a problem. Read one function, close the file,
rewrite it from memory, and add the problem to redo.txt.

Run `python solutions.py` to prove these pass the exact tests in exercises.py.
"""
from functools import lru_cache


def is_palindrome_clean(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
    # O(n) time, O(n) space. Two pointers from both ends would be O(1) space — Chapter 02.


def word_frequencies(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    out: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:          # <= keeps the merge stable
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])             # exactly one of these is non-empty
    out.extend(b[j:])
    return out


def fast_pow(x: int, n: int, mod: int) -> int:
    if n == 0:
        return 1 % mod
    half = fast_pow(x, n // 2, mod)
    result = half * half % mod
    if n % 2:
        result = result * x % mod
    return result
    # O(log n): n halves every call. Iterative "binary exponentiation" is the same idea.


def transpose(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    out = [[0] * rows for _ in range(cols)]   # note: NOT [[0]*rows]*cols
    for r in range(rows):
        for c in range(cols):
            out[c][r] = grid[r][c]
    return out
    # one-liner: [list(col) for col in zip(*grid)]


def flatten(nested: list) -> list[int]:
    out: list[int] = []
    for x in nested:
        if isinstance(x, list):
            out.extend(flatten(x))    # trust the recursive call
        else:
            out.append(x)
    return out


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
    # Without the cache this is O(2^n). With it every n is computed once: O(n).
    # Bottom-up with two variables is O(1) space — see Chapter 10.


BIG_O = {
    "A": "O(n)",
    "B": "O(n^2)",
    "C": "O(log n)",
    "D": "O(n^2)",       # 0+1+...+(n-1) = n(n-1)/2
    "E": "O(1)",
    "F": "O(n log n)",   # the sort dominates the linear scan
    "G": "O(n)",         # set membership is O(1) average
    "H": "O(n*m)",       # list membership is O(m) each time
}


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)   # run exercises.py's checks against these solutions
    exercises._check()
