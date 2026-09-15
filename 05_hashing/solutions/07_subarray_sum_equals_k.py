from collections import defaultdict


def subarray_sum(nums, k):
    # O(n) time, O(n) space
    # A subarray ending here sums to k iff some earlier prefix equals cur - k;
    # count those with a hash map. {0: 1} represents the empty prefix.
    seen = defaultdict(int)
    seen[0] = 1
    cur = ans = 0
    for x in nums:
        cur += x
        ans += seen[cur - k]
        seen[cur] += 1
    return ans
