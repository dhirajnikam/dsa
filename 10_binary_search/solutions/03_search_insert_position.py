# O(log n) time, O(1) space
# Half-open boundary search for the first index with nums[i] >= target (may be len(nums)).
def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo
