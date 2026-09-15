def longest_consecutive(nums):
    # O(n) time, O(n) space
    # Only walk upward from sequence heads (x - 1 absent); every value is then touched O(1) times.
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best
