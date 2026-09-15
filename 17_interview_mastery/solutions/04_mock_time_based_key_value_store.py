# What a strong candidate says:
# "Are timestamps strictly increasing per key? And get wants the latest value at or before
#  the given time, empty string if none? Then each key's history is already sorted as it
#  arrives, so set is an O(1) append and get is a binary search for the rightmost timestamp
#  <= t. If writes could arrive out of order I would need sorted insertion instead."
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    # O(1) set, O(log n) get, O(total writes) space
    # Per key: parallel lists of timestamps and values kept sorted by construction;
    # bisect_right finds how many timestamps are <= t, so index-1 is the answer.
    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key, value, timestamp):
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        i = bisect_right(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""
