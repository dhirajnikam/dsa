"""
Problem: Functions, defaults, multiple returns, mutation
Difficulty: Warm-up | Topic: parameters, return tuples, references

1. min_max(nums) -> (min, max) in one pass without using min()/max().
2. append_safe(item, lst=None) -> returns a NEW list each call when lst is None.
   The classic mutable-default bug: append_safe(1) twice must give [1] both times.
3. apply_n(f, x, n) -> f applied n times to x. apply_n(lambda v: v * 2, 1, 5) == 32.
4. swap_in_place(lst, i, j) -> mutate lst so positions i and j are swapped; return None.

Contract details:
min_max receives a non-empty list. apply_n receives n >= 0.
swap_in_place receives valid indices. append_safe appends to a supplied list;
when no list is supplied, each call must create an independent list.

Hints:
2. `if lst is None: lst = []`
4. lst[i], lst[j] = lst[j], lst[i]
"""


def min_max(nums: list[int]) -> tuple[int, int]:
    raise NotImplementedError


def append_safe(item, lst=None) -> list:
    raise NotImplementedError


def apply_n(f, x, n: int):
    raise NotImplementedError


def swap_in_place(lst: list, i: int, j: int) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_max([3, -1, 7, 2]) == (-1, 7), 'Check: min_max([3, -1, 7, 2]) == (-1, 7)'
    assert min_max([5]) == (5, 5), 'Check: min_max([5]) == (5, 5)'
    assert append_safe(1) == [1] and append_safe(1) == [1], 'Check: append_safe(1) == [1] and append_safe(1) == [1]'
    assert append_safe(2, [1]) == [1, 2], 'Check: append_safe(2, [1]) == [1, 2]'
    assert apply_n(lambda v: v * 2, 1, 5) == 32, 'Check: apply_n(lambda v: v * 2, 1, 5) == 32'
    assert apply_n(lambda v: v + "a", "", 3) == "aaa", 'Check: apply_n(lambda v: v + "a", "", 3) == "aaa"'
    a = [1, 2, 3]
    assert swap_in_place(a, 0, 2) is None and a == [3, 2, 1], 'Check: swap_in_place(a, 0, 2) is None and a == [3, 2, 1]'
    # Boundary and misconception checks: predict each result before running.
    assert min_max([-3, -9, -5]) == (-9, -3), 'Check: min_max([-3, -9, -5]) == (-9, -3)'
    a = append_safe("x")
    b = append_safe("y")
    assert a == ["x"] and b == ["y"] and a is not b, 'Check: a == ["x"] and b == ["y"] and a is not b'
    assert apply_n(lambda x: x + 1, 9, 0) == 9, 'Check: apply_n(lambda x: x + 1, 9, 0) == 9'
    items = [1, 2]
    assert swap_in_place(items, 1, 1) is None and items == [1, 2], 'Check: swap_in_place(items, 1, 1) is None and items == [1, 2]'
    print("ok")
