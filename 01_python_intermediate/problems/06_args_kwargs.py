"""
Problem: Variadic arguments and unpacking
Difficulty: Easy | Topic: *args, **kwargs, unpacking, keyword-only args

1. total(*args) -> sum of all positional arguments. total() == 0.
2. build_query(**kwargs) -> "k1=v1&k2=v2" with keys sorted. build_query() == "".
3. call_with(f, args, kwargs) -> f(*args, **kwargs).
4. merge_dicts(*dicts) -> new dict; later dicts win on key conflicts. Inputs untouched.
5. first_last_middle(seq) -> (first, last, middle_list) using starred assignment.
   [1,2,3,4] -> (1, 4, [2,3]);  [1,2] -> (1, 2, []).  seq has at least 2 items.
6. describe(name, *, age, city="?") -> f"{name} ({age}) from {city}". age is keyword-only:
   describe("a", 30) must raise TypeError.

Hints:
2. "&".join(f"{k}={v}" for k, v in sorted(kwargs.items()))
4. {**a, **b} or a loop with .update().
5. first, *middle, last = seq
6. Everything after a bare * in the signature is keyword-only.
"""


def total(*args) -> int:
    raise NotImplementedError


def build_query(**kwargs) -> str:
    raise NotImplementedError


def call_with(f, args: tuple, kwargs: dict):
    raise NotImplementedError


def merge_dicts(*dicts: dict) -> dict:
    raise NotImplementedError


def first_last_middle(seq: list) -> tuple:
    raise NotImplementedError


def describe(name: str, *, age: int, city: str = "?") -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert total() == 0 and total(1) == 1 and total(1, 2, 3) == 6
    assert total(*range(5)) == 10
    assert build_query() == ""
    assert build_query(b=2, a=1) == "a=1&b=2"
    assert call_with(total, (1, 2), {}) == 3
    assert call_with(build_query, (), {"x": 1}) == "x=1"
    d1, d2 = {"a": 1, "b": 2}, {"b": 3}
    assert merge_dicts(d1, d2) == {"a": 1, "b": 3} and d1 == {"a": 1, "b": 2}
    assert merge_dicts() == {}
    assert first_last_middle([1, 2, 3, 4]) == (1, 4, [2, 3])
    assert first_last_middle([1, 2]) == (1, 2, [])
    assert describe("a", age=30) == "a (30) from ?"
    assert describe("a", age=30, city="Pune") == "a (30) from Pune"
    try:
        describe("a", 30)
        assert False
    except TypeError:
        pass
    print("ok")
