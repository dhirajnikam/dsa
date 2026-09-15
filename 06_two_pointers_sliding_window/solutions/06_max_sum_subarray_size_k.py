def max_sum_subarray_k(nums, k):
    # O(n) time, O(1) space
    # Fixed window: add the entering element, drop the one that fell off the left.
    if len(nums) < k:
        return 0
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
