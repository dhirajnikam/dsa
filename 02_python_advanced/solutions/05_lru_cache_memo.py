from functools import lru_cache, wraps


def memoize(f):
    @wraps(f)
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = f(*args)
        return wrapper.cache[args]
    wrapper.cache = {}
    return wrapper


@lru_cache(maxsize=None)
def climb_stairs(n):  # O(n) time, O(n) space
    if n < 2:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)


@lru_cache(maxsize=None)
def grid_paths(m, n):  # O(m*n) time and space
    if m == 1 or n == 1:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)


def num_decodings(s):  # O(n) time, O(n) space
    @lru_cache(maxsize=None)
    def ways(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        total = ways(i + 1)
        if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
            total += ways(i + 2)
        return total
    return ways(0)


@lru_cache(maxsize=None)
def count_partitions(n, k):  # O(n*k) time and space
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return count_partitions(n, k - 1) + count_partitions(n - k, k)
