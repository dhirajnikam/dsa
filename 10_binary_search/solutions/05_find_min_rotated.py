# O(log n) time, O(1) space
# If nums[mid] > nums[hi] the rotation point is right of mid; otherwise mid could be the minimum.
def find_min(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
