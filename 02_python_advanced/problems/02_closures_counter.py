"""
Problem: Closures
Difficulty: Easy | Topic: closures, nonlocal, late binding, higher-order functions

1. make_counter(start=0) -> function that returns start+1, start+2, ... on successive calls.
   Independent counters must not share state.
2. make_accumulator() -> function acc(x) that returns the running total of everything passed so far.
3. compose(*funcs) -> a function applying funcs right to left: compose(f, g)(x) == f(g(x)).
   compose() with no functions is the identity.
4. make_multipliers(n) -> list of n functions; the i-th returns x * i.
   The naive [lambda x: x * i for i in range(n)] is WRONG (all use the final i). Fix it.
5. memo_once(f) -> a function that calls f the first time and returns the cached result
   forever after, ignoring arguments (a "lazy value").

Hints:
1. Rebinding an outer variable needs `nonlocal`.
3. Loop over reversed(funcs); or use functools.reduce.
4. Bind i at definition time: lambda x, i=i: x * i, or use a helper factory function.
"""


def make_counter(start: int = 0):
    raise NotImplementedError


def make_accumulator():
    raise NotImplementedError


def compose(*funcs):
    raise NotImplementedError


def make_multipliers(n: int) -> list:
    raise NotImplementedError


def memo_once(f):
    raise NotImplementedError


if __name__ == "__main__":
    c1, c2 = make_counter(), make_counter(10)
    assert c1() == 1 and c1() == 2 and c2() == 11 and c1() == 3
    acc = make_accumulator()
    assert acc(5) == 5 and acc(10) == 15 and acc(-15) == 0
    inc = lambda x: x + 1
    dbl = lambda x: x * 2
    assert compose(inc, dbl)(5) == 11 and compose(dbl, inc)(5) == 12
    assert compose()(7) == 7 and compose(inc)(7) == 8
    assert compose(str, inc, dbl)(3) == "7"
    ms = make_multipliers(4)
    assert [m(10) for m in ms] == [0, 10, 20, 30]
    assert make_multipliers(0) == []
    calls = []
    lazy = memo_once(lambda: calls.append(1) or 42)
    assert calls == []
    assert lazy() == 42 and lazy() == 42 and lazy("ignored") == 42
    assert calls == [1]
    print("ok")
