from collections import OrderedDict, defaultdict


class LFUCache:
    # O(1) average per operation, O(capacity) space
    # key -> (value, freq) plus freq -> OrderedDict of keys (insertion order = recency).
    # min_freq only ever rises on a touch (bucket emptied) and resets to 1 on a new insert,
    # so eviction is always popitem(last=False) from bucket[min_freq].
    def __init__(self, capacity):
        self.cap = capacity
        self.vals = {}                       # key -> (value, freq)
        self.buckets = defaultdict(OrderedDict)  # freq -> keys in LRU order
        self.min_freq = 0

    def _touch(self, key):
        value, freq = self.vals[key]
        del self.buckets[freq][key]
        if not self.buckets[freq]:
            del self.buckets[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.buckets[freq + 1][key] = None
        self.vals[key] = (value, freq + 1)

    def get(self, key):
        if key not in self.vals:
            return -1
        self._touch(key)
        return self.vals[key][0]

    def put(self, key, value):
        if self.cap == 0:
            return
        if key in self.vals:
            self._touch(key)
            self.vals[key] = (value, self.vals[key][1])
            return
        if len(self.vals) == self.cap:
            evicted, _ = self.buckets[self.min_freq].popitem(last=False)
            if not self.buckets[self.min_freq]:
                del self.buckets[self.min_freq]
            del self.vals[evicted]
        self.vals[key] = (value, 1)
        self.buckets[1][key] = None
        self.min_freq = 1
