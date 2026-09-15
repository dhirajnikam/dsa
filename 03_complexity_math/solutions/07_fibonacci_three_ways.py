import sys

sys.setrecursionlimit(5000)


def fib_naive(n):  # O(2^n) time, O(n) stack
    calls = 0

    def f(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return f(k - 1) + f(k - 2)
    return f(n), calls


def fib_memo(n, memo=None):  # O(n) time, O(n) space
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_iter(n):  # O(n) time, O(1) space
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_calls_formula(n):  # O(n)
    prev, cur = 1, 1  # calls(0), calls(1)
    for _ in range(n - 1):
        prev, cur = cur, 1 + cur + prev
    return cur


def first_fib_with_digits(d):
    a, b, i = 0, 1, 0
    while len(str(a)) < d:
        a, b = b, a + b
        i += 1
    return i
