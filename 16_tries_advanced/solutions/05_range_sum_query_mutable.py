class NumArray:
    # O(n log n) build, O(log n) update and query, O(n) space
    # Fenwick tree: tree[i] (1-indexed) stores the sum of the block of size (i & -i)
    # ending at i. Update walks up by adding the lowest bit, prefix walks down by removing it.
    def __init__(self, nums):
        self.nums = list(nums)
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i, x in enumerate(nums):
            self._add(i, x)

    def _add(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def _prefix(self, i):  # sum of nums[0..i]
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def update(self, index, val):
        self._add(index, val - self.nums[index])
        self.nums[index] = val

    def sum_range(self, left, right):
        return self._prefix(right) - (self._prefix(left - 1) if left else 0)
