"""
Problem: LFU Cache
Difficulty: Hard | Pattern: Design (hash map + frequency buckets)
Source: LeetCode 460

Design a Least Frequently Used cache:
  LFUCache(capacity)
  get(key)        -> value, or -1 if absent. Counts as a use.
  put(key, value) -> insert or update. Counts as a use. If inserting would exceed
                     capacity, evict the least frequently used key; break ties by
                     evicting the least recently used among them.
Both operations must be O(1) average.

Example:
  c = LFUCache(2)
  c.put(1, 1); c.put(2, 2); c.get(1) -> 1
  c.put(3, 3)          # evicts key 2 (freq 1; key 1 has freq 2)
  c.get(2) -> -1; c.get(3) -> 3
  c.put(4, 4)          # keys 1 and 3 both freq 2; 1 is least recent -> evict 1
  c.get(1) -> -1; c.get(3) -> 3; c.get(4) -> 4

Hints:
1. Maps: key -> (value, freq) and freq -> OrderedDict of keys (insertion order = recency).
2. Keep min_freq. A helper touch(key) moves the key from bucket f to bucket f+1; if bucket
   f was min_freq and became empty, min_freq += 1.
3. On inserting a new key at capacity: popitem(last=False) from bucket min_freq, then
   insert with freq 1 and set min_freq = 1.
4. capacity == 0: put must be a no-op.

Expected: O(1) average time per operation, O(capacity) space
"""
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    z = LFUCache(0)
    z.put(0, 0)
    assert z.get(0) == -1

    u = LFUCache(2)
    u.put(1, 1)
    u.put(1, 10)          # update counts as a use; freq(1) = 2
    u.put(2, 2)
    u.put(3, 3)           # evicts 2 (freq 1)
    assert u.get(1) == 10
    assert u.get(2) == -1
    assert u.get(3) == 3

    t = LFUCache(3)
    t.put(1, 1); t.put(2, 2); t.put(3, 3)
    t.get(1); t.get(2); t.get(3)      # all freq 2; recency order 1, 2, 3
    t.put(4, 4)                       # evicts 1
    assert t.get(1) == -1
    assert sorted(t.get(k) for k in (2, 3, 4)) == [2, 3, 4]
    print("ok")
