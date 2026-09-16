"""
Problem: Insert Delete GetRandom O(1)
Difficulty: Medium | Pattern: list + dict(value -> index), swap-with-last deletion
Source: LeetCode 380

Implement RandomizedSet:
  insert(val) -> bool  : insert val if not present; return True if inserted.
  remove(val) -> bool  : remove val if present; return True if removed.
  get_random() -> int  : return a random element, each with equal probability. Set is non-empty.
All three must be average O(1).

Example:
  rs = RandomizedSet()
  rs.insert(1) -> True
  rs.remove(2) -> False
  rs.insert(2) -> True
  rs.get_random() -> 1 or 2
  rs.remove(1) -> True
  rs.insert(2) -> False
  rs.get_random() -> 2

Constraints:
  -2^31 <= val <= 2^31 - 1
  up to 2 * 10^5 calls

Hints:
1. A set gives O(1) insert/remove but random.choice needs indexing. A list gives indexing but O(n) remove.
2. Combine: list of values + dict value -> its index in the list.
3. To remove in O(1): swap the target with the LAST list element, fix that element's index in
   the dict, then pop the list.

Expected: O(1) average per operation, O(n) space
"""

import random


class RandomizedSet:
    def __init__(self):
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def get_random(self) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    rs = RandomizedSet()
    assert rs.insert(1) is True, 'Check: rs.insert(1) is True'
    assert rs.remove(2) is False, 'Check: rs.remove(2) is False'
    assert rs.insert(2) is True, 'Check: rs.insert(2) is True'
    assert rs.get_random() in (1, 2), 'Check: rs.get_random() in (1, 2)'
    assert rs.remove(1) is True, 'Check: rs.remove(1) is True'
    assert rs.insert(2) is False, 'Check: rs.insert(2) is False'
    assert rs.get_random() == 2, 'Check: rs.get_random() == 2'
    assert rs.remove(2) is True, 'Check: rs.remove(2) is True'
    assert rs.remove(2) is False, 'Check: rs.remove(2) is False'
    rs = RandomizedSet()
    for v in range(10):
        assert rs.insert(v) is True, 'Check: rs.insert(v) is True'
    assert rs.remove(0) is True and rs.remove(9) is True and rs.remove(5) is True, 'Check: rs.remove(0) is True and rs.remove(9) is True and rs.remove(5) is True'
    remaining = {1, 2, 3, 4, 6, 7, 8}
    assert all(rs.get_random() in remaining for _ in range(50)), 'Check: all(rs.get_random() in remaining for _ in range(50))'
    assert {rs.get_random() for _ in range(2000)} == remaining, 'Check: {rs.get_random() for _ in range(2000)} == remaining'
    assert rs.insert(0) is True and rs.remove(0) is True, 'Check: rs.insert(0) is True and rs.remove(0) is True'
    assert rs.insert(-7) is True and rs.get_random() in remaining | {-7}, 'Check: rs.insert(-7) is True and rs.get_random() in remaining | {-7}'
    print("ok")
