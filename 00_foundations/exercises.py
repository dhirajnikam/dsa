"""00 · Foundations — exercises.

Run:  python exercises.py
Each function below is a problem. Replace `raise NotImplementedError` with your solution.
The checker prints PASS / FAIL / TODO per problem. Stuck for 30 minutes? Read the hint in
LESSON.md. Stuck for 40? Open solutions.py, read only that one function, close it, rewrite it.
"""


def is_palindrome_clean(s: str) -> bool:
    """Return True if `s` reads the same forwards and backwards, considering only
    alphanumeric characters and ignoring case.

    Example: "A man, a plan, a canal: Panama" -> True
             "race a car" -> False
             "" -> True
    """
    raise NotImplementedError


def word_frequencies(text: str) -> dict[str, int]:
    """Split `text` on whitespace, lowercase every word, and return {word: count}.

    Example: "The cat the DOG" -> {"the": 2, "cat": 1, "dog": 1}
             "" -> {}
    """
    raise NotImplementedError


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two already-sorted lists into one sorted list in O(len(a) + len(b)).
    Do NOT call sorted() — the point is the two-pointer merge.

    Example: [1, 4, 7], [2, 3, 9] -> [1, 2, 3, 4, 7, 9]
             [], [1] -> [1]
    """
    raise NotImplementedError


def fast_pow(x: int, n: int, mod: int) -> int:
    """Return (x ** n) % mod in O(log n) multiplications, n >= 0.

    Example: fast_pow(2, 10, 1000) -> 24     (1024 % 1000)
             fast_pow(3, 0, 7) -> 1
             fast_pow(2, 10**18, 10**9 + 7) must return instantly.
    """
    raise NotImplementedError


def transpose(grid: list[list[int]]) -> list[list[int]]:
    """Return the transpose: rows become columns. grid may be non-square.

    Example: [[1, 2, 3],
              [4, 5, 6]]  ->  [[1, 4],
                               [2, 5],
                               [3, 6]]
    """
    raise NotImplementedError


def flatten(nested: list) -> list[int]:
    """Flatten arbitrarily nested lists of ints into one flat list, preserving order.

    Example: [1, [2, [3, 4]], [], 5] -> [1, 2, 3, 4, 5]
    """
    raise NotImplementedError


def fib(n: int) -> int:
    """Return the n-th Fibonacci number: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).
    Must be fast for n = 90 (naive recursion will never finish).

    Example: fib(10) -> 55
    """
    raise NotImplementedError


# Fill in the Big-O of each snippet as a string like "O(n)", "O(n^2)", "O(log n)", "O(n log n)", "O(1)".
# A: for i in range(n): total += i
# B: for i in range(n):
#        for j in range(n): total += i * j
# C: while n > 1: n //= 2
# D: for i in range(n):
#        for j in range(i): total += 1
# E: x = arr[len(arr) // 2]
# F: arr.sort(); for x in arr: print(x)
# G: for x in arr: if x in set_of_items: count += 1        (set lookup)
# H: for x in arr: if x in list_of_items: count += 1       (list lookup, len m)
BIG_O = {
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",   # use n and m, e.g. "O(n*m)"
}


# ----------------------------------------------------------------------------- checks

def _t_is_palindrome_clean():
    assert is_palindrome_clean("A man, a plan, a canal: Panama") is True
    assert is_palindrome_clean("race a car") is False
    assert is_palindrome_clean("") is True
    assert is_palindrome_clean("0P") is False


def _t_word_frequencies():
    assert word_frequencies("The cat the DOG") == {"the": 2, "cat": 1, "dog": 1}
    assert word_frequencies("") == {}
    assert word_frequencies("a a a") == {"a": 3}


def _t_merge_sorted():
    assert merge_sorted([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9]
    assert merge_sorted([], [1]) == [1]
    assert merge_sorted([1, 1], [1]) == [1, 1, 1]
    assert merge_sorted([5, 6], [1, 2]) == [1, 2, 5, 6]


def _t_fast_pow():
    assert fast_pow(2, 10, 1000) == 24
    assert fast_pow(3, 0, 7) == 1
    assert fast_pow(2, 10**18, 10**9 + 7) == pow(2, 10**18, 10**9 + 7)
    assert fast_pow(7, 13, 13) == pow(7, 13, 13)


def _t_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1]]) == [[1]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def _t_flatten():
    assert flatten([1, [2, [3, 4]], [], 5]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[[[1]]]]) == [1]


def _t_fib():
    assert fib(0) == 0 and fib(1) == 1 and fib(10) == 55
    assert fib(90) == 2880067194370816120


def _t_big_o():
    want = {"A": "O(n)", "B": "O(n^2)", "C": "O(log n)", "D": "O(n^2)",
            "E": "O(1)", "F": "O(n log n)", "G": "O(n)", "H": "O(n*m)"}
    norm = lambda s: s.replace(" ", "").replace("²", "^2").replace("*", "").lower()
    if all(v == "" for v in BIG_O.values()):
        raise NotImplementedError
    for k, v in want.items():
        assert BIG_O[k] != "", f"{k} is blank"
        assert norm(BIG_O[k]) == norm(v), f"{k}: got {BIG_O[k]!r}, want {v!r}"


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
