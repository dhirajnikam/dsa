def max_subarray(nums):
    # O(n) time, O(1) space
    # cur = best sum ending here; a negative prefix never helps, so restart when cur < 0.
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
