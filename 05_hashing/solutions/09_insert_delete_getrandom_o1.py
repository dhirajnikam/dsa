import random


class RandomizedSet:
    # O(1) average per op, O(n) space
    # Values live in a list (for random indexing); a dict maps value -> list index.
    # Removal swaps the victim with the last element so popping is O(1).
    def __init__(self):
        self.vals = []
        self.idx = {}

    def insert(self, val):
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.idx:
            return False
        i, last = self.idx.pop(val), self.vals[-1]
        self.vals[i] = last
        if last != val:
            self.idx[last] = i
        self.vals.pop()
        return True

    def get_random(self):
        return random.choice(self.vals)
