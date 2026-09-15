"""
Problem: Lazy sequences with generators
Difficulty: Easy | Topic: generators, yield, laziness, iterators

1. fib(): infinite generator yielding 0, 1, 1, 2, 3, 5, ...
2. take(n, it): generator yielding the first n items of any iterable (fewer if it runs out).
3. evens(it): generator yielding only the even items of an iterable.
4. chunks(it, k): generator yielding lists of k consecutive items; the last chunk may be shorter.
   chunks([1,2,3,4,5], 2) -> [1,2], [3,4], [5]
5. running_sum(it): generator yielding cumulative sums. [1,2,3] -> 1, 3, 6

Every function must be lazy: list(take(5, fib())) must terminate even though fib() is infinite.
Do not build a list inside fib/evens/running_sum.

Hints:
1. a, b = 0, 1; while True: yield a; a, b = b, a + b
2. Loop over the iterable and count; return (or break) once n items are yielded. Handle n <= 0.
4. Collect into a buffer; yield and reset it when len == k; yield the leftover at the end if non-empty.
"""
from collections.abc import Iterable, Iterator


def fib() -> Iterator[int]:
    raise NotImplementedError


def take(n: int, it: Iterable) -> Iterator:
    raise NotImplementedError


def evens(it: Iterable[int]) -> Iterator[int]:
    raise NotImplementedError


def chunks(it: Iterable, k: int) -> Iterator[list]:
    raise NotImplementedError


def running_sum(it: Iterable[int]) -> Iterator[int]:
    raise NotImplementedError


if __name__ == "__main__":
    import types
    assert isinstance(fib(), types.GeneratorType)
    assert list(take(8, fib())) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list(take(0, fib())) == []
    assert list(take(5, [1, 2])) == [1, 2]
    assert list(take(6, evens(fib()))) == [0, 2, 8, 34, 144, 610]
    assert list(evens([])) == []
    assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(chunks([], 3)) == []
    assert list(take(3, chunks(fib(), 3))) == [[0, 1, 1], [2, 3, 5], [8, 13, 21]]
    assert list(running_sum([1, 2, 3])) == [1, 3, 6]
    assert list(take(5, running_sum(fib()))) == [0, 1, 2, 4, 7]
    g = fib()
    next(g)
    next(g)
    assert next(g) == 1 and next(g) == 2
    print("ok")
