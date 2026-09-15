def min_subarray_len(target, nums):
    # O(n) time, O(1) space
    # Positives only: grow r, then shrink l while the window still satisfies sum >= target,
    # recording each valid length.
    l, total, best = 0, 0, float("inf")
    for r, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if best == float("inf") else best
