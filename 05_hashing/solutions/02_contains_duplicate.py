def contains_duplicate(nums):
    # O(n) time, O(n) space
    # Early exit on the first repeat; a set answers "seen before?" in O(1).
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
