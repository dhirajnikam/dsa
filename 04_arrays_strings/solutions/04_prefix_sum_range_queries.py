from itertools import accumulate


class NumArray:
    # O(n) build, O(1) per query, O(n) space
    # prefix[i] = sum(nums[:i]); a range sum is a difference of two prefixes.
    def __init__(self, nums):
        self.prefix = [0] + list(accumulate(nums))

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
