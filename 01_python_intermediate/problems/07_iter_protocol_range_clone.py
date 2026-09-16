"""
Problem: Reimplement range
Difficulty: Medium | Topic: iterator protocol, __iter__, __len__, __contains__, __getitem__

Implement class Range(start, stop=None, step=1) that behaves like the built-in range for ints,
WITHOUT storing the numbers in a list (Range(0, 10**12) must be instant).

  Range(5)          -> 0..4
  Range(2, 5)       -> 2, 3, 4
  Range(10, 0, -3)  -> 10, 7, 4, 1
  step == 0 -> ValueError

Support:
  for x in r          (__iter__, make it a generator)
  len(r)              (__len__, O(1) via formula, 0 for empty ranges)
  x in r              (__contains__, O(1): check bounds and (x - start) % step == 0)
  r[i]                (__getitem__, negative indexes allowed, IndexError when out of range)
  repr(r) == "Range(2, 5, 1)"

Hints:
1. len: if step > 0: max(0, (stop - start + step - 1) // step) else max(0, (start - stop - step - 1) // -step)
2. Iterating twice must work; that is why __iter__ should be a fresh generator each call.
3. __getitem__: normalize i by adding len when negative, then start + i * step.
"""


class Range:
    def __init__(self, start: int, stop: int | None = None, step: int = 1):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, x: int) -> bool:
        raise NotImplementedError

    def __getitem__(self, i: int) -> int:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    assert list(Range(5)) == [0, 1, 2, 3, 4], 'Check: list(Range(5)) == [0, 1, 2, 3, 4]'
    assert list(Range(2, 5)) == [2, 3, 4], 'Check: list(Range(2, 5)) == [2, 3, 4]'
    assert list(Range(10, 0, -3)) == [10, 7, 4, 1], 'Check: list(Range(10, 0, -3)) == [10, 7, 4, 1]'
    assert list(Range(5, 5)) == [] and len(Range(5, 2)) == 0, 'Check: list(Range(5, 5)) == [] and len(Range(5, 2)) == 0'
    for args in [(5,), (2, 5), (10, 0, -3), (0, 10, 4), (7, -8, -5), (3, 3)]:
        assert len(Range(*args)) == len(range(*args)), args
        assert list(Range(*args)) == list(range(*args)), args
    r = Range(10, 0, -3)
    assert list(r) == list(r), 'Check: list(r) == list(r)'  # re-iterable
    assert 7 in r and 8 not in r and 0 not in r and 10 in r, 'Check: 7 in r and 8 not in r and 0 not in r and 10 in r'
    assert r[0] == 10 and r[3] == 1 and r[-1] == 1 and r[-4] == 10, 'Check: r[0] == 10 and r[3] == 1 and r[-1] == 1 and r[-4] == 10'
    try:
        r[4]
        assert False, 'Check: False'
    except IndexError:
        pass
    big = Range(0, 10**12, 7)
    last = range(0, 10**12, 7)[-1]
    assert len(big) == len(range(0, 10**12, 7)) and last in big and last - 1 not in big, 'Check: len(big) == len(range(0, 10**12, 7)) and last in big and last - 1 not in big'
    assert big[-1] == last and 10**12 not in big, 'Check: big[-1] == last and 10**12 not in big'
    try:
        Range(0, 5, 0)
        assert False, 'Check: False'
    except ValueError:
        pass
    assert repr(Range(2, 5)) == "Range(2, 5, 1)", 'Check: repr(Range(2, 5)) == "Range(2, 5, 1)"'
    print("ok")
