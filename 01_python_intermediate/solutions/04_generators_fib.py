from collections.abc import Iterable, Iterator


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n, it):
    if n <= 0:
        return
    for i, x in enumerate(it):
        yield x
        if i + 1 >= n:
            return


def evens(it):
    for x in it:
        if x % 2 == 0:
            yield x


def chunks(it, k):
    buf = []
    for x in it:
        buf.append(x)
        if len(buf) == k:
            yield buf
            buf = []
    if buf:
        yield buf


def running_sum(it):
    total = 0
    for x in it:
        total += x
        yield total
