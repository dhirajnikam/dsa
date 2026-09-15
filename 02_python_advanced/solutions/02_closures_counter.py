def make_counter(start=0):
    n = start

    def inc():
        nonlocal n
        n += 1
        return n
    return inc


def make_accumulator():
    total = 0

    def acc(x):
        nonlocal total
        total += x
        return total
    return acc


def compose(*funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed


def make_multipliers(n):
    return [lambda x, i=i: x * i for i in range(n)]


def memo_once(f):
    cache = []

    def wrapper(*args, **kwargs):
        if not cache:
            cache.append(f())
        return cache[0]
    return wrapper
