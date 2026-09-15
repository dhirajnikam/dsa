# O(log n) time, O(1) space
# lower_bound(x) = first index with nums[i] >= x. First = lower_bound(t), last = lower_bound(t+1) - 1.
def search_range(nums: list[int], target: int) -> list[int]:
    def lower_bound(x: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= x:
                hi = mid
            else:
                lo = mid + 1
        return lo

    first = lower_bound(target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, lower_bound(target + 1) - 1]
