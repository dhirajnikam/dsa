def can_partition(nums):
    # O(n * target) time, O(target) space
    # dp[s] = subset summing to s exists; dp[s] |= dp[s - x], iterating s downward so
    # each x is used at most once.
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            if dp[s - x]:
                dp[s] = True
        if dp[target]:
            return True
    return dp[target]
