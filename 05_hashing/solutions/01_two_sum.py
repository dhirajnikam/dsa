def two_sum(nums, target):
    # O(n) time, O(n) space
    # seen maps value -> index; look up the complement before inserting the current value.
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
