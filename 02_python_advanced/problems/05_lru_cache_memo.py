"""
Problem: Memoization
Difficulty: Easy | Topic: functools.lru_cache, hand-rolled memo decorator, top-down recursion
Source: LeetCode 70, 62, 91

1. memoize(f): your own decorator. Cache results keyed by the positional args tuple.
   The wrapped function gets .cache (the dict) so tests can inspect it.
2. climb_stairs(n): ways to climb n steps taking 1 or 2 at a time. climb_stairs(3) == 3.
   Decorate with @lru_cache(maxsize=None). Must handle n = 500 instantly.
3. grid_paths(m, n): number of monotone (right/down) paths in an m x n grid from top-left to
   bottom-right. grid_paths(3, 7) == 28. Use @lru_cache.
4. num_decodings(s): ways to decode a digit string where "1".."26" map to letters A..Z.
   "0" cannot stand alone and "06" is invalid. "226" -> 3, "06" -> 0, "" -> 1.
   Use recursion on an index with @lru_cache or your memoize.
5. count_partitions(n, k): number of ways to write n as a sum of positive integers each <= k,
   order ignored. count_partitions(5, 5) == 7. Use memoization.

Hints:
1. def wrapper(*args): if args not in wrapper.cache: wrapper.cache[args] = f(*args); return it.
2. ways(n) = ways(n-1) + ways(n-2), base ways(0) = 1, ways(1) = 1.
4. Recurse on index i: take one digit if s[i] != "0"; take two if 10 <= int(s[i:i+2]) <= 26.
5. p(n, k) = p(n, k-1) + p(n-k, k); p(0, k) = 1; p(n, 0) = 0 for n > 0; k > n -> p(n, n).
"""
from functools import lru_cache, wraps


def memoize(f):
    raise NotImplementedError


def climb_stairs(n: int) -> int:
    raise NotImplementedError


def grid_paths(m: int, n: int) -> int:
    raise NotImplementedError


def num_decodings(s: str) -> int:
    raise NotImplementedError


def count_partitions(n: int, k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    calls = []

    @memoize
    def square(x):
        calls.append(x)
        return x * x

    assert square(4) == 16 and square(4) == 16 and square(5) == 25, 'Check: square(4) == 16 and square(4) == 16 and square(5) == 25'
    assert calls == [4, 5] and square.cache == {(4,): 16, (5,): 25}, 'Check: calls == [4, 5] and square.cache == {(4,): 16, (5,): 25}'
    assert [climb_stairs(n) for n in range(6)] == [1, 1, 2, 3, 5, 8], 'Check: [climb_stairs(n) for n in range(6)] == [1, 1, 2, 3, 5, 8]'
    assert climb_stairs(500) == 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626, 'Check: climb_stairs(500) == 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626'
    assert grid_paths(3, 7) == 28 and grid_paths(1, 1) == 1 and grid_paths(1, 9) == 1, 'Check: grid_paths(3, 7) == 28 and grid_paths(1, 1) == 1 and grid_paths(1, 9) == 1'
    assert grid_paths(18, 18) == 2333606220, 'Check: grid_paths(18, 18) == 2333606220'
    assert num_decodings("12") == 2 and num_decodings("226") == 3, 'Check: num_decodings("12") == 2 and num_decodings("226") == 3'
    assert num_decodings("06") == 0 and num_decodings("0") == 0 and num_decodings("") == 1, 'Check: num_decodings("06") == 0 and num_decodings("0") == 0 and num_decodings("") == 1'
    assert num_decodings("10") == 1 and num_decodings("27") == 1, 'Check: num_decodings("10") == 1 and num_decodings("27") == 1'
    assert num_decodings("1" * 60) == 2504730781961, 'Check: num_decodings("1" * 60) == 2504730781961'
    assert count_partitions(5, 5) == 7 and count_partitions(5, 2) == 3, 'Check: count_partitions(5, 5) == 7 and count_partitions(5, 2) == 3'
    assert count_partitions(0, 3) == 1 and count_partitions(3, 0) == 0, 'Check: count_partitions(0, 3) == 1 and count_partitions(3, 0) == 0'
    assert count_partitions(100, 100) == 190569292, 'Check: count_partitions(100, 100) == 190569292'
    print("ok")
