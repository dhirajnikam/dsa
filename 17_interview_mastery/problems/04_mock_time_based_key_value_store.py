"""
Problem: Mock interview 4 - Time Based Key-Value Store
Difficulty: Medium | Pattern: Hash map + binary search on sorted timestamps
Source: LeetCode 981

Interviewer says:
  "Build a key-value store where every write has a timestamp, and reads can ask for the
   value as of a particular time."

Ask about: are timestamps strictly increasing per key (or globally)? What should a read
return when no value existed yet at that time? Are keys and values strings? How many
operations? Can the same timestamp be written twice?

Hints (constraints you should have asked about):
1. set(key, value, timestamp) and get(key, timestamp). Timestamps for set are strictly
   increasing across all calls (so per key they arrive sorted, no duplicates).
   get returns the value with the largest timestamp <= the query timestamp, or "" if none.
   Up to 2 * 10^5 calls. Keys and values are strings.
2. Because timestamps arrive sorted, append to a per-key list of (timestamp, value).
   get is a binary search for the rightmost timestamp <= t: bisect_right on the
   timestamps, then index - 1.
3. Keep two parallel lists per key (times, values) or use bisect with a key= function
   (Python 3.10+). Either way, no sorting is ever needed.
4. Follow-up: if timestamps could arrive out of order, you would need sorted insertion
   (bisect.insort, O(n)) or a balanced tree; say so.

Expected: O(1) set, O(log n) get where n is writes to that key, O(total writes) space
"""
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        raise NotImplementedError

    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    m = TimeMap()
    m.set("foo", "bar", 1)
    assert m.get("foo", 1) == "bar"
    assert m.get("foo", 3) == "bar"
    m.set("foo", "bar2", 4)
    assert m.get("foo", 4) == "bar2"
    assert m.get("foo", 5) == "bar2"
    assert m.get("foo", 3) == "bar"
    assert m.get("foo", 0) == ""
    assert m.get("missing", 10) == ""

    t = TimeMap()
    t.set("a", "1", 10)
    t.set("a", "2", 20)
    t.set("a", "3", 30)
    t.set("b", "x", 25)
    assert t.get("a", 9) == ""
    assert t.get("a", 10) == "1"
    assert t.get("a", 19) == "1"
    assert t.get("a", 20) == "2"
    assert t.get("a", 29) == "2"
    assert t.get("a", 30) == "3"
    assert t.get("a", 1000) == "3"
    assert t.get("b", 24) == ""
    assert t.get("b", 25) == "x"
    print("ok")
