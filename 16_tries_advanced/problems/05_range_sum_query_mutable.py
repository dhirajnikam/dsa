"""
Problem: Range Sum Query - Mutable
Difficulty: Medium | Pattern: Fenwick tree / segment tree
Source: LeetCode 307

Design a class over an integer array nums:
  NumArray(nums)
  update(index, val)     -> set nums[index] = val
  sum_range(left, right) -> sum of nums[left..right] inclusive
Both operations are called many times, so O(n) per call is too slow.

Example:
  a = NumArray([1, 3, 5]); a.sum_range(0, 2) -> 9
  a.update(1, 2); a.sum_range(0, 2) -> 8

Hints:
1. Fenwick tree: tree[i] covers a block of size (i & -i) ending at i (1-indexed).
   add(i, delta): while i <= n: tree[i] += delta; i += i & -i
   prefix(i):     while i > 0:  s += tree[i]; i -= i & -i
2. update is add(index, val - nums[index]); keep a plain copy of nums for the old value.
3. sum_range(l, r) = prefix(r) - prefix(l - 1). Watch the 0/1-index shift.
4. A segment tree also works and additionally supports min/max. Either is accepted.

Expected: O(n) build (O(n log n) is fine), O(log n) update and query, O(n) space
"""


class NumArray:
    def __init__(self, nums: list[int]) -> None:
        raise NotImplementedError

    def update(self, index: int, val: int) -> None:
        raise NotImplementedError

    def sum_range(self, left: int, right: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    a = NumArray([1, 3, 5])
    assert a.sum_range(0, 2) == 9, 'Check: a.sum_range(0, 2) == 9'
    a.update(1, 2)
    assert a.sum_range(0, 2) == 8, 'Check: a.sum_range(0, 2) == 8'
    assert a.sum_range(1, 1) == 2, 'Check: a.sum_range(1, 1) == 2'
    assert a.sum_range(2, 2) == 5, 'Check: a.sum_range(2, 2) == 5'
    b = NumArray([7])
    assert b.sum_range(0, 0) == 7, 'Check: b.sum_range(0, 0) == 7'
    b.update(0, -3)
    assert b.sum_range(0, 0) == -3, 'Check: b.sum_range(0, 0) == -3'
    c = NumArray([0, 0, 0, 0, 0, 0, 0, 0])
    c.update(7, 10)
    c.update(0, 1)
    assert c.sum_range(0, 7) == 11, 'Check: c.sum_range(0, 7) == 11'
    assert c.sum_range(1, 6) == 0, 'Check: c.sum_range(1, 6) == 0'
    assert c.sum_range(7, 7) == 10, 'Check: c.sum_range(7, 7) == 10'
    c.update(7, 4)
    assert c.sum_range(3, 7) == 4, 'Check: c.sum_range(3, 7) == 4'
    print("ok")
