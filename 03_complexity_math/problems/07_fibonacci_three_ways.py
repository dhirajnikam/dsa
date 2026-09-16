"""
Problem: Fibonacci three ways
Difficulty: Easy | Topic: exponential vs linear, memoization, iteration, measuring calls
Source: LeetCode 509

fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).

1. fib_naive(n) -> (value, calls): plain double recursion, and the total number of function
   calls made (including the top-level one). fib_naive(5) == (5, 15). fib_naive(20)[1] == 21891.
   That call count IS the exponential blowup: roughly 2 * fib(n+1) - 1 calls.
2. fib_memo(n) -> value using a dict cache passed through recursion (or lru_cache). O(n).
   Must handle n = 1000 (bump the recursion limit if needed).
3. fib_iter(n) -> value using two variables and a loop. O(n) time, O(1) space. Handle n = 10**5.
4. fib_calls_formula(n) -> the number of calls fib_naive makes, computed WITHOUT recursion:
   calls(0) = calls(1) = 1, calls(n) = 1 + calls(n-1) + calls(n-2). Use a loop.
5. first_fib_with_digits(d) -> the index of the first Fibonacci number with at least d digits.
   first_fib_with_digits(3) == 12 (fib(12) = 144). first_fib_with_digits(1) == 0.

Hints:
1. Use a helper with a nonlocal counter, or return (value, calls) pairs and add them up.
2. def fib_memo(n, memo=None): if memo is None: memo = {} ...  or @lru_cache on an inner function.
5. Iterate fib_iter's loop until len(str(value)) >= d.
"""
import sys

sys.setrecursionlimit(5000)


def fib_naive(n: int) -> tuple[int, int]:
    raise NotImplementedError


def fib_memo(n: int) -> int:
    raise NotImplementedError


def fib_iter(n: int) -> int:
    raise NotImplementedError


def fib_calls_formula(n: int) -> int:
    raise NotImplementedError


def first_fib_with_digits(d: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert fib_naive(0) == (0, 1) and fib_naive(1) == (1, 1) and fib_naive(2) == (1, 3), 'Check: fib_naive(0) == (0, 1) and fib_naive(1) == (1, 1) and fib_naive(2) == (1, 3)'
    assert fib_naive(5) == (5, 15) and fib_naive(10) == (55, 177) and fib_naive(20) == (6765, 21891), 'Check: fib_naive(5) == (5, 15) and fib_naive(10) == (55, 177) and fib_naive(20) == (6765, 21891)'
    for n in range(25):
        assert fib_naive(n)[1] == fib_calls_formula(n), n
    assert fib_calls_formula(100) == 1146295688027634168201, 'Check: fib_calls_formula(100) == 1146295688027634168201'
    assert [fib_memo(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Check: [fib_memo(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'
    assert fib_memo(90) == 2880067194370816120, 'Check: fib_memo(90) == 2880067194370816120'
    assert fib_memo(1000) == fib_iter(1000) and len(str(fib_memo(1000))) == 209, 'Check: fib_memo(1000) == fib_iter(1000) and len(str(fib_memo(1000))) == 209'
    assert [fib_iter(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Check: [fib_iter(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'
    assert fib_iter(90) == 2880067194370816120 and fib_iter(10**5) % (10**9 + 7) == 911435502, 'Check: fib_iter(90) == 2880067194370816120 and fib_iter(10**5) % (10**9 + 7) == 911435502'
    assert first_fib_with_digits(1) == 0 and first_fib_with_digits(2) == 7 and first_fib_with_digits(3) == 12, 'Check: first_fib_with_digits(1) == 0 and first_fib_with_digits(2) == 7 and first_fib_with_digits(3) == 12'
    assert first_fib_with_digits(1000) == 4782, 'Check: first_fib_with_digits(1000) == 4782'
    print("ok")
