def rob(nums):
    # O(n) time, O(1) space
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i]); prev2/prev1 hold dp[i-2]/dp[i-1].
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
